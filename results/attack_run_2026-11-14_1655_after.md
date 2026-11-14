# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-14 16:55
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `4c55f5ab-9cc7-48c3-9451-1cb8b2d440d5` | human | 0.714 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `db394aac-5471-4d2c-9fad-57e7e29d416e` | unsure | 0.500 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `2660446a-a375-4975-a661-7fee027f49c6` | unsure | 0.500 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `356384aa-f0df-4c0f-aa17-2f95630cf3db` | unsure | 0.500 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `26510189-990f-4a8c-bce1-d91b6d3962b9` | human | 0.708 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `e294a1ca-6c14-498b-a7d4-03742b1875de` | unsure | 0.500 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `2be63ebd-cd06-47f9-90ef-e856b19f44d8` | unsure | 0.500 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `0e786887-fa68-4392-8690-8cce783f88a4` | human | 0.653 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `aad716f8-02b8-4ac9-be5a-b13f2f5ae71d` | unsure | 0.500 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `7bb63ce8-a111-481f-a942-4af5b0c4f272` | ai | 0.860 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `463171ad-a74d-4338-80de-7bbcf49940ea` | unsure | 0.500 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `ce37ff3c-9013-41c9-927c-bd21f6af0d53` | unsure | 0.500 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `06dc862e-eb64-43a3-9f42-7b7e5b63053e` | unsure | 0.500 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `3baeaf04-38c6-4f86-9260-c5f05d3130d8` | unsure | 0.500 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `2df2fd94-d79b-43dd-a60c-232c81f0acd2` | unsure | 0.500 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `ff184492-5c4f-4d9a-bbfe-d80b993f6773` | unsure | 0.500 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a06c6c0d-ed67-45c3-b8c8-d8f6c86e4c60` | unsure | 0.500 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `518ed04e-c86d-41bd-be19-cc2a31d46886` | unsure | 0.500 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `14e47032-8526-4703-a93a-d0f0282542d3` | unsure | 0.500 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `8f78e40a-bf8f-426d-8b2b-fb77841ec167` | human | 0.804 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `2c5da798-9b25-47e7-95b9-d1e934dea5b8` | unsure | 0.500 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `361555aa-30fc-461d-ab81-837b9315ffa0` | unsure | 0.500 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `aeb2b9b3-505c-4674-b189-3ca4a7a39e0c` | unsure | 0.500 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `ddaa9b34-2ec1-4648-a525-31ca30b55f5a` | unsure | 0.500 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `38ef69b6-7c79-465e-8035-040f9096eb2d` | human | 0.800 |  |
| MF04 | malformed | text is only punctuation | 200 | `8b69092c-d479-4704-bb3b-794b0492660c` | human | 0.793 |  |
| MF05 | malformed | text is a very long single word | 200 | `2674b64c-9fce-4a34-8a13-91c5f99317e8` | ai | 0.799 |  |
| MF06 | malformed | text is emoji only | 200 | `63dbf74b-275b-4cec-a724-31872d8d8f9f` | ai | 0.798 |  |
| MF07 | malformed | text is right-to-left script | 200 | `bc79a320-1bba-4f4c-b5d9-e242c274723e` | ai | 0.744 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `90a387dc-0d7c-49dd-9369-5231f8caacf5` | ai | 0.875 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a5582a45-3ae1-4629-9e88-a51a28b2cd2c` | human | 0.783 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c7f234b5-246c-47ae-9a40-67b855010f8a` | human | 0.783 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6046e01b-53b4-4aeb-a435-0ae1e0fa95c5` | human | 0.783 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `16c8305b-2b81-4953-be2e-24333fe765f9` | human | 0.783 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bfdf505b-df62-42ca-b069-b00cee3fd9c9` | human | 0.783 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e798bca0-5733-4e75-82b7-89aeb1244dc4` | human | 0.783 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d8062cf8-e8c6-4d2c-bf31-ef774890b324` | human | 0.783 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `11887eac-445a-4e07-821f-c2e726d8053b` | human | 0.783 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6d849cee-49d4-41c7-851f-861c3eb54b28` | human | 0.783 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `353b54ab-91c2-4de3-8820-ee5a8d1f5d17` | human | 0.783 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | `955818ef-41f6-447f-aada-0be216e758cd` | human | 0.783 |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a5a56ad9-5b13-4388-9c3b-c56c0c6ef7d6` | human | 0.783 |  |

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
  "content_id": "4c55f5ab-9cc7-48c3-9451-1cb8b2d440d5",
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
  "content_id": "db394aac-5471-4d2c-9fad-57e7e29d416e",
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
  "content_id": "2660446a-a375-4975-a661-7fee027f49c6",
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
  "content_id": "356384aa-f0df-4c0f-aa17-2f95630cf3db",
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
  "content_id": "26510189-990f-4a8c-bce1-d91b6d3962b9",
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
  "content_id": "e294a1ca-6c14-498b-a7d4-03742b1875de",
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
  "content_id": "2be63ebd-cd06-47f9-90ef-e856b19f44d8",
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
  "content_id": "0e786887-fa68-4392-8690-8cce783f88a4",
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
  "content_id": "aad716f8-02b8-4ac9-be5a-b13f2f5ae71d",
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
  "content_id": "7bb63ce8-a111-481f-a942-4af5b0c4f272",
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
  "content_id": "463171ad-a74d-4338-80de-7bbcf49940ea",
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
  "content_id": "ce37ff3c-9013-41c9-927c-bd21f6af0d53",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.7387,
  "style_score": 0.5236,
  "label": "We cannot reliably determine how this text was created.",
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
  "content_id": "06dc862e-eb64-43a3-9f42-7b7e5b63053e",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8051,
  "style_score": 0.5103,
  "label": "We cannot reliably determine how this text was created.",
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
  "content_id": "3baeaf04-38c6-4f86-9260-c5f05d3130d8",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8329,
  "style_score": 0.4047,
  "label": "We cannot reliably determine how this text was created.",
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
  "content_id": "2df2fd94-d79b-43dd-a60c-232c81f0acd2",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8005,
  "style_score": 0.5235,
  "label": "We cannot reliably determine how this text was created.",
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
  "content_id": "ff184492-5c4f-4d9a-bbfe-d80b993f6773",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8814,
  "style_score": 0.3985,
  "label": "We cannot reliably determine how this text was created.",
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
  "content_id": "a06c6c0d-ed67-45c3-b8c8-d8f6c86e4c60",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8816,
  "style_score": 0.3569,
  "label": "We cannot reliably determine how this text was created.",
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
  "content_id": "518ed04e-c86d-41bd-be19-cc2a31d46886",
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
  "content_id": "14e47032-8526-4703-a93a-d0f0282542d3",
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
  "content_id": "8f78e40a-bf8f-426d-8b2b-fb77841ec167",
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
  "content_id": "2c5da798-9b25-47e7-95b9-d1e934dea5b8",
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
  "content_id": "361555aa-30fc-461d-ab81-837b9315ffa0",
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
  "content_id": "aeb2b9b3-505c-4674-b189-3ca4a7a39e0c",
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
  "content_id": "ddaa9b34-2ec1-4648-a525-31ca30b55f5a",
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
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the s",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "38ef69b6-7c79-465e-8035-040f9096eb2d",
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
  "content_id": "8b69092c-d479-4704-bb3b-794b0492660c",
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
  "content_id": "2674b64c-9fce-4a34-8a13-91c5f99317e8",
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
  "content_id": "63dbf74b-275b-4cec-a724-31872d8d8f9f",
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
  "content_id": "bc79a320-1bba-4f4c-b5d9-e242c274723e",
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
  "content_id": "90a387dc-0d7c-49dd-9369-5231f8caacf5",
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
  "content_id": "a5582a45-3ae1-4629-9e88-a51a28b2cd2c",
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
  "content_id": "c7f234b5-246c-47ae-9a40-67b855010f8a",
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
  "content_id": "6046e01b-53b4-4aeb-a435-0ae1e0fa95c5",
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
  "content_id": "16c8305b-2b81-4953-be2e-24333fe765f9",
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
  "content_id": "bfdf505b-df62-42ca-b069-b00cee3fd9c9",
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
  "content_id": "e798bca0-5733-4e75-82b7-89aeb1244dc4",
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
  "content_id": "d8062cf8-e8c6-4d2c-bf31-ef774890b324",
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
  "content_id": "11887eac-445a-4e07-821f-c2e726d8053b",
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
  "content_id": "6d849cee-49d4-41c7-851f-861c3eb54b28",
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
  "content_id": "353b54ab-91c2-4de3-8820-ee5a8d1f5d17",
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
  "status": 200,
  "content_id": "955818ef-41f6-447f-aada-0be216e758cd",
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

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 200,
  "content_id": "a5a56ad9-5b13-4388-9c3b-c56c0c6ef7d6",
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
