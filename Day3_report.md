# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student
- Name: Бақытбек
- Group: IB-23-5b
- Token: D1-IB-23-5b-02-B7C2
- Repo: [add your GitHub repository link here]

## 2) Lab 4.5.5 completion evidence
- API docs (Try it out) screenshots: Not available, because the DEVASC VM / lab environment was unavailable.
- Postman screenshots: Not available, because the API host was unreachable from macOS.
- Python run screenshot: Local project structure and files were prepared on macOS, but the live API run could not be completed due to missing lab access.

## 3) Artifacts checklist
- artifacts/day3/books_before.json: No
- artifacts/day3/books_sorted_isbn.json: No
- artifacts/day3/mybook_post.json: No
- artifacts/day3/books_by_me.json: No
- artifacts/day3/add100_report.json: No
- artifacts/day3/postman_collection.json: No
- artifacts/day3/postman_environment.json: No
- artifacts/day3/curl_get_books.txt: No
- artifacts/day3/curl_get_books_isbn.txt: No
- artifacts/day3/curl_get_books_sorted.txt: No
- artifacts/day3/summary.json: No

## 4) Command outputs (paste exact)
### 4.1 Script run
```text
python src/day3_library_lab.py --count 100
```
Not executed successfully because `library.demo.local` was unreachable.

### 4.2 Tests
```text
pytest -q
```
Not executed successfully because required API-generated artifacts were unavailable.

## 5) Problems & fixes (at least 1)
- Problem: The API host `library.demo.local` was not reachable from my MacBook. Both `ping` and `curl` to `http://library.demo.local/api/v1/books` did not return a response. The special DEVASC VM environment was not available, so I could not access the lab API from my local machine.
- Fix: I prepared the full project structure, Python script, JSON schema, pytest file, and report template on macOS. However, the live API artifacts could not be generated because the lab environment was unavailable.
- Proof: Terminal checks with `ping library.demo.local` and `curl http://library.demo.local/api/v1/books` did not complete successfully.
