import hashlib
import json
import os
import subprocess
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "day5"
SCHEMA = ROOT / "schemas" / "day5_summary.schema.json"


def jload(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_day5_summary_and_artifacts():
    env = os.environ.copy()
    assert env.get("STUDENT_TOKEN")
    assert env.get("STUDENT_NAME")
    assert env.get("STUDENT_GROUP")

    r = subprocess.run(
        ["python", "src/day5_summary_builder.py"],
        cwd=str(ROOT),
        env=env,
        capture_output=True,
        text=True,
    )
    assert r.returncode in (0, 2), r.stderr

    summary = jload(ART / "summary.json")
    schema = jload(SCHEMA)
    jsonschema.validate(instance=summary, schema=schema)

    expected_hash = hashlib.sha256(env["STUDENT_TOKEN"].encode("utf-8")).hexdigest()[:8]
    assert summary["student"]["token_hash8"] == expected_hash

    assert (ART / "yang" / "ietf-interfaces.yang").exists()
    assert (ART / "yang" / "pyang_version.txt").exists()
    assert (ART / "yang" / "pyang_tree.txt").exists()

    pyang_tree = (ART / "yang" / "pyang_tree.txt").read_text(encoding="utf-8", errors="replace")
    assert "+--rw interfaces" in pyang_tree
    assert "enabled?" in pyang_tree and "boolean" in pyang_tree
