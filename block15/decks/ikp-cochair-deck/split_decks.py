"""Split the combined IKP co-chair deck into one deck per chaired session."""
import os, re, shutil, sys

SRC = r"C:\Users\mitch\BGIN_IKP\block15\decks\ikp-cochair-deck\Block15_IKP_CoChair_Sessions.tex"
OUT = r"C:\Users\mitch\BGIN_IKP\block15\decks"
LOGOS = [r"C:\Users\mitch\BGIN_IKP\block15\decks\ikp-cochair-deck\bgin_logo.png",
         r"C:\Users\mitch\BGIN_IKP\block15\decks\ikp-cochair-deck\bgin_mark.png"]

src = open(SRC, encoding="utf-8").read()
pre, body = src.split("\\begin{document}\n", 1)
body = body.replace("\\end{document}", "")

# blocks keyed by the label after "% ===...= "
blocks = {}
order = []
for chunk in re.split(r"\n(?=% =+ )", body):
    m = re.match(r"% =+ (.+)\n", chunk)
    if not m:
        continue
    key = m.group(1).strip()
    blocks[key] = chunk.strip("\n") + "\n"
    order.append(key)
print("blocks:", order)

def block(key):
    return blocks[key]

def preamble(footer_left, footer_right):
    p = pre.replace("BGIN Block 15 --- IKP Working Group sessions\\hfill Washington, D.C. \\textbar{} 15--16 Oct 2026 / \\insertframenumber",
                    footer_left + "\\hfill " + footer_right + " / \\insertframenumber")
    assert footer_left in p
    return p

def title_frame(accent, title, sub, who, when, note):
    return r"""%% ================================================================ TITLE
{\setbeamertemplate{footline}{}
\begin{frame}[plain,t]
  \begin{tikzpicture}[remember picture,overlay]
    \fill[bar] (current page.north west) rectangle ([yshift=-3.5cm]current page.north east);
    \node[anchor=north east,inner sep=0] at ([xshift=-7mm,yshift=-5mm]current page.north east){\includegraphics[height=1.9cm]{bgin_logo.png}};
    \node[anchor=west,text=white,font=\Large\bfseries,text width=11.2cm,align=left] at ([xshift=7mm,yshift=-1.35cm]current page.north west){%s};
    \node[anchor=west,text=%s,font=\small,text width=11.2cm,align=left] at ([xshift=7mm,yshift=-2.85cm]current page.north west){%s};
    \node[anchor=west,font=\normalsize,text width=13.2cm] at ([xshift=7mm,yshift=-4.6cm]current page.north west){%s};
    \node[anchor=north west,font=\small,text=soft,text width=13.2cm,align=left] at ([xshift=7mm,yshift=-5.0cm]current page.north west){%s};
    \node[anchor=west,font=\scriptsize,text=soft,text width=13cm,align=left] at ([xshift=7mm,yshift=-6.5cm]current page.north west){%s};
  \end{tikzpicture}
\end{frame}}
""" % (title, accent, sub, who, when, note)

def context_frame(leadcmd, title, lead, agenda, takeaway):
    items = "\n".join("    \\item %s" % a for a in agenda)
    return r"""%% ================================================================ CONTEXT
\begin{frame}{%s}
  \%s{%s}
  \begin{enumerate}\footnotesize\setlength{\itemsep}{0.5mm}
%s
  \end{enumerate}
  \takeaway{%s}
\end{frame}
""" % (title, leadcmd, lead, items, takeaway)

def engage_frame(bullets, qrs, takeaway):
    b = "\n".join("        \\item %s" % x for x in bullets)
    cols = len(qrs)
    spec = "@{\\hspace{1mm}}".join([">{\\centering\\arraybackslash}p{1.85cm}"] * cols)
    row1 = " &\n          ".join("\\qrcode[height=1.35cm]{%s}" % u for u, _, _ in qrs)
    row2 = " & ".join("\\textbf{%s}" % l for _, l, _ in qrs)
    row3 = " & ".join(t for _, _, t in qrs)
    return r"""%% ================================================================ ENGAGE
\begin{frame}{How to Engage}
  \begin{columns}[T]
    \begin{column}{0.55\textwidth}
      \begin{itemize}\small
%s
      \end{itemize}
    \end{column}
    \begin{column}{0.42\textwidth}
      \begin{center}\tiny
        \begin{tabular}{@{}%s@{}}
          %s \\[0.5mm]
          %s \\
          %s
        \end{tabular}
      \end{center}
    \end{column}
  \end{columns}
  \takeaway{%s}
\end{frame}
""" % (b, spec, row1, row2, row3, takeaway)

def close_frame(big, small, foot):
    return r"""%% ================================================================ CLOSE
{\setbeamertemplate{footline}{}
\begin{frame}[plain]
  \begin{tikzpicture}[remember picture,overlay]
    \fill[bar] (current page.north west) rectangle (current page.south east);
    \node[anchor=south,text=white,font=\Large\bfseries,text width=13.5cm,align=center,execute at begin node=\nohyph] at ([yshift=6mm]current page.center){%s};
    \node[anchor=north,text=white,font=\small,text width=13.5cm,align=center,execute at begin node=\nohyph] at ([yshift=3mm]current page.center){%s};
    \node[anchor=north,text=soft,font=\small,text width=13.5cm,align=center,execute at begin node=\nohyph] at ([yshift=-9mm]current page.center){%s};
    \node[anchor=south east,inner sep=0] at ([xshift=-7mm,yshift=5mm]current page.south east){\includegraphics[height=1.4cm]{bgin_logo.png}};
  \end{tikzpicture}
\end{frame}}
""" % (big, small, foot)

def retitle(tex, old, new):
    assert old in tex, old
    return tex.replace(old, new, 1)

SESS = "https://bgin-global.org/events/20261015-block15/sessions/"
REPO = "https://github.com/bgin-global/pqc-agility-competition"
DISC_PQC = "https://bgin.discourse.group/c/post-quantum-crypto-agility-competition/44"
DISC = "https://bgin.discourse.group"
FORENSICS_DOC = "https://docs.google.com/document/d/1Of9E5govjRFNRjdyvHQIeV42LHegUGC1dRoFYreQk8E/edit"

decks = {}

# ---------------------------------------------------------------- 1-4
d = []
d.append(title_frame("pqc",
    "PQC Migration (1) --- Resource Estimates into Judging Criteria",
    "IKP session 1-4 \\textperiodcentered{} Workshop W2 of the PQC Migration Prize series",
    "Mitchell Travers (chair) \\textperiodcentered{} Kanta Matsuura \\textperiodcentered{} Tadahiko Itoh \\textperiodcentered{} BGIN IKP Working Group",
    "BGIN Block \\#15 \\textbar{} Georgetown University Capitol Campus, Washington, D.C. \\textbar{} 15 October 2026, Room B, 09:50--11:20 \\textbar{} hybrid",
    "Picks up from the opening keynote (Alex Pruden, Project Eleven, 09:20) and continues in session 1-7 at 11:30 \\textperiodcentered{} facts follow bgin-global/pqc-agility-competition, draft v0 \\textperiodcentered{} ecosystem-neutral: no chain and no scheme is endorsed"))
d.append(context_frame("lead", "This Session --- What It Is For",
    "First of two IKP working sessions on the PQC Migration Prize (hosted by METI/NEDO; BGIN coordinates and runs the neutral testbed). From the keynote to the competition: crypto agility as the thing being evaluated --- deployment, evaluation, testbeds and migration governance, not new primitives.",
    ["Tour of the public competition repository: governance, outcomes O1--O6, the 22-metric register (draft v0), the scheme register and the harness specification",
     "Resource estimates and the ECDSA.fail community: what the benchmark numbers mean for migration timelines and for judging criteria",
     "Open question: is the headline quantity total overhead or migration speed?",
     "Open question: who must upgrade first --- node operators or users --- and how the metrics reflect that burden split",
     "Open question: scoring the legitimate-owner-versus-attacker race during a migration window",
     "Tagging each metric by the attack class it defends against --- on-spend, at-rest, on-setup (the GDC26 taxonomy)"],
    "Leave with directions per metric for the v0 $\\rightarrow$ v1 pass that session 1-7 consolidates, and owners for the three open questions above."))
d.append(block("6 not another primitive"))
d.append(block("7 the numbers"))
d.append(block("8 taxonomy"))
d.append(block("9 estimate -> criterion"))
d.append(block("10 three lanes"))
d.append(r"""%% ================================================================ discussion
\begin{frame}{Session 1-4 --- Discussion Items}
  \begin{enumerate}\small
    \item What would make a \textbf{resource estimate} usable for an evaluator --- assumptions, error bars, and what must not be collapsed into a Q-day date? What language does the rubric refuse (single Q-day, vendor screenshots)?
    \item Which \textbf{objects} move first: at-rest keys, on-spend paths, credentials, the proof and key-management path (PQ ZKP, MPC)? Open question 6 needs an owner.
    \item Is the headline quantity \textbf{total overhead} or \textbf{migration speed}? Who upgrades first, and how does M-12 record the burden split?
    \item Should the ECDSA.fail benchmark's \textbf{public-note discipline} (exact model and harness named, re-run by a validator) be the admission rule for agent-produced numbers in the record? (Decision 0001.)
    \item What does the \textbf{``PQC-ready chain'' definition} have to contain for M-22 to be scorable by December?
  \end{enumerate}
  \par\vspace{1mm}
  {\small Everything raised here is consolidated into the metric register v1 in session 1-7 at 11:30, where the scheme-scope rulings and the committee seating are taken.}
\end{frame}
""")
d.append(retitle(block("15 timeline"), "PQC --- From This Room to the 2028 Award", "From This Room to the 2028 Award"))
d.append(engage_frame(
    ["\\textbf{Evaluation committee} --- draft call text, metrics and rubrics in Phase A; nominate via the issue template, with a conflict-of-interest disclosure.",
     "\\textbf{Technical advisor} --- Bitcoin / Ethereum / measurement input without winner votes.",
     "\\textbf{Metric or scheme proposal} --- an issue, then a pull request to the register. Every commit is signed and signed-off; a PR is the record.",
     "\\textbf{SSR workshop, 13 Dec} --- accepted papers feed the competition specification.",
     "\\textbf{Next}: session 1-7 at 11:30, same room --- agility as a governance property, the NIST path, the W2 decisions."],
    [(SESS + "1-4", "This session", "bgin-global.org/events/ 20261015-block15/sessions/1-4"),
     (REPO, "Repository", "github.com/bgin-global/ pqc-agility-competition"),
     (DISC_PQC, "Discourse category", "bgin.discourse.group/c/ post-quantum-crypto-agility-competition/44")],
    "Discussion on Discourse; the repository is the record. Nothing is final until the committee ratifies it and the host publishes the call."))
d.append(close_frame("An estimate enters the rubric as a declared assumption with error bars --- never as a date.",
    "The hard problem is deployment, evaluation, and migration governance. Not selecting a new primitive. Not a Q-day. Not an endorsement.",
    "BGIN IKP Working Group \\textperiodcentered{} Post-Quantum Crypto Agility Competition category on the BGIN Discourse \\textperiodcentered{} github.com/bgin-global/pqc-agility-competition"))
decks["1-4-pqc-estimates/Block15_1-4_PQC_Resource_Estimates"] = (
    preamble("BGIN Block 15 --- IKP 1-4: PQC Migration (1)", "Washington, D.C. \\textbar{} 15 Oct 2026, 09:50"), d)

# ---------------------------------------------------------------- 1-7
d = []
d.append(title_frame("pqc",
    "PQC Migration (2) --- Crypto Agility as Governance; the NIST Path; the Decisions",
    "IKP session 1-7 \\textperiodcentered{} Workshop W2 of the PQC Migration Prize series \\textperiodcentered{} with NIST participation",
    "Mitchell Travers (chair) \\textperiodcentered{} Kanta Matsuura \\textperiodcentered{} Tadahiko Itoh \\textperiodcentered{} BGIN IKP Working Group",
    "BGIN Block \\#15 \\textbar{} Georgetown University Capitol Campus, Washington, D.C. \\textbar{} 15 October 2026, Room B, 11:30--13:00 \\textbar{} hybrid",
    "The decisions session: seat the evaluation committee, take the scheme-scope rulings, move the metric register from v0 to v1 \\textperiodcentered{} facts follow bgin-global/pqc-agility-competition, draft v0 \\textperiodcentered{} ecosystem-neutral: no chain and no scheme is endorsed"))
d.append(context_frame("lead", "This Session --- What It Is For",
    "Second IKP working session on the PQC Migration Prize --- the decisions session. Crypto agility as a governance property and the NIST PQC signature migration path across Bitcoin, Ethereum and other ecosystems. Block 15 is the second workshop (W2) of the six-month series on the pathway from competition to BGIN Standard to ISO/TC 307.",
    ["Seating the evaluation committee (Phase A): nominations, conflict-of-interest disclosures, chairs",
     "Scheme-scope rulings for the testbed: ML-DSA, SLH-DSA, FN-DSA, XMSS, LMS and the classical baselines --- recorded as decision records",
     "Metrics register v0 $\\rightarrow$ v1: consolidating the feedback from session 1-4",
     "Reference CPU class and reference transaction mix / block --- anchors for the performance metrics",
     "Whether consensus-layer and user-level evidence are scored on one rubric or two",
     "Proposed open-benchmark model for calibration tracks (decision record 0001)",
     "Pathway and next steps: testbed workshop (Nov), rubric, ``PQC-ready chain'' definition and call-text input package at the SSR co-located workshop (13 Dec, Baltimore), BGIN Standard outline (Feb 2027) toward ISO/TC 307"],
    "Leave with a seated committee, a v1 metric register, scheme rulings on record, and named owners for the open questions --- not a locked migration spec."))
d.append(block("11 agility"))
d.append(block("12 NIST path"))
d.append(block("13 decisions"))
d.append(retitle(block("14 open questions"), "PQC --- The Open Questions That Need Owners Today", "The Open Questions That Need Owners Today"))
d.append(retitle(block("15 timeline"), "PQC --- From This Room to the 2028 Award", "From This Room to the 2028 Award"))
d.append(engage_frame(
    ["\\textbf{Evaluation committee} --- nominate via the issue template; seats are individuals with COI disclosure, not projects.",
     "\\textbf{Second convener} --- the record cannot move on one signing key; a second convener with a key restores the approval rule.",
     "\\textbf{Testbed node host} --- a university or neutral lab; the call opens at W3 (November); hosting is separated from judging.",
     "\\textbf{SSR workshop, 13 Dec} --- rubric v1, the ``PQC-ready chain'' definition, and the call-text input package.",
     "\\textbf{Submit / build} --- when the official call opens (planned 2027)."],
    [(SESS + "1-7", "This session", "bgin-global.org/events/ 20261015-block15/sessions/1-7"),
     (REPO, "Repository", "github.com/bgin-global/ pqc-agility-competition"),
     (DISC_PQC, "Discourse category", "bgin.discourse.group/c/ post-quantum-crypto-agility-competition/44")],
    "Discuss on Discourse, record by pull request, rule by decision record. Every vote and every scope ruling gets an ADR."))
d.append(close_frame("Agility is harder than readiness, and it is what future-proofs the system.",
    "The register tracks NIST's list; it never extends it. When the list moves, the agility metrics are what say whether a stack can follow.",
    "BGIN IKP Working Group \\textperiodcentered{} Post-Quantum Crypto Agility Competition category on the BGIN Discourse \\textperiodcentered{} github.com/bgin-global/pqc-agility-competition"))
decks["1-7-pqc-agility/Block15_1-7_PQC_Agility_Governance"] = (
    preamble("BGIN Block 15 --- IKP 1-7: PQC Migration (2)", "Washington, D.C. \\textbar{} 15 Oct 2026, 11:30"), d)

# ---------------------------------------------------------------- 2-6
d = []
d.append(title_frame("pop",
    "Privacy Enhanced Authentication, ZKP \\& Proof of Personhood",
    "IKP session 2-6 \\textperiodcentered{} authentication that proves the claim without disclosing the person",
    "Mitchell Travers (chair) \\textperiodcentered{} World as main discussant \\textperiodcentered{} contributors to the IKP proof-of-personhood paper",
    "BGIN Block \\#15 \\textbar{} Georgetown University Capitol Campus, Washington, D.C. \\textbar{} 16 October 2026, Room B, 11:30--13:00, then the World lunch session 13:00--14:00 \\textbar{} hybrid",
    "Builds on the Block 14 reports \\emph{Privacy Enhanced Authentication and Key Management} and \\emph{Proof of Personhood} and the open IKP meetings since \\textperiodcentered{} disclosure: the chair also co-chairs the ToIP DTG ZKP Task Force; observations on that work are personal and from public materials"))
d.append(context_frame("poplead", "This Session --- What It Is For",
    "Privacy-enhanced authentication at a high level, the proof-of-personhood taxonomy and the distinctions it has to keep, verifiable trust agents acting for a person, and where zero-knowledge proofs do the work. Twenty minutes for contributors, then open discussion into the IKP proof-of-personhood paper.",
    ["Why now: agentic AI raises the cost of not knowing a counterparty is human",
     "Prove the claim, not the identity: minimal disclosure, unlinkability, what each proof proves, where the biometric lives, what revocation means when the binding cannot be rotated",
     "The taxonomy, with World as main discussant: unique human versus specific human, humanity versus uniqueness, linkability scope, strength expression, continuity, agent authority",
     "Verifiable trust agents: an agent acting for a person carrying personhood assurance with delegated scope",
     "ZKP where it earns its place: predicates that carry strength, client-side proving on everyday phones, post-quantum readiness of the stack",
     "Contributions (20 min); then the gaps nobody owns yet; then next steps into the paper, public comment, and the ISO TC 307 Technical Report path"],
    "Leave with room comments on the paper's structure, a contributor list, and the unclaimed gaps confirmed as IKP's contribution."))
d.append(block("17 why now"))
d.append(block("18 prove the claim"))
d.append(block("19 the layers"))
d.append(block("20 five distinctions"))
d.append(block("21 three graphs + dual agent"))
d.append(block("22 verifiable trust agents"))
d.append(block("23 ZKP where it earns its place"))
d.append(block("24 gaps nobody owns"))
d.append(block("25 discussion"))
d.append(block("26 next steps"))
d.append(engage_frame(
    ["\\textbf{Read} the two Block 14 meeting reports on the Privacy Enhanced Authentication hub.",
     "\\textbf{Add research questions} to the ZKP / biometric authentication pathway thread on the IKP Discourse.",
     "\\textbf{Join} the open, topic-focused IKP meetings on the taxonomy between Blocks.",
     "\\textbf{Comment} on the proof-of-personhood paper when it is released for public comment; contributors are credited in it.",
     "\\textbf{Stay} for the lunch session with World, 13:00 in this room: proof of a unique human in practice, and the client-side ZK tooling behind it."],
    [(SESS + "2-6", "This session", "bgin-global.org/events/ 20261015-block15/sessions/2-6"),
     ("https://bgin-global.org/projects/privacy-enhanced-auth", "Project hub", "bgin-global.org/projects/ privacy-enhanced-auth"),
     (DISC, "BGIN Discourse", "bgin.discourse.group")],
    "The paper goes out for public comment after this Block; the room's comments decide what it says about strength, uniqueness and agent authority."))
d.append(close_frame("Prove the claim, not the identity.",
    "The person is proven at the overlap: what they know, what they promise, and the trust that emerges between two agents that can never fully see each other.",
    "BGIN IKP Working Group \\textperiodcentered{} Privacy Enhanced Authentication hub on bgin-global.org \\textperiodcentered{} bgin.discourse.group"))
decks["2-6-pea-zkp-pop/Block15_2-6_PEA_ZKP_Proof_of_Personhood"] = (
    preamble("BGIN Block 15 --- IKP 2-6: Privacy Enhanced Authentication, ZKP \\& Proof of Personhood", "Washington, D.C. \\textbar{} 16 Oct 2026, 11:30"), d)

# ---------------------------------------------------------------- 2-9
d = []
d.append(title_frame("aml",
    "AML Policy, Forensics \\& Analytics --- a Common Taxonomy",
    "Joint FASE / IKP session 2-9 \\textperiodcentered{} the \\emph{Forensics \\& Analysis} document in public comment, and the common lexicon of harmful on-chain activities",
    "Mitchell Travers (Co-Chair, IKP) \\textperiodcentered{} Chloe White (Co-Chair, FASE)",
    "BGIN Block \\#15 \\textbar{} Georgetown University Capitol Campus, Washington, D.C. \\textbar{} 16 October 2026, Room A, 15:40--17:10 \\textbar{} hybrid",
    "Continues the Block 14 joint session \\emph{Forensics \\& Analysis --- Common Lexicon of Harmful Activities} (Tokyo, March 2026) \\textperiodcentered{} the lexicon records typologies and signals, not verdicts; no tool, vendor or jurisdiction is endorsed"))
d.append(context_frame("amllead", "This Session --- What It Is For",
    "Review the comments received on the public-comment document, settle the forensics-versus-analytics framing, advance the common lexicon, agree what guidance VASPs, investigators and educators need, and ask what can be inferred, by whom, with what safeguards.",
    ["The Forensics \\& Analysis document in public comment: review of comments received",
     "Forensics versus analytics: settling the common framing",
     "The illicit-activity common lexicon: terms in progress and how practitioners and policymakers use them",
     "Guidance for VASPs, investigators and educators",
     "Privacy and proportionality in analytics: what can be inferred, by whom, and with what safeguards",
     "Next steps toward publication"],
    "Leave with comment dispositions, the framing settled as the document's first section, and the lexicon's v1 scope and record shape."))
d.append(block("28 where it came from"))
d.append(block("29 forensics vs analytics"))
d.append(block("30 lexicon in progress"))
d.append(block("31 machine-readable"))
d.append(block("32 privacy & proportionality"))
d.append(block("33 guidance for three audiences"))
d.append(block("34 discussion + next steps"))
d.append(engage_frame(
    ["\\textbf{Comment} on \\emph{Distinguishing blockchain forensics from analytics} --- the public-comment document on the Forensics \\& Analysis hub.",
     "\\textbf{Bring a typology, a signal, or a case} to the lexicon; the FASE working folder carries the illicit-activities lexicon drafts.",
     "\\textbf{Regulators and investigators}: tell the room which existing definitions you are bound to, so the mapping exercise starts from them.",
     "\\textbf{Analytics and surveillance firms}: typology and signal class, not proprietary heuristics, is what the lexicon asks for.",
     "\\textbf{Everything else}: the IKP and FASE categories on the BGIN Discourse."],
    [(SESS + "2-9", "This session", "bgin-global.org/events/ 20261015-block15/sessions/2-9"),
     (FORENSICS_DOC, "Public-comment document", "Distinguishing blockchain forensics from analytics (Google Doc)"),
     (DISC, "BGIN Discourse", "bgin.discourse.group")],
    "Publish the framing document; keep the lexicon living, versioned and machine-readable."))
d.append(close_frame("Analytics generates leads; forensics proves.",
    "The problem was never a lack of definitions. It is the cacophony of them. One lexicon, three audiences, with proportionality written on every entry.",
    "BGIN FASE and IKP Working Groups \\textperiodcentered{} Forensics \\& Analysis and Common Lexicon hubs on bgin-global.org \\textperiodcentered{} bgin.discourse.group"))
decks["2-9-aml-forensics/Block15_2-9_AML_Forensics_Analytics"] = (
    preamble("BGIN Block 15 --- FASE/IKP 2-9: AML Policy, Forensics \\& Analytics", "Washington, D.C. \\textbar{} 16 Oct 2026, 15:40"), d)

# ---------------------------------------------------------------- write
for rel, (p, frames) in decks.items():
    folder, name = rel.split("/")
    outdir = os.path.join(OUT, folder)
    os.makedirs(outdir, exist_ok=True)
    for lg in LOGOS:
        shutil.copy(lg, outdir)
    tex = p + "\\begin{document}\n\n" + "\n".join(frames) + "\n\\end{document}\n"
    path = os.path.join(outdir, name + ".tex")
    open(path, "w", encoding="utf-8", newline="\n").write(tex)
    print("wrote", path, len(frames), "frames")
