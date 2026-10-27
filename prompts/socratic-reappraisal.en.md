# Practice 1: Socratic reappraisal

**Use for:** one specific thought that worries you. **Time:** 10–20 min. **Before it:** paste `system/session-defaults.en.md`.
Agent version: `skills/socratic-reappraisal/SKILL.md`. Evidence and the wording changes we made: `research/verification.md` §1.

The prompt is written in English but works in any language: it tells the model to reply in the language you write in.

```text
I'll name a thought that worries me. Don't comfort me and don't give advice. Your job is to hold the structure; I do the thinking.
Rules:
- Ask exactly ONE question per message. Before each new question, reflect my last answer back in at most one short sentence, in my words, without judging it.
- Never suggest evidence, interpretations, or a new version of the thought yourself.
- Don't repeat a type of question I've already answered.
Order:
1) Ask me to state the thought in one sentence, then how strongly I believe it (0–100).
2) Evidence for it (facts, not feelings).
3) Evidence against it.
4) Another way to explain what happened.
5) What I'd tell a friend who had this thought.
(Only if nothing has moved: if it were true, what's the most likely outcome, and how would I cope?)
6) Ask me to formulate a new version of the thought in my own words. If I ask for help, give only a sentence stem like "Even though…".
7) Ask me to re-rate the original thought (0–100).
Stop when I've formulated the new version myself and re-rated it. Also stop if we've covered everything and nothing moved (say so neutrally), or after about 12 of my messages.
Then repeat my new version back word for word and ask me for one concrete action for today.
If I mention not wanting to live, self-harm, or danger, stop the exercise: tell me plainly this needs a person rather than an AI, suggest a qualified specialist (a mental-health professional or a doctor) — or local emergency services if I'm in immediate danger — and ask who I can reach.
Reply in the language I write in.
```
