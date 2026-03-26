Понял тебя. Вот **строго единый блок**, без разрывов, без вынесений — всё подряд как в шаблоне:

````markdown
# Day 5 Report — Module 8 Capstone

## 1) Student
- Name: Бақытбек Мирас Жасуланұлы
- Group: IB-23-5b
- Token: D1-IB-23-5b-02-B7C2
- Repo: https://github.com/dwcwdcec/devnet-day1-IB-23-5b-miras

## 2) YANG (8.3.5)
- Evidence files:
  - artifacts/day5/yang/ietf-interfaces.yang
  - artifacts/day5/yang/pyang_version.txt
  - artifacts/day5/yang/pyang_tree.txt
- Screenshot (optional): pyang tree output generated successfully

## 3) Webex (8.6.7)
- Room title contains token_hash8: Yes
- Message text contains token_hash8: Yes
- Evidence files:
  - artifacts/day5/webex/me.json
  - artifacts/day5/webex/rooms_list.json
  - artifacts/day5/webex/room_create.json
  - artifacts/day5/webex/message_post.json
  - artifacts/day5/webex/messages_list.json

## 4) Packet Tracer Controller REST (8.8.3)
- external_access_check contains “empty ticket”: Yes
- serviceTicket saved: Yes
- Evidence files:
  - artifacts/day5/pt/external_access_check.json
  - artifacts/day5/pt/network_devices.json
  - artifacts/day5/pt/hosts.json
  - artifacts/day5/pt/postman_collection.json
  - artifacts/day5/pt/postman_environment.json
  - artifacts/day5/pt/pt_internal_output.txt

## 5) Commands output (paste exact)
```text
python src/day5_summary_builder.py
pytest -q
````

## 6) Problems & fixes (at least 1)

* Problem: The initially downloaded YANG file was a pointer instead of the actual module, which caused pyang parsing errors and resulted in an empty tree output.
* Fix: Downloaded the correct versioned YANG module and its dependency, then regenerated the tree using pyang.
* Proof: The file pyang_tree.txt contains "+--rw interfaces" and "enabled? boolean", and the summary.json shows validation_passed: true.

```

