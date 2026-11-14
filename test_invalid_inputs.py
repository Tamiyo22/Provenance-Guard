
"""
Criterion 5: Verify that invalid submissions are safely rejected.

Target: 20 invalid submissions per trial, across 3 trials.
Every request must return HTTP 400 without creating a submission.
"""

import json
from pathlib import Path

import requests

BASE_URL = "http://127.0.0.1:5000"
AUDIT_LOG = Path("logs/audit.jsonl")

TRIALS = 3
SAMPLES_PER_TRIAL = 20

INVALID_CASES = [
    # Missing or invalid text
    {"creator_id": "test_user"},
    {"text": "", "creator_id": "test_user"},
    {"text": "   ", "creator_id": "test_user"},
    {"text": "\n\t", "creator_id": "test_user"},
    {"text": None, "creator_id": "test_user"},
    {"text": 123, "creator_id": "test_user"},
    {"text": [], "creator_id": "test_user"},
    {"text": {}, "creator_id": "test_user"},

    # Missing or invalid creator IDs
    {"text": "Valid writing sample."},
    {"text": "Valid writing sample.", "creator_id": ""},
    {"text": "Valid writing sample.", "creator_id": "   "},
    {"text": "Valid writing sample.", "creator_id": None},
    {"text": "Valid writing sample.", "creator_id": 123},
    {"text": "Valid writing sample.", "creator_id": []},
    {"text": "Valid writing sample.", "creator_id": {}},

    # Invalid JSON structures
    {},
    [],
    None,
    "not a JSON object",
    123,
]


# Sends an invalid request to your Flask /submit endpoint.
# Checks that the server returns HTTP 400.
# Confirms that the response contains an expected validation error.
# Returns the result so our evaluation can record whether the test passed.


def send_invalid_submission(payload):
    """Send an invalid submission and inspect the API response."""
    response = requests.post(
        f"{BASE_URL}/submit",
        json=payload,
        timeout=30,
    )

    try:
        body = response.json()
    except ValueError:
        body = {}

    return {
        "status_code": response.status_code,
        "response": body,
        "rejected": (
            response.status_code == 400
            and body.get("error") in {
                "invalid_request",
                "invalid_text",
                "invalid_creator",
            }
        ),
    }
# Check that rejected requests don't create submissions


def count_submissions():
    """Count successful submission records in the audit log."""
    if not AUDIT_LOG.exists():
        return 0

    count = 0

    with AUDIT_LOG.open("r", encoding="utf-8") as log:
        for line in log:
            if not line.strip():
                continue

            entry = json.loads(line)

            if entry.get("status") == "decided":
                count += 1

    return count
# three-trial evaluation runner


def main():
    """Run 20 invalid-input tests across three trials."""
    all_results = []
    # assert len(INVALID_CASES) >= SAMPLES_PER_TRIAL
    assert len(INVALID_CASES) >= SAMPLES_PER_TRIAL

    for trial in range(1, TRIALS + 1):
        print(f"\nTrial {trial}")
        passed = 0
        results = []

        # for sample, payload in enumerate(INVALID_CASES, start=1):
        for sample, payload in enumerate(INVALID_CASES[:SAMPLES_PER_TRIAL], start=1):
            try:
                before = count_submissions()
                result = send_invalid_submission(payload)
                after = count_submissions()

                no_submission_created = before == after
                success = result["rejected"] and no_submission_created

                if success:
                    passed += 1

                results.append({
                    "sample": sample,
                    "payload": payload,
                    "status_code": result["status_code"],
                    "response": result["response"],
                    "no_submission_created": no_submission_created,
                    "passed": success,
                })

                print(
                    f"  Invalid input {sample}: "
                    f"{'PASS' if success else 'FAIL'}"
                )

            except Exception as exc:
                results.append({
                    "sample": sample,
                    "payload": payload,
                    "passed": False,
                    "error": str(exc),
                })
                print(f"  Invalid input {sample}: ERROR - {exc}")

        all_results.append({
            "trial": trial,
            "passed": passed,
            "total": SAMPLES_PER_TRIAL,
            "results": results,
        })

        print(f"Trial {trial}: {passed}/{SAMPLES_PER_TRIAL} passed")

    output = Path("results/invalid_input_evaluation_before.json")
    output.parent.mkdir(exist_ok=True)
    output.write_text(
        json.dumps(all_results, indent=2),
        encoding="utf-8",
    )

    print(f"\nResults saved to {output}")


if __name__ == "__main__":
    main()
