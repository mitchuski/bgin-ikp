# BGIN working plan — week of 21 September 2026

Scope: the three open BGIN lanes — the PQC Migration Prize (competition repo + SSR workshop), the IKP proof-of-personhood / privacy-enhanced-authentication track, and the presentations this week and up to Block 15. Written Monday 21 Sep from the live state (Discourse, GitHub, the site fork, this KB). Doors marked **= Mitch** need a post, a merge, a name or a ruling that only the co-chair gives.

---

## 0. The week at a glance

| When | What | State on Monday |
|---|---|---|
| **Tue 22 Sep** | ToIP ZKP TF Round 1 closes (cross-lane; the predicate vocabulary the taxonomy has to land in) | Round 2 opener drafted for 23 Sep (see `project_dtgwg_zkp_tf_mage`) |
| **Thu 24 Sep 12:00–13:00 UTC** | **IKP WG call: Privacy & Proof of Personhood — Privacy Enhanced Authentication.** World presents its taxonomy + ProveKit; then a workshop on personhood verification, privacy guarantees, ZK; Block 15 prep; standards next steps | Announced today: Discourse **1058** + Luma `g4altrcq` (Zoom). Banner made 14 Sep. **No run sheet, no reader, no question pack yet.** |
| Late Sep (undated) | PQC **W1 kickoff** — ratify OUTCOMES, adopt governance v0, name conveners, nominations open | Nominations open since 11 Sep (**0 received**); conveners "to be named at W1"; **no W1 date set** |
| Mon 12 Oct (AoE) | **SSR 2026 PQC workshop paper deadline** (Mitch = Program Co-chair with Kanta Matsuura; Org chair Matsuo) | CFP live at ssresearch26.umbc.edu; PC invites went out (replies were due 11 Sep); **nothing about the workshop in the repo, category 44 or thread 1001** |
| ≈ Thu 8 Oct | Block 15 written contributions (fee waiver = contribution + presentation) | WP-09 separation-of-duties READY; PoP paper still in Block 14 meeting-report form |
| 15–16 Oct | **Block 15** — 1-4 / 1-7 PQC (15 Oct 09:50, 11:30 Room B); **2-6 PEA/ZKP/PoP (16 Oct 11:30 Room B)** | Keynote page in PR **#107** (open, mergeable, 5 days); **all three IKP sessions have empty speaker/moderator fields** |
| 3–5 Nov | IIW #43 = ZKP TF Working Draft milestone | the operative deadline for the §7.3 predicate form |
| 13 Dec | SSR PQC workshop = **W4** (rubric v1, "PQC-ready chain" v1, call-text package) | anchor named in ROADMAP; workshop not yet linked |

---

## 1. Thursday's call is the presentation this week — build the pack (Tue/Wed)

**Goal for the hour:** World's taxonomy is heard as an *assurance-semantics layer* over the predicate set the ZKP TF already publishes (the convergence note's central claim), the nine open questions get owners, and the room leaves with the Block 15 session 2-6 shape and a contributions ask.

Build, in this order (all local, same pattern as the 10 Sep reader):

1. **Run sheet + reader** `readers/2026-09-24-ikp-pop-call/` — 60 min: World taxonomy (15) · ProveKit (10) · workshop on the four separations the taxonomy must keep (humanity ≠ uniqueness · linkability scope · strength expression · continuity · agent authority) (20) · Block 15 2-6 shape + contributions (10) · standards next steps (5). Carry the ProveKit numbers from Scott Jones's 9 Sep notes (iPhone SE 3 2–3 s; 2 GB Android <30 s; <500 MB; ~340 KB WASM; "trusted setup is a distribution problem before it is a trust problem").
2. **Question pack** = convergence note §9 (nine questions) reduced to the five the hour can hold, each with the seam it tests, plus the §7.3 *show* form as the target shape of any answer (every parameter bound, adversary and horizon declared, negative space written).
3. **Block 15 2-6 scoping card** — the two hub-meeting lines already on the site (what each proof proves / where the biometric lives / revocation; personhood as agentic AI raises the cost of not knowing) + the ask: written contributions by ≈ 8 Oct, speakers for 2-6.
4. **Pre-call Discourse** (**= Mitch**): reply on **1058** with the agenda + the note's five separations; one-line cross-posts on **1012** (Block 15 IKP agenda: sessions 3 + 4 → 2-6) and, if the note is to be public, the convergence note itself (as-circulated 27 Aug; ruling: post the note, or the five-separation summary only).
5. **Post-call** (Fri): meeting notes to Discourse (new IKP topic, house style: no salutation, record not correspondence); `privacy-enhanced-auth` hub `statusText` update on the site fork (one-line PR, same shape as #107); the PoP paper gets Appendix B's integration points as a section outline.

Dependencies: none on Mitch except the posts. The ZKP TF Round 2 opener (23 Sep) should reference the same predicate form so the two rooms hear one vocabulary.

---

## 2. PQC competition — unblock the record before W1

The repo is clean (main `86c780a`, 21 signed commits, CI green, only Dependabot #1 open). What is stale is *outside* the repo:

| # | Item | Action | Door |
|---|---|---|---|
| P1 | **PR #107** keynote session page | merge (mergeable, Vercel preview green, no review needed on bgin-homepage) | **= Mitch** |
| P2 | Keynote Discourse pack (3 replies: 1054 · 1012 · 1001) | post after P1 — reader at `readers/2026-09-16-block15-keynote-pack/` (`python -m http.server 8794`) | **= Mitch** |
| P3 | Held posts **03 metrics** + **04 testbed** (were "week of 14 Sep") | post this week; they are the substance the W1/W2 argument runs on. Pack: `block15/DISCOURSE_POSTING_PACK_2026-09-11.md` steps 5–6 | **= Mitch** |
| P4 | **7C** deck reply on 1001 | the deck is already hosted on bgin-global.org since #106 merged with Mitch's approval → gate is met; post 7C, or post the paper paragraph only | **= Mitch** (ruling) |
| P5 | **W1 date** | propose: W1 = a 60-min open call in the week of 28 Sep, or fold W1 into the **8 Oct IKP call** (next in the fortnightly cadence after 24 Sep). Outputs: OUTCOMES ratified, conveners named, nominations reminder. Draft the W1 agenda + `workshops/` record from TEMPLATE (agent) | date **= Mitch** |
| P6 | **Second convener** | the solo-convener blocker is the reason approvals sit at 0 and every team is `mitchuski` only. Candidate list is Mitch's; the onboarding recipe is `docs/SIGNING.md` §1–3 + team membership. Restore approvals=1 when seated | **= Mitch** |
| P7 | Nominations = 0 after 10 days | one reminder reply on **1055** after 03/04 are up; name the two tracks explicitly (theoretical security · implementation efficiency) | **= Mitch** |
| P8 | Dependabot **#1** (codeql-action 3→4) | rebase requested 13 Sep; approve or close. FF-push the signed head, never the buttons | **= Mitch** |
| P9 | Private lane: CLEARANCE held-row unsigned; 8 org owners can read the IKP `.docx` | sign the row; rule on the docx staying in | **= Mitch** |
| P10 | CBT / Tokyo academic session (~17 Sep, the "earlier open academic discussion" the SSR CFP names) | find out whether it ran and what it produced; add a resources row + a line in 03 metrics if so | ask Matsuo **= Mitch**; row = agent |

Repo work the agent can do now without a ruling: W1 agenda + record skeleton (P5), a `resources/README.md` row for the SSR workshop (P11 below), ROADMAP W4 row pointing at the live CFP, README calendar row "2026 Oct 12 — SSR workshop paper deadline".

---

## 3. SSR 2026 PQC workshop — the W4 anchor is live and unannounced

Facts: *Post-Quantum Cryptography for Blockchains Workshop*, Sun 13 Dec 2026 10:00–16:00 ET, Hilton Baltimore Inner Harbor, Carroll A-B; papers 12 Oct (AoE), notification 6 Nov; LNCS 12/6 pages, double-blind, ≥2 reviews; organizing responsibility BGIN; "peer-reviewed papers presented here … are intended to be reflected in the competition specification"; PC service ≠ Evaluation Committee service.

| # | Item | Action | Door |
|---|---|---|---|
| S1 | Announce on category 44 + 1001 | one short post: CFP link, 12 Oct, the sentence that ties papers to the competition specification, the PC ≠ EC line | draft = agent · post **= Mitch** |
| S2 | Repo: ROADMAP W4 row + resources row + README calendar | link the CFP; state the 12 Oct deadline; the "Tokyo academic discussion" as W1's academic anchor once confirmed | agent, signed PR, FF-push |
| S3 | PC roster | replies were due 11 Sep — confirm who said yes; permission to list names; the page lists none yet | **= Mitch** (with Matsuura) |
| S4 | **A BGIN-authored paper?** The repo already holds a competition-design contribution (open-benchmark model, T1 track, the draw as the Gap, the 22-metric register, reproduction tolerance). Deadline is *before* Block 15. **COI: a Program Co-chair submitting to his own workshop** — either the other chair handles it blind, or it goes to SSR 2027 / CoDecFin 2027 instead | ruling **= Mitch** before any drafting |
| S5 | Metrics ↔ paper loop | whatever 03 metrics draws on Discourse this week becomes the "open questions" section reviewers will see; keep the thread and the paper in one vocabulary | agent |

---

## 4. Proof of personhood → Block 15 → standards

| # | Item | Action | Door |
|---|---|---|---|
| H1 | **PoP paper** (`personhood/IKP_Proof_of_Personhood.docx` is still the Block 14 meeting report, "Date: TBD") | restructure into the paper for public comment at 2-6: three-graph model + dual-agent separation (Block 14) + **assurance decomposition as a contributed section** + convergence mapping as annex + the §5 unclaimed gaps (coercion/rental, threat model per category, domain governance) as the BGIN-specific contribution. Outline this week; draft after Thursday's input | outline = agent · authorship **= Mitch** |
| H2 | WP-09 `bgin_separation_of_duties.md` | READY; submit as the written contribution for the fee waiver by ≈ 8 Oct; decide which session it presents in (2-6 or 2-4) | **= Mitch** |
| H3 | Sessions **1-4 / 1-7 / 2-6** have no speakers/moderator on the site | after Thursday: fill 2-6 (World + LF ZKP WG side by side, as 1012 proposed); PQC sessions from the ecdsa.fail community + NIST-facing names from 1012. Site PR = descriptive fill only, same scope rule as #107 | names **= Mitch** · PR = agent |
| H4 | Hub `privacy-enhanced-auth` | statusText already says the taxonomy meeting is "being prepared" — after the call, say it happened + link the notes; add the convergence note as a document row if public | agent PR · merge **= Mitch** |
| H5 | ZKP TF seam | file the cred-spec issues the note §8 lists (strength expression on PHC-qualifying VMCs · humanity/uniqueness separable · enrolment-anchor primitive · Agent-card assurance) — #58 was opened today (AL); check which of the four it covers, file the rest | agent drafts · post **= Mitch** |
| H6 | World Foundation reply | §10.1 of the note: the convergence finding + both DTG references + intro to the Credentials TF. Thursday is the moment | **= Mitch** |
| H7 | CoDecFin 2027 (W6 anchor) | FC notification was expected 15 Sep; fc27.ifca.ai lists no workshops yet — confirm with Matsuo; PC co-chair seat still "vacant" on 1036 | **= Mitch** |

---

## 5. Order of operations (what to do first)

1. **Tue:** P1 merge #107 → P2 post keynote pack. Agent builds the 24 Sep pack (§1 items 1–3) + S1/S2 drafts.
2. **Wed:** Mitch posts 1058 agenda reply + 1012 cross-post; posts 03 + 04 (+ 7C ruling); reviews the pack.
3. **Thu 12:00 UTC:** the call. Agent captures notes from the recording/transcript if provided.
4. **Fri:** meeting notes topic; hub statusText PR; PoP paper outline; W1 date + agenda proposal; SSR announcement post; nominations reminder.
5. **Week of 28 Sep:** W1 (if that week); H1 draft; H3 speaker fill; S4 ruling; H5 issues.
6. **By 8 Oct:** WP-09 + PoP paper submitted; session pages filled; 12 Oct SSR deadline passes (paper or not).

## 6. Rulings needed from Mitch (one line each)

- Post the convergence note on Discourse, or only its five-separation summary?
- W1: standalone call week of 28 Sep, or folded into the 8 Oct IKP call?
- Second convener: who?
- 7C: post with the deck link, or paper paragraph only?
- SSR paper from the repo: yes (other chair handles blind) / no / redirect to CoDecFin 2027?
- IKP `.docx` stays in the private repo readable by 8 owners, or comes out?

## 7. Standing rules that apply

No Claude attribution in bgin-global commits/PRs (DCO only) · pushes, posts, merges = Mitch · FF-push the signed head, never the merge buttons · no org-wide changes as a new owner · Discourse house style: no salutation, no second person, the post carries the ask and the link, the record carries the detail · work locally, no artifact pages.

Sources: Discourse 1058 / 1048 / 1012 / 1036 / category 44 (read 21 Sep) · Luma g4altrcq · GitHub bgin-global/pqc-agility-competition + bgin-homepage (gh, 21 Sep) · ssresearch26.umbc.edu PQC workshop CFP · `03_PC_Invitation_OnePager_EN.pdf` (Downloads, 12 Sep) · `personhood/proof-of-human-convergence-WF.md` · `pqc/PQC_AGILITY_REPO_RESUME.md` · `Downloads/2026-09-09 - ProveKit notes for the ToIP ZKP Task Force.md`.
