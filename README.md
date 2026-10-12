# BGIN_IKP — the IKP working-group knowledge base

**Who:** Mitchell Travers (privacymage) · co-chair, BGIN IKP (Identity, Key Management
& Privacy) Working Group. Cross-role disclosure: also co-chair of the ToIP DTG ZKP Task
Force — DTG observations here are personal, drawn from public materials.

**What this is:** the consolidated home for IKP working-group material on this machine,
gathered by the 2026-08-27 dream cycle from its scattered tellings (Downloads, memory
topic files, the Programme pipeline, BGINAI dirs, the DTG workbenches). Each file here is
the **chosen canonical copy**; `SOURCES.md` records where every one came from and which
duplicates it supersedes. Work in this directory from now on.

---

## The five live threads (agenda of 2026-08-28)

1. **Block 15** — 15–16 Oct 2026, Georgetown, DC. Submissions ≈ 8 Oct (fee waiver =
   written contribution + presentation). → `block15/`
2. **PQC** *(current focus)* — GDC26 Geneva 1–3 Sep breakout "PQC Migration on DLTs:
   Crypto Agility, ZKP, and Resource Estimates". → `pqc/` + `gdc26/`
3. **Privacy & personhood taxonomy** — WF Proof of Human convergence; World Foundation ×
   IKP event Mon 8 Sep. → `personhood/`
4. **ZKP in DTG** — first proof proposal + ADR-001 evaluation, open for comments.
   → `zkp-dtg-bridge/`
5. **WG operations & precedent** — SR-0011, Block 14 records, site-edit mechanics.
   → `wg-ops/`

## Directory map

| dir | holds |
|---|---|
| `block15/` | Call for Participation (authoritative facts + official IKP theme list) · the 28 Aug call agenda (canonical copy) · `bgin_separation_of_duties.md` (WP-09, **finished submission candidate**, venue-stamped Block 15) |
| `gdc26/` | The GDC26 session-proposal posts (three breakouts incl. both IKP sessions + the bgin.ai travelling-demo proposal) |
| `pqc/` | The PQC-migration hub source docx (canonical of 4 Downloads copies) · the shor_mage/ecdsa.fail ↔ agentprivacy overlap map (substrate for "resource estimates") |
| `personhood/` | The WF convergence note **as circulated 27 Aug** + the v2 lineage variant · the IKP proof-of-personhood paper source docx · the Block 14 session record (the paper's origin, three-graph model) · the open letter to the ePrint 2026/333 authors |
| `zkp-dtg-bridge/` | ADR-001 "Community-Anchored Proof" (local archive of docs.fpp.storm.ws, fetched 27 Aug) · proof-of-liveness requirements **v0.4 (current)** and v0.3 (superseded) · the predicate & assurance-boundary decision doc |
| `wg-ops/` | SR-0011 ZKP study (published PDF + consolidated md; Mitchell = editor — the IKP paper precedent) · Shin'ichiro Matsuo research 1:1 transcript · Jan collaboration proposal · commenting template · Block 14 programme + `block14-program-data.ts` (the shape a Block 15 site PR takes) |
| `chronicles/` | Reflected chronicles of work in this lane (master series lives in `agentprivacy_master/docs/chronicles/`) |

## Standing rulings & cautions

- **Version rulings:** proof-of-liveness = **v0.4** (merged upstream 24 Aug); the
  convergence note as-circulated = `proof-of-human-convergence-WF.md` here (v2 kept for
  its revision-note lineage); PQC docx = the `(2)` Downloads copy, others superseded.
- **Excluded on purpose (secrets/credentials — never sync, never publish):**
  `BGINAI - 13\BGIN-Agent-Framework-main\.env`, `Downloads\bgin-swordsman-backup-*.txt`.
- **This KB is a private working set.** The transcript and internal drafts are not
  cleared for publication; anything leaving this directory goes through its own gate.
- **Pushes, posts, site PRs = Mitchell.** The only write path to the BGIN site is a PR
  from `~/bgin-homepage-fork` (`contents/projects.ts` etc.), branched fresh off
  upstream/main.

## Working plan

**`WORKING_PLAN_2026-09-21.md`** — the current plan across PQC (competition repo + SSR workshop), proof of personhood (24 Sep call → Block 15 2-6 → standards) and this week's presentations. Read it first.

## Open doors (as of 2026-08-27)

- Lock the GDC26 PQC run-sheet on the 28 Aug call (last call before Geneva).
- WF × IKP event 8 Sep — confirm agenda; convergence note tabled alongside.
- Block 15 submissions ≈ 8 Oct: `bgin_separation_of_duties.md` is ready; the
  proof-of-personhood paper takes the assurance decomposition as a contributed section.
- ADR-001 comments (where they land: ADR channel vs ZKP TF threads).
- Privacy-enhanced-auth hub is the thinnest on the site — natural co-chair edit.
