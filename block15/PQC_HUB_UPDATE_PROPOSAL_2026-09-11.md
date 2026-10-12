# Proposal — update `/projects/pqc-migration` for Block 15

Written 2026-09-11. Patch built and verified on branch `pqc-migration-hub-block15` in `~/bgin-homepage-fork` (off `upstream/main` @ `64d4513`, the Capitol Campus venue merge of 2026-09-10). Patch file: `pqc-migration-hub-block15_2026-09-11.patch` beside this note (text files only; the 2.4 MB deck is staged in the fork but not in the patch). **Staged, not committed, not pushed.** Updated 13:15 with the GDC26 scene-setting deck (§2E).

Verification: `tsc --noEmit` clean · `next lint` clean · `next build` green · rendered `/projects/pqc-migration` and `/projects/privacy-enhanced-auth` checked over HTTP for every new string and link.

---

## 1. Observation loop (what is true today)

### The competition repository — `bgin-global/pqc-agility-competition`

| Fact | State on 2026-09-11 |
|---|---|
| `main` | 3 signed commits, unchanged since 2026-09-05 (`bb9d99e`) |
| README on `main` | **still carries the "Staging location" note** (PR #2 removes it) |
| PRs | #1 Dependabot · #2 transfer note · #3 channels · #4 DCO bot fix — all OPEN, all blocked on a second code-owner reviewer |
| Local | `outreach/discourse-launch` (`d0cda86`, signed) ahead of `origin/main` by 1, **not pushed** — `docs/CONFIDENTIALITY.md` + 7 Discourse drafts |
| Private lane | `bgin-global/pqc-agility-competition-private` `2819945`, CI green |
| Public announcement | Named on the **10 Sep IKP call agenda** (Discourse 1048 #2: "repo is now live … evaluation committee is forming") — that is the only public mention so far |

### Discourse (`bgin.discourse.group`, JSON read-only)

| Where | State |
|---|---|
| Category 44 *Post-Quantum Crypto Agility Competition* | exists (created 09-09 12:08), **only the About topic** — placeholder text, 0 launch posts, `can_create_topic` for anonymous = false |
| IKP category (8) | newest: 1048 Sep-10 call (agenda posted) · 1045 GDC26 report published (Matsuo, 09-03: "bring comments, corrections, proposed definitions of a PQC-ready chain, and evaluation-committee interest into this thread") · 1034/1026 Aug calls (Block 15 IKP session list confirmed) · 1012 Block 15 proposed agenda (Jul-03) |
| 987 *BGIN × NEDO PQC competition — roadmap* (Matsuo, May-12) | the canonical public calendar: GDC Sep 1–3 → CBT Sep 17 → EF Retreat Oct 9–12 → **Block 15 "PQC session with NIST"** → CSS Oct 19–23 (guideline drafting) → **SSR Dec 13–15 (publication of guidelines / call)** → applications Jan 2027 → deadline Sep 2027 → shortlist Dec 2027 → winner Jul–Sep 2028 |
| 931 *FC-CoDecFin PQC-Competition Session Report (draft)* | the "unchecked source" from RESUME — it is a **public** otter.ai summary post (Mar-21) with Fukuda's corrections; 10–15-university testbed, 4–6-month experiments, "multi-million JPY" prize (not "$1M"). Safe to cite as a public thread. |
| 1036 CoDecFin 2027 (FC'27, 8–12 Feb 2027, Barbados) | proposed special areas include **"Post-Quantum Cryptography Migration, Evaluation, and Crypto Agility"** and new **"Advanced Key Management"**; notification expected 15 Sep |
| 914 (Japanese, General) | NEDO internal costing / committee-referral thread — **not cited** on the site |
| 1032 FIPS 'n' Chips PQC panel · 1030 NIST NVD | CS-category FYIs, not hub material |

### The website (`bgin-global/bgin-homepage`, `main` pushed 2026-09-10)

- Hub data = `contents/projectHubs.ts` (+ `hubSchedules.ts`, `lib/block15-hub-meetings.ts`). You have **admin** on the upstream repo now (org owner) — PR from a branch on upstream or from the fork both work.
- The pqc-migration hub today: GDC26 report as secondary CTA, 7 documents (GDC26 ×3, Block 14 ×2, Block 13, Block 12), two `relatedInitiatives` ("NEDO/METI technology competition", "SSR 2026 PQC workshop track"), three generic participate bullets, roadmap ending "2027+ Public migration guidance". **No mention of the repository, the committee, the metrics, the testbed, the workshop series, or the January 2027 opening.**
- Block 15 program: 1-2 Keynote PQC (09:20) · 1-4 IKP PQC Migration (09:50–11:20, Room B) · 1-7 IKP PQC Migration (2) (11:30–13:00) · 2-6 IKP PEA/ZKP/PoP (16 Oct 11:30–13:00). Session plans on the hub are generic.
- Other IKP hubs: `accountable-wallet` (Published, no Block 15 session — hub copy already says "if scheduled", consistent) · `forensics-analysis` (Public Comment, session 2-9, fine) · **`privacy-enhanced-auth` = thinnest hub: one Drive link, no documents, although the Block 14 PEA+KM and PoP meeting-report PDFs are already on the site (`documents.ts` B14_mr_20 / B14_mr_22) and the July research-pathway post exists.**

---

## 2. Proposed changes (all in the patch)

### A. `contents/projectHubs.ts` — pqc-migration hub

| Field | Change | Why |
|---|---|---|
| new constants `PQC_COMPETITION_REPO`, `PQC_COMPETITION_DISCOURSE` | exported next to `WG_META` | reused by `hubSchedules.ts`; one place to edit if the repo moves |
| `pitch` | + "…for the METI/NEDO PQC Migration Prize" | the hub now carries the coordination role |
| `overview` | + one sentence on the 2026–2028 prize coordination: committee, metrics/rubric, neutral testbed, six workshops Sep 2026 → Feb 2027, host's call text; closes with "BGIN does not select algorithms and does not run the competition" | the neutrality line from 1012/GDC26, verbatim posture |
| `statusText` | rewritten: GDC26 report → repository open Sep 2026 (draft v0: governance, O1–O6, 22-metric register, testbed schemes/harness, roadmap) → committee forming, nominations open → Block 15 = W2 (seat committee, metrics v0→v1, scheme scope rulings) → 13 Dec SSR = call-text package + "PQC-ready chain" definition | mirrors README "Status" + ROADMAP W2/W4 + GDC26 report's December deliverable |
| `deliverables` | 4 → 6: adds evaluation framework (metrics, rubric, PQC-ready definition), neutral testbed evidence (BSafe.network concept, pre-existing NIST-class schemes, BTC/ETH-mappable), call-text inputs to the host | = OUTCOMES O1, O2, O5 |
| `secondaryCta` | GDC26 report → **"Competition repository"** (GitHub) | the CTA is the join path; the GDC26 report stays as document row 2 and in News. *Alternative if the web team prefers a BGIN-hosted CTA: keep GDC26 and rely on the document row.* |
| `nextMilestone` | "Block 15 (Oct) · committee seated" | |
| `documents` | + row 1 "Working repository" (GitHub) · + Roadmap (Discourse 987) · + FC/CoDecFin 2026 session report draft (931) · + IKP PQC thread (1001) · + competition Discourse category (44) | the public record trail; every link verified live |
| `relatedInitiatives` | NEDO entry rewritten as **"PQC Migration Prize Competition (METI/NEDO, 2026–2028)"** with: hosted/funded by Japan not BGIN; NIST-process schemes, NIST = primitive authority; applications planned Jan 2027; **both winner dates carried** (mid-Sep 2028 briefing / Mar 2029 GDC26 report); path competition → BGIN Standard → ISO/TC 307 → Japan criteria. SSR entry dated (13 Dec 2026, Baltimore) and tied to the call-text window. + third entry "Ecosystem calendar around Block 15" (CBT, EF Retreat, CSS/BWS, CoDecFin 2027 special area) | facts from 987 + README + 1036; the date disagreement is carried, not resolved, matching the repo's rule |
| `participateBullets` | 3 → 5: nominate (issue template + COI policy) · propose/challenge a metric or scope ruling (C-01…C-06) · offer a testbed node · bring "PQC-ready chain" definitions to the GDC26 thread + Block 15 (15 Oct) · Discourse (IKP + competition category) | = README "How to engage" + Matsuo's ask in 1045 |

### B. `contents/hubSchedules.ts` — pqc-migration roadmap + meetings

- Roadmap 5 → 8 rows: Block 14 ✓ · GDC26 ✓ · **Sep 2026 repository + nominations ✓** · **Oct 2026 Block 15 — committee seated, metrics v1, scope rulings (current)** · Nov testbed/node call/COI · **13 Dec SSR — call text + PQC-ready definition** · Jan 2027 applications open (planned by the host) · 2027–28 evaluation → BGIN Standard → ISO/TC 307.
- Meetings: + a `Workshop` item for the SSR co-located workshop (13 Dec, Baltimore; links to `workshops/ROADMAP.md`). Merge order in `mergeBlock15Meetings` renders it after the three Block 15 sessions and before the WG call. WG-call plan now names the repository drafts and nominations.

### C. `lib/block15-hub-meetings.ts` — session plans

- **1-2 Keynote**: deployment/agility/governance framing; connect GDC26 findings to the evaluation work.
- **1-4 PQC (1)**: resource estimates + ECDSA.fail community → judging criteria; pressure-test metrics v0 and the open questions (reference hardware, block mix).
- **1-7 PQC (2)**: crypto agility as a governance property + NIST signature migration path, with NIST participation; seat the committee, take scope rulings, metrics v1.
- **2-6 PEA/ZKP/PoP**: the biometric-ZKP comparison questions + personhood under agentic AI, taxonomy review.
- Source: 1012 #1 (sessions 1–3) as reconfirmed on the 13 Aug call (1026 #2). Session *titles* in `lib/block15-program-data.ts` are left alone — those are the programme owner's.

### D. `privacy-enhanced-auth` hub (separable — drop if you want the PR to be PQC-only)

- `statusText`, `deliverables` (+ taxonomy line), `secondaryCta` → Block 14 PEA+KM report PDF, `workingFolder` = the Drive link, `nextMilestone` "Block 15 (16 Oct session)", documents 1 → 5 (Block 14 PEA+KM, Block 14 PoP, Block 13 ZKP+PEA, research pathway post 1012/2, Drive), `relatedSlugs` + pqc-migration, participate bullets. All three PDFs exist under `public/documents/`.
- Taxonomy wording kept to what is already public (10 Sep agenda + the 1012 pathway post); nothing from the private working note.

### E. GDC26 scene-setting deck + the PRX Quantum paper (added 13:15)

Source: `Downloads/GDC26_ Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities_ Resource Estimates and Mitigations.pdf` — 30 slides, Google Quantum AI, **"When ECC and RSA Break: Urgency of Migrating to Post-Quantum Cryptography"**, presented 3 Sep 2026 at GDC26 by Adam Zalcman (on-programme speaker, so named in the meeting report already); based on PRX Quantum **7**, 031001 (21 Aug 2026), doi.org/10.1103/j3xf-bw18 (also arXiv 2603.28846 / IACR ePrint 2026/625 — open access). Read in full: no copyright, confidentiality or "do not distribute" notice on any slide; content = ECDLP exposure → capability-driven timelines (QEC, copy-paste modules, compiling) → attacks by on-chain consequence and by capability required (on-spend / at-rest / on-setup) → migrate-to-PQC stack. Contains a Scott Aaronson photo + quote (sourced to his blog) and Google chip photos.

Wired in:
- file → `public/documents/meeting-reports/gdc26/GDC26_PQC_Migration_DLTs_Slides_GoogleQuantumAI.pdf` (follows the existing `GDC26_*_Slides.pdf` naming; served, 2,498,291 bytes)
- hub `documents`: + "Slides (speaker)" row for the deck · + "Paper" row → the DOI (2026/08)
- news page `/news/260903-gdc26-pqc-migration` Slides section: one paragraph — the scene-setting slides are also available (PDF) + the open-access paper (title, PRX Quantum 7, 031001, 21 Aug 2026) as the source of the resource estimates and the attack classes
- `contents/documents.ts`: entry `GDC26_slides_04` (author Other, what other, theme pqc, related pqc-migration) so it shows in the Publications library beside the BGIN Beamer deck (`GDC26_slides_03`)

**Gate — third-party material.** The paper link is clean (open access). The deck is the speaker's: hosting a copy on bgin-global.org is a C-THIRDPARTY question under the competition repo's own rule. It is built on the assumption the deck was handed over for the session record; **confirm with Adam Zalcman (or that GDC has published it) before the push**. If not cleared, drop the PDF + the two deck references (hub row, news paragraph's first link, `GDC26_slides_04`) and keep the paper row — three small edits. No copy on the site names floor participants; the news paragraph does not claim permission.

### F. The competition category as the public door (added 13:40)

Mitch is setting up https://bgin.discourse.group/c/post-quantum-crypto-agility-competition/44 as the public competition group; both the website and the repo now point there.

- **Site** — new optional hub field `forum?: { label, href }` in `ProjectHub` (documented in the type): when set, the filled "Work on Discourse" action (and the participate-section "How to work on Discourse" guide link) route to it via `/start/discourse?next=…` (same-host validation already in `contents/discourse.ts`), and a "{label} ↗" link renders beside "Open this WG on Discourse ↗" in the hero and the participate footer. pqc-migration sets `forum = { "Competition category on Discourse", PQC_COMPETITION_DISCOURSE }`; `discourseUrl` stays IKP so the WG chip/links and WG-call item are unchanged. `statusText` mentions the category. Verified: 3 hrefs to the category on the rendered hub, 2 orientation links with `next=` the category; other hubs untouched (`privacy-enhanced-auth` still routes to IKP).
- **Repo** — signed commit `4bd887b` on `docs/communication-channels` (PR #3, the channels PR): README (intro + "Discuss & amplify"), GOVERNANCE §7 channel row, CONTRIBUTING "Discourse first", SUPPORT row 1, `resources/README.md` first row, CHANGELOG "Changed". Also **fixed a 404**: SUPPORT linked the IKP category by a slug that does not resolve (`…/identity-key-management-and-privacy`) → `…/ikp-wg/8`. `verify-history.sh` clean (2 commits, 0 unsigned, 0 no-DCO). **Not pushed** — `git push origin docs/communication-channels` updates PR #3 in place (its "last-push approval" rule only matters once a review exists).

Follow-up outside this PR: the competition repo `resources/README.md` provenance table should carry the paper DOI (and the deck, once cleared) — METRICS open question 6 (attack classes) cites exactly this taxonomy.

---

## 3. Sequencing — do these before (or with) the site merge

1. **Post the Discourse launch** (category 44 is still the placeholder — now the primary Discourse door on the hub, so this comes first). The hub now links to that category; merging the site while it is empty is a dead door. Order: push `outreach/discourse-launch` → post `00-category-about` + `01-launch` (+ 02–05 as you like) → fill `outreach/README.md`. If you would rather merge the site first, delete the "Post-Quantum Crypto Agility Competition — Discourse category" document row (one block) and keep the rest.
2. **Merge PR #2** (or at least #4 → #2) so the repository README stops saying "Staging location … will be transferred" — the site's secondary CTA lands on that README. Blocker unchanged: one approval from a code owner who is not the author. Fastest lever remains `required_approving_review_count: 0` in `.github/rulesets/main.json` + `ORG=bgin-global scripts/bootstrap-github.sh rulesets` until the second convener is seated.
3. **Clear the deck** with the speaker (§2E) — or strip it.
4. **Then** the site PR: `cd ~/bgin-homepage-fork && git commit` (message below) → `git push -u origin pqc-migration-hub-block15` → `gh pr create -R bgin-global/bgin-homepage --base main`. Vercel preview will show both hubs.

Suggested commit message:

```
Update the PQC Migration hub for Block 15: competition repository, committee, roadmap

- gdc26: add the Google Quantum AI scene-setting deck (speaker slides) and
  the PRX Quantum paper (DOI) to the PQC hub, the GDC26 meeting-report page
  and the publications library.
- pqc-migration: overview/status carry the METI/NEDO PQC Migration Prize
  coordination (repository open Sep 2026, committee forming, W2 at Block 15,
  SSR 13 Dec call-text window); repository as secondary CTA; document rows
  for the repository, roadmap thread, CoDecFin session report, PQC thread
  and competition category; related initiatives rewritten with both
  provisional winner dates; participate bullets = the three ways to engage.
- hubSchedules: eight-step roadmap through Jan 2027 applications; SSR
  workshop as a meeting item.
- block15-hub-meetings: session plans 1-2 / 1-4 / 1-7 / 2-6 from the IKP
  Block 15 agenda.
- privacy-enhanced-auth: link the Block 13/14 meeting reports already on
  the site, the ZKP/biometric research pathway, and the 16 Oct session.
```

---

## 4. Not done, on purpose (your call)

- **News item** "PQC Migration Prize: coordination repository open, evaluation committee forming" — would need `contents/news.ts` + `app/news/2609xx-…/page.tsx`. Draft description if wanted: *"BGIN's public coordination repository for the Japan-hosted PQC Migration Prize is open: governance, outcomes, a 22-metric evaluation register, testbed specifications and a six-workshop roadmap, all draft v0. Evaluation-committee nominations are open; Block 15 seats the committee."* Better timed with the Discourse launch than before it.
- **Block 15 programme titles** (`lib/block15-program-data.ts` 1-4 / 1-7 are both "IKP: PQC Migration") — could become "PQC: resource estimates and evaluation criteria" / "PQC: crypto agility and the NIST signature migration"; programme owner's file, not touched.
- `BLOCK15_KEY_HUBS` vs registration-news inconsistency (Accountable Wallet named a priority theme in news id 16, absent from the key-hub list) — noted 2026-08-18, still present, not in this patch.
- Cited nothing from Discourse 914 (NEDO costing, Japanese) or from the IKP `.docx` transcript.

## 5. Sources read this session

Discourse JSON: categories · IKP category p0/p1 · latest p0–p2 · topics 1048 1045 1044 1034 1026 1023 1012 1011 1001 987 941 931 887 (+ posts 21–27) 882 843 1036 1032 1030 914 · category 44. GitHub: `gh pr list`, repo metadata for both repos, upstream `bgin-homepage` log/permissions/PRs. Local: `~/pqc-agility-competition` (README, ROADMAP, OUTCOMES, outreach drafts, RESUME), `~/BGIN_IKP/readers/2026-09-10-ikp-call/`, site sources on `upstream/main`.
