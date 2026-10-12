# Block 15 decks — PQC Migration Prize (built 2026-09-29)

Two Beamer decks in the house style of the GDC26 breakout deck (dark title bar, grey lead box, "Takeaway" line, BGIN mark in the footer). Both compile with MiKTeX: `latexmk -pdf <file>.tex` (beamer, booktabs, fontawesome5, tikz, qrcode). Facts follow `bgin-global/pqc-agility-competition` at draft v0 (main `86c780a`) and the Block 15 record in `~/BGIN_IKP`. Everything shown is unratified.

## 1. `pqc-session-deck/Block15_PQC_Migration_Sessions.pdf` — 26 slides

The deck for the two IKP PQC Migration sessions (15 Oct, Room B, 09:50–13:00), rebuilt from the GDC26 deck as a whole rather than lightly edited.

| Part | Slides | Content |
|---|---|---|
| Opening | 1–4 | Title; the morning in one page (keynote + two sessions); the job is not to pick another primitive; what moved since GDC26 |
| Session 1 | 5–9 | Resource estimates into judging criteria: the numbers (PRX Quantum, ECDSA.fail, Project Eleven); on-spend / at-rest / on-setup; how an estimate becomes a criterion (M-19, M-22, M-20, G1); discussion items |
| **Bitcoin lane** | 10–17 | Why Bitcoin does not migrate like TLS; exposure classes by output type (P2PK, P2PKH/P2WPKH reused or not, P2SH/P2WSH, P2TR key-in-output, Lightning); candidate sizes in Bitcoin units against B-01/B-02 with the witness-weight note; paths under ruling (C-01 hybrid, C-02 P2QRH/BIP-360 reference only, S-04/S-05 state, M-21); what the testbed measures on the Bitcoin lane (drawn); what stays outside Bitcoin Core's remit and outside BGIN's; three asks (advisor seat, fixtures by PR, a node or a name) |
| Session 2 | 18–23 | Agility as O3 (M-12/13/14/21); agility as a governance property, O4; the NIST path (FIPS 204/205/206, SP 800-208, ACVP/CAVP, LAMPS, on-ramp out by G1); what Block 15 decides (W2 outputs); open questions 1–6 |
| Close | 24–26 | Timeline to the 2028 award (drawn); how to engage with QR codes; close |

Things to confirm before use: the session descriptions match the Discourse/roadmap wording (resource estimates → judging criteria; agility as governance + NIST path with NIST participation); the exposure-class table is standard Bitcoin fact but is the one slide with content not in the repo — check the wording with a Bitcoin reviewer; Matsuo is co-credited on the title as on the GDC26 deck.

## 2. `competition-repo-deck/PQC_Competition_Repository.pdf` — 27 slides

Companion deck on the work done in the coordination repository, organised by the README's five jobs.

| Part | Slides | Content |
|---|---|---|
| Opening | 1–4 | Title; what the repository is and is not; the path and the roles; repository map (drawn) |
| Job 1 committee | 5–7 | Governance phases A/A2/B/C and composition (12–18 seats); decision process and COI |
| Job 2 outcomes | 8–9 | O1–O6 with done-when and ratifying workshop; non-outcomes |
| Job 3 metrics | 10–12 | The register M-01..M-22 grouped; rubric gates G1–G4, tracks, dimensions, conventions |
| Job 4 testbed | 13–19 | BSafe.network concept and phases T0/T1/T2; scheme register S/B/C; harness interface, manifest, reproduction protocol; decision 0001 open-benchmark model; first tracks T1–T4 and the draw as the Gap; the calibration harness instance (`harness/`) and the two defects it caught |
| Job 5 + record | 20–26 | Roadmap W1–W6; integrity layer and the squash-merge incident; the confidentiality rule; outreach and sources; status at Block 15 and open doors (second convener, nominations, node hosts, SSR paper, 0002); how to contribute with QR codes |
| Close | 27 | "The repository is the record." |

## Also in this tree

- `../../gdc26/pqc-deck-bitcoin-core/` — the earlier light Bitcoin Core rework of the GDC26 deck (17 slides), superseded by deck 1 above but kept.
- `../sponsor-deck-bitcoin-core/` — an abandoned start on the Block 15 sponsorship pitch deck (wrong deck; does not compile). Delete or finish.

## Beamer gotchas met while building

- A `tabular` (or a bare `{\small ...}` paragraph) as the first thing in a frame drops the content or the title bar. Start frames with the `\lead{}` box or wrap tables in `center`.
- `\\[Nmm]` immediately before `\begin{columns}` errors ("no line here to end"); use `\par\vspace`.
- `\vspace` at the top of a `[t]` frame is discarded; title-slide text is placed as tikz overlay nodes instead.

## 3. Per-session decks (built 2026-10-12) — one deck per session the IKP co-chair chairs

Generated from the combined deck `ikp-cochair-deck/Block15_IKP_CoChair_Sessions.tex` (37 slides) by `ikp-cochair-deck/split_decks.py`; each is self-contained (own title, "This Session" agenda slide, the thread's content, engage with three QR codes, close). Same house style; accents orange = PQC, violet = personhood, teal = forensics. Build each with `latexmk -pdf`; `preview/` holds 60-dpi renders.

| Folder | Deck | Session | Slides |
|---|---|---|---|
| `1-4-pqc-estimates/` | `Block15_1-4_PQC_Resource_Estimates.pdf` | 1-4 IKP: PQC Migration (1), 15 Oct 09:50 Room B | 11 |
| `1-7-pqc-agility/` | `Block15_1-7_PQC_Agility_Governance.pdf` | 1-7 IKP: PQC Migration (2), 15 Oct 11:30 Room B | 9 |
| `2-6-pea-zkp-pop/` | `Block15_2-6_PEA_ZKP_Proof_of_Personhood.pdf` | 2-6 IKP: Privacy Enhanced Authentication, ZKP & Proof of Personhood, 16 Oct 11:30 Room B | 14 |
| `2-9-aml-forensics/` | `Block15_2-9_AML_Forensics_Analytics.pdf` | 2-9 AML Policy, Forensics & Analytics (FASE/IKP, with Chloe White), 16 Oct 15:40 Room A | 11 |

To change content, edit the combined deck (the content slides are shared) or the per-deck title / agenda / engage / close text in `split_decks.py`, then re-run the script and rebuild. The confirm-before-use list in `ikp-cochair-deck/README.md` applies to all four.
