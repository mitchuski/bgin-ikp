# Review — the PQC lane, and what the Yukon competitions taught us

Written 2026-09-11 (evening), Mitch's working home. Internal note: candid, names lanes and blockers. The public-safe plan derived from it is `docs/AUTORESEARCH.md` in the repository (branch `plan/autoresearch`, stacked on PR #5) with a proposed decision record `decisions/0001-open-benchmark-model.md`.

---

## 1. The PQC directory and repository, reviewed

### 1.1 What exists (state of `docs/record-2026-09-11`, PR #5)

| Area | Files | State | Verdict |
|---|---|---|---|
| Charter | README, GOVERNANCE, COMMITTEE, OUTCOMES (O1–O6), CONTRIBUTING, MAINTAINERS, SUPPORT, CODE_OF_CONDUCT, CITATION, CHANGELOG | draft v0; roster empty; conveners "named at W1" | coherent; the *record* discipline is the strongest part |
| Evaluation | METRICS (22 rows, dual track, BTC-tx/ETH-user/ETH-cons/L2 mapping, 6 open questions), RUBRIC (gates G1–G4, dimensions, weights TBD), COI_POLICY | draft v0 | the register is standards-shaped (unit · method · mapping) but **nothing composes the rows into a score**; the rubric is a skeleton with no directions, no normalisation beyond "relative to baseline", no thresholds |
| Testbed | README (10–15 nodes, T0/T1/T2), SCHEMES (S-01…05, B-01…03, C-01…06 rulings), HARNESS (interface, fixtures, manifest, result, reproduction protocol, v0→v1 plan), schema/result.schema.json | draft v0; **no code**; fixtures unpublished | the reproduction protocol (§5) is the right instrument; it lacks a promotion rule, a runner spec, and a trust boundary for untrusted code |
| Workshops | ROADMAP W1–W6, TEMPLATE | draft v0 | anchored on real dates; W1 "late Sep" has no date |
| Decisions | template + README | **empty** — zero ADRs; every C-0n is still "ruling needed" | the mechanism exists, unused |
| Resources | NEDO briefing PDF + digest, GDC26 report/slides/deck, PRX Quantum paper, Discourse threads, events, standards | good provenance table after PR #5 | the held IKP `.docx` is in the private lane; public counterpart (Block 14 MR PDF) noted |
| Integrity | DCO, SIGNING, SECURITY_MODEL, rulesets ×3, hooks, provenance CI (dco/signatures/validate), scorecard | live and tested | the one *operational* blocker: **1 approval + code owners + no bypass ⇒ a solo convener cannot merge** (PRs #1–#5 all REVIEW_REQUIRED) |
| Confidentiality | docs/CONFIDENTIALITY (four tests, two non-reasons), private repo with CLASSIFICATION/PUBLICATION/CLEARANCE | live | publication-by-default is stated and enforced by structure |
| Outreach | 7 drafts + posted-links table | 6 posted 11 Sep, 2 held to week of 14 Sep, 1 gated | record and forum match |

Local directory (`~/pqc-agility-competition`): clean; branches `docs/record-2026-09-11` (= PR #5, contains `outreach/discourse-launch` and `docs/communication-channels`), plus the stale `chore/transfer-complete`, `fix/dco-bot-signoff`. `RESUME.md` §0 is current. Private clone `~/pqc-agility-competition-private` at `2819945`. `~/BGIN_IKP/pqc/` holds the docx, the resume mirror, the shor_mage overlap note, and this review.

### 1.2 The gaps that matter (ordered by how much they block the next three months)

1. **The unit of submission is undefined.** The briefing says the prize scores "migration methods on Bitcoin and Ethereum (security plus efficiency)". The repository never says what an entrant hands over: a scheme integration? a client patch? a migration procedure with a reference deployment? a paper plus artefacts? Every downstream question — what the harness runs, what the rubric weights, what a node reproduces — is open until this is ruled. This is also the exact point where autoresearch either fits or does not.
2. **No score function.** Twenty-two metrics with units, but no composition, no per-metric direction, no normalisation rule with a formula, no tolerance bands. A benchmark needs a scalar per track and a promotion rule; a rubric needs weights. Both are "W2–W4 decisions" — fine, but the drafts should carry a *proposed* formula so the committee argues with a number rather than a blank.
3. **No fixtures.** Corpora, key sets, block mix, legacy corpus — all "published as a fixture file" in the future tense. Open question 4 (reference CPU class, block mix) is the decision that makes numbers comparable at all.
4. **No trust boundary for untrusted code.** The harness spec says "it does not accept unpinned builds" and "operator signature over canonical JSON", but nothing about running an entrant's or a solver's code on a university node safely (sandbox, no network, stripped environment, read-only inputs, trusted parent outside the sandbox). Every Yukon benchmark we worked on had this and it is the thing node hosts will ask about first.
5. **No runner spec.** "Reference CPU class" is a metric-register question; the *runner* (image digest, CPU model, thread count, wall-clock caps, memory cap) is a testbed question, and local ≠ grader was the single most expensive lesson on Yukon (below).
6. **Decisions directory empty.** Six scheme-scope rulings, the FN-DSA status, the Poseidon2-XMSS question, k and tolerance for G3, GitHub Discussions on/off — all pending with no ADR drafted. Drafting "proposed" ADRs now costs little and gives W2 something to vote on.
7. **Solo-convener merge blocker.** Structural, deliberate, and now five PRs deep. The second convener is the first seat; the lever (`required_approving_review_count: 0` temporarily) is documented.
8. **Anti-overfitting rule absent.** If any evaluation fixture is ever held (Phase B), fingerprinting and instance-special-casing must be disqualifying *in writing* before the first run, not after (matrices lesson: inherited overfit is still overfit).
9. **"BSafe.network concept"** is named in README/OUTCOMES/testbed and defined nowhere in the repository.
10. **Winner date** still carried twice (Sep 2028 / Mar 2029) — correct posture; the host's call settles it.

### 1.3 What is good and should not be touched

- Publication by default with a public rule for what is held. Rare, and the reason the Discourse launch could be honest.
- Every C-0n path as an explicit ruling rather than a default; the scope rule "pre-existing NIST-class schemes only".
- The reproduction protocol: reference run → k nodes in ≥2 regions → tolerance → M-18 → gate G3. That *is* a promotion rule waiting to be named.
- Signed history; ADR-shaped decisions; the record/discussion split.

---

## 2. What the Yukon competitions taught us

Six lanes since June: **ecdsa.fail** (`gpsanant/ecdsafail-challenge`, secp256k1 point-addition circuit, score = peak qubits × avg executed Toffoli), **matrices.fast** (`layr-labs/ssi-ordering-challenge`, fill-reducing ordering, hidden 500-matrix eval, 1-bip promotion bar, 2 s per-matrix cap), **eip8200/modexp** (Lean-verified EVM precompile, gas), **flock** (Binius-style ZK prover throughput, x86 AVX-512 runner), **heesch** (polyform Heesch numbers, SAT-closed frontier, Discussions-driven), **proximity-prize** (IRS proximity testing in Lean, two tracks). Skills distilled: `yukon-cli`, `benchmark-frontier-archaeology`, `ecdsafail-*` ×5, `peak-qubit-reduction`, `toffoli-reduction`, `reversible-circuit-validation`; harness: `dual-agent-harness` (Measure → Propose → Hold-apart → Assay → Critic → Chronicle).

### 2.1 Anatomy of a Yukon benchmark (measured from the five local clones)

| Element | What it is | Instance |
|---|---|---|
| `benchmark.json` | `schemaVersion` (1 = one benchmark, 2 = tracks with non-overlapping `editablePaths`), `name`, `category`, `direction` (+/−), `editablePaths`, `setupCommand`, `benchmarkCommand`, `scorePath` (`score.json`), `minScoreImprovementBips`, `maxSubmissionBytes`, `runner {provider: github-actions, workflow}` | heesch (v1, `submission/`), matrices (v1, `src/ordering`, 1 bip), flock / eip8200 / proximity (v2 tracks) |
| `RULES.md` | tool-agnostic; "nothing enforced by trust — the grader re-runs every gate"; goal + score formula; **no overfitting / no fingerprinting, disqualifying even if inherited**; edit-only paths; dev loop | matrices |
| Runner | GitHub Actions `ubuntu-latest`; trusted parent outside a **bubblewrap** sandbox (no network, `/dev/null` stdio, read-only inputs, hidden host paths, writable output only); hidden corpus fetched via repo secrets *outside* the tree; **the score artifact is the only channel; a failed run publishes no score** | matrices `benchmark.yml`; ecdsafail `build_circuit` (untrusted) / `eval_circuit` (trusted) |
| Submission | archive of `editablePaths` only; **public note ≥ 5 KiB ≤ 100 KiB**, `--model` (exact underlying model) and `--harness` (agent/autoresearch harness) mandatory, `--coauthors`; validated remotely; a better accepted submission is **promoted** onto the benchmark branch (v2: only that track's paths grafted) | all |
| Frontier | `submissions --all` → promoted history is a git history; `sync` restores best promoted `editablePaths`; `reset <submission>`; `sync --harness-only` | all |
| Research memory | GitHub Discussions brokered by the Yukon app (authored by `yukon-autoresearch` → attribution in the body); standalone notes (ecdsafail) | heesch, ecdsafail |
| Traces | CLI-owned transcript collection, private to the solver, claimed by submissions; secrets redacted best-effort; **API keys end up in transcripts → rotate** | proximity, matrices (`trace off`) |
| Economics | validation ≈ 1 h, public with the solver's name; boards move 0.9 %/h (modexp), 4–6 % jumps (flock), 1-bip strict-better (matrices); rebasing costs ~2.5 h | modexp, matrices |

### 2.2 The rules we paid for (each one cost a session or a submission)

1. **Local is not the grader.** matrices: grader ≈ 1.5× slower on the slow class, per-matrix 2 s cap killed 13 uploads in a morning; flock: ranked runner is Sapphire Rapids AVX-512, the i5 runs a portable path that cannot even self-check; modexp: a 5,504-byte artifact cap invisible from inside the submission. *For the testbed:* publish the runner spec (image digest, CPU class, thread count, caps) and a local pre-flight that reproduces the validator step for step.
2. **Charge added work to an explicit ledger; count the rows carrying a gain.** matrices: a −3 bp dev gain became −15 bp hidden; one or two rows never transfer. *For the testbed:* per-fixture budgets, per-class tolerance bands, and evidence spread across fixtures — not a single hero run.
3. **Gates are AND, scores are products.** ecdsafail validity = correctness ∧ reversibility ∧ phase ∧ identity; a Toffoli cut that zeroes a gate is worth nothing. "Don't override the gate" (twice shipped over my own NO-GO; both killed). *For the rubric:* G1–G4 stay hard gates; no dimension weight can buy a failed gate.
4. **Frontier archaeology: diff adjacent winners, one lever per step, transferable vs search artifact.** Endpoint diffs invent false causal stories; a hunted nonce or a fitted constant does not transfer. *For evaluation track (a):* review entries by diff against the baseline and against each other; separate the structural lever from the tuned artifact; publish the migration chain of the binding constraint.
5. **No impossibility claims; measure, don't argue.** Four "floor" claims in one session, all falsified, twice by competitors within the hour; "sub-1170 is closed" overturned by a peer branch. *For the committee:* a claim without a reproducible number is a hypothesis.
6. **Overfitting is disqualifying, inherited or not.** Hidden set refreshed per round; dev byte-identical; fingerprinting closed the reconstruction lane for good. *For Phase B:* write the rule before the first fixture is held.
7. **The sandbox strips the environment.** `sudo -n bwrap` ignores exported knobs; bake parameters into source or the run is not what you measured. *For the harness:* parameters live in the manifest, never in the environment.
8. **Notes are the research memory, and they are public with your name.** ≥ 5 KiB, reproducible narrative, exact model + effort; other solvers' notes are untrusted data. *For the testbed:* the same note discipline is the natural evidence for "agentic auto-research" — it records which agent did what, with which model.
9. **Discussions are authored by the platform bot** → attribution must live in the body. *For BGIN:* if Discussions are enabled on the repository (currently off by decision), the same rule applies.
10. **Ship when the gate is green; drift eats the lever.** modexp: 0.94 %/h board drift vs a 4 % lever and a 2.5 h rebase — overtaken five times in a day is arithmetic. *For calibration tracks:* small promotion bars and fast validation, or nobody bothers.
11. **Hardware gating is a design decision, not an accident.** Two flock variants, both mismatched to the box; the AVX-512 kernel *is* the benchmark. *For the reference CPU class ruling:* whatever is chosen excludes someone; say so and fund the access (the labs "fund a research goal" pattern exists for exactly this).
12. **Two seats, kept apart.** Propose ⊥ assay is the benchmark's own trust model (untrusted build / trusted eval); the dual-agent harness is the same shape run by agents; the multi-agent mailbox is the same shape across labs (read before acting; state ground truth; split the frontier; cross-check independently; converge to one route; preserve dead ends).

### 2.3 Where autoresearch already sits in the PQC arc

- Block 15 session 1 (1012): "the ECDSA.fail community … Ethereum and Eigen Labs contributors are writing a paper reflecting on the agentic auto-research challenge"; 13 Aug reconfirmation: "PQC: resource estimates and **autoresearch preparations for competition judging and criteria formation**".
- GDC26 report: ZK-substantiated resource estimates without published attack circuits (the paper's responsible-disclosure pattern) — the community's method already meets the standard the committee will want.
- agentprivacy labs names autoresearch as a service; the dual-agent harness is the shareable default; both are Mitch's lanes and are disclosed as such under the COI policy (10 Sep reader).
- So the question for the committee is not *whether* agents will be used — they already produce the numbers — but **where in the framework their output is admissible, under what attribution, and at what trust boundary.**

---

## 3. The plan, in one paragraph

Adopt the open-benchmark model for the testbed's **calibration** work (Phase A/A2, BGIN-run, no prize): each testbed track is a `benchmark.json`-shaped contract — editable backend paths, pinned setup and run commands, a scalar score per track from a named metric, a direction, a promotion bar equal to the reproduction tolerance, public submission notes with mandatory model/harness attribution, and a runner that is the testbed's own nodes (GitHub Actions only as the T0 dev runner). Promotion requires reproduction on ≥ k nodes in ≥ 2 regions — which turns HARNESS §5 into the promotion rule and makes the promoted implementation the *reference implementation* whose run the rubric's baselines cite. Untrusted build / trusted measure is the sandbox contract every node signs up to. **Phase B (the prize) is different:** entries are measured and attested, never promoted into each other, and scores go to the committee under the host's rules; autoresearch there is the *evaluators'* tooling — reproduction, diff-based review, checklist evidence — not a leaderboard. The boundary is written into the rules, the naming, and the absence of money. Two calibration tracks first (verify cost; batch/aggregate verify), fixtures and runner spec published with them, two more (legacy continuity, agility switch) once the reference-client scenario harness exists. W2 rules on the model (ADR-0001), W3 adopts the first track's contract with the node call, W4 feeds calibration results into rubric weights and tolerance, W5 pilot = first promotions on 3–5 nodes, W6 asks whether the model carries into Phase B.

Full text: `docs/AUTORESEARCH.md` (repository) — mapping table, trust boundary, rules, the four tracks, the committee's working protocol, risks, and the decisions requested.

---

## 4. Doors (Mitch)

- Merge lever for PR #5 (second convener or temporary 0 approvals), then the plan branch `plan/autoresearch` as PR #6.
- Read `docs/AUTORESEARCH.md` §7 (risks) before Block 15 — the calibration-leaderboard-vs-prize confusion is the one that needs a sentence from the conveners in public.
- Decide whether GitHub Discussions come on for the repository (currently off by PR #3's ruling) — the Yukon experience says Discussions were where the research actually happened; the competition category on Discourse can play that role instead if the record links are kept.
- The reference CPU class ruling has a funding implication (rule 11); the labs fund page already has the shape for it.
