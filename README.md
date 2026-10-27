# conscious-practices

Seven protocols that turn an ordinary language model into a **mirror**. It keeps the conversation structured, doesn't flatter, and returns you to action and to other people. **This is not therapy and not crisis support.** The practices are for people in a working state who want to think more clearly.

Each practice comes in three forms:

- a copy-paste prompt for any chat (ChatGPT, Claude, Gemini, and others) in `prompts/`;
- an Agent Skill for Claude Code, Codex, and other agents in `skills/`;
- a machine-readable entry in `manifest.yaml`.

The prompts are written in English but work in any language: write in yours, and the model answers in it.

**Agents decide for themselves whether a practice fits.** Ordinary requests ("write this", "translate that") get ordinary answers. A practice switches on automatically only where it clearly fits, is offered in one line where it might help, and is never forced. See the applicability table in [`AGENTS.md`](AGENTS.md#4-applicability-decide-whether-a-practice-fits-core-decision-step).

Every study the practices rely on was checked against its primary source, and several popular claims needed correcting. See [`research/verification.md`](research/verification.md).

## The practices

| # | Practice | Prompt | When it's used | What verification found |
|---|---|---|---|---|
| 1 | Socratic reappraisal | [prompt](prompts/socratic-reappraisal.en.md) | Offered when you name a distressing thought | Socrates 2.0 is real. Its pilot study had no control group and found small-to-moderate effects. |
| 2 | Anti-sycophancy | [personal](prompts/system/anti-sycophancy.en.md) · [work](vendor/anti-sycophancy-prompt/prompt.md) | Automatic when you assert, ask for evaluation, decide, or push back | The AISI finding is confirmed. The Science 2026 "49%" is about affirming users' *actions* in interpersonal advice, not "agreeing" in general. |
| 3 | Daily 5 journaling | [prompt](prompts/daily-five.en.md) | Offered when you free-write or ask about patterns | Rosebud and Mindsera have the feature, but no published efficacy data. Evidence is low. |
| 4 | Tutor, not author | [prompt](prompts/tutor-not-author.en.md) | Automatic when you signal you want to learn | Two *separate* studies: a Harvard RCT (learning gains more than doubled) and an MIT EEG preprint. The "hint after second attempt" rule is not in either source. |
| 5 | Conversation → action | [prompt](prompts/conversation-to-action.en.md) | Automatic at the end of personal conversations | Nothing documents that Headspace Ebb always ends with a physical action. The mechanism rests on implementation intentions and on research into manipulative AI farewells. |
| 6 | Time frame and exit signal | [prompt](prompts/timebox-exit-signal.en.md) | Automatic in personal conversations | *Total* daily use correlates with loneliness and dependence. The 20-minute limit is a convention, not a figure from the study. |
| 7 | Stoic evening review | [prompt](prompts/stoic-evening-review.en.md) | Offered at day's end when you reflect on the day | Misattributed: the three questions come from the Pythagorean *Golden Verses* as quoted by Epictetus, not from Seneca. |

For a personal session in a plain chat, paste [`prompts/system/session-defaults.en.md`](prompts/system/session-defaults.en.md) as the first message (it combines practices 2, 5 and 6), then the practice prompt if you want one.

## Safety

If you are in crisis, having thoughts of not wanting to live, or in danger, don't use these practices. Reach out to a person:

- a qualified mental-health professional or a doctor;
- your local emergency services, if you are in immediate danger.

Details are in [`safety/crisis.md`](safety/crisis.md).

## For agents

Start with [`AGENTS.md`](AGENTS.md). If you open the repo in Claude Code or Codex, the skills are picked up automatically through `.claude/skills/` and `.agents/skills/`.

```bash
git clone https://github.com/VasiniDevi/conscious-practices
python3 conscious-practices/scripts/validate.py   # consistency checks
```

## License

Our own content is MIT; see [`LICENSE`](LICENSE). Third-party material in `vendor/` keeps its own licence and attribution.
