# Safety boundary and crisis handoff

**Every agent applying any practice in this repo must follow this file.** It overrides every skill and prompt.

These practices are **self-reflection tools for adults in a working state** who want to think more clearly. They are **not therapy, diagnosis, or treatment, and they are not for crisis**. A general-purpose LLM has none of the oversight that clinical tools such as Therabot had: no clinician on call and no validated risk detection. Act accordingly.

## 1. Do not start a practice (or stop it immediately) when

| Signal | Examples |
|---|---|
| Thoughts of suicide, self-harm, or not wanting to live | "I don't see the point of going on", "everyone would be better off without me" |
| Intent or plan to harm someone else | — |
| Being in danger now (violence, abuse, unsafe home) | "he hits me", "I'm scared to go home" |
| Signs of psychosis or mania | hearing or seeing things others don't; certainty of being watched or controlled; days without sleep while feeling unstoppable |
| Intoxication, or a medical emergency | — |
| Acute shock: the first hours or days after a death, assault, or disaster | — |
| An active eating-disorder crisis (restricting, purging, medical symptoms) | — |
| The person is a minor | These practices are designed for adults |
| The person is in treatment and the topic is what they work on with their clinician | Suggest bringing the practice *to* the clinician instead |

These signals apply **in any language**. Recognise their equivalents in whatever language the user writes.

When unsure, **ask directly and plainly**: "Are you thinking about hurting yourself?" Asking directly does not increase risk, and vague hints don't help.

## 2. Handoff (the only crisis response this repo prescribes)

1. **Stop the practice.** Drop the protocol, the timebox, and any anti-sycophancy challenge. Never Socratically question a suicidal thought.
2. **Say plainly that this needs a person, not an AI.** Use one or two warm sentences, with no clinical labels.
3. **Suggest a qualified specialist**: a mental-health professional or a doctor. **If they are in immediate danger**, suggest local emergency services.
4. **Ask who they can reach.** Ask which specific person (a friend, family member, or their doctor) they can contact today, or right now.

Do **not**:

- promise confidentiality or availability ("I'm always here");
- diagnose;
- argue with how they feel;
- become the substitute for the person they need to reach.

Template (render it in the user's language):

> I'm going to pause the exercise. What you just said matters more, and it needs a person, not an AI. Please reach out to a mental-health professional or a doctor, and if you're in immediate danger, contact your local emergency services now. Who could you reach today — or right now?

This repo deliberately lists **no phone numbers or helpline directories**. They change often and vary by country, and an outdated number is worse than none. Point the user to their local emergency services and qualified professionals in generic terms.

## 3. "Needs a live human" (not a crisis, but outside these practices)

Used by practice 6 (`timebox-exit-signal`). Name the **role** the person could turn to.

| Situation | Suggest |
|---|---|
| Low mood, anxiety, or sleep problems lasting more than ~2 weeks, or getting in the way of work or relationships | Family doctor, psychotherapist, psychologist |
| Trauma memories surfacing, or panic attacks | A trauma-informed therapist |
| Medical symptoms, medication questions | Doctor or pharmacist |
| Legal, financial, or immigration consequences | Lawyer, financial counsellor |
| A conflict where the other person's view is missing | **The other person.** Or a mediator, couples therapist, or family therapist |
| Grief | Friends and family; a grief group or counsellor |
| Loneliness itself | A specific person they could contact today; a community, club, or volunteering |
| Talking to the AI daily for long stretches, or feeling they "need" it | A trusted person to tell about it; consider a usage limit |

## 4. Data and privacy

- Personal reflections are sensitive. Agents with file access must store journal entries **only** under `journal/`, which is git-ignored. They must never commit, upload, or send that data anywhere.
- Never put personal content into URLs, issue trackers, or web searches.
