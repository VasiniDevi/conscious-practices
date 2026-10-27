#!/usr/bin/env python3
"""Consistency checks for conscious-practices.

Checks:
  1. manifest.yaml parses and every practice has the required fields,
     including activation (auto|offer|explicit), applies_when, does_not_apply_when.
  2. Every manifest skill/prompt path exists and is non-empty.
  3. Every skills/<id>/SKILL.md has valid Agent Skills frontmatter
     (agentskills.io spec: name rules, name == directory, description 1..1024
     chars, containing "Use when" and "Not for"), plus the repo's required
     sections (incl. "When to apply").
  4. skills/ directories and manifest ids match one-to-one.
  5. .claude/skills/<id> and .agents/skills/<id> exist and resolve to skills/<id>.
  6. Every prompt and skill carries the generic crisis handoff ("emergency
     services"; skills also point to safety/crisis.md). Only English prompt
     files (*.en.md) are allowed.
  7. Relative Markdown links and backticked repo paths resolve.
  8. vendor/* directories contain LICENSE and ATTRIBUTION.md.
  9. journal/ is git-ignored.
 10. English only: no Cyrillic text outside research/.
 11. No phone numbers or helpline directories anywhere (generic handoff only).

Zero dependencies: uses PyYAML if installed, otherwise a small built-in
parser that covers the YAML subset used in this repo.

Usage: python3 scripts/validate.py   (exit code 0 = OK, 1 = errors)
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


# --------------------------------------------------------------------------- YAML
def _scalar(s: str):
    s = s.strip()
    if s == "":
        return None
    if s[0] in "\"'":
        q = s[0]
        end = s.rfind(q)
        inner = s[1:end]
        return json.loads('"' + inner.replace('"', '\\"') + '"') if q == '"' else inner.replace("''", "'")
    if s.startswith("[") and s.endswith("]"):
        body = s[1:-1].strip()
        if not body:
            return []
        items, cur, quote = [], "", None
        for ch in body:
            if quote:
                cur += ch
                if ch == quote:
                    quote = None
            elif ch in "\"'":
                quote = ch
                cur += ch
            elif ch == ",":
                items.append(_scalar(cur))
                cur = ""
            else:
                cur += ch
        items.append(_scalar(cur))
        return items
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if s in ("true", "false"):
        return s == "true"
    return s


def _strip_comment(line: str) -> str:
    out, quote = "", None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out += ch
    return out.rstrip()


def mini_yaml(text: str):
    """Parse a block-style YAML subset: mappings, lists, flow lists, scalars."""
    lines = []
    for raw in text.splitlines():
        line = _strip_comment(raw)
        if line.strip():
            lines.append((len(line) - len(line.lstrip(" ")), line.strip()))

    def parse(i: int, indent: int):
        if i >= len(lines):
            return None, i
        if lines[i][1].startswith("- "):
            seq = []
            while i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("- "):
                content = lines[i][1][2:]
                if re.match(r"^[\w\-]+:(\s|$)", content):
                    # mapping item: re-inject as a mapping at indent+2
                    lines[i] = (indent + 2, content)
                    val, i = parse(i, indent + 2)
                    seq.append(val)
                else:
                    seq.append(_scalar(content))
                    i += 1
            return seq, i
        mapping = {}
        while i < len(lines) and lines[i][0] == indent and not lines[i][1].startswith("- "):
            key, _, rest = lines[i][1].partition(":")
            key = key.strip()
            rest = rest.strip()
            i += 1
            if rest:
                mapping[key] = _scalar(rest)
            elif i < len(lines) and lines[i][0] > indent:
                mapping[key], i = parse(i, lines[i][0])
            elif i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("- "):
                mapping[key], i = parse(i, indent)
            else:
                mapping[key] = None
        return mapping, i

    val, _ = parse(0, lines[0][0] if lines else 0)
    return val


def load_yaml(text: str):
    try:
        import yaml  # type: ignore

        return yaml.safe_load(text), "PyYAML"
    except ImportError:
        return mini_yaml(text), "built-in parser"


# --------------------------------------------------------------------------- checks
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_PRACTICE_FIELDS = [
    "id", "number", "name", "summary", "activation", "applies_when",
    "does_not_apply_when", "triggers", "duration_minutes", "inputs",
    "exit_condition", "closing", "skill", "prompts", "evidence_level",
    "verdict", "sources",
]
ACTIVATION_MODES = {"auto", "offer", "explicit"}
CYRILLIC_RE = re.compile(r"[\u0400-\u04FF]")
# Phone-number-like emergency/helpline numbers (not inside DOIs, versions, URLs paths)
PHONE_RE = re.compile(r"(?<![\w./-])(?:112|911|999|988|116[ -]?123|8-800[\d-]*)(?![\w./-])")
HELPLINE_RE = re.compile(r"findahelpline|iasp\.info|helpline directory|crisis line number", re.I)
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".txt", ".json", ""}
EVIDENCE_LEVELS = {"moderate", "moderate-low", "low", "tradition"}
REQUIRED_SKILL_SECTIONS = ["When to apply", "Hard rules", "Protocol", "Exit", "Closing action", "Safety handoff", "Example"]
CRISIS_MARKER = "emergency services"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def check_file(rel: str, ctx: str) -> Path | None:
    p = ROOT / rel
    if not p.is_file():
        err(f"{ctx}: missing file {rel}")
        return None
    if not read(p).strip():
        err(f"{ctx}: empty file {rel}")
    return p


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 4 :]


def check_skill(skill_dir: Path, parser_name: str) -> None:
    rel = skill_dir.relative_to(ROOT)
    p = skill_dir / "SKILL.md"
    if not p.is_file():
        err(f"{rel}: missing SKILL.md")
        return
    fm_text, body = split_frontmatter(read(p))
    if fm_text is None:
        err(f"{rel}/SKILL.md: missing YAML frontmatter")
        return
    try:
        fm, _ = load_yaml(fm_text)
    except Exception as e:  # noqa: BLE001
        err(f"{rel}/SKILL.md: frontmatter does not parse ({e})")
        return
    if not isinstance(fm, dict):
        err(f"{rel}/SKILL.md: frontmatter is not a mapping")
        return
    name = fm.get("name")
    desc = fm.get("description")
    if not isinstance(name, str) or not (1 <= len(name) <= 64) or not NAME_RE.match(name):
        err(f"{rel}/SKILL.md: invalid name {name!r} (lowercase a-z0-9 and single hyphens, 1-64 chars)")
    elif name != skill_dir.name:
        err(f"{rel}/SKILL.md: name {name!r} != directory {skill_dir.name!r}")
    if not isinstance(desc, str) or not (1 <= len(desc) <= 1024):
        err(f"{rel}/SKILL.md: description must be a 1-1024 char string (got {len(desc) if isinstance(desc, str) else type(desc).__name__})")
    else:
        if "Use when" not in desc:
            err(f"{rel}/SKILL.md: description lacks a 'Use when…' clause")
        if "Not for" not in desc:
            err(f"{rel}/SKILL.md: description lacks a 'Not for…' clause")
    md = fm.get("metadata")
    if md is not None and (not isinstance(md, dict) or not all(isinstance(v, str) for v in md.values())):
        err(f"{rel}/SKILL.md: metadata must map strings to strings")
    if "compatibility" in fm and len(str(fm["compatibility"])) > 500:
        err(f"{rel}/SKILL.md: compatibility > 500 chars")
    for sec in REQUIRED_SKILL_SECTIONS:
        if not re.search(rf"^##+ .*{re.escape(sec)}", body, re.M):
            err(f"{rel}/SKILL.md: missing section containing '{sec}'")
    if "safety/crisis.md" not in body or CRISIS_MARKER not in body:
        err(f"{rel}/SKILL.md: safety handoff must reference safety/crisis.md and '{CRISIS_MARKER}'")
    if len(body.splitlines()) > 500:
        warnings.append(f"{rel}/SKILL.md: body > 500 lines (spec recommends splitting)")


def check_links() -> None:
    link_re = re.compile(r"\]\(([^)\s]+)\)")
    tick_re = re.compile(r"`((?:skills|prompts|safety|research|vendor|scripts)/[^`\s]+)`")
    for md in ROOT.rglob("*.md"):
        relmd = md.relative_to(ROOT)
        parts = relmd.parts
        if parts[0] in (".git", "journal", ".claude", ".agents"):
            continue
        text = read(md)
        for target in link_re.findall(text):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = target.split("#")[0]
            if path and not (md.parent / path).exists():
                err(f"{relmd}: broken link -> {target}")
        if parts[0] == "vendor":
            continue
        for ref in tick_re.findall(text):
            if any(c in ref for c in "<>*{}"):
                continue
            ref = ref.rstrip(".,;:")
            if not (ROOT / ref).exists():
                err(f"{relmd}: referenced path does not exist: {ref}")


def iter_text_files():
    for f in ROOT.rglob("*"):
        rel = f.relative_to(ROOT)
        if rel.parts[0] in (".git", "journal") or "__pycache__" in rel.parts:
            continue
        if f.is_symlink() or not f.is_file() or f.suffix not in TEXT_SUFFIXES:
            continue
        if f.name == "validate.py":  # contains the patterns themselves
            continue
        yield f, rel


def check_content() -> None:
    for f, rel in iter_text_files():
        try:
            text = read(f)
        except UnicodeDecodeError:
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if CYRILLIC_RE.search(line) and rel.parts[0] != "research":
                err(f"{rel}:{n}: Cyrillic text (repo is English-only; practices run in the user's language at runtime)")
            if PHONE_RE.search(line):
                err(f"{rel}:{n}: phone/helpline number found (use generic crisis wording)")
            if HELPLINE_RE.search(line):
                err(f"{rel}:{n}: helpline directory reference found (use generic crisis wording)")
        if rel.parts[0] == "research" and CYRILLIC_RE.search(text):
            warnings.append(f"{rel}: contains Cyrillic (allowed in research/ only for original quotes)")


def main() -> int:
    mpath = ROOT / "manifest.yaml"
    if not mpath.is_file():
        print("ERROR: manifest.yaml missing")
        return 1
    manifest, parser_name = load_yaml(read(mpath))
    print(f"manifest.yaml parsed with {parser_name}")

    for key in ("safety",):
        check_file(manifest.get(key, ""), "manifest." + key)
    for k, v in (manifest.get("research") or {}).items():
        check_file(v, f"manifest.research.{k}")
    sd = manifest.get("session_defaults") or {}
    for lang, v in (sd.get("prompts") or {}).items():
        p = check_file(v, f"session_defaults.prompts.{lang}")
        if p and CRISIS_MARKER not in read(p):
            err(f"{v}: no crisis handoff ('{CRISIS_MARKER}')")
    if lang_keys := [k for k in (sd.get("prompts") or {}) if k != "en"]:
        err(f"session_defaults.prompts: only 'en' allowed, found {lang_keys}")
    for f in ("applies_when", "does_not_apply_when"):
        if not sd.get(f):
            err(f"session_defaults: missing '{f}'")

    practices = manifest.get("practices") or []
    ids = [p.get("id") for p in practices]
    if len(ids) != len(set(ids)):
        err("manifest: duplicate practice ids")
    numbers = sorted(p.get("number") for p in practices)
    if numbers != list(range(1, len(practices) + 1)):
        err(f"manifest: practice numbers should be 1..N, got {numbers}")
    for sid in sd.get("practices") or []:
        if sid not in ids:
            err(f"session_defaults references unknown practice {sid!r}")

    for p in practices:
        pid = p.get("id", "?")
        ctx = f"practice {pid}"
        for f in REQUIRED_PRACTICE_FIELDS:
            if f not in p:
                err(f"{ctx}: missing field '{f}'")
        if p.get("evidence_level") not in EVIDENCE_LEVELS:
            err(f"{ctx}: evidence_level {p.get('evidence_level')!r} not in {sorted(EVIDENCE_LEVELS)}")
        if p.get("activation") not in ACTIVATION_MODES:
            err(f"{ctx}: activation {p.get('activation')!r} not in {sorted(ACTIVATION_MODES)}")
        for f in ("applies_when", "does_not_apply_when", "triggers"):
            v = p.get(f)
            if not (isinstance(v, list) and v and all(isinstance(x, str) and x for x in v)):
                err(f"{ctx}: '{f}' must be a non-empty list of strings")
        for vname, vpath in (p.get("variants") or {}).items():
            check_file(vpath, f"{ctx} variant {vname}")
        if not p.get("sources"):
            err(f"{ctx}: no sources")
        skill = p.get("skill", "")
        if skill != f"skills/{pid}/SKILL.md":
            err(f"{ctx}: skill path should be skills/{pid}/SKILL.md (got {skill})")
        check_file(skill, ctx)
        extra_langs = [k for k in (p.get("prompts") or {}) if k != "en"]
        if extra_langs:
            err(f"{ctx}: only 'en' prompts allowed, found {extra_langs}")
        for lang in ("en",):
            rel = (p.get("prompts") or {}).get(lang)
            if not rel:
                err(f"{ctx}: missing prompts.{lang}")
                continue
            path = check_file(rel, ctx)
            if path:
                t = read(path)
                if "```" not in t:
                    err(f"{rel}: no fenced prompt block")
                if CRISIS_MARKER not in t:
                    err(f"{rel}: no crisis handoff ('{CRISIS_MARKER}')")
        for c in p.get("composes_with") or []:
            if c not in ids:
                err(f"{ctx}: composes_with unknown id {c!r}")
        closing = p.get("closing")
        if closing not in ("none", "optional", "self") and closing not in ids:
            err(f"{ctx}: closing {closing!r} is not none/optional/self or a practice id")
        for agent_dir in (".claude/skills", ".agents/skills"):
            link = ROOT / agent_dir / pid
            if not (link / "SKILL.md").is_file():
                err(f"{ctx}: {agent_dir}/{pid}/SKILL.md not reachable")
            elif (link.resolve()) != (ROOT / "skills" / pid).resolve():
                err(f"{ctx}: {agent_dir}/{pid} does not resolve to skills/{pid}")

    skill_dirs = sorted(d for d in (ROOT / "skills").iterdir() if d.is_dir())
    for d in skill_dirs:
        check_skill(d, parser_name)
        if d.name not in ids:
            err(f"skills/{d.name}: not listed in manifest.yaml")
    for agent_dir in (".claude/skills", ".agents/skills"):
        for d in (ROOT / agent_dir).iterdir():
            if d.name not in ids:
                err(f"{agent_dir}/{d.name}: not in manifest")

    vendor = ROOT / "vendor"
    if vendor.is_dir():
        for d in vendor.iterdir():
            if d.is_dir():
                for need in ("LICENSE", "ATTRIBUTION.md"):
                    if not (d / need).is_file():
                        err(f"vendor/{d.name}: missing {need}")

    for need in ("AGENTS.md", "CLAUDE.md", "README.md", "LICENSE", "safety/crisis.md"):
        check_file(need, "repo")
    if "@AGENTS.md" not in read(ROOT / "CLAUDE.md"):
        err("CLAUDE.md does not import @AGENTS.md")
    gi = ROOT / ".gitignore"
    if not gi.is_file() or not re.search(r"^/?journal/?$", read(gi), re.M):
        err(".gitignore must ignore journal/")

    for pf in (ROOT / "prompts").rglob("*.md"):
        if not pf.name.endswith(".en.md"):
            err(f"{pf.relative_to(ROOT)}: only *.en.md prompt files are allowed (English only)")

    check_content()
    check_links()

    print(f"practices: {len(practices)} | skills: {len(skill_dirs)} | "
          f"prompts: {len(list((ROOT / 'prompts').rglob('*.md')))}")
    for w in warnings:
        print(f"WARNING: {w}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        print(f"FAILED: {len(errors)} error(s)")
        return 1
    print("OK: all checks passed")
    return 0


if __name__ == "__main__":
    os.chdir(ROOT)
    sys.exit(main())
