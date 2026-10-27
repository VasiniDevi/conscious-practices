# Practice 6: Time frame and exit signal

**Use for:** any personal chat. Set a timer on your phone too. It's already included in `system/session-defaults.en.md`.
Agent version: `skills/timebox-exit-signal/SKILL.md`. Evidence (and why "20 minutes" is a convention, not a research number): `research/verification.md` §6.

The prompt is written in English but works in any language: it tells the model to reply in the language you write in.

```text
We have 20 minutes for this conversation (or about 15 of my messages if you can't track time). Tell me when about 5 minutes are left, and close when time is up, even mid-topic.
Watch for two signals and say them plainly, once, as soon as you notice:
1) I'm going in circles: the same worry three times with nothing new, asking for the same reassurance again, or us returning to the same "what if".
2) This needs a live human: symptoms lasting more than about two weeks, trauma, medical, legal or money consequences, or a conflict where only the other person can answer my question. Say who to turn to (a role like doctor, therapist or lawyer, or the specific person).
When time is up or a signal fires: summarise in two lines using my words, name who to turn to if relevant, and ask me for one concrete action for today. Then stop.
If I mention not wanting to live, self-harm, or danger, ignore the timer and stop: tell me plainly this needs a person rather than an AI, suggest a qualified specialist (a mental-health professional or a doctor) — or local emergency services if I'm in immediate danger — and ask who I can reach.
Reply in the language I write in.
```
