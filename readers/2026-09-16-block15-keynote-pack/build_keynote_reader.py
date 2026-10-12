"""Build the Block 15 keynote posting-pack reader from the 09-11 reader template.

Output: ~/BGIN_IKP/readers/2026-09-16-block15-keynote-pack/index.html + pack.md
"""
import json, re, pathlib

HOME = pathlib.Path.home()
TEMPLATE = HOME / "BGIN_IKP/readers/2026-09-11-discourse-posting-pack/index.html"
OUT_DIR = HOME / "BGIN_IKP/readers/2026-09-16-block15-keynote-pack"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SESSION = "https://bgin-global.org/events/20261015-block15/sessions/1-2"
PROGRAM = "https://bgin-global.org/events/20261015-block15#program"
REG = "https://www.eventbrite.com/e/bgin-block15-tickets-1990274282957"
CAT44 = "https://bgin.discourse.group/c/post-quantum-crypto-agility-competition/44"
HEADSHOT = "https://bgin-global.org/images/Events/person/AlexPruden.jpeg"

T1054 = "https://bgin.discourse.group/t/workshop-series-w1-w6-sep-2026-feb-2027/1054"
T1012 = "https://bgin.discourse.group/t/block-15-ikp-sessions-proposed-agenda/1012"
T1001 = "https://bgin.discourse.group/t/ikp-post-quantum-cryptography-thread-06-26/1001"
C22 = "https://bgin.discourse.group/c/block-meetings/22"

ABSTRACT = (
    "Cryptography has long been treated as foundational infrastructure: choose secure primitives, implement them correctly, and expect them to remain reliable for decades. That assumption is beginning to break down. Advances in quantum computing are creating a clear migration imperative for widely deployed public-key cryptography, while AI is accelerating both the pace and sophistication of security threats.",
    "In this environment, the challenge is no longer simply choosing the “right” cryptographic algorithm. Organizations need the ability to adapt their cryptographic infrastructure as threats, standards, and technologies evolve. This talk will explore crypto agility as an essential design principle for digital assets and blockchain systems, the practical challenges of migrating systems that secure billions of dollars in value, and why organizations should begin preparing for cryptographic change well before existing standards are broken.",
)

POST_1054 = f"""**The W2 anchor fills in.** The Block 15 keynote slot named above — 15 October, 09:20–09:50 — is *Crypto Agility in the Quantum and AI Era*: **Alex Pruden**, CEO & Co-Founder of Project Eleven.

In the speaker's words: {ABSTRACT[1]}

The talk's three arcs — agility as a design principle for digital-asset systems, the practical cost of migrating systems that secure billions in value, and preparing before standards break — are the frame the two IKP sessions then work in at 09:50 and 11:30, where the committee is seated and the scheme rulings are argued.

Abstract, bio, and speaker links on the session page: {SESSION}"""

POST_1012 = f"""**Keynote for the PQC morning.** Block 15 opens 15 October with *Crypto Agility in the Quantum and AI Era* — **Alex Pruden** (CEO & Co-Founder, Project Eleven), 09:20–09:50, Room A — directly before proposed sessions 1 and 2 above (09:50–11:20 and 11:30–13:00, Room B).

Project Eleven is an applied lab at the intersection of quantum computing and cryptography, hardening digital assets for the post-quantum era; Pruden was previously the first employee and then CEO of Aleo. Abstract and full bio: {SESSION}

Speaker slots in sessions 1 and 2 are still being filled — proposals on this thread. Written contributions presented at the meeting carry the registration fee waiver: {REG}"""

POST_1001 = f"""For the archive: Block 15 opens with a PQC keynote — *Crypto Agility in the Quantum and AI Era*, **Alex Pruden** (CEO & Co-Founder, Project Eleven), 15 October 09:20–09:50, hybrid. Abstract and bio: {SESSION}

The IKP PQC migration sessions follow 09:50–13:00; the competition work continues in the *Post-Quantum Crypto Agility Competition* category: {CAT44}"""

TOPIC_TITLE = "Block 15 opening keynote: Crypto Agility in the Quantum and AI Era — Alex Pruden, Project Eleven"
POST_TOPIC = f"""**Block 15 opens with a keynote on crypto agility.** 15 October, 09:20–09:50, Room A, Georgetown University Capitol Campus, Washington D.C. — hybrid.

![Alex Pruden]({HEADSHOT})

*Crypto Agility in the Quantum and AI Era* — **Alex Pruden**, CEO & Co-Founder, Project Eleven.

In the speaker's words:

> {ABSTRACT[0]}
>
> {ABSTRACT[1]}

Project Eleven is an applied lab of builders and technologists at the intersection of quantum computing and cryptography, hardening digital assets and building the financial rails for the post-quantum era. Before founding it, Pruden was the first employee and then CEO of Aleo, after a decade at GGV Capital, Coinbase, and Andreessen Horowitz. Full bio and links on the session page.

**The morning that follows.** The keynote sets the frame for the two IKP PQC migration sessions in Room B: 09:50–11:20 on resource estimates and the ECDSA.fail community's numbers as judging criteria; 11:30–13:00 on crypto agility as a governance property and the NIST signature migration path, with NIST participation.

- Session page and speaker bio: {SESSION}
- Full program: {PROGRAM}
- Registration (hybrid; fee waivers for written contributions presented at the meeting, submissions close about a week before): {REG}
- The competition work the keynote frames: {CAT44}"""

posts = [
    {
        "id": "s1", "step": "1", "label": "Workshop series thread", "kind": "reply",
        "whereHtml": f'reply on <a href="{T1054}">Workshop series W1–W6, Sep 2026 → Feb 2027</a> (1054, category 44) — its <em>Nearest anchors</em> paragraph already names the 09:20 slot',
        "title": None, "body": POST_1054, "gate": None, "gateKind": None, "postedAt": None, "postedUrl": None,
    },
    {
        "id": "s2", "step": "2", "label": "Block 15 IKP agenda thread", "kind": "reply",
        "whereHtml": f'reply on <a href="{T1012}">Block 15 IKP Sessions: Proposed Agenda</a> (1012, IKP WG) — the keynote sits before proposed sessions 1 and 2',
        "title": None, "body": POST_1012, "gate": None, "gateKind": None, "postedAt": None, "postedUrl": None,
    },
    {
        "id": "s3", "step": "3", "label": "IKP PQC thread", "kind": "reply",
        "whereHtml": f'reply on <a href="{T1001}">IKP Post Quantum Cryptography Thread 06/26</a> (1001, IKP WG) — the archive thread; one paragraph',
        "title": None, "body": POST_1001, "gate": None, "gateKind": None, "postedAt": None, "postedUrl": None,
    },
    {
        "id": "s4", "step": "4", "label": "Standalone announcement", "kind": "new topic · optional",
        "whereHtml": f'new topic in <a href="{C22}">Block Meetings</a> (category 22 — no Block 15 topics there yet; <em>General</em> is the alternative)',
        "title": TOPIC_TITLE, "body": POST_TOPIC,
        "gate": "Optional — the three replies are the announcement on the existing threads. Post this only if a standalone Block 15 topic is wanted. It embeds the headshot from the website, so it needs the site merge first.",
        "gateKind": "flag", "postedAt": None, "postedUrl": None,
    },
]

html = TEMPLATE.read_text(encoding="utf-8")

def sub1(pattern, repl, flags=re.S):
    global html
    new, n = re.subn(pattern, lambda m: repl, html, count=1, flags=flags)
    assert n == 1, pattern
    html = new

sub1(r"<title>.*?</title>", "<title>Block 15 Keynote Posting Pack</title>")
sub1(r'<p class="eyebrow">.*?</p>', '<p class="eyebrow">BGIN · Block 15 · 15 Oct 09:20 · Discourse announcement</p>')
sub1(r"<h1>.*?</h1>", "<h1>Block 15 Keynote Posting Pack</h1>")
sub1(r'<p class="standfirst">.*?</p>',
     '<p class="standfirst">Three replies announce the opening keynote — <em>Crypto Agility in the Quantum and AI Era</em>, Alex Pruden (CEO &amp; Co-Founder, Project Eleven) — on the threads that already carry Block 15. A fourth, optional, is a standalone topic. Every post links the session page, so the website merge comes first.</p>')
sub1(r'<span id="totalCount">\d+</span>', '<span id="totalCount">4</span>')

before = f'''<ul class="checklist" id="beforeList">
          <li><input type="checkbox" id="pre-site"><label for="pre-site"><b>Website first.</b> Commit + push <code>block15-pqc-keynote</code> (<code>~/bgin-homepage-fork</code>), open the PR on bgin-global/bgin-homepage (no Claude attribution), check the Vercel preview of <code>/events/20261015-block15/sessions/1-2</code>, merge.</label></li>
          <li><input type="checkbox" id="pre-200"><label for="pre-200">Production shows the abstract and headshot at <a href="{SESSION}">{SESSION.replace('https://', '')}</a> — the URL exists today with the placeholder text, so the check is the content, not the status code.</label></li>
          <li><input type="checkbox" id="pre-clear"><label for="pre-clear">The abstract, bio, headshot and social links are used exactly as the speaker supplied them; nothing else about the speaker is stated anywhere.</label></li>
        </ul>'''
sub1(r'<ul class="checklist" id="beforeList">.*?</ul>', before)

after = '''<ul class="checklist">
          <li><input type="checkbox" id="post-tick"><label for="post-tick">Tick each step above as it lands; the counter and this browser remember it.</label></li>
          <li><input type="checkbox" id="post-social"><label for="post-social">Socials (X, LinkedIn) are the web team's channel — the first paragraph of step 4 lifts as-is if they want copy.</label></li>
        </ul>'''
sub1(r'<section class="checks after" id="after">\s*<h2>After posting</h2>\s*<ul class="checklist">.*?</ul>',
     '<section class="checks after" id="after">\n        <h2>After posting</h2>\n        ' + after)

foot = '''<footer class="foot">
        <p>Source of the posts: the speaker's abstract, bio and headshot as supplied to BGIN on 16 September 2026; session times from the published Block 15 program. Website change: <code>~/bgin-homepage-fork</code> branch <code>block15-pqc-keynote</code> (session 1-2 only). The markdown pack sits beside this file as <code>pack.md</code>.</p>
        <p>Regenerate after editing a draft: <code>python build_keynote_reader.py</code> (scratchpad; copy kept beside this file).</p>
      </footer>'''
sub1(r'<footer class="foot">.*?</footer>', foot)

sub1(r'<script type="application/json" id="posts">.*?</script>',
     '<script type="application/json" id="posts">' + json.dumps(posts, ensure_ascii=False).replace("</", "<\\/") + "</script>")
sub1(r"var KEY = '[^']*';", "var KEY = 'block15-keynote-pack-v1';")

(OUT_DIR / "index.html").write_text(html, encoding="utf-8", newline="\n")

# markdown pack beside it
md = ["# Block 15 keynote — Discourse posting pack (2026-09-16)", "",
      "Post after the website merge (the session page carries the abstract, bio and headshot).", ""]
for p in posts:
    md += [f"## Step {p['step']} — {p['label']} ({p['kind']})", "",
           re.sub(r"<[^>]+>", "", p["whereHtml"]), ""]
    if p["gate"]:
        md += [f"> **Gate:** {p['gate']}", ""]
    if p["title"]:
        md += [f"**Title:** {p['title']}", ""]
    md += [p["body"], "", "---", ""]
(OUT_DIR / "pack.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
print("wrote", OUT_DIR / "index.html", len(html), "bytes;", len(posts), "posts")
