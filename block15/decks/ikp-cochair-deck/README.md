# Block 15 — the IKP co-chair's four sessions (built 2026-10-12)

`Block15_IKP_CoChair_Sessions.pdf` — 37 slides, one Beamer deck in the house style of the GDC26 / Block 15 PQC decks (dark title bar, grey lead box, "Takeaway" line, BGIN mark in the footer; section accents orange = PQC, violet = personhood, teal = forensics). Build with MiKTeX: `latexmk -pdf Block15_IKP_CoChair_Sessions.tex` (beamer, booktabs, fontawesome5, tikz, qrcode). `preview/` holds 60-dpi renders of every slide.

## Sessions covered (from `bgin-global.org/events/20261015-block15`, read 2026-10-12)

| Slot | When | Room | Session | Chair / speakers |
|---|---|---|---|---|
| 1-4 | 15 Oct 09:50–11:20 | B | IKP: PQC Migration (1) — resource estimates into judging criteria | chair Mitchell Travers; Kanta Matsuura, Tadahiko Itoh |
| 1-7 | 15 Oct 11:30–13:00 | B | IKP: PQC Migration (2) — agility as governance, NIST path, W2 decisions | chair Mitchell Travers; Kanta Matsuura, Tadahiko Itoh |
| 2-6 | 16 Oct 11:30–13:00 | B | IKP: Privacy Enhanced Authentication, ZKP & Proof of Personhood | chair Mitchell Travers; World main discussant; lunch 2-L with World follows |
| 2-9 | 16 Oct 15:40–17:10 | A | AML Policy, Forensics & Analytics — Common Taxonomy (FASE/IKP) | chairs Mitchell Travers, Chloe White |

Not covered (Cyber-chaired joint sessions where IKP contributes): 2-4 Security AI Agent, 2-8 Offline Key Management. The keynote (1-2, Alex Pruden) is referenced, not presented.

## Deck map

| Part | Slides | Content |
|---|---|---|
| Opening | 1–4 | Title; the IKP track in one page; one group, three threads; what moved since Block 14 |
| PQC (1-4 / 1-7) | 5–15 | Section; not another primitive; the numbers (PRX Quantum, ECDSA.fail, Project Eleven); on-spend / at-rest / on-setup; estimate → criterion (M-19, M-22, M-20, G1); three lanes (drawn); agility metrics (M-12/13/14/20/21); NIST path; W2 outputs; six open questions; timeline to 2028 |
| PEA / ZKP / PoP (2-6) | 16–26 | Section; why now; prove the claim not the identity; the convergence stack (WF / DTG / ePrint 2026/333 / BGIN); five distinctions; three graphs + two agents (drawn); verifiable trust agents + WP-09 separation of duties; ZKP where it earns its place (ProveKit numbers, PQ readiness of the stack); gaps nobody owns; discussion items; where it goes (paper → public comment → ISO TC 307 TR; the afternoon) |
| AML / Forensics / Analytics (2-9) | 27–34 | Section; where the work came from (Blocks 11–15, drawn); forensics vs analytics table; lexicon terms in progress (market abuse, scams by construction, wash trading, AML/CFT); typology → signals → controls → evidence (drawn); privacy and proportionality (ties to 2-6 regulatory interface); guidance for VASPs / investigators / educators; discussion + path to publication |
| Close | 35–37 | What IKP leaves Block 15 with; how to engage (six QR codes); close |

## Sources

- Programme: `~/bgin-homepage-fork/lib/block15-program-data.ts` (branch `block15-pea-session-agenda`, head fd245ca) and the live event page.
- PQC: `bgin-global/pqc-agility-competition` main 86c780a (draft v0; nothing ratified); `../pqc-session-deck/` slides reused and condensed.
- Personhood: `personhood/proof-of-human-convergence-WF.md` (Aug 2026), `personhood/05_Block14_ProofOfPersonhood.md`, Block 14 MRs, `block15/bgin_separation_of_duties.md` (WP-09), the 10 Sep IKP call reader (ProveKit numbers).
- Forensics: Block 14 MR *Forensics & Analysis — Common Lexicon of Harmful Activities* (transcript), the project hubs `forensics-analysis` / `illicit-activities`, the public-comment document *Distinguishing blockchain forensics from analytics*.

## Things to confirm before use

- The 24 Sep IKP call (World taxonomy + ProveKit) has no notes in this KB; slides 17–20 are built from the convergence note and the 10 Sep reader, not from that call.
- Whether W1 ran and ratified OUTCOMES (slide 13 hedges "if not at W1"); COMMITTEE.md is still empty.
- Slide 30 lexicon figures (56 % insider-signal listings; 99 % of pump.fun tokens; ~14 % / $250 M prediction-market wash trading) are the Block 14 presenter's numbers, kept as "one survey"; drop if the presenter should not be echoed.
- The forensics-vs-analytics table (slide 29) is a proposed framing for the room, not the public-comment document's wording.
- Chloe White's title (Co-Chair, FASE) follows the programme data.
