# 2026-09-12 · The Prover and the Proposer

> **Provenance.** A chronicle is the narrative working record of a significant day — what
> moved, in what order, and why the ordering is the method. This is a **BGIN_IKP reflection**
> written first in this KB (no master copy yet; the master series may adopt it). Voice:
> framework. **Signed by the First Person: not yet.** It is also a **handoff**: §5 is the recipe
> for building the PQC competition dual-agent harness instance formally, which is the First
> Person's build, not the agent's.
>
> **Runtime traces** (what carries this chronicle's claims):
> - The review: `../pqc/PQC_REVIEW_AND_YUKON_2026-09-11.md` — the repository gaps ranked, the
>   twelve rules paid for on six Yukon lanes, the benchmark anatomy measured from five local
>   `benchmark.json` manifests.
> - The plan and the structure on branch `plan/autoresearch` of
>   `bgin-global/pqc-agility-competition` (signed commits `ef5034e`, `629f42a`, `fc95d40`; PR #6, stacked on PR #5):
>   `docs/AUTORESEARCH.md` (§5b *Proposers and provers*), `decisions/0001-open-benchmark-model.md`,
>   `testbed/tracks/README.md`, `testbed/tracks/T1-verify-single/{benchmark.json, RULES.md,
>   runner.json, fixtures/README.md}`, `testbed/tracks/SUBMISSION_NOTE_TEMPLATE.md`,
>   `testbed/schema/result.schema.json` (`manifest.runner`, `manifest.draw`).
> - The harness read: `~/dual-agent-harness` (public as `mitchuski/agentprivacy-harness`,
>   `95e395d`) — `engine/gap.mjs` `deriveSeed({hSource, hProposal, salt})` =
>   `sha256(hSource ‖ hProposal ‖ salt)`; `engine/dual_agent_loop.mjs` `deriveHoldApart`,
>   `runHarness(config, rt, runArgs)`; `tools/new_instance.mjs`; `examples/field-guide/
>   harness.config.mjs` (objective · gate · heldApartRule · keystoneOnlyWrites · finders ·
>   prompts · schemas); `TRUSTS.md` T2/T3/T5/T6; `templates/chronicle.md`.
> - What the forum shows: category 44 with 1053 / 1054 / 1055 posted 11 Sep; the website hub
>   live since PR #106 merged 13:22 UTC.

---

*Two days ago the competition had a record and no instrument. The record was good — signed
history, a metric register with units, a testbed specification with a reproduction rule — but
nothing in it could be run, and nothing in it said what an entrant hands over. The day's work
was to look at the six leaderboards we had spent the summer on, write down what they cost us to
learn, and notice that the testbed already has the two seats of the harness we built for
ourselves: the proposer, who commits a signature scheme or a way of switching between them;
and the prover, a node that runs it and signs what it saw. Between them, a draw the proposer
cannot predict. That is not an analogy. It is the shape of the evidence the committee needs.*

**Scope:** the review of the PQC directory and repository against what the Yukon competitions
taught; the proposal that the testbed's calibration tracks run as open benchmarks; the
structure that lets that happen (a track contract, T1 drafted, the draw and the runner in the
result schema, directions, the measurement seat in the COI policy); the recognition that this
is a dual-agent harness instance; and the recipe for building that instance formally.

## 1. What six leaderboards cost

The summer's lanes — ecdsa.fail, matrices.fast, the EIP-8200 modexp precompile, flock, heesch,
the Proximity Prize — were entered as research and ran as an education. The review ranks the
repository's gaps and lists the twelve rules we paid for; three of them decide the shape of
what follows.

**Local is not the grader.** The matrices grader ran the slow class 1.5× slower than the bench
and a 2-second per-matrix cap killed thirteen uploads in a morning; flock's ranked runner is a
Sapphire Rapids and the i5 could not even self-check; modexp had a 5,504-byte artifact cap
invisible from inside the submission. A testbed that does not publish its runner, and does not
give the solver the validator step to pre-flight, will spend its node-hours on this lesson
again. So the T1 contract carries `runner.json` and a T0 development runner whose score is a
claimed score and never a promotion.

**Gates are AND; scores are products.** Validity on ecdsa.fail was correctness ∧ reversibility ∧
phase ∧ identity; a Toffoli cut that zeroed one was worth nothing; twice I shipped over my own
NO-GO and both were killed. The rubric's G1–G4 stay hard gates, and no dimension weight buys a
failed one. T5 in the harness's language: any zero collapses the product.

**Overfitting is disqualifying, inherited or not.** The matrices hidden set was refreshed per
round, the dev set was byte-identical, fingerprinting closed the reconstruction lane for good,
and a −3 bp dev gain became −15 bp hidden. Written as a rule it protects the record; built into
the draw it protects the evidence. That is the difference the harness makes.

## 2. The plan: two uses, one boundary

`docs/AUTORESEARCH.md` proposes that the testbed's **calibration** work — Phase A/A2, BGIN-run,
no prize — runs as open benchmark tracks: one manifest per track in the shape the community
benchmarks already use, editable backend paths, pinned commands, a scalar from a named metric
against the classical baseline, a promotion bar **equal to the reproduction tolerance**, public
notes with the model and the harness named, untrusted build and trusted measure on every node.
The reference run of `HARNESS.md` §5 becomes the promoted submission; the promoted backend
becomes the reference implementation the rubric's baselines cite.

The prize evaluation is different and the document says so in every place it could be
confused: entries are measured and attested, never promoted into one another, no leaderboard,
no money. Autoresearch sits on the calibration tracks as an attributed solver, and in Phase B
as the evaluators' tooling — reproduction, diff-based review, checklist evidence. The question
the committee actually owns is not whether agents are used (they already produce the numbers
the field cites) but where their output is admissible, under what attribution, and behind
which trust boundary.

Four tracks are named. T1 `verify-single` is deliberately boring: median ML-DSA-65 verify over
the classical baseline on the reference CPU class. It exists to make the CPU-class ruling, the
tolerance band and the runner specification real before anything harder depends on them.

## 3. The structure that was added

On `plan/autoresearch`, everything marked *proposed* pending `decisions/0001` at W2:

| Where | What |
|---|---|
| `testbed/tracks/README.md` | the track contract: directory shape, lifecycle proposed → open → frozen → closed, promotion, what a track is not |
| `T1-verify-single/benchmark.json` | the manifest in the open-benchmark shape (`editablePaths`, `setupCommand`, `benchmarkCommand`, `scorePath`, `direction`, `minScoreImprovementBips` = tolerance, `runner`, `fixtures.draw`, `notes`) |
| `T1-verify-single/RULES.md` | goal and formula; edit only `backends/ml-dsa/`; no fingerprinting; no change to what is measured; one lever per submission; roles; what the track is not |
| `T1-verify-single/runner.json` | CPU class (TBD by ruling), threads, caps, the bubblewrap sandbox with the trusted parent outside it |
| `T1-verify-single/fixtures/README.md` | the banks pending, and **the draw**: `seed = SHA-256(h_fixtures ‖ h_submission ‖ salt_round)` |
| `tracks/SUBMISSION_NOTE_TEMPLATE.md` | `Model:` / `Harness:` / `Effort:` / `Base:` lines, then goal, setup, hypothesis, changes, commands, results table, failures, caveats, next step |
| `schema/result.schema.json` | `manifest.runner`, `manifest.draw` (`h_fixtures`, `h_submission`, `salt_round_commitment`, `salt_round`, `seed`), `track`, `scalar` |
| `evaluation/METRICS.md` | proposed directions per row (lower / higher / gate-or-ordinal) |
| `evaluation/COI_POLICY.md` | the measurement seat: hosts are not submitters on the tracks they measure; submitters are not judges; agent attribution mandatory; calibration results are not judgements |
| `HARNESS.md` §5 | the promotion rule and the draw, as item 6 |
| CI | the validate job now parses `testbed/tracks/*/*.json` |

## 4. The recognition

The testbed's two roles are the harness's two seats, and the value of the evidence *is* their
separation.

| Harness seat | Testbed role |
|---|---|
| Measure | the trusted scorer reads the baseline on the node's own hardware |
| Propose — soulbae 🧙 `bnot` | the submitter commits an archive of the editable paths and a public note: an implementation of a scheme, or a mechanism for switching between schemes |
| Hold-apart — the Gap ⿻ `xor` | the fixture draw, derived from the proposal's digest and a round secret the proposer never sees; it holds only the axioms — manifest, fixture bank, schema |
| Assay — soulbis ⚔️ `neg` | k nodes in two regions run the drawn instances inside the sandbox and sign canonical results |
| Critic | the committee's track (a) review reads the promoted diff: one lever, transferable or artifact, where the binding cost moved |
| Chronicle | `promoted/` and the workshop record |

Four things follow that a plain leaderboard does not have, and the plan's §5b states them:
overfitting impossible by construction rather than by rule (the proposer commits before the
draw); *what you prove alone is a candidate; only what another signs beside you is real*
(promotion is k independent attestations over the same draw, and the gate is multiplicative);
strangers can meet (a new solver and a new node agree on nothing but the axioms, which is what
makes a self-hosted validator equivalent to a node); and crypto-agility is tested against a
switch the author cannot rehearse (for T3/T4 the Gap draws the *scenario* — which scheme pair,
when the switch or rollback triggers, which legacy signatures must still verify).

One more, which the harness's own `THREATS.md` names as its open target: the runtime does not
yet enforce the seat topology with process mounts. **The testbed does.** The bubblewrap sandbox
with the trusted parent outside it is the process boundary T2 asks for; the node is where the
separation bound stops being a promise and becomes a mount. The instance gets from the testbed
the enforcement the harness lacks, and the testbed gets from the harness the draw it lacked.

## 5. Handoff — building the instance formally

This is the First Person's build. The agent's part is the recipe and the seat cards; the door
(T6) is yours: the repository push, the node onboarding, the first real round.

**5.1 Scaffold.** `node tools/new_instance.mjs <dir> pqc-calibration --prover <a different
model than the proposer>` from the harness root. The scaffold copies the ledgers
(`frontier.json`, `claims_register.md`, `manifest.yaml`, `notes/KILLED_LEVERS.md`) and a blank
config, and tells you what remains. Do not let it pretend to be finished. Suggested home:
`~/pqc_harness/` beside the repository clone, never inside `editablePaths`.

**5.2 Objective.** In `harness.config.mjs`:

```js
objective: {
  metric: 'scalar',   // T1: median_verify_us(S-01) / median_verify_us(B-01), lower is better
  gate: 'the track gates as an AND: known-answer tests pass · build pinned · no network · result validates against result.schema.json · attestation present · reproduced on ≥ k nodes in ≥ 2 regions within tolerance (T5: any zero collapses)',
  hardConstraint: 'only backends/ml-dsa/ changed; verification unchanged in what it checks; parameter set unchanged (RULES.md)',
  canary: 'the promoted reference implementation itself: it passes every gate by construction, so a failure is always the candidate\'s, never the gate\'s',
},
```

**5.3 The gate, and why it is a sample not a census.** The field-guide instance is a census
(N = 32 facts, every one probed). T1's population is a fixture bank of 2^16 messages — too large
to enumerate, so `gate: { N: 65536, count: 10000, mode: 'sample' }`; the engine's `conform.mjs`
will accept sample mode because N ≫ `censusThreshold`. Detection here is not "did a fact
survive" but "does the median move outside the tolerance band on an unpredictable draw"; the
coverage stanza the assay seat prints should say so in those words.

**5.4 The draw is the fixture draw.** The engine already computes
`seed = sha256(hSource ‖ hProposal ‖ salt)` and hands it to the Gap. Bind the three terms to the
track: `hSource = h_fixtures` (the digest of the published bank), `hProposal = h_submission`
(the canonical archive of the editable paths — sorted, LF, no timestamps; `engine/gap.mjs`
`canonicalize` is the reference for canon bytes), `salt = salt_round` (the round secret whose
hash the conveners publish before submissions close; revealed with the results). Two things to
decide and write into the config's `heldApartRule`: that the salt is **per round, not per
proposal** (every node must run the same draw for reproduction to compare like with like — the
engine's `perProposalSalt` is the wrong tool here), and that the Gap seat writes the draw
indices into `gap.json` exactly as the engine derived them, so the auditor's
`sha256sum proposal_canon.json` re-derivation still holds.

**5.5 The assay seat is a node.** The prover's card changes the most. In the field guide the
assay answers questions from `candidate.md`; here the assay **runs the harness** —
`harness run --track T1-verify-single --runner runner.json --draw <seed>` inside the sandbox —
and its `verdict.json` carries `result.json` (schema-valid, attested) and the scalar, with
`status: VALIDATED | MIRAGE | BLOCKED`: BLOCKED if the seed does not re-derive or the runner
does not match `runner.json`; MIRAGE if a gate fails on a candidate that "reads fine" — name
the gate; VALIDATED only if every gate holds and the scalar beats `frontier.json` by more than
the bar. One assay seat per node; the round's verdict is the conjunction over k nodes. This is
where the multi-node reproduction of `HARNESS.md` §5 becomes the harness's own multiplicative
gate.

**5.6 The proposer's card.** `finders` are lenses, one per lever family, exactly as the
field guide has `line-editor` and `restructurer`. For T1: `vectorised-ntt`, `hash-path`,
`memory-layout`, `verify-batch-reuse`; for the agility tracks later: `hybrid-composition`,
`staged-cutover`, `rollback-path`. The proposal schema requires `leverId`, `lens`, `rationale`,
`expectedMetric`, `hardConstraintNote`, and — the change from the field guide — `patch` (the
diff confined to the editable paths) and `note` (the submission note, ≥ 5 KiB, with the Model /
Harness / Effort lines the seat must fill from its own identity). The proposer never sees the
salt, the draw, or a node.

**5.7 Keystone-only writes.** `frontier.json` is the promoted history — the keystone
serialises a promotion only after k verdicts agree (GR-10). `claims_register.md` carries the
tier of every claim (a T0 score is a *claimed* score; a promotion is *enforced-by:
k attestations*). `notes/KILLED_LEVERS.md` is where the critic's structural kills go with a
re-open condition (GR-6). The `promoted/` directory in the track is the public projection of
`frontier.json`, written by the keystone, with the note and the attestations beside the result.

**5.8 Critic and chronicle.** The critic's card is frontier archaeology in one paragraph:
diff the promoted candidate against the incumbent scoped to the editable paths; name the single
lever; classify it transferable (a structural change, a knob) or artifact (a constant tuned to
this runner); say where the binding cost moved; name exactly one next lead. The chronicle seat
writes from `templates/chronicle.md`, verdict first, reversals at the same prominence as wins
(GR-7). Both feed the workshop record (`workshops/TEMPLATE.md`) — the committee reads the
critic's paragraph, not the transcript.

**5.9 What conform must prove.** Beyond the algebra on Z/64Z, the instance's `conform.mjs`
pass should refuse: a config whose promotion bar is smaller than its tolerance band (a
promotion inside the noise); a config whose salt is per proposal (reproduction would compare
different draws); a proposal schema without the attribution lines; a runner in a verdict that
does not match `runner.json`. Write those four checks before the first real round — they are
the four ways this instance can lie while looking green.

**5.10 Order of work.** (1) Scaffold and run the stub driver once so the files land and the
seeds derive (`node drivers/run.mjs --instance ~/pqc_harness --driver stub --run smoke`, then
`verify_run.mjs`). (2) Replace the field-guide seat cards with §5.2–5.8; keep the stub driver
until the cards produce schema-valid proposals and verdicts. (3) Point `measure` at a real
`harness run` on a T0 job — this needs the harness v0 of `HARNESS.md` §7 (liboqs +
libsecp256k1 + blst, single node, M-01…M-05), which does not exist yet and is the actual
critical path. (4) Run one round on a local model with the T0 runner as the single assay seat.
(5) When 0002 fixes k and tolerance, add the node seats. (6) Only then open T1 — by decision
record, on the public channel, with the sentence about what the track is not.

**5.11 Disclosure.** The harness is one of the conveners' lanes. The COI clause added to
`evaluation/COI_POLICY.md` says conveners with an interest in an autoresearch harness disclose
it before any vote on the benchmark model; the instance's own `manifest.yaml` should name the
harness and the runtime in the public form the repository README gives: *Harness: <runtime>
with the agentprivacy dual-agent harness (pqc-calibration instance)*.

**5.12 A note on the star — kept as a note.** The harness already emits an instance's
seating as data (`tools/star.mjs` → `star.json`, format `star.v1`: the instance at its
declared or content-derived vertex, each validated result seated at κ mod 64), and the
Swordsman's Key renders keys that way — `/skye`, the night of many keys, each risen by its own
κ, the sky shot carrying every risen key. When the calibration tracks have a hosted site, a
submitter's runtime could appear as a star lit by the node attestations it has been signed on,
and a track's sky would be its promoted history as a constellation; scaled, perhaps, by the
signature sizes it measured (M-01, M-06), which is the picture every room will ask the
committee for. The rule that already governs the instrument carries over unchanged: colour
and geometry, never proof — the attestation is the evidence, the star shows where it landed.
Do not build this before §5.10 step 3; do not let the visual become a claim. One paragraph in
`docs/AUTORESEARCH.md` §5b says the same and nothing in the plan depends on it.

## 6. Built the same evening — two homes, one lineage

The instance now exists in both places the First Person named. **In the record:** PR #7
(`harness/instance`, signed `bda4f4b` + `1572a23`, CI green) — `harness/upstream/` vendors the
origin's default distribution verbatim at the pinned commit `790a3b7` (111 files, sha256 each in
`UPSTREAM.json`; `scripts/sync-harness.sh` is the harness-only sync, `--verify` the audit; the
vendored engine passes its own eleven gates in the competition tree) and `harness/instance/` is
the pqc-calibration instance, scaffolded with the upstream's own tool and filled for T1 exactly
as §5 prescribes — with one correction below. `tools/measure.mjs` reports *unmeasured* and
`frontier.json` carries OT-1; conformance fails on that and only that, by design, and CI reports
it until a baseline exists. A stub round is on record and `verify_run` re-derives every seed.
**Locally:** `~/pqc_harness`, scaffolded from the origin checkout itself (the newer scaffolder
that writes `connection.local.json`), overlaid with the repository's instance files
(`sync-from-repo.sh`, one direction); the same stub round verifies against the origin engine.

**Two defects, found by running** (the upstream's own rule: invisible to inspection, obvious on
execution). `draw()` takes one byte per pick, so a 10,000-draw from 65,536 never passed index
10,230 — exact for the field guide's census, a biased and therefore tunable draw for a large
bank; `seedBytes()` expands with a one-byte counter and repeats after 8,192 bytes. Recorded in
`UPSTREAM.json`, `notes/UPSTREAM_DEFECTS.md` and the claims register (C-PQC-3, PROVEN by the
saved `gap.json`); reported upstream. **T1 cannot open on a biased draw.** The fix is a few
lines in the origin — your tree, your other session — and arrives in the record by the sync
when the pin moves.

**Fixed the same afternoon.** The two defects were fixed in the origin (`~/dual-agent-harness`,
commit `ea25f42` on `main`: draw v2 — 32-bit rejection-sampled picks, a 4-byte expansion
counter, `drawVersion` recorded in every `gap.json`, v1 kept as the legacy replay; `gap.test.mjs`
pins both the defect and the fix; all 21 origin gates pass, every saved run still re-derives; the
origin's chronicle `2026-09-12_the-draw-that-stayed-in-the-shallows.md`, index line left for the
keystone because `chronicles/README.md` was mid-edit by the other session). Only the fix's hunks
were staged — the other session's 401 uncommitted lines stayed in its working tree. Then the
discovery that `dist/` is gitignored upstream: the distribution is *generated*, so
`scripts/sync-harness.sh` now builds it in a clean temporary worktree at the pinned commit — the
pin names the source commit and anyone can regenerate and compare. Re-vendored at `ea25f42`
(113 files — the earlier copy had been a stale generation); the post-fix stub round
(`runs/smoke-v2/`) reaches index **65,527** of 65,536, the pre-fix round stays as the record of the
finding; PR #7 green (`33fb8af`, `a6eca5f`). A third, documentation-only nit (D-3: the upstream
template links `ENTRY.md` relative to the harness root) is recorded and the record's link check
now excludes the vendored tree. **The origin's `main` is one commit ahead of GitHub — pushing it is
the First Person's.**

## Reversals

**§5.4 reversed in part.** The engine's `perProposalSalt(saltSecret, hProposal)` is *not* the
wrong tool: it is deterministic in the run secret, so k nodes given the same round secret derive
identical draws. The round secret *is* the run's `saltSecret` — committed by hash before
submissions close, shared with the assay nodes after commitment, revealed with the results. The
instance config says this in `heldApartRule`; the chronicle's earlier sentence stands corrected.

Two things were narrowed: the plan says the testbed adopts the
harness's *shape* — commitment before draw, independent signatures, shared root of axioms only
— not the software; and `perProposalSalt`, which the field-guide instance uses, is named as the
wrong tool for a multi-node draw.

## Ledger entries returned

- **claims_register (proposed):** *C-PQC-1* "the fixture draw makes fixture overfitting
  impossible by construction" — tier: **argued**, enforced-by: nothing yet (the draw is
  specified, not implemented). Promote to *enforced* only when a node's `result.json` carries a
  `draw` that re-derives from published bytes.
- **claims_register (proposed):** *C-PQC-2* "promotion = k independent attestations over one
  draw" — tier: **specified** (`HARNESS.md` §5 item 6, `tracks/README.md`); enforced-by: the
  keystone's write rule once the instance exists.
- **KILLED_LEVERS (none).**

## Handoff

- **Open questions:** the unit of submission for the prize (W2/W4 — decides whether Phase B
  entries are shaped like components or like deployments); the reference CPU class and what it
  excludes (with the funding line); GitHub Discussions on or off for the repository; whether the
  round salt is committed by the conveners or by a node quorum.
- **Blocked items:** PRs #5 → #6 → #7 — one approval from a convener who is not the author, or a
  temporary `required_approving_review_count: 0`; the harness v0 (§5.10 step 3) is unbuilt and is
  the critical path to any real round. (D-1 fixed at `ea25f42`; no longer blocks.)
- **Single next action:** push the origin's `main` (`ea25f42`) so the pin in `UPSTREAM.json` is
  auditable from GitHub; then the merge lever for #5 → #6 → #7; then the harness v0 (§5.10 step 3).
