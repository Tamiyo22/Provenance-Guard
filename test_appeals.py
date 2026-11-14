
"""
Criterion 4: Verify that valid appeals are processed reliably.

Target: 20 successful appeals per trial, across 3 trials.
"""

import json
from pathlib import Path

import requests

BASE_URL = "http://127.0.0.1:5000"
AUDIT_LOG = Path("logs/audit.jsonl")

TRIALS = 3
APPEALS_PER_TRIAL = 20


def create_submission(trial: int, sample: int) -> str:
    """Create a fresh submission and return its content ID."""

    body = {
        "text": (
            f"This is evaluation sample {sample} from trial {trial}. "
            "I wrote this paragraph to test whether the appeal process "
            "correctly records a request for human review."
        ),
        "creator_id": f"appeal_eval_{trial}_{sample}",
    }

    response = requests.post(
        f"{BASE_URL}/submit",
        json=body,
        timeout=90,
    )

    response.raise_for_status()

    content_id = response.json().get("content_id")

    if not content_id:
        raise ValueError("Submission did not return a content_id.")

    return content_id


def submit_appeal(content_id: str, trial: int, sample: int) -> dict:
    """Submit an appeal and return the response details."""

    reasoning = (
        f"Appeal evaluation: trial {trial}, sample {sample}. "
        "I wrote this text myself and request a human review."
    )

    response = requests.post(
        f"{BASE_URL}/appeal",
        json={
            "content_id": content_id,
            "reasoning": reasoning,
        },
        timeout=30,
    )

    return {
        "content_id": content_id,
        "reasoning": reasoning,
        "status_code": response.status_code,
        "response": response.json(),
    }


def verify_appeal(content_id: str, reasoning: str) -> bool:
    """Verify the original submission and appeal in the audit log."""

    if not AUDIT_LOG.exists():
        return False

    entries = []

    with AUDIT_LOG.open("r", encoding="utf-8") as log:
        for line in log:
            entry = json.loads(line)

            if entry.get("content_id") == content_id:
                entries.append(entry)

    original_exists = any(
        entry.get("status") == "decided"
        for entry in entries
    )

    appeal_recorded = any(
        entry.get("event") == "appeal"
        and entry.get("status") == "under_review"
        and entry.get("reasoning") == reasoning
        for entry in entries
    )

    return original_exists and appeal_recorded


def main():
    """Run 20 appeal tests in each of three trials."""

    all_results = []

    for trial in range(1, TRIALS + 1):
        print(f"\nTrial {trial}")

        passed = 0
        results = []

        for sample in range(1, APPEALS_PER_TRIAL + 1):
            try:
                content_id = create_submission(trial, sample)
                appeal = submit_appeal(content_id, trial, sample)

                response_ok = (
                    appeal["status_code"] == 200
                    and appeal["response"].get("status") == "under_review"
                    and appeal["response"].get("content_id") == content_id
                )

                audit_ok = verify_appeal(
                    content_id,
                    appeal["reasoning"],
                )

                success = response_ok and audit_ok

                if success:
                    passed += 1

                results.append({
                    "sample": sample,
                    "content_id": content_id,
                    "response_ok": response_ok,
                    "audit_ok": audit_ok,
                    "passed": success,
                })

                print(f"  Appeal {sample}: {'PASS' if success else 'FAIL'}")

            except Exception as exc:
                results.append({
                    "sample": sample,
                    "passed": False,
                    "error": str(exc),
                })
                print(f"  Appeal {sample}: ERROR - {exc}")

        all_results.append({
            "trial": trial,
            "passed": passed,
            "total": APPEALS_PER_TRIAL,
            "results": results,
        })

        print(f"Trial {trial}: {passed}/{APPEALS_PER_TRIAL} passed")

    output = Path("results/appeal_evaluation_before.json")
    output.parent.mkdir(exist_ok=True)

    output.write_text(
        json.dumps(all_results, indent=2),
        encoding="utf-8",
    )

    print(f"\nResults saved to {output}")


if __name__ == "__main__":
    main()
