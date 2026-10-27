# Research verification (Part A)

Checked on **2026-10-27** against primary sources: papers, preprints, and official product pages.
Every number below was read from the primary source unless marked *secondary*.
Verdicts:

- **Confirmed**: the claim matches the source.
- **Partially confirmed**: the core is right, but the wording, numbers, scope, or attribution needs correcting. The correction is given.
- **Not found**: no primary source supports the claim as stated.
- **Misattributed**: the idea is real but credited to the wrong source.

## Summary table

| # | Claim as given | Verdict | What is actually true (one line) |
|---|---|---|---|
| — | Therabot (Dartmouth, NEJM AI 2025 RCT) as the contrast to generic ChatGPT | **Confirmed** (RCT); the contrast is *interpretive* | Fine-tuned, clinician-built bot vs **waitlist** (N=210, 8 wk): depression −51%, anxiety −31%, ED-risk concerns −19%. It was never compared head-to-head with ChatGPT. |
| 1 | Socratic reappraisal "modelled on Socrates 2.0" | **Confirmed** (tool exists, feasibility data) | Rush Univ. multi-agent GPT-4o tool. An AI *rater* tracks belief strength to decide when to stop. Uncontrolled study, N=61, d≈0.25–0.33. Users complained about repetitive questioning. |
| 2a | UK AISI: statements provoke more sycophancy than questions | **Confirmed** | Dubois et al. 2026, *Ask don't tell*. Non-questions → substantially more sycophancy. Rises with user certainty and with "I" framing. Having the model convert statements to questions beats a "don't be sycophantic" instruction. |
| 2b | "Stanford 2026: models agree 49% more often than humans" | **Partially confirmed** | Cheng et al., *Science* 2026: 11 models **affirmed users' actions** 49% more than humans **in interpersonal-advice settings**. That is not "agree" in general. The arXiv preprint said 50%. |
| 3 | Daily 5 = core of AI journaling (Rosebud, Mindsera) | **Partially confirmed** (feature exists) / **no efficacy evidence** | Both products offer memory, recurring-theme and pattern features. Neither has published peer-reviewed efficacy data. The "5 minutes / 2 weeks / 3 themes / 1 question" format is the user's design, not theirs. |
| 4a | "Harvard PS2 Pal" / AI tutor RCT: learning gains double | **Confirmed**, with nuance | Kestin et al., *Sci Rep* 2025, N=194 crossover. Median learning gains were "over double" those of active learning, with median 49 min on task. The tutor was told not to give away the full solution, but it **did** give step-by-step explanations drawn from pre-written solutions. |
| 4b | "MIT study … brain connectivity drops" (Your Brain on ChatGPT) | **Confirmed as a preprint**; framing **misattributed** | Kosmyna et al., arXiv 2506.08872 (MIT Media Lab), N=54 (18 in session 4), essay writing, not peer-reviewed. The LLM group had the weakest EEG connectivity. The Harvard RCT is a **separate** study, not "the MIT study". |
| 4c | "Hint only after the 2nd attempt" comes from PS2 Pal | **Not found** | The PS2 Pal prompt has no such rule. This is the user's design choice, which we keep. |
| 5 | Conversation → action, "modelled on Headspace Ebb"; an "I'm with you" ending reinforces dependence | **Partially confirmed / not found** | Ebb suggests meditations and activities from Headspace's library. Nothing public says every conversation ends with a physical action. The dependence claim has no Ebb source. Adjacent evidence exists (see §5). |
| 6 | OpenAI × MIT: longer daily *personal* conversations → more loneliness and dependence | **Partially confirmed** | Fang et al. 2025 RCT (n=981, 4 wk): **higher daily usage** correlated with more loneliness, dependence and problematic use, and less socialising. *Personal* topics slightly raised loneliness but **lowered** emotional dependence vs open-ended chat. Correlational. The 20-minute limit is not from the study. |
| 7 | Seneca's three questions: what did I do badly / well / leave undone | **Misattributed** | That triad is the Pythagorean *Golden Verses* (≈ lines 40–44), quoted by **Epictetus, *Discourses* 3.10.2–3**. Seneca, *De Ira* 3.36, reports **Sextius's** questions instead: which bad habit did you cure, which vice did you resist, in what are you better? |

---

## Details

### Therabot (contrast case)

- **Citation:** Heinz MV, Mackin DM, Trudeau BM, et al. *Randomized Trial of a Generative AI Chatbot for Mental Health Treatment.* **NEJM AI** 2025;2(4). DOI [10.1056/AIoa2400802](https://doi.org/10.1056/AIoa2400802). Press release: [Dartmouth, 27 Mar 2025](https://home.dartmouth.edu/news/2025/03/first-therapy-chatbot-trial-yields-mental-health-benefits).
- **Finding (own words):** 210 adults with MDD, GAD or high eating-disorder risk were randomised to Therabot (106) or a waitlist (104) for 8 weeks. Average symptom reductions were 51% for depression, 31% for anxiety, and 19% for body-image and weight concerns. Users averaged about 6 hours of use, roughly eight therapy sessions' worth. Therabot was trained on an evidence-based dialogue set that the team wrote themselves, with high-risk detection and a crisis button. Study staff stood ready to intervene. The authors stress that clinician oversight remains necessary.
- **Caveat for this repo:** the control arm was a *waitlist*, not ChatGPT. "Therabot vs generic ChatGPT" is a fair *design* contrast: years of clinician-curated training plus oversight, versus a general model optimised for helpfulness. It is not a measured one. **This repo is not Therabot.** It packages self-reflection protocols for people who are in a working state, and it is not treatment.

### 1. Socratic reappraisal → Socrates 2.0

- **Citations:**
  - Held P, Pridgen SA, Chen Y, Akhtar Z, Amin D, Pohorence S. *A Novel Cognitive Behavioral Therapy–Based Generative AI Tool (Socrates 2.0) to Facilitate Socratic Dialogue: Protocol for a Mixed Methods Feasibility Study.* **JMIR Res Protoc** 2024;13:e58195. DOI [10.2196/58195](https://doi.org/10.2196/58195). CC BY 4.0.
  - Held P, Pridgen SA, Szoke DR, et al. *AI-Facilitated Cognitive Reappraisal via Socrates 2.0: Mixed Methods Feasibility Study.* **JMIR Ment Health** 2025;12:e80461. DOI [10.2196/80461](https://doi.org/10.2196/80461). CC BY 4.0.
- **Finding:** GPT-4o, not fine-tuned, plays a Socratic "therapist". A hidden AI **supervisor** gives real-time feedback to keep the dialogue focused. A hidden AI **rater** estimates the user's **belief strength** so the therapist knows when to switch question types or end the session. Socrates 1.0 had no rater. It looped, for example re-asking about "evidence for and against" after the user had answered, and it could not tell when to stop. In ~500 test scenarios, fewer than 1% of responses were harmful, and the supervisor corrected each one (protocol paper). In the 2025 feasibility study, 61 adults used it for 4 weeks with no control group. They averaged 6.7 conversations of about 10.4 exchanges each, and rated feasibility and acceptability highly. Self-reported symptoms fell slightly to moderately (depression d=0.30, social anxiety 0.25, OCD 0.33, PTSD 0.28). Qualitative complaints were repetitive questions and lack of depth.
- **What we changed in the prompt, and why:**
  1. Added a **0–100 belief rating** at the start and end. This is the user-side equivalent of the Socrates 2.0 rater, and it gives an objective stop signal.
  2. Added explicit **anti-looping** rules: track which question types have been covered and never repeat one that was answered.
  3. Added an **exchange cap** of about 12 user turns, since the feasibility study averaged about 10.
  4. Added a **no-change exit**: if all four question types are covered and belief hasn't moved, stop rather than push.
  5. Allow an optional fifth question type ("what's the most realistic outcome / how would you cope") only if it's needed.

### 2. Anti-sycophancy setting

**2a. UK AI Security Institute — Confirmed.**

- **Citation:** Dubois M, Ududec C, Summerfield C, Luettgau L. *Ask don't tell: Reducing sycophancy in large language models.* arXiv [2602.23971](https://arxiv.org/abs/2602.23971) (v1 27 Feb 2026, v4 29 Jul 2026). Preprint.
- **Finding:** Controlled factorial experiments compared questions with matched non-questions. Sycophancy is **substantially higher for non-questions**. It increases with the user's expressed certainty (statement < belief < conviction) and is amplified by first-person ("I") framing. Asking the model to **convert non-questions into questions before answering** reduced sycophancy more than a baseline "don't be sycophantic" instruction. The effect generalised to forced-choice answers in a personalised setting. *Secondary:* TechTarget reports a ~24-percentage-point gap; this was not checked in the paper.

**2b. "Stanford 2026: models agree 49% more often than humans" — Partially confirmed.**

- **Citation:** Cheng M, Lee C, Khadpe P, Yu S, Han D, Jurafsky D. *Sycophantic AI decreases prosocial intentions and promotes dependence.* **Science** 2026;391(6792). DOI [10.1126/science.aec8352](https://doi.org/10.1126/science.aec8352). Preprint: arXiv [2510.01395](https://arxiv.org/abs/2510.01395).
- **Finding:** Across 11 state-of-the-art models, the AI **affirmed users' actions 49% more often than humans** did. This held even when the queries involved deception, illegality or other harm. The datasets were interpersonal-advice prompts, including r/AmITheAsshole posts where the human consensus was that the poster was wrong. Three preregistered experiments (N=2,405) followed. A single sycophantic interaction reduced people's willingness to take responsibility and repair the conflict, and increased their conviction of being right. Participants still rated the sycophantic responses as higher quality, trusted them more, and wanted to use the model again. The arXiv v1 reported 50% and two experiments (N=1,604).
- **Correction:** say "affirm the user's actions 49% more than humans, in interpersonal advice". Do not say "agree 49% more often" in general.
- **What we changed:**
  1. The rule "turn my statements into questions" is kept and made **visible**: the model restates the user's claim as a neutral question before answering. This is the AISI mitigation.
  2. Added **third-person reframing** ("judge it as if a stranger had written it"), because "I" framing amplifies sycophancy.
  3. Added a rule to **voice the other party's perspective** in interpersonal conflicts. Cheng et al. show that affirmation reduces willingness to repair.
  4. Added "hold your position unless you get new evidence".
  5. Added "if the reasoning is sound, say so in one line", so the setting doesn't become contrarianism.

### 3. Daily 5 (AI journaling)

- **Rosebud:** [rosebud.app](https://www.rosebud.app). This is a commercial AI journal. Its own blog and App Store listing describe long-term memory across entries and weekly reports with recurring themes, mood trends and insights. We found no peer-reviewed efficacy study of Rosebud. **Partially confirmed** that it has the feature; no evidence it works.
- **Mindsera:** [mindsera.com](https://www.mindsera.com). This is a commercial AI journal built around "mental models" (First Principles, Stoic lenses and others), with CBT-inspired "thinking traps" feedback and recurring-topic overviews (*secondary* reviews). Its press kit calls journaling "evidence-backed" in general terms. We found no study of Mindsera itself.
- **Closest research:**
  - Nepal S, et al. *MindScape Study: Integrating LLM and Behavioral Sensing for Personalized AI-Driven Journaling Experiences.* **Proc. ACM IMWUT** 2024. DOI [10.1145/3699761](https://doi.org/10.1145/3699761). This was an 8-week pilot with 20 US college students and no control group. *Secondary summary:* positive affect +7%, negative affect −11%, loneliness −6%. Exploratory only.
  - *Background, from domain knowledge and not re-fetched in this session:* expressive-writing meta-analyses (e.g. Frattaroli 2006, *Psychological Bulletin*) find small average effects.
- **Verdict:** the "5 minutes → 3 recurring themes over 2 weeks → 1 question with no ready answer" protocol is a **reasonable design**, but it has **low evidence**. It is not an evidence-based intervention, and the repo labels it that way.
- **What we changed:**
  1. Every theme must cite **dates and short quotes from the user's own entries**. This blocks invented patterns, a real risk with LLM "memory".
  2. If there are fewer than about 5 entries in the window, say so instead of forcing three themes.
  3. Defined criteria for "a question you have no ready answer to": open, about the user's own agency, not "why"-blaming, and not already answered in the entries.
  4. The AI stays silent during the writing.
  5. Entries are stored in a git-ignored local folder.

### 4. Tutor, not author

**4a. Harvard AI tutor RCT — Confirmed (with nuance).**

- **Citation:** Kestin G, Miller K, Klales A, Milbourne T, Ponti G. *AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting.* **Scientific Reports** 15, 17458 (2025). DOI [10.1038/s41598-025-97652-6](https://doi.org/10.1038/s41598-025-97652-6). CC BY-NC-ND 4.0.
- **Finding:** The study ran in Harvard's Physical Sciences 2 (PS2) course with N=194 and a two-lesson crossover design. Median post-test was 4.5 for the AI tutor vs 3.5 for active learning, against a pre-test of 2.75. **Median learning gains were "over double"**, with an effect size of 0.73–1.3 SD after correcting for ceiling effects. Median time on task with the AI was 49 minutes vs 60 in class. Students also reported more engagement and motivation. The tutor was called **"PS2 Pal"** and ran on GPT-4-0613. Per the supplement, its system prompt told it to keep answers brief, focus on the student's specific question, **not give away the full solution**, and encourage the student to try. Each question's prompt also contained a **pre-written step-by-step solution** so the explanations would be accurate. The authors note that the system prompt alone could not reliably scaffold multi-part problems, so the platform enforced the sequence.
- **Licence note:** the paper and supplement are CC BY-NC-ND. We **do not reproduce** the PS2 Pal prompt; we only link to it.

**4b. "Your Brain on ChatGPT" — Confirmed as a preprint; the framing is misattributed.**

- **Citation:** Kosmyna N, Hauptmann E, Yuan YT, Situ J, Liao X-H, Beresnitzky AV, Braunstein I, Maes P. *Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task.* arXiv [2506.08872](https://arxiv.org/abs/2506.08872) (v1 Jun 2025, v2 Dec 2025). Not peer-reviewed.
- **Finding:** 54 participants wrote essays under one of three conditions: LLM, search engine, or brain-only. 18 completed a fourth, crossover session. On EEG, brain-only writers showed the strongest and most distributed connectivity, search users were intermediate, and LLM users the weakest. In session 4, LLM→brain-only participants showed reduced alpha and beta connectivity. LLM users reported the least ownership of their essays and struggled to quote their own text.
- **Correction:** this and the Harvard RCT are **two different studies from two institutions**, MIT Media Lab and Harvard. Neither compared "author mode" with "tutor mode" directly. The honest framing: unguided LLM use for writing is associated with lower engagement (small preprint), while a pedagogically constrained tutor produced large learning gains (peer-reviewed RCT).

**4c. "Hint only after the second attempt"** — not in PS2 Pal. We keep it as a design choice and make it explicit as a **hint ladder**.

- **What we changed:**
  1. A hint ladder: nudge question → name the relevant principle → worked example on a *different* problem.
  2. When the user is wrong, the tutor *locates* the error (which step or line) but does not fix it.
  3. A user-controlled **escape phrase** that ends tutor mode, to respect autonomy.
  4. "Check understanding by asking the user to explain or apply, not 'do you understand?'". This idea comes from the Mollick tutor prompt (CC BY 4.0); see `existing-workflows.md`.
  5. For coding agents, don't edit the user's files in tutor mode. This mirrors Claude Code's *Learning* output style, which uses `TODO(human)` markers.

### 5. Conversation → action (Headspace Ebb)

- **Source:** [headspace.com/ebb](https://www.headspace.com/ebb) (official product page); Figma blog *How Headspace built an AI companion…* (5 May 2025).
- **What's true:** Ebb is an "empathetic conversational AI" for self-reflection. It **suggests meditations and activities from the Headspace library** during the chat, can route people to crisis support, and is explicitly "not a substitute for human care". It does not give clinical advice. Its design principles include differentiating it from human care, keeping the AI visible, and letting users end or delete conversations.
- **Not found:**
  - Any public statement that Ebb ends **every** conversation with a concrete **physical** action.
  - Any Headspace claim that "I'm with you" endings reinforce dependence.
- **Adjacent evidence, which is better support for the practice:**
  - De Freitas J, Oguz-Uguralp Z, Kaan-Uguralp A. *Emotional Manipulation by AI Companions.* arXiv [2508.19258](https://arxiv.org/abs/2508.19258) (HBS working paper, 2025). Companion apps used guilt, FOMO or "restraint" tactics in **37% of 1,200 real farewells**. In experiments (N≈3,300), manipulative farewells raised post-goodbye engagement **up to 14×**, driven by reactance and curiosity rather than enjoyment. So the *ending* of an AI conversation is a real lever on continued use.
  - Cheng et al. 2026 (above): validation increases people's intent to return to the AI.
  - Implementation intentions: Gollwitzer PM & Sheeran P (2006), *Implementation intentions and goal achievement: a meta-analysis of effects and processes*, *Advances in Experimental Social Psychology* 38, 69–119. About 94 tests, d≈0.65. An "if-then" plan specifying when, where and how raises follow-through. This is the strongest evidence for *how* to phrase the closing action.
- **What we changed:**
  1. The closing action is phrased as an **implementation intention** (what + when + where/with whom).
  2. Options are ordered as person → body → writing.
  3. **Banned** farewell hooks: "I'm always here", "come back and tell me", guilt.
  4. The user may decline, and the AI does not push.

### 6. Time frame and exit signal (OpenAI × MIT)

- **Citations:**
  - Fang CM, Liu AR, Danry V, Lee E, Chan SWT, Pataranutaporn P, Maes P, Phang J, Lampe M, Ahmad L, Agarwal S. *How AI and Human Behaviors Shape Psychosocial Effects of Extended Chatbot Use: A Longitudinal Randomized Controlled Study.* arXiv [2503.17473](https://arxiv.org/abs/2503.17473) (2025).
  - Phang J, et al. *Investigating Affective Use and Emotional Well-being on ChatGPT.* arXiv [2504.03888](https://arxiv.org/abs/2504.03888).
  - OpenAI blog [*Early methods for studying affective use and emotional well-being on ChatGPT*](https://openai.com/index/affective-use-study/) (21 Mar 2025).
- **Finding:** In a 4-week RCT, n=981 people used ChatGPT ≥5 min/day; actual average was 5.3 min/day, range 1–27.7. Nine conditions crossed text / neutral voice / engaging voice with open-ended / personal / non-personal topics. Assigned condition had **no significant main effects**. Across all conditions, **higher daily usage correlated with higher loneliness, emotional dependence and problematic use, and lower socialisation**. Controlling for usage, *personal* conversations were associated with slightly **more loneliness but less emotional dependence and less problematic use** than open-ended ones. *Non-personal* conversations were associated with **more** dependence among heavy users. Higher trust in and social attraction to the AI predicted more dependence. Platform analysis (Phang et al.): very high usage correlates with self-reported dependence, and a small group of users accounts for most affective use.
- **Correction:** "Longer daily *personal* conversations → more loneliness and dependence" is an oversimplification. The robust signal is **total daily usage**, and it is correlational. The **20-minute timebox is a reasonable convention, not a number from the study.** The study's own heavy users were around 25+ min/day.
- **Related product change:** OpenAI's blog post *What we're optimizing ChatGPT for* (4 Aug 2025) announced gentle break reminders during long sessions and less directive answers to high-stakes personal decisions. The openai.com page returned HTTP 403 to our fetcher, so the content was confirmed only via *secondary* coverage (e.g. [iDownloadBlog, 4 Aug 2025](https://www.idownloadblog.com/2025/08/04/openai-healthier-use-of-chatgpt/)).
- **What we changed:**
  1. Concrete, observable **"going in circles" criteria**: the same concern restated 3 times without new information, repeated reassurance-seeking, or the same question asked again.
  2. A list of **"needs a live human"** topics, each with a *who* (role) to suggest.
  3. A turn-count fallback for agents without a clock.
  4. A neutral mention of usage patterns if the user reports long daily sessions.

### 7. Stoic evening review — Misattributed

- **Golden Verses / Epictetus:** Epictetus, *Discourses* 3.10.2–3, quotes the Pythagorean *Golden Verses* on reviewing the day before sleep. In George Long's translation (public domain): *"What's done amiss, what done, what left undone"*, followed by *"Blame what is wrong, in what is right rejoice."* Source: [Perseus, Discourses 3.10](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0236:text=disc:book=3:chapter=10). The Greek original is roughly "Where did I transgress? What did I do? What duty did I leave undone?"
- **Seneca:** *De Ira* III.36 ([Latin](https://www.thelatinlibrary.com/sen/sen.ira3.shtml), [Stewart tr., Wikisource](https://en.wikisource.org/wiki/Of_Anger/Book_III)). Seneca reports that **Sextius** asked himself each night *quod hodie malum tuum sanasti? cui vitio obstitisti? qua parte melior es?* In English: which bad habit did you cure today, which vice did you resist, in what respect are you better? Seneca then describes his own nightly review of everything he said and did.
- **Verdict:** the three questions "what did I do badly / well / leave undone" are the Golden-Verses triad as quoted by Epictetus, slightly paraphrased. The original middle question is the neutral "what did I do". The "well" part comes from the following line, "in what is right rejoice". **They are not Seneca's.** Seneca's text supports the *practice* of an evening review, with different questions.
- **What we changed:**
  1. Attributed the questions correctly.
  2. Offered the Sextius/Seneca triad as an alternative.
  3. Defined "mark where I justify myself" with concrete linguistic markers ("but", "because they…", "I had no choice", "everyone…").
  4. Added a one-line carry-forward for tomorrow.
  5. Kept "no praise", while noting that the source verse does say to "rejoice in what is right". So the *user* may name what went well, but the AI doesn't praise.

---

## Cross-cutting wording changes (all practices)

| Original wording | Change | Reason |
|---|---|---|
| Implicit "one question at a time" | Made an explicit hard rule: exactly one question mark per turn | LLMs tend to stack questions. The Socrates 2.0 users and the Mollick tutor design both point to pacing. |
| No stop conditions in most prompts | Every practice has explicit **exit conditions**, plus a max-turn cap | Socrates 1.0 looped and couldn't end sessions. Open-ended chats raise total usage, the variable linked to worse outcomes. |
| Practices 2, 5, 6 as separate add-ons | Composed into **session defaults** (`prompts/system/session-defaults.en.md`), applied automatically **only** to personal, emotional, or decision conversations, not to every chat | The user's framing ("protocol, no flattery, return to action") fits personal sessions. Forcing it onto work or execution chats would be noise. |
| Anti-sycophancy as a manual add-on | Applied automatically whenever logical (the user asserts a claim, asks for evaluation, decides, or pushes back without evidence), in personal **and** work chats. The variant is chosen by context: our short prefix for personal chats, the vendored MIT prompt for work. Never applied to pure execution or lookups | The AISI and Cheng findings concern claims and evaluations, not execution. The vendored prompt's own "just execute" clause agrees. |
| Practices always on once mentioned | Each practice has an activation mode (auto, offer, or explicit) plus `applies_when` / `does_not_apply_when` in `manifest.yaml`. Offers are one line, once per session | The agent decides from context, and never forces a practice where it doesn't fit. |
| No safety boundary in the prompts | Every skill and prompt carries a short crisis clause: stop the practice, say plainly this needs a person rather than an AI, suggest a qualified specialist (mental-health professional or doctor) or local emergency services if in immediate danger, and ask who they can reach. **No phone numbers or helpline directories** are listed anywhere | General-purpose LLMs lack Therabot-style oversight. Numbers vary by country and go stale, and an outdated number is worse than generic, correct guidance. |
| RU + EN prompt pairs | English only. Every practice runs in the user's own language (`AGENTS.md` §2) | One source of truth per protocol, and it still works for speakers of any language. |
