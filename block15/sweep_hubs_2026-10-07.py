"""One-off sweep: Block 15 session pointers + FASE documents on project hubs and sessions 2-3 / 2-5."""
import json, re, subprocess, sys

ROOT = r"C:\Users\mitch\bgin-homepage-fork"
HUBS = ROOT + r"\contents\projectHubs.ts"
q = lambda v: json.dumps(v, ensure_ascii=False)

DP = "https://docs.google.com/document/d/1JEJYKLRpNIGZe36kCbjQbzbGc7PGF02U/edit"
SR = "https://docs.google.com/document/d/1td0hDHE-Ahq9KG7I-pS0QULtQtvqCy1mmG1pkqdUfks/edit"
DECK = "https://docs.google.com/presentation/d/1C7DsLsA9UCPvYBO8r6eXIehZN3-fa7aJUiiCU6yczXc/edit"

# --- sessions: documents via the apply script ---
sess = {
    "2-3": {"documents": [
        {"title": "Discussion Paper: The Industrial Structure of Digital Assets (Study Group on the Ideal Industrial Structure for Digital Assets, version of 11 June 2026)", "link": DP, "type": "Discussion Paper"},
        {"title": "FASE contribution: Offshore, Infrastructure, Public Goods — early findings on three open questions (discussion draft, 23 Sep 2026)", "link": DECK, "type": "Slides"},
    ]},
    "2-5": {"documents": [
        {"title": "BGIN SR (FASE): Compute-as-Commodity — Observable Flows in Decentralised Compute Infrastructure (open for comment)", "link": SR, "type": "Study Report"},
    ]},
}
tmp = ROOT + r"\..\BGIN_IKP\block15\_sweep_sessions.json"
json.dump(sess, open(tmp, "w", encoding="utf-8"), ensure_ascii=False)
subprocess.run([sys.executable, ROOT + r"\..\BGIN_IKP\block15\apply_block15_sessions.py", tmp], check=True)

# --- hubs ---
s = open(HUBS, encoding="utf-8").read()


def hub_span(slug):
    m = re.search(r'\n  \{\n    slug: "' + re.escape(slug) + r'",', s)
    return m.start(), s.index("\n  },", m.end())


def set_field(slug, key, val):
    global s
    a, b = hub_span(slug)
    body = s[a:b]
    pat = re.compile(r"\n    " + key + r":\s*\n?\s*\"(?:[^\"\\]|\\.)*\",")
    sep = "\n      " if len(q(val)) > 70 else " "
    new = f"\n    {key}:{sep}{q(val)},"
    if pat.search(body):
        body = pat.sub(lambda _: new, body, count=1)
    else:  # insert before nextMilestone / documents
        anchor = "\n    nextMilestone:" if "\n    nextMilestone:" in body else "\n    documents:"
        body = body.replace(anchor, new + anchor, 1)
    s = s[:a] + body + s[b:]


def prepend_docs(slug, docs):
    global s
    a, b = hub_span(slug)
    body = s[a:b]
    items = "".join(
        f"\n      {{\n        type: {q(d['type'])},\n        title: {q(d['title'])},\n        when: {q(d['when'])},\n        href: {q(d['href'])},\n      }},"
        for d in docs)
    assert "\n    documents: [" in body, slug
    body = body.replace("\n    documents: [", "\n    documents: [" + items, 1)
    s = s[:a] + body + s[b:]


MILESTONES = {
    "ai-blockchain": "Block 15 · 15 Oct, 09:50 (session 1-3)",
    "agent-standards": "Block 15 · 15 Oct, 09:50 (session 1-5, open space)",
    "security-supply-chain": "Block 15 · 15 Oct, 11:30 (session 1-6)",
    "harmonization": "Block 15 · 16 Oct, 09:50 (session 2-3)",
    "security-ai-agent": "Block 15 · 16 Oct, 09:50 (session 2-4)",
    "cybersecurity-information-sharing": "Block 15 · 16 Oct, 09:50 (session 2-4) · ISO path",
    "decentralization-metrics": "Block 15 · 16 Oct, 11:30 (session 2-5)",
    "privacy-enhanced-auth": "Block 15 · 16 Oct, 11:30 (session 2-6) + lunch session with World",
    "stablecoin-guide": "Block 15 · 16 Oct, 14:00 (session 2-7)",
    "offline-key-management": "Block 15 · 16 Oct, 14:00 (session 2-8)",
    "forensics-analysis": "Block 15 · 16 Oct, 15:40 (session 2-9)",
    "illicit-activities": "Block 15 · 16 Oct, 15:40 (session 2-9)",
    "st-pp": "Block 15 · 16 Oct, 15:40 (session 2-10)",
}
for slug, v in MILESTONES.items():
    set_field(slug, "nextMilestone", v)

set_field("harmonization", "statusText",
    "The Discussion Paper \"The Industrial Structure of Digital Assets\" (Study Group on the Ideal Industrial Structure for Digital Assets) was first presented at Block 14 in Tokyo and has been revised through open consultation; the current version is dated 11 June 2026. A FASE contribution (discussion draft, 23 September 2026) reports early findings on three of its six open questions: competitive asymmetry, infrastructure and global markets, and public chains as public goods. Block 15 session 2-3 takes all six questions to the room.")
set_field("harmonization", "latestDocumentTitle", "Discussion Paper: The Industrial Structure of Digital Assets (11 June 2026)")
prepend_docs("harmonization", [
    {"type": "Discussion", "title": "The Industrial Structure of Digital Assets — Discussion Paper (version of 11 June 2026)", "when": "2026/06", "href": DP},
    {"type": "Slides", "title": "FASE contribution: Offshore, Infrastructure, Public Goods (discussion draft)", "when": "2026/09", "href": DECK},
])

set_field("decentralization-metrics", "statusText",
    "Report work in progress, informed by jurisdictional debates (e.g. maturity / classification). The FASE study report \"Compute-as-Commodity\" asks whether decentralised compute networks can be considered commodity markets: it applies six commodity-market criteria to Akash, Bittensor, Render and Aethir, tests whether the blockchain layer is load-bearing, and separates productive from circular flows. It is open for comment and is discussed at Block 15 session 2-5.")
set_field("decentralization-metrics", "latestDocumentTitle", "BGIN SR: Compute-as-Commodity (open for comment)")
prepend_docs("decentralization-metrics", [
    {"type": "Draft", "title": "BGIN SR (FASE): Compute-as-Commodity — Observable Flows in Decentralised Compute Infrastructure", "when": "2026/10", "href": SR},
])

set_field("ai-blockchain", "statusText",
    "Block 15 session 1-3 gives an overview of the AI and blockchain industry as it stands today — agents that hold wallets and pay in stablecoins, on-chain provenance for data, models and outputs, AI for on-chain analytics and auditing — and puts the policy questions to the room: accountability when an autonomous agent transacts, agent identity and authorisation, and AML/CFT and consumer protection for machine-initiated activity. The discussion scopes the FASE AI + Blockchain workstream.")

set_field("privacy-enhanced-auth", "statusText",
    "Block 14 produced two meeting reports (Privacy Enhanced Authentication and Key Management; Proof of Personhood). An IKP research pathway on zero-knowledge proofs for biometric authentication opened in July 2026, and the privacy / proof-of-personhood taxonomy has been taken through open, topic-focused IKP meetings since. At Block 15 the dedicated session on 16 October (2-6) covers privacy-enhanced authentication, the proof-of-personhood taxonomy, verifiable trust agents and zero-knowledge proofs, with World as a main discussant; World follows with a lunchtime industry session.")

open(HUBS, "w", encoding="utf-8", newline="").write(s)
print("hubs updated")
