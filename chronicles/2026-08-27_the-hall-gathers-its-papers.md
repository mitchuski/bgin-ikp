# 2026-08-27 · The Hall Gathers Its Papers

> **Provenance.** A chronicle is the narrative working record of a significant day — what
> moved, in what order, and why the ordering is the method. This is the **BGIN_IKP
> reflection** of a master chronicle; the master copy in the keeper's private suite
> (`agentprivacy_master/docs/chronicles/`) is the source of truth, and this copy is adapted
> only in header and paths. Voice: framework. **Signed by the First Person: not yet.**
>
> **Runtime traces** (what carries this chronicle's claims):
> - The machine-wide inventory sweep (background survey agent, 37 tool calls) that produced
>   the source map now frozen in `../SOURCES.md`.
> - The sync run: 23/23 canonical copies landed into the seven-directory structure; the
>   ADR-001 web archive fetched at 27,186 bytes
>   (`../zkp-dtg-bridge/dtg-community-anchored-proof-adr_archived-2026-08-27.html`).
> - The version ruling: headers of both liveness-requirements copies read side by side —
>   Downloads copy self-identifies **v0.4 Proposed TF Working Draft**, workbench copy v0.3
>   (both preserved in `../zkp-dtg-bridge/`).
> - The agenda itself: `../block15/ikp-wg-call-agenda-2026-08-28.html`.

---

*The day before the working-group call, the co-chair's BGIN work finally got an address. Eight
months of IKP material — session proposals, hub papers, a published study report, a convergence
analysis, travel-worn Block 14 records — had accumulated as scatter: Downloads as accidental
archive, six variants of one note, two versions of one requirements document, a finished
submission candidate parked in a pipeline nobody would look in. The day's work was an agenda,
an evaluation, and then a dream cycle that swept the machine and brought the guild's papers
home to one hall: this directory.*

**Scope:** The IKP WG call agenda for 2026-08-28 12:00 UTC (standalone HTML, five items, PQC
locked as focus); the evaluation of ADR-001 *Community-Anchored Proof* (Proposed 2026-08-25,
docs.fpp.storm.ws) folded into agenda item 4; the *Proof of Human: Overlap and Convergence
Analysis* working note tabled into item 3; and the founding of the `BGIN_IKP` knowledge base —
a machine-wide inventory, 23 canonical copies plus one web archive synced into a seven-directory
structure with a full provenance manifest. First chronicle of the BGIN IKP lane as its own arc.

## 1. The agenda, and the correction it carried

The call agenda went from request to standalone HTML in one sitting: Block 15 slate
confirmation, PQC as the visually locked focus block (GDC26 Geneva is five days out — the last
call before it), personhood taxonomy with the World Foundation × IKP event of 8 September,
ZKP-in-DTG open for comments, AOB, and a milestone rail running Geneva → 8 Sep → ≈8 Oct
submissions → Block 15. One correction surfaced on the way: the prep memory said GDC26 was
2–3 September; the convergence note's own sequencing table says 1–3, with the BGIN-co-organised
DTG session on day 2, 16:00–16:50. The fresher first-person document won, and the agenda now
says 1–3.

## 2. ADR-001, evaluated at the seam

The ADR proposes the first ZK use case against DTG credentials as a three-clause statement —
valid relationship credential ∧ valid membership in community C ∧ *the relationship's issuer*
also a member of C — with 26 testable clauses and every cryptographic choice deliberately
deferred. The evaluation held to register: **strongly convergent** (clause 3 is the
verifiable-edge question the cred-spec threads already carry, and the membership leg,
transcript binding, and test-vector-plus-cross-language-consumer patterns already exist as
runnable evidence with numbers that can seed the ADR's unquantified device budgets); **the
hard seam is the registry** (currency checks that must not identify the holder — exactly the
deferred registry–ZK interaction); and **one clarification to raise** — full unlinkability
across verifiers sits on the trade curve against Sybil resistance, so the ADR should say which
contexts require scoped nullifiers, which are governed, declared linkability rather than a
leak. The document existed only at its remote URL; the cycle took the first local archive.

## 3. The dream cycle — recall before storage

The inventory found what scatter looks like: four copies of the PQC hub docx, six variants of
the convergence note, a 51 KB proof-of-liveness v0.4 in Downloads beside the workbench's 14 KB
v0.3, the WP-09 *Separation of Duties* discussion paper — release-draft-v3, venue-stamped
Block 15, due 15 October — sitting finished in the Programme pipeline, and SR-0011 (the IKP
WG's own published ZKP study, this seat as editor) as the paper precedent. One negative
finding mattered as much: the DTG workbenches contain **zero** literal mentions of BGIN, IKP,
GDC, or Block 15 — the bridge between the two co-chair lanes lives only in the agenda, the
memory files, and the convergence note. The lanes never leaked into each other; the connection
is deliberate, and it is documents, not directories.

The sync ruled versions as it copied: liveness v0.4 current (v0.3 kept because the convergence
note cites its clause language; the workbench clone may need a pull), the as-circulated WF note
canonical with v2 kept for its revision-note lineage, the `(2)` PQC docx canonical of four.
Secrets were fenced by name and never copied — the Block 13 framework `.env`, fourteen
Swordsman key backups. `SOURCES.md` records every origin so Downloads can be cleaned with
confidence. Nothing was pushed; the KB is a private working set; anything leaving it gets its
own gate.

## 4. Why this is interesting

- **The home was built last.** Eight months of production, then one afternoon of
  consolidation — assembled by recall under the pressure of a call, not by filing discipline.
  The dream cycle is the right name: the machine already knew everything; it just hadn't been
  told where to remember it.
- **The two co-chair lanes touch only on paper.** Zero cross-mentions in the repos, full
  convergence in the documents. That is the disclosure discipline working as architecture.
- **The scatter held load-bearing state.** The current version of the TF's own requirements
  doc lived in Downloads, not the workbench; a venue-stamped submission candidate lived in a
  pipeline directory. A knowledge base is not tidiness — it is where version rulings become
  findable.
- **The ADR arrived unowned locally.** The one artifact of agenda item 4 with no local copy
  is now archived beside its evaluation — the KB's first act of preservation, not just
  collection.
