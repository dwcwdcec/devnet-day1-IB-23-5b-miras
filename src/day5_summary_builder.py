#!/usr/bin/env python3
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ART = Path("artifacts/day5")
SCHEMA_VERSION = "5.0"


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def token_hash8(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    if not path.exists():
        return ""
    return sha256_text(path.read_text(encoding="utf-8", errors="replace"))


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path):
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main() -> int:
    token = os.getenv("STUDENT_TOKEN", "").strip()
    name = os.getenv("STUDENT_NAME", "").strip()
    group = os.getenv("STUDENT_GROUP", "").strip()
    th8 = token_hash8(token) if token else ""

    pyang_tree = ART / "yang" / "pyang_tree.txt"
    room_create = ART / "webex" / "room_create.json"
    message_post = ART / "webex" / "message_post.json"
    pt_external = ART / "pt" / "external_access_check.json"
    pt_devices = ART / "pt" / "network_devices.json"
    pt_hosts = ART / "pt" / "hosts.json"

    pyang_text = read_text(pyang_tree)
    room_create_json = read_json(room_create)
    message_post_json = read_json(message_post)
    pt_external_text = read_text(pt_external)
    pt_devices_text = read_text(pt_devices)
    pt_hosts_text = read_text(pt_hosts)

    room_title = room_create_json.get("title", "")
    message_text = message_post_json.get("text", "")

    yang_ok = "+--rw interfaces" in pyang_text and "enabled?" in pyang_text and "boolean" in pyang_text
    webex_ok = th8 != "" and th8 in room_title and th8 in message_text
    pt_ok = (
        "empty ticket" in pt_external_text.lower()
        and '"version": "1.0"' in pt_devices_text
        and '"version": "1.0"' in pt_hosts_text
    )

    summary = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": now_utc(),
        "student": {
            "token": token,
            "token_hash8": th8,
            "name": name,
            "group": group,
        },
        "yang": {
            "ok": yang_ok,
            "evidence_sha": {
                "ietf_interfaces_yang": sha256_file(ART / "yang" / "ietf-interfaces.yang"),
                "pyang_version": sha256_file(ART / "yang" / "pyang_version.txt"),
                "pyang_tree": sha256_file(ART / "yang" / "pyang_tree.txt"),
            },
        },
        "webex": {
            "ok": webex_ok,
            "room_title_contains_hash8": th8 in room_title if th8 else False,
            "message_text_contains_hash8": th8 in message_text if th8 else False,
            "evidence_sha": {
                "me": sha256_file(ART / "webex" / "me.json"),
                "rooms_list": sha256_file(ART / "webex" / "rooms_list.json"),
                "room_create": sha256_file(ART / "webex" / "room_create.json"),
                "message_post": sha256_file(ART / "webex" / "message_post.json"),
                "messages_list": sha256_file(ART / "webex" / "messages_list.json"),
            },
        },
        "pt": {
            "ok": pt_ok,
            "empty_ticket_seen": "empty ticket" in pt_external_text.lower(),
            "evidence_sha": {
                "external_access_check": sha256_file(ART / "pt" / "external_access_check.json"),
                "service_ticket": sha256_file(ART / "pt" / "serviceTicket.txt"),
                "network_devices": sha256_file(ART / "pt" / "network_devices.json"),
                "hosts": sha256_file(ART / "pt" / "hosts.json"),
                "pt_internal_output": sha256_file(ART / "pt" / "pt_internal_output.txt"),
                "postman_collection": sha256_file(ART / "pt" / "postman_collection.json"),
                "postman_environment": sha256_file(ART / "pt" / "postman_environment.json"),
            },
        },
        "bonus": {
            "optional_ok": False,
            "evidence_sha": {},
        },
        "validation_passed": bool(yang_ok and webex_ok and pt_ok),
        "run": {
            "python": sys.version.split()[0],
            "platform": sys.platform,
        },
    }

    out = ART / "summary.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["validation_passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
