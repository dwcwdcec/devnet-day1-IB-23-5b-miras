# Day 1 Report — DevNet Sprint

## 1. Student
- Name: Бақытбек Мирас Жасуланұлы
- Group: IB-23-5b
- GitHub repo: https://github.com/dwcwdcec/devnet-day1-IB-23-5b-miras
- Day1 Token: D1-IB-23-5b-02-B7C2

## 2. NetAcad progress (Module 1)
- Completed items: 1.1, 1.2, 1.3
- Screenshot(s): 
  - NetAcad progress screenshot attached

## 3. VM evidence
- File: `artifacts/day1/env.txt` exists: Yes
- Screenshot(s):
  - Terminal output with env.txt attached

## 4. Repo structure (must match assignment)
- src/day1_api_hello.py : Yes
- tests/test_day1_api_hello.py : Yes
- schemas/day1_summary.schema.json : Yes
- artifacts/day1/summary.json : Yes
- artifacts/day1/response.json : Yes

## 5. Commands run

### 5.1 Script run
{
  "schema_version": "1.0",
  "generated_utc": "2026-03-25T17:43:25.435551+00:00",
  "student": {
    "token": "D1-IB-23-5b-02-B7C2",
    "name": "Бақытбек",
    "group": "IB-23-5b"
  },
  "api": {
    "url": "https://jsonplaceholder.typicode.com/todos/1",
    "status_code": 200,
    "validation_passed": true,
    "validation_errors": [],
    "response_sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "run": {
    "python": "3.14.0",
    "platform": "darwin"
  }
}

### 5.2 Tests
. [100%]
1 passed in 0.23s

## 6. What I learned
- Created and used Python virtual environment
- Installed dependencies using pip
- Performed HTTP GET request to REST API
- Saved API response to JSON file
- Calculated SHA256 hash
- Wrote and executed unit tests using pytest

## 7. Problems and solutions
- Problem: DEVASC VM could not be launched on Mac due to ARM vs x86 incompatibility.
- Fix: Completed the assignment using macOS terminal with the same structure and required artifacts.
- Proof: artifacts/day1/env.txt, script output, pytest results
