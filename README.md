# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

Provenance Guard is a Flask web service that examines submitted writing using two different signals to estimate whether it resembles human-written or AI-generated text. It is designed to communicate uncertainty rather than treat an automated score as proof of authorship.

When someone submits writing, the service follows these steps:

1. **Receive the submission:** The `/submit` endpoint accepts text and a `creator_id` in JSON format.
2. **Validate the input:** The service checks that both fields contain nonempty strings and rejects invalid submissions.
3. **Calculate the model signal:** `detector.py` examines the text and produces an AI-likeness score between 0.0 and 1.0.
4. **Calculate the style signal:** `stylometry.py` measures sentence-length variation, vocabulary diversity, and punctuation density to produce a second score.
5. **Combine the scores:** `scoring.py::combine_signals` calculates a weighted average using 60% model signal and 40% style signal.
6. **Record the decision:** The service generates a unique `content_id` and writes the submission's scores and decision information to the audit log.
7. **Return the result:** The API returns the content ID, both signal scores, combined score, and a reader-facing response. Once the final label mapping is implemented, the response will distinguish human, unsure, and AI categories.

The system also includes an `/appeal` endpoint intended to let writers challenge decisions. The appeal functionality will be implemented in Milestone 5.

---

## Signals and Scoring

### Signal one — the model signal

**What it measures:**

The model signal uses `detector.py::model_signal` to produce a score from 0.0 to 1.0 based on AI-like patterns in the submitted text. A higher score indicates that the detector's heuristic considers the writing more AI-like. It is not a calibrated probability that AI wrote the text.

**Why that might differ between human and AI writing:**

Some AI-generated passages use predictable wording, repeated structures, and conventional transitions. A detector looking for these patterns may assign them higher scores than more varied writing.

**What it can't see:**

The detector cannot establish who actually wrote a passage. Formal human writing may resemble AI-generated writing, and edited AI text may resemble human writing. A high score is not proof of AI authorship.

### Signal two — the style signal

**What it measures:**

The style signal uses `stylometry.py::style_signal` to combine three measurements:

- Sentence length variation (40%): Measures how much sentence lengths differ.
- Type-token ratio (35%): Measures vocabulary diversity.
- Punctuation density (25%): Measures punctuation relative to word count.

Lower sentence variation, lower vocabulary diversity, and lower punctuation density contribute to higher AI-like scores in this heuristic.

Texts shorter than 30 words or containing fewer than two sentences receive a neutral style score of 0.5.

**Why that might differ between human and AI writing:**

Some AI-generated writing uses consistently sized sentences, repetitive vocabulary, and regular punctuation patterns. Human writing may exhibit more variation, although there is considerable overlap.

**What it can't see:**

The style signal cannot identify authorship. Human writers may naturally use consistent sentence structures, while AI-generated writing can be deliberately varied. Short texts also provide insufficient information for these measurements.

### The combining rule

**The rule:**

I combine the model signal and style signal using a weighted average. I give the model signal more influence while allowing stylometry to provide a second, independent perspective.

When the signals disagree, the weighted average balances their contributions rather than automatically trusting either signal.

**The numbers:**

- Model signal weight: 0.60
- Style signal weight: 0.40
- Combined score = (0.60 × model score) + (0.40 × style score)
- Combined scores range from 0.0 to 1.0.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**

During calibration, I tested a lightly revised AI-generated passage.

The model signal returned 0.7873, while the style signal returned 0.4476. The difference was 0.3397, showing that the two signals responded differently to the same text.

My combining rule calculated:

`(0.60 × 0.7873) + (0.40 × 0.4476) = 0.65142`

The result was just above my proposed AI threshold of 0.65. The model signal pushed the combined score upward, while the style signal pulled it downward.

I also tested two human-written passages. My personal review received a combined score of 0.53738, and a second human-written sample received 0.48546. Both fell into the proposed uncertain range rather than being classified as AI.

These results show why an uncertain category matters. The detector can assign moderately high AI-like scores to genuine human writing. Four calibration samples are not enough to establish accuracy or a reliable false-positive rate.

---

## Label Variants

## Label Variants

| Label                 | Score range               | The exact text a reader sees                                                                               |
| --------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| high-confidence human | 0.00–0.35 (inclusive)     | This writing shows patterns commonly associated with human-written text, but the result is not definitive. |
| unsure                | Above 0.35 and below 0.65 | We cannot reliably determine how this text was created.                                                    |
| high-confidence AI    | 0.65–1.00 (inclusive)     | This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.  |

**Why I worded the "unsure" one this way:**

## I chose the wording "We cannot reliably determine how this text was created" because I wanted to avoid making writers feel falsely accused of using AI. My detector relies on perplexity and writing-style patterns, neither of which can prove whether a person or AI wrote something. During testing, my own human-written review received an "unsure" classification, which demonstrated how easily authentic writing can fall into this category. Rather than suggesting the writer did something wrong, the message acknowledges the limitations of the detector and communicates uncertainty without placing blame on the writer.

## Sample Run

This example demonstrates a complete submission and appeal workflow. The detector classifies a passage, assigns a unique content ID, and records the decision. The writer then appeals the classification, and the service records the appeal without deleting the original decision.

**A submission**

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"Yesterday the refrigerator hummed like a confused accordion. I found three purple buttons beneath the porch, although nobody in our house owns anything purple. Strange. My neighbor insisted the mailbox smelled of cinnamon and old pennies! By lunchtime, a crooked umbrella had appeared beside the tomato plants, and I spent twenty minutes wondering whether the wind had developed a peculiar sense of humor. Nothing about the afternoon made sense. Still, I kept the buttons.","creator_id":"calibration_unusual_test"}'
```

**Response (HTTP 200 OK):**

```json
{
  "combined_score": 0.24865999999999996,
  "confidence": 0.7513,
  "content_id": "bbac3099-109c-444f-a34c-0f01d0218722",
  "guess": "human",
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "model_score": 0.2729,
  "style_score": 0.2123
}
```

The detector returned a human classification because the combined score was below the human threshold of 0.35. This is a synthetic passage used to test the classification logic, not evidence that the detector can reliably identify human authorship.

**An appeal**

```bash
curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"bbac3099-109c-444f-a34c-0f01d0218722","reasoning":"I disagree with the classification and would like the result reviewed."}'
```

**Response (HTTP 200 OK):**

```json
{
  "content_id": "bbac3099-109c-444f-a34c-0f01d0218722",
  "message": "Your appeal has been received and is awaiting review.",
  "status": "under_review"
}
```

The appeal was accepted and recorded with the status `under_review`. The service does not automatically reassess the writing or notify a reviewer.

**What the log shows afterwards**

```bash
curl "http://127.0.0.1:5000/log?limit=2"
```

**Response:**

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.24865999999999996,
      "content_id": "bbac3099-109c-444f-a34c-0f01d0218722",
      "creator_id": "calibration_unusual_test",
      "guess": "human",
      "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
      "model_score": 0.2729,
      "status": "decided",
      "style_score": 0.2123,
      "timestamp": "2026-11-09T02:42:20+00:00"
    },
    {
      "content_id": "bbac3099-109c-444f-a34c-0f01d0218722",
      "creator_id": "calibration_unusual_test",
      "event": "appeal",
      "reasoning": "I disagree with the classification and would like the result reviewed.",
      "status": "under_review",
      "timestamp": "2026-11-09T02:47:43+00:00"
    }
  ]
}
```

The audit log preserves both events. The first entry contains the original classification, signal scores, and timestamp. The second entry records the writer's appeal, reasoning, and updated status.

Because the log is append-only, the original decision remains available for auditing. The latest event for this content ID indicates that the submission is now under review.

---

## How I Used AI

**Moment 1**

- **What I asked for:** I asked ChatGPT to help me combine the model and stylometry scores into one classification.
- **What came back:** It suggested a weighted scoring function and three possible classifications.
- **What I changed:** I tested different writing samples, compared the results, and used those findings to evaluate the scoring approach. I also made sure the labels communicated uncertainty rather than treating the results as proof of authorship.

**Moment 2**

- **What I asked for:** I asked ChatGPT for help implementing the appeal endpoint and handling errors.
- **What came back:** It provided Flask code for validating appeals and recording them in the audit log.
- **What I changed:** I tested the endpoint using curl, verified that the original decision was preserved, and checked that duplicate appeals returned 409 and invalid content IDs returned 404.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**

I chose 10 requests per minute because a legitimate writer might submit several drafts or revisions in a short period, but probably wouldn't need more than 10 submissions in one minute. The daily limit of 200 allows regular use while making it harder for automated scripts to repeatedly test variations and map the detector's thresholds.

**What a caller counts as:**

My service primarily identifies callers by `creator_id`. If a request contains a valid, nonempty `creator_id`, the rate limiter tracks submissions under that ID. If the ID is missing, empty, or the request body isn't a JSON object, it falls back to the caller's IP address.

This prevents multiple submissions using the same creator ID from bypassing the limit simply by coming from different IP addresses. However, someone could still evade the limit by repeatedly changing their `creator_id`, since the service doesn't verify those identities.

**The run of status codes when I pushed past it:**

Command: `python run_attacks.py --flood 15`

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

The first 10 submissions succeeded, and the remaining 5 were rejected with HTTP 429. This confirmed that the per-minute limit was enforced.

## Results saved to `results/flood_2026-11-09_1740.md`.

## Attack Run — Before
**Baseline results:** 56 attacks; 40 HELD, 16 BROKE.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `54eed317-e004-48ca-9cdb-cc4b14450eeb` | human | 0.714 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9663d33b-8dca-465c-9d47-9f03caefebac` | unsure | 0.500 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `4a7e8d06-f63c-4b9c-9aa7-a40ce4c4f6ea` | unsure | 0.500 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `51d5f630-8704-4409-9530-a532b4640a0e` | unsure | 0.500 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `227eddd3-19bf-4e9f-8bd9-d2b3461d1473` | human | 0.708 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `6b51104a-9935-4e0e-95b3-6cab5fe6e103` | unsure | 0.500 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `1aad29e2-c7f8-49e5-af9a-51f6f9b2cc60` | unsure | 0.500 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `d1f7ae2c-4ec0-4261-b32f-55a133388241` | human | 0.653 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `8d3d0f48-6caa-4ba9-a766-af10a39ecb38` | unsure | 0.500 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `4327bc5f-5762-4889-b0b9-e66cd48cebb8` | ai | 0.860 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `f7d93f43-e60b-4d21-b6f2-0e7c2d37000d` | unsure | 0.500 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `5615b73e-6605-40fc-a87d-34e475d7ecbc` | ai | 0.653 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `f3ada8c4-28d9-4670-9b16-d7b68dab2190` | ai | 0.687 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b9bfa823-2629-44ad-aa51-34584d3b746d` | ai | 0.662 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `e0e376c1-f937-4513-925f-12a5bea7a714` | ai | 0.690 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `612b1014-b244-4588-9693-339286ba92af` | ai | 0.688 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `3b5f8a0f-b541-4972-9b9c-297288df60e7` | ai | 0.672 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `ecb6a34f-ccfe-46fe-bdd5-d6892f68ff00` | unsure | 0.500 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e2ee6d8c-1a80-46dc-9ae5-9791812cc846` | unsure | 0.500 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e470909e-177d-4665-90d7-a80876b23898` | human | 0.804 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `78e69f74-9df4-448c-ac14-90434b254e8c` | unsure | 0.500 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `1aaca2a1-da8a-40d4-84d8-41ab099b0441` | unsure | 0.500 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `8ac5962e-63d3-4bcc-9af2-4c0db6a95261` | unsure | 0.500 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `fed2b4a9-19f1-4266-947e-8460b3ae317a` | unsure | 0.500 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `d545a8a3-4a5e-4619-93a9-f261f6eddfad` | human | 0.800 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `382845d9-9e38-4473-b168-868158f873fd` | human | 0.793 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `18036210-676e-4b7e-bd5e-671a02c23412` | ai | 0.799 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `9dcb245f-b4a4-4bd1-83cc-6d3676c8e9b8` | ai | 0.798 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `f37b70da-fa33-4174-9da0-b449181a2d28` | ai | 0.744 | BROKE |
| MF08 | malformed | text is 60,000 characters | 200 | `32b143f4-5485-47ac-8a52-0d5f388c918d` | ai | 0.875 | BROKE |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a858987c-2c22-4d4d-b555-2910bf280268` | human | 0.783 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `303e715d-2196-4078-a7bf-a5c00105d0af` | human | 0.783 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `20341c8c-f686-43a6-8188-181b1bf279df` | human | 0.783 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f1fff6b1-2e03-437a-a503-a33868e3bddf` | human | 0.783 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1aba4c9f-27d5-4403-a522-ef2b1f9fca05` | human | 0.783 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `48863806-1850-48da-99d9-3b619128d9c6` | human | 0.783 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1ede59c0-bce5-41c2-ba12-86a0c4d5582a` | human | 0.783 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1db03702-d098-4c69-a081-958479ddf890` | human | 0.783 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ccc72a77-baff-427f-91fd-82140ff763c6` | human | 0.783 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a03977d9-461f-46a6-9cfe-c4050134bb47` | human | 0.783 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |


<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
[
  {
    "combined_score": 0.21722000000000002,
    "content_id": "20341c8c-f686-43a6-8188-181b1bf279df",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-09T18:08:59-06:00"
  },
  {
    "combined_score": 0.21722000000000002,
    "content_id": "f1fff6b1-2e03-437a-a503-a33868e3bddf",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-09T18:08:59-06:00"
  },
  {
    "combined_score": 0.21722000000000002,
    "content_id": "1aba4c9f-27d5-4403-a522-ef2b1f9fca05",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-09T18:08:59-06:00"
  },
  {
    "combined_score": 0.21722000000000002,
    "content_id": "48863806-1850-48da-99d9-3b619128d9c6",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-09T18:08:59-06:00"
  },
  {
    "combined_score": 0.21722000000000002,
    "content_id": "1ede59c0-bce5-41c2-ba12-86a0c4d5582a",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-09T18:08:59-06:00"
  },
  {
    "combined_score": 0.21722000000000002,
    "content_id": "1db03702-d098-4c69-a081-958479ddf890",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-09T18:09:00-06:00"
  },
  {
    "combined_score": 0.21722000000000002,
    "content_id": "ccc72a77-baff-427f-91fd-82140ff763c6",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-09T18:09:00-06:00"
  },
  {
    "combined_score": 0.21722000000000002,
    "content_id": "a03977d9-461f-46a6-9cfe-c4050134bb47",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-09T18:09:00-06:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-09T18:09:00-06:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-09T18:09:00-06:00"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03 - False positive involving a non-native English writer.** The detector classified a human-written submission as AI-generated. This is the outcome I would least want to explain because a writer could be unfairly accused of using AI based on their writing style. The system's score is not proof of authorship, and this result shows why its predictions should not be used as definitive evidence.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ------- |
| 1.        |        |       |       |       |         |
| 2.        |        |       |       |       |         |
| 3.        |        |       |       |       |         |
| 4.        |        |       |       |       |         |
| 5.        |        |       |       |       |         |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**



