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

**My limits:** **_ per minute, _** per day

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

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
