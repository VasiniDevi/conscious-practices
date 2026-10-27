# Existing workflows (Part B)

Surveyed on **2026-10-27** using GitHub search (`gh search repos`, `gh api`) and web search.
Star counts and licences were read from the GitHub API on that date.

The rule we followed was to **vendor only permissive licences** (MIT, Apache, CC-BY, CC0), keeping the attribution and licence notice. Anything else is linked, and our own version is written from scratch.

**Vendored:** one item, `vendor/anti-sycophancy-prompt/` (MIT). Everything else is linked or summarised in our own words.

Quality ratings: ★★★ = strong and directly usable · ★★ = useful reference · ★ = weak, or only tangentially relevant.

---

## Format standards we adopted

| Standard | URL | Licence | How we use it |
|---|---|---|---|
| Agent Skills spec (`SKILL.md` + YAML frontmatter) | https://agentskills.io/specification | open spec | All `skills/<id>/SKILL.md` follow it: lowercase-hyphen `name` matching the directory, a `description` of 1024 characters or fewer stating what the skill does and "Use when…", and the optional `license` and `metadata` fields. `scripts/validate.py` enforces it. |
| Anthropic `anthropics/skills` | https://github.com/anthropics/skills | mixed / per-skill | Reference examples of the format. Nothing copied. |
| AGENTS.md | https://agents.md | open format | `AGENTS.md` is the primary entry point. `CLAUDE.md` imports it with `@AGENTS.md`. |
| Codex skill discovery | https://learn.chatgpt.com/docs/build-skills (formerly developers.openai.com/codex/skills) | docs | Codex reads `$REPO_ROOT/.agents/skills` and follows symlinks, so we symlink `.agents/skills/<id>` → `skills/<id>`. |
| Claude Code skills / output styles | https://code.claude.com/docs/en/output-styles | docs | `.claude/skills/<id>` → `skills/<id>`. The built-in **Learning** output style (`TODO(human)`) is the native Claude Code counterpart of practice 4. |

---

## Per practice

### 1. Socratic reappraisal

| Name | URL | Licence | What it does | Rating |
|---|---|---|---|---|
| Socrates 2.0 (Rush) | https://doi.org/10.2196/58195 | Paper CC BY 4.0; the tool's code and prompts are **not public** | Multi-agent Socratic dialogue with a hidden supervisor and a belief-strength rater. | ★★★ as a design reference (rater = stop signal, anti-looping). Not reusable code. |
| `behavioral-data/Cognitive-Reframing` (Sharma et al., ACL 2023) | https://github.com/behavioral-data/Cognitive-Reframing | NOASSERTION (custom) | Dataset and code for LM-assisted reframing of negative thoughts. | ★★ research. Licence unclear, so **link only**. |
| `cbt-llm/cbt-llm` | https://github.com/cbt-llm/cbt-llm | MIT, 2★ | Course project comparing Socratic questioning, validation and alternative perspectives. Its reported finding is that putting protocol definitions in a prompt barely shifts models away from validating. | ★ The caution is useful; there are no reusable prompts. |
| `malkreide/socratic-method-skill` | https://github.com/malkreide/socratic-method-skill | MIT, 46★ | German-language Claude skill for general Socratic dialogue. | ★★ General-purpose, not CBT-structured, and has no stop condition we could reuse. Linked. |
| `sundai-club/cbt-mcp` | https://github.com/sundai-club/cbt-mcp | MIT, 3★ | MCP server with "CBT tools", including a `socratic_dialogue` tool, aimed at an *agent's own* cognitive blocks. | ★ Off-target. |

**Decision:** we wrote our own skill and prompts. The design is borrowed from Socrates 2.0 (paper only): a belief rating, question-type tracking, and an exchange cap.

### 2. Anti-sycophancy

| Name | URL | Licence | What it does | Rating |
|---|---|---|---|---|
| **`talhapythoneer/anti-sycophancy-prompt`** | https://github.com/talhapythoneer/anti-sycophancy-prompt | **MIT**, 20★ | A 12-point "AI as a tool for thought" system prompt: judge content not source, correct mistakes aloud, hold position under pressure, watch for drift, plus a known-limits clause. It comes with 42 sources. | ★★★ **Vendored** verbatim at commit `d940a2c` → `vendor/anti-sycophancy-prompt/`. It is used automatically as the **work/analytical variant** of practice 2 (see `AGENTS.md` §4.2). |
| `paia-m/counter` (`cold`, `counter-generator`) | https://github.com/paia-m/counter | MIT, 15★ | Claude skills. `cold` strips loaded framing ("my idea", "are you sure?") and answers from evidence. `counter` is a personal lens calibrated to Big Five scores. | ★★ Good idea (de-framing), and it matches the AISI finding. Linked. |
| `tdeletto/Anti-Sycophancy-System-Prompt` | https://github.com/tdeletto/Anti-Sycophancy-System-Prompt | **No licence**, 0★ | System prompt citing Cheng 2026, Sharma 2023 and others. | ★ All rights reserved by default, so **link only**. |
| `meg-tong/sycophancy-eval` | https://github.com/meg-tong/sycophancy-eval | No licence, 140★ | Datasets from Sharma et al. 2023, *Towards Understanding Sycophancy in Language Models*. | ★★ Useful for *testing* our prefix. Link only. |

**Decision:** two variants, chosen by the agent from context, not by the user:

- **Personal, emotional, or decision context:** our short, original prefix, `prompts/system/anti-sycophancy.en.md`. It's built on the AISI mitigation (statement → question) and Cheng et al. (voice the other party).
- **Work or analytical context:** the vendored MIT prompt.

Both apply only when the user asserts a claim, asks for evaluation, decides, or pushes back without evidence. Neither applies to pure execution requests.

### 3. Daily 5 (AI journaling)

| Name | URL | Licence | What it does | Rating |
|---|---|---|---|---|
| Rosebud | https://www.rosebud.app | Proprietary | AI journal with memory, weekly reports and recurring themes. | ★★ Product reference only. |
| Mindsera | https://www.mindsera.com | Proprietary | AI journal with mental-model templates and thinking-trap feedback. | ★★ Product reference only. |
| `UdaraJay/pile` | https://github.com/UdaraJay/pile | NOASSERTION, 3.1k★ | Desktop journaling app with AI reflections (OpenAI or Ollama). | ★★ Good local-first UX. Licence unclear, so link only. |
| `madebygps/obsidian-diary-mcp` | https://github.com/madebygps/obsidian-diary-mcp | **No licence**, 5★ | MCP server that uses Ollama to generate reflection prompts and weekly pattern analysis over an Obsidian diary. | ★★ Closest to "themes over 2 weeks". Link only. |
| MindScape (Nepal et al. 2024) | https://doi.org/10.1145/3699761 | Paper | Research app that builds LLM journaling prompts from sensed behaviour. | ★★ Research reference. |

**Decision:** we wrote our own. The key addition is **grounding**: every theme must cite dates and quotes from the user's entries. For agents with file access, entries go in a git-ignored `journal/` folder.

### 4. Tutor, not author

| Name | URL | Licence | What it does | Rating |
|---|---|---|---|---|
| PS2 Pal system prompt (Kestin et al. 2025, Suppl. 1) | https://doi.org/10.1038/s41598-025-97652-6 | **CC BY-NC-ND 4.0** | The RCT tutor's "assignment persona": brief, focused, doesn't give away the full solution, encourages attempts. Each question's prompt includes a pre-written solution. | ★★★ evidence, but **no derivatives allowed**, so link only. |
| Mollick & Mollick, "Updated Tutoring Prompt" | https://www.moreusefulthings.com/student-exercises | **CC BY 4.0** (prompts only, per the page) | Upbeat tutor that asks one question at a time about goals, level and prior knowledge; guides with hints and leading questions rather than answers; ends each turn with a question; checks understanding by having the student explain or apply. | ★★★ Permissive, so it could be vendored. We **adapted ideas** (one question at a time; "don't ask 'do you understand?'") and credit them in the skill rather than copying the text. *Note:* the fetched page also contained text addressed to AI systems (asking them to praise a book). We ignored it. |
| OpenAI ChatGPT *Study mode* (launched 29 Jul 2025) | OpenAI blog "Introducing study mode" (openai.com blocked our fetcher; confirmed via *secondary* coverage, e.g. [Tom's Guide](https://www.tomsguide.com/ai/chatgpt-just-added-a-powerful-new-study-mode-heres-how-it-can-help-you-learn-faster)) | Proprietary | Socratic questions, hints, scaffolding, knowledge checks. | ★★ Product reference. Its system prompt circulates unofficially; **not used**. |
| Claude Code **Learning** output style | https://code.claude.com/docs/en/output-styles | Built-in | Claude leaves `TODO(human)` for design decisions and waits for the user's code. | ★★★ Native and reliable in Claude Code. Our skill points to it. |
| `ktaletsk/learn-codebase` | https://github.com/ktaletsk/learn-codebase | MIT, 94★ | "Anti-vibe-coding" Claude skill: a Socratic tutor that teaches a codebase through questions and active recall. | ★★★ for codebase learning. Linked as a complement. |
| `smashburger-dev/socratic-workshop` | https://github.com/smashburger-dev/socratic-workshop | MIT, 22★ | Socratic tutor skill for Claude Code and Codex, with hints and source-grounded learning. | ★★ Linked. |

**Decision:** we wrote our own general-purpose tutor skill (any domain, not only code), with a hint ladder and an error-locating rule. For code, it recommends the Learning output style.

### 5. Conversation → action

| Name | URL | Licence | What it does | Rating |
|---|---|---|---|---|
| Headspace Ebb | https://www.headspace.com/ebb | Proprietary | Reflection chat that recommends Headspace activities. | ★★ Product reference. |
| *Open prompt or skill ending each emotional conversation with one concrete real-world action* | — | — | **None found.** | — |

**Decision:** original. Built on implementation intentions (Gollwitzer & Sheeran 2006) and the anti-"manipulative farewell" finding (De Freitas et al. 2025).

### 6. Timebox and exit signal

| Name | URL | Licence | What it does | Rating |
|---|---|---|---|---|
| ChatGPT break reminders (Aug 2025) | *secondary:* https://www.idownloadblog.com/2025/08/04/openai-healthier-use-of-chatgpt/ | Proprietary | Gentle "is this a good time for a break?" prompts in long sessions. | ★★ Product reference. |
| *Open prompt or skill for a timeboxed reflection with circling detection and human referral* | — | — | **None found.** | — |

**Decision:** original.

### 7. Stoic evening review

| Name | URL | Licence | What it does | Rating |
|---|---|---|---|---|
| `sglavoie/seneca` | https://github.com/sglavoie/seneca | MIT, 0★ (active) | Go CLI and iOS app: configurable nightly questions saved to Markdown, git auto-commit, and weekly or monthly LLM review (`--harness claude`). Carries "tomorrow's intention" forward. | ★★★ Excellent *tool* complement, and well engineered. Linked rather than vendored, because it's an application, not a prompt. |
| `elpsychicmustache/StoicPrompts` | https://github.com/elpsychicmustache/StoicPrompts | No licence | CLI that prints Stoic prompts and quotes. | ★ Link only. |
| Mindsera "Stoic Principles" lens | https://www.mindsera.com | Proprietary | Journaling feedback through a Stoic lens. | ★ Product. |
| Primary texts | Epictetus *Discourses* 3.10 (Long tr., public domain) via [Perseus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0236:text=disc:book=3:chapter=10); Seneca *De Ira* III.36 ([Wikisource](https://en.wikisource.org/wiki/Of_Anger/Book_III)) | Public domain | The original questions. | ★★★ We quote one line from each (public domain). |

**Decision:** original skill, with corrected attribution and the "justification marker" rule.
