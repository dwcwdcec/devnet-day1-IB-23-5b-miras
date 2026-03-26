# Day 2 Report — Git + Data Formats + Tests

## 1. Student
- Name: Бақытбек Мирас Жасуланұлы
- Group: IB-23-5b
- GitHub repo: https://github.com/dwcwdcec/devnet-day1-IB-23-5b-miras
- Day2 Token: D1-IB-23-5b-02-B7C2

## 2. NetAcad progress (Module 2–3)
- Completed items: 2.2, 3.1–3.6
- Screenshot(s):
  - NetAcad progress screenshot attached

## 3. Git evidence
- File: `artifacts/day2/git_log.txt` exists: Yes
- File: `artifacts/day2/conflict_log.txt` exists: Yes
- Merge conflict was created in README.md by modifying the same section in two different branches and resolved manually by combining both changes.

## 4. Repo structure (Day2 artifacts)
- src/day2_data_formats.py : Yes
- tests/test_day2_data_formats.py : Yes
- schemas/day2_summary.schema.json : Yes
- artifacts/day2/normalized.json : Yes
- artifacts/day2/normalized.yaml : Yes
- artifacts/day2/normalized.xml : Yes
- artifacts/day2/normalized.csv : Yes
- artifacts/day2/summary.json : Yes
- artifacts/day2/pr_link.txt : Yes

## 5. Commands run

### 5.1 Script run
{
  "schema_version": "2.0",
  "generated_utc": "2026-03-25T18:24:11.442046+00:00",
  "student": {
    "token": "D1-IB-23-5b-02-B7C2",
    "token_hash8": "4e19a17f",
    "name": "Бақытбек",
    "group": "IB-23-5b"
  },
  "input": {
    "path": "artifacts/day1/response.json",
    "sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "outputs": {
    "normalized_json_sha256": "77aab9fa4e8e5ccdb5a670973c252c3761b77cef12b1e9167897a6ecf27c95fb",
    "normalized_yaml_sha256": "2a6ee4b37760e30c8b448cbaa472c40f15374607d7f9968df069d9057618bf74",
    "normalized_xml_sha256": "782f3fb0bbd35daea48d554248637c030695ef96a0a98f8cac8c9f97e7c75f50",
    "normalized_csv_sha256": "9af19065e7bd19c229c763845302c4bdf1f7aac430cb3f88db0c1efb76e33eba"
  },
  "computed": {
    "title_len": 18
  }
}

### 5.2 Tests
.. [100%]
2 passed in 0.38s

The script successfully generated normalized data in multiple formats (JSON, YAML, XML, CSV) and created a summary file with SHA256 hashes. All outputs were validated using pytest, and all tests passed successfully.

## 6. What I learned
- Worked with multiple data formats: JSON, YAML, XML, CSV
- Generated SHA256 hashes for data validation
- Used environment variables from `.env`
- Implemented automated testing using pytest
- Validated data using JSON Schema
- Worked with Git branches, pull requests, and merge conflicts

## 7. Problems and solutions
- Problem: `pip` command was not found on macOS
- Fix: Created and activated a virtual environment using `python3 -m venv .venv` and `source .venv/bin/activate`
- Proof: successful execution of `pip install -r requirements.txt`

- Problem: Script failed due to missing environment variables
- Fix: Loaded variables using `export $(cat .env | xargs)`
- Proof: successful execution of script and passing tests

- Problem: Needed to create a merge conflict
- Fix: Modified the same section in README.md in two different branches and resolved it manually
- Proof: `artifacts/day2/conflict_log.txt`
