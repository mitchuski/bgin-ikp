"""Patch Block 15 session fields in bgin-homepage-fork/lib/block15-program-data.ts from a JSON file.

JSON shape: { "<session id>": { "summary"?: str, "speakers"?: str, "moderator"?: str,
                                "title"?: str, "room"?: str,
                                "agenda"?: [str], "documents"?: [{title, link, type}] } }
Only the fields given are replaced. Usage: python apply_block15_sessions.py <updates.json> [ts path]
"""
import json, re, sys

ts = sys.argv[2] if len(sys.argv) > 2 else r"C:\Users\mitch\bgin-homepage-fork\lib\block15-program-data.ts"
updates = json.load(open(sys.argv[1], encoding="utf-8"))
src = open(ts, encoding="utf-8").read()
q = lambda v: json.dumps(v, ensure_ascii=False)
I = " " * 10  # field indent inside a session object


def block_span(s, sid):
    m = re.search(r'\n        \{\n          id: "' + re.escape(sid) + r'",', s)
    if not m:
        raise SystemExit(f"session {sid} not found")
    end = s.index("\n        },", m.end())
    return m.start(), end


def set_scalar(body, key, val):
    pat = re.compile(r"(\n" + I + key + r":)\s*\n?\s*\"(?:[^\"\\]|\\.)*\",")
    if pat.search(body):
        sep = f"\n{I}  " if key in ("summary", "title") and len(q(val)) > 60 else " "
        return pat.sub(lambda _: f"\n{I}{key}:{sep}{q(val)},", body, count=1)
    # field absent (e.g. 1-6 has no speakers): insert after wg
    return re.sub(r"(\n" + I + r'wg: "[^"]*",)', lambda m: m.group(1) + f"\n{I}{key}: {q(val)},", body, count=1)


def set_list(body, key, items):
    if key == "agenda":
        inner = "".join(f"\n{I}  {q(x)}," for x in items)
    else:
        inner = "".join(
            f"\n{I}  {{\n{I}    title: {q(d['title'])},\n{I}    link: {q(d['link'])},\n{I}    type: {q(d['type'])},\n{I}  }},"
            for d in items)
    new = f"\n{I}{key}: [{inner}\n{I}]," if items else f"\n{I}{key}: [],"
    pat = re.compile(r"\n" + I + key + r": \[(?:\]|.*?\n" + I + r"\]),", re.S)
    if not pat.search(body):
        raise SystemExit(f"{key} not found")
    return pat.sub(lambda _: new, body, count=1)


for sid, fields in updates.items():
    a, b = block_span(src, sid)
    body = src[a:b]
    for k in ("title", "room", "summary", "speakers", "moderator"):
        if k in fields:
            body = set_scalar(body, k, fields[k])
    for k in ("agenda", "documents"):
        if k in fields:
            body = set_list(body, k, fields[k])
    src = src[:a] + body + src[b:]
    print("updated", sid, sorted(fields))

open(ts, "w", encoding="utf-8", newline="").write(src)
