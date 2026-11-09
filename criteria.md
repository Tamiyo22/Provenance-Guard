# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Minimize false positives

Across a test set of 20 independently verified human-written samples, no more than 1 sample (5%) should receive a high-confidence AI-generated label. This target must hold independently across all three evaluation trials.

**Why this target:**

False positives are especially harmful because incorrectly accusing a genuine writer of using AI can damage their reputation and trust in the platform. I chose a conservative 5% maximum for the evaluation sample because protecting human writers is more important than detecting every AI-generated submission.

---

## 2. Meaningful score separation

Using 20 verified human-written samples and 20 known AI-generated samples, the average AI-likelihood score for AI-generated writing should be at least 0.20 higher than the average score for human-written writing. This difference must hold across all three trials.

**Why this target:**

The system should distinguish between human and AI writing rather than producing similar scores for every submission. A minimum average difference of 0.20 provides a measurable separation target without assuming perfect detection.

---

## 3. Complete label coverage

All three classification labels—high-confidence AI, high-confidence human, and unsure—must be reachable. Every valid score between 0.0 and 1.0, including boundary values, must map to exactly one label, with no gaps or overlaps.

**Why this target:**

Uncertainty is an essential part of responsible AI detection. Every possible score needs an appropriate interpretation so the system does not make unsupported accusations or fail to classify borderline submissions.

---

## 4. Reliable appeal processing

In a test of 20 valid appeals referencing existing submissions, 100% must change the submission status to `under_review`, create an audit-log record containing the appeal reasoning, and return confirmation. This must hold across all three trials.

**Why this target:**

Writers need a dependable way to challenge potentially incorrect classifications. Because an appeal is a fundamental safeguard against false accusations, valid appeals should never be silently ignored or lost.

---

## 5. Safe handling of invalid input

In a test containing 20 invalid submissions, including missing text, empty strings, whitespace-only text, and missing creator IDs, 100% must return HTTP 400 without creating a submission record. This must hold across all three trials.

**Why this target:**

Invalid submissions should be rejected before any detection or scoring occurs. Consistent input validation prevents misleading classifications, unnecessary processing, and incomplete records from entering the system.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
