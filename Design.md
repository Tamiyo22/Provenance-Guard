# Provenance Guard — System Design

## 1. Project Overview

Provenance Guard is a backend service designed to evaluate whether submitted writing appears to be human-written or AI-generated.

Because AI detection is inherently unreliable, the system prioritizes minimizing false accusations against human writers. It uses two different detection signals, communicates uncertainty through reader-facing labels, and provides an appeal process.

## 2. Submission Pipeline

1. A writer submits text and a creator ID through `POST /submit`.
2. The service validates the incoming JSON and assigns a unique content ID.
3. A pretrained model in `detector.py` evaluates patterns associated with AI-generated writing.
4. A stylometric analyzer in `stylometry.py` measures statistical properties of the text.
5. The system combines the two signals using a scoring function in `scoring.py`.
6. The combined score determines the appropriate reader-facing label. The decision and relevant scores are recorded in an audit log.
7. The service returns the result as JSON, including the content ID, guess, confidence score, and label.

## 3. Detection Signals

### Signal 1 — Pretrained Text Detector

**Measures:** Patterns learned from examples of human-written and AI-generated text.

**Why it might help:** Language models can produce recognizable statistical and linguistic patterns.

**Limitations:** Formal, highly structured, or polished human writing may resemble AI-generated text. The detector may also struggle with unfamiliar writing styles or edited AI content.

### Signal 2 — Stylometric Analysis

**Measures:** Sentence-length variation, vocabulary diversity, and punctuation patterns.

**Why it might help:** Different writing processes can produce different measurable patterns.

**Limitations:** Human writing varies significantly across authors and genres. AI-generated writing can also be edited to mimic human writing patterns.

## 4. False Positive Scenario

A writer submits an original poem that receives a high-confidence AI label.

This is a particularly harmful error because it could damage the writer's reputation or relationship with the platform.

The system should communicate that its assessment is probabilistic rather than definitive.

The writer can submit an appeal explaining why they believe the decision is incorrect. The submission status changes to `under_review`, and the appeal is recorded for later review.

An appeal does not automatically change the original detection score.

## 5. API Design

### POST /submit

**Request fields:**
- `text`: The submitted writing.
- `creator_id`: Identifier for the writer.

**Response fields:**
- `content_id`: Unique identifier for the submission.
- `guess`: The system's classification.
- `confidence`: A score between 0 and 1.
- `label`: A plain-English description of the result.

### POST /appeal

**Request fields:**
- `content_id`: Identifier of the submission being appealed.
- `reasoning`: The writer's explanation.

**Response fields:**
- `content_id`: The appealed submission.
- `status`: `under_review`.
- `message`: Confirmation that the appeal was recorded.

## 6. Safety and Design Priorities

- Minimize false accusations against genuine human writers.
- Avoid presenting automated detection as proof of authorship.
- Use an uncertainty category when evidence is insufficient.
- Record decisions and appeals for accountability.
- Keep the scoring logic understandable and testable.

## 7. Planned Evaluation

Before implementing the scoring system, five measurable acceptance criteria will be defined in `criteria.md`.

Testing will examine false positives, score variation, label coverage, appeal handling, and invalid input.

Actual results will be documented separately so that the original acceptance criteria remain unchanged.