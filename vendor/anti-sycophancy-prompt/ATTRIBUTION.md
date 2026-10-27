# Attribution

- **Work:** "AI Tool For Thought — System Prompt" (`prompt.md`)
- **Author:** Talha Pythoneer
- **Source:** https://github.com/talhapythoneer/anti-sycophancy-prompt
- **Commit vendored:** `d940a2c7ed210c6edc9300e64ff3798d49a41b4a` (fetched 2026-10-27)
- **Licence:** MIT. The full text is in [`LICENSE`](LICENSE) in this directory and applies to the files here.
- **Modifications:** none. `prompt.md` is byte-for-byte as published. The upstream `sources.md` (42 references) was not vendored; see the upstream repo.

## How this repo uses it

This prompt is the **work/analytical variant** of practice 2 (`skills/anti-sycophancy`). The agent selects the variant from the conversation's context; the user doesn't choose (`AGENTS.md` §4.2):

| Context | Variant |
|---|---|
| Work or analytical chat (reviewing ideas, plans, code, texts, research, strategy) **and** the user asserts a claim, asks for evaluation, makes a decision, or pushes back without new evidence | **This prompt** (12-point "tool for thought" contract) |
| Personal, emotional, or decision conversation | Our short prefix, `prompts/system/anti-sycophancy.en.md` |
| Pure execution request, factual lookup, or crisis | Neither |

Its point 10 ("When I say 'just execute', drop all of the above") matches our do-not-apply rule for execution requests.
