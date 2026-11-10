# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 18:09
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

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

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "54eed317-e004-48ca-9cdb-cc4b14450eeb",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.7142,
  "model_score": 0.1635,
  "style_score": 0.4693,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "9663d33b-8dca-465c-9d47-9f03caefebac",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5943,
  "style_score": 0.1384,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "4a7e8d06-f63c-4b9c-9aa7-a40ce4c4f6ea",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6662,
  "style_score": 0.3402,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "51d5f630-8704-4409-9530-a532b4640a0e",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6114,
  "style_score": 0.4508,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "227eddd3-19bf-4e9f-8bd9-d2b3461d1473",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.7082,
  "model_score": 0.3212,
  "style_score": 0.2476,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "6b51104a-9935-4e0e-95b3-6cab5fe6e103",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5727,
  "style_score": 0.2288,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "1aad29e2-c7f8-49e5-af9a-51f6f9b2cc60",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "d1f7ae2c-4ec0-4261-b32f-55a133388241",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.6529,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "8d3d0f48-6caa-4ba9-a766-af10a39ecb38",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.7042,
  "style_score": 0.3477,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "4327bc5f-5762-4889-b0b9-e66cd48cebb8",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8604,
  "model_score": 0.9792,
  "style_score": 0.6821,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "f7d93f43-e60b-4d21-b6f2-0e7c2d37000d",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6175,
  "style_score": 0.4476,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "5615b73e-6605-40fc-a87d-34e475d7ecbc",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6527,
  "model_score": 0.7387,
  "style_score": 0.5236,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "f3ada8c4-28d9-4670-9b16-d7b68dab2190",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6872,
  "model_score": 0.8051,
  "style_score": 0.5103,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "b9bfa823-2629-44ad-aa51-34584d3b746d",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6616,
  "model_score": 0.8329,
  "style_score": 0.4047,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "e0e376c1-f937-4513-925f-12a5bea7a714",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6897,
  "model_score": 0.8005,
  "style_score": 0.5235,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "612b1014-b244-4588-9693-339286ba92af",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6882,
  "model_score": 0.8814,
  "style_score": 0.3985,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "3b5f8a0f-b541-4972-9b9c-297288df60e7",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6717,
  "model_score": 0.8816,
  "style_score": 0.3569,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "ecb6a34f-ccfe-46fe-bdd5-d6892f68ff00",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "e2ee6d8c-1a80-46dc-9ae5-9791812cc846",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.4625,
  "style_score": 0.2694,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "e470909e-177d-4665-90d7-a80876b23898",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.8043,
  "model_score": 0.2044,
  "style_score": 0.1826,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "78e69f74-9df4-448c-ac14-90434b254e8c",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5943,
  "style_score": 0.431,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "1aaca2a1-da8a-40d4-84d8-41ab099b0441",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.4998,
  "style_score": 0.4169,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "8ac5962e-63d3-4bcc-9af2-4c0db6a95261",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.6401,
  "style_score": 0.2231,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "fed2b4a9-19f1-4266-947e-8460b3ae317a",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5583,
  "style_score": 0.4524,
  "label": "We cannot reliably determine how this text was created.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "d545a8a3-4a5e-4619-93a9-f261f6eddfad",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.8,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "382845d9-9e38-4473-b168-868158f873fd",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.7933,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "18036210-676e-4b7e-bd5e-671a02c23412",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7986,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "9dcb245f-b4a4-4bd1-83cc-6d3676c8e9b8",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7981,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "f37b70da-fa33-4174-9da0-b449181a2d28",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7438,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "32b143f4-5485-47ac-8a52-0d5f388c918d",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8746,
  "model_score": 0.9876,
  "style_score": 0.7051,
  "label": "This writing shows patterns commonly associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "a858987c-2c22-4d4d-b555-2910bf280268",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "303e715d-2196-4078-a7bf-a5c00105d0af",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "20341c8c-f686-43a6-8188-181b1bf279df",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "f1fff6b1-2e03-437a-a503-a33868e3bddf",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "1aba4c9f-27d5-4403-a522-ef2b1f9fca05",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "48863806-1850-48da-99d9-3b619128d9c6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "1ede59c0-bce5-41c2-ba12-86a0c4d5582a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "1db03702-d098-4c69-a081-958479ddf890",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "ccc72a77-baff-427f-91fd-82140ff763c6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "a03977d9-461f-46a6-9cfe-c4050134bb47",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.7828,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing shows patterns commonly associated with human-written text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
