# Practice 5: Conversation → action

**Use for:** the end of any emotional or personal conversation. It's already included in `system/session-defaults.en.md`; use this standalone version to add it to an ongoing chat.
Agent version: `skills/conversation-to-action/SKILL.md`. Evidence: `research/verification.md` §5.

The prompt is written in English but works in any language: it tells the model to reply in the language you write in.

```text
Let's close this conversation. Ask me for ONE concrete action I'll do today: something doable within about 30 minutes that's physical and real-world, not more thinking.
- Let me choose it. Only if I'm stuck, offer up to three options in this order: contact a specific person (call or message), move my body (a walk, 10 minutes of slow breathing), or write (a letter, sent or not).
- If my answer is vague, ask once: "What exactly, and when?" I want a plan with what, when, where, and with whom.
- Then restate my plan in one line and stop.
- Don't end with "I'm always here for you", don't invite me to come back and report, and don't try to keep the conversation going. If I decline, just say "Okay" and end.
- If I mention not wanting to live, self-harm, or danger, stop: tell me plainly this needs a person rather than an AI, suggest a qualified specialist (a mental-health professional or a doctor) — or local emergency services if I'm in immediate danger — and ask who I can reach.
Reply in the language I write in.
```
