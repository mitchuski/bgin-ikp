# Discourse posting pack — Post-Quantum Crypto Agility Competition (category 44)

Generated 2026-09-11 from `outreach/discourse/*` at `cd11dc3` on `outreach/discourse-launch` (bgin-global/pqc-agility-competition). Paste the body blocks verbatim — Discourse renders this markdown. Titles go in the title field. Category for steps 2–6: **Post-Quantum Crypto Agility Competition** (https://bgin.discourse.group/c/post-quantum-crypto-agility-competition/44).

## Before posting

- Category settings: check that logged-in users can create topics in the category (anonymous currently cannot, which is normal); set the category description from step 1; consider a category logo later, not now.
- **Push `outreach/discourse-launch` first** (`git push -u origin outreach/discourse-launch`, then a PR). Step 2 says the rule for what is held is public — that is `docs/CONFIDENTIALITY.md`, which lives only on that branch until it merges. If posting before the merge, link it by branch URL: https://github.com/bgin-global/pqc-agility-competition/blob/outreach/discourse-launch/docs/CONFIDENTIALITY.md.
- Step 1's first paragraph (192 chars) is what category lists show — keep it the first paragraph.
- After steps 2–6 are up, edit the launch post (step 2) and replace the three *Separate topic to follow* lines with links to steps 4, 5, 6.
- Then fill the *Posted* column in `outreach/README.md` and commit (signed) — the record catches up with what was said.
- Step 7C carries the scene-setting deck: post it only once the speaker has cleared hosting the deck on bgin-global.org; otherwise post the paper paragraph and drop the slides line.


---

## Step 1 — edit the About topic (category description)

**Where:** [About the Post-Quantum Crypto Agility Competition category](https://bgin.discourse.group/t/about-the-post-quantum-crypto-agility-competition-category/1050) (category 44), replacing the placeholder template text.


```markdown
Working category for the PQC Migration Prize — the crypto-agility competition hosted by METI/NEDO and coordinated internationally by BGIN. Committee, metrics, testbed, workshops, and the call.

### What this category is for

The competition runs 2026–2028. The Japanese Government (METI/NEDO) hosts it, publishes the call, sets the rules and awards the prize. BGIN coordinates internationally and runs the neutral evaluation testbed. This category is where the work between those two things happens in the open.

Topics that belong here:

- Evaluation committee — nominations, composition, conflicts, ratification.
- Metrics and rubric — what is measured, in what units, against which reference configuration.
- Schemes and scope — which signature schemes and which integration paths are in the testbed, and which are rulings rather than defaults.
- Testbed — harness, result schema, node hosting, reproduction.
- Workshops W1–W6 (Sep 2026 → Feb 2027) — agendas, records, decisions.
- Call text — inputs BGIN hands to the host.

### What it is not for

Threat-narrative debate about a single "Q-day" date, and proposals for new PQC primitives. The competition starts from NIST process outputs; the hard problem on public chains is deployment, evaluation, testbeds and migration governance. General PQC discussion continues on the [IKP Post Quantum Cryptography thread](https://bgin.discourse.group/t/ikp-post-quantum-cryptography-thread-06-26/1001).

### The record

Discussion happens here. The record is the repository: **https://github.com/bgin-global/pqc-agility-competition** — governance, outcomes, the metric register, the rubric, the testbed specification, the workshop roadmap and every decision record. The public face is the project hub on the BGIN website: https://bgin-global.org/projects/pqc-migration. Everything in it is `draft v0` until the evaluation committee ratifies it and the host publishes the official call. Nothing decided in a post is decided until it is in the repository.
```


---

## Step 2 — launch topic

**Where:** new topic in *Post-Quantum Crypto Agility Competition* (category 44).

**Title:** `The PQC Migration Prize: the working repository is open, and three things are open with it`


```markdown
The crypto-agility competition discussed at GDC26 and through the IKP working group now has a category here, a working repository, and a hub on the BGIN website.

**Repository:** https://github.com/bgin-global/pqc-agility-competition
**Hub:** https://bgin-global.org/projects/pqc-migration

The Japanese Government (METI/NEDO) hosts the competition, publishes the call, sets the rules and awards the prize. BGIN coordinates internationally and runs the neutral evaluation testbed. Between now and the call, the work is public: form the evaluation committee, ratify the outcomes, draft the metrics and rubric, and specify the testbed. Six workshops from late September 2026 to February 2027 carry that work; applications open January 2027 as planned.

The repository holds all of it in draft: `GOVERNANCE.md`, `OUTCOMES.md` (O1–O6), `evaluation/METRICS.md` (22 candidate metrics), `evaluation/RUBRIC.md`, `testbed/SCHEMES.md` and `testbed/HARNESS.md`, and `workshops/ROADMAP.md`. Every document is marked `draft v0`. None of it is settled; that is the point of publishing it now rather than after.

### Three ways to take part

1. **Nominate someone for the evaluation committee** — including yourself. Composition is a draft table ratified at W1. Separate topic to follow.
2. **Propose or challenge a metric, or argue a scheme scope ruling.** The metric register carries 22 candidates and six open questions; the scheme table carries six integration paths (`C-01`–`C-06`) that are explicitly rulings, not defaults. Separate topic to follow.
3. **Offer a testbed node.** Geographic distribution is what makes the evidence neutral, and the node call is a W3 output. Separate topic to follow.

Each of the three has a GitHub issue template. A post here is fine too; the repository is where it ends up either way.

One more, asked plainly: the repository's rule is that nothing merges without a review from a convener who is not the author, and there is no administrator bypass. With one convener seated, the record cannot move. A **second convener with a signing key** is the first seat to fill, and it is asked for here before anything else is.

### Two things stated plainly

**Dates disagree, and both are carried.** The July community briefing targets winner selection for mid-September 2028; the GDC26 meeting report says March 2029. Both are provisional and the host's call text settles it. The repository carries both, attributed, rather than picking one.

**Not everything can be public, and the rule for that is public.** Some source material was circulated to working-group members without a publication clearance, nominations and conflict-of-interest disclosures name people, and draft call text is the host's to announce. That material is held in a separate, access-controlled repository. What makes something eligible to be held — and the gate it passes through to be released — is published in the open repository, along with a register of what has been released and what has been refused. Unfinished work and disagreement are not reasons to hold anything; they stay in public.

### Sources

- GDC26 meeting report — [Post-Quantum Cryptography Migration on DLTs](https://bgin-global.org/news/260903-gdc26-pqc-migration) (3 Sep 2026), and its [thread here](https://bgin.discourse.group/t/gdc26-meeting-report-published-post-quantum-cryptography-migration-on-dlts/1045).
- METI/NEDO community briefing (July 2026) — in the repository at `resources/`, with a plain-text digest.
- [IKP Post Quantum Cryptography thread 06/26](https://bgin.discourse.group/t/ikp-post-quantum-cryptography-thread-06-26/1001).
- The resource estimates and attack classes the GDC26 room used — *Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations*, PRX Quantum 7, 031001 (21 Aug 2026), open access: https://doi.org/10.1103/j3xf-bw18.
```


---

## Step 3 — workshop series (pin this topic)

**Where:** new topic in category 44. Pin this one.

**Title:** `Workshop series W1–W6, Sep 2026 → Feb 2027`


```markdown
Six working sessions take the competition from a briefing to a call. Each rides an existing calendar anchor where one exists. **All dates are provisional until organisers confirm them**, and the roadmap in the repository is the version that gets corrected: `workshops/ROADMAP.md`.

| # | Target | Anchor | Decisions |
|---|---|---|---|
| **W1 Kickoff** | late Sep 2026 | GDC26 report; CBT session (~Sep 17) | Outcomes ratified; governance v0 adopted provisionally; nominations opened; conveners named |
| **W2 Committee & metrics** | mid Oct 2026 | EF Quantum Retreat (Oct 9–12); **BGIN Block 15 (Oct 15–16, Georgetown University Capitol Campus, Washington D.C.)**; CSS/BWS (Oct 19–23) | Committee seated; chairs elected; metric register v0 → v1; scheme scope rulings; open questions assigned |
| **W3 Testbed** | Nov 2026 | CSS/BWS drafting output | Harness interface and result schema adopted; reference CPU class and block mix decided; COI policy adopted; node call issued |
| **W4 Rubric & call text** | Dec 2026 | **SSR co-located PQC workshop (Dec 13, Baltimore)** | Rubric v1; "PQC-ready chain" definition v1; call-text input package delivered to the host |
| **W5 Pilot** | Jan 2027 | Applications open (planned) | Pilot nodes running reference runs; reproduction tolerance calibrated; rubric v1.1 |
| **W6 Retrospective** | Feb 2027 | CoDecFin 2027 at FC'27 (Feb 8–12, Barbados; proposed special area *PQC Migration, Evaluation, and Crypto Agility*) | Phase A retrospective; continuation confirmed; BGIN Standard outline v0 |

### Nearest anchors

**BGIN Block 15**, Georgetown University Capitol Campus (111 Massachusetts Avenue NW), Washington D.C., 15–16 October, hybrid. PQC keynote 15 Oct 09:20–09:50; IKP PQC migration sessions 09:50–11:20 and 11:30–13:00. The first session takes resource estimates and the ECDSA.fail community's numbers into judging criteria; the second takes crypto agility as a governance property and the NIST signature migration path, with NIST participation. That is where the committee is seated and the scheme rulings are argued — the session to attend if only one is possible. Event page and registration: https://bgin-global.org/events/20261015-block15 · https://www.eventbrite.com/e/bgin-block15-tickets-1990274282957 (fee waivers for written contributions presented at the meeting; submissions close about a week before).

**SSR 2026 co-located PQC workshop**, Baltimore, 13 December (working date). The formal call-text window, and where the "PQC-ready chain" definition the GDC26 report names as a December deliverable has to exist.

### Between workshops

Discussion in this category; the record in pull requests; rulings in decision records. Conveners post a short status here after each session with a link to the record. Nothing is decided in a thread — a thread is where the argument happens and the repository is where the outcome lands.

### The path

```
Competition / evaluation → BGIN Standard → ISO (ISO/TC 307, BGIN Category A liaison) → Japan crypto-asset security criteria
```

The workshops are the first arrow. The reason the metric units and the reference configuration get argued about this hard, this early, is the second one: a metric that is not standards-ready does not survive the trip.
```


---

## Step 4 — committee nominations

**Where:** new topic in category 44.

**Title:** `Evaluation committee: nominations are open`


```markdown
Nominations are open for the evaluation committee of the PQC Migration Prize. Nominations are collected now; nothing is decided until W1 ratifies the composition table, and seats are filled at W2.

**How:** the *Committee nomination* issue template at https://github.com/bgin-global/pqc-agility-competition/issues/new/choose, or a reply here and it will be carried over.

### What the committee does

Two evaluation tracks, following the NIST-style split named in the GDC26 report:

- **Theoretical security review** — assumptions, parameter choices, composition (hybrids, aggregation, ZK wrapping), key-management risk, side-channel posture, migration-window threat model. Written review against a checklist; no testbed run needed.
- **Implementation and performance** — measured cost and behaviour on the neutral testbed, reproduced across nodes.

Both tracks need people. So does the work before either starts: the metric register, the rubric weights, and the scheme scope rulings are committee decisions, and they happen in the next three months.

### What is being looked for

The composition table in `GOVERNANCE.md` §3 is a draft: 12–18 seats across academic cryptography, protocol engineering on Bitcoin and Ethereum, wallet and custody, measurement and testbed operations, and standards. It is a draft, and arguing with it is a legitimate way to respond to this post. The quorum rule is open too.

Self-nomination is normal and expected.

### What a nomination involves

A nomination records the lane proposed, relevant experience, and declared interests. Anyone seated files a conflict-of-interest disclosure before taking part in evaluation work — the policy is public at `evaluation/COI_POLICY.md`; the disclosures themselves are not.

That is the general shape: **decisions are published, deliberation is not.** A seated member's roster entry carries only what that person agreed to publish, which is asked at nomination. The fact that a member recused, and what from, is published; the disclosure behind it is not. Nominations that are declined are kept on the record with the reason, because a competition that discards that record cannot show it was neutral.

### Conveners

Conveners are named on ratification at W1. That is one of the things W1 is for. Before W1, one seat is needed immediately: a **second convener with a signing key**, because the repository's review rule (a code-owner approval that is not the author's, no bypass) means a single convener cannot merge anything — including the committee's own nominations. Setup is `docs/SIGNING.md` §1–3; it takes an afternoon.

Names for the two track leads — theoretical security, implementation and performance — are the next ask, and nominations for them are read first.
```


---

## Step 5 — metrics and scheme scope

**Where:** new topic in category 44.

**Title:** `Metric register v0 and the scheme scope rulings: comment before W2`


```markdown
Two draft documents are open for comment ahead of W2 (mid-October, around Block 15).

- **`evaluation/METRICS.md`** — 22 candidate metrics. Every row is `candidate` until the committee adopts or parks it. A metric without units, method and target mapping is not adoptable, so incomplete rows are the useful thing to attack.
- **`testbed/SCHEMES.md`** — five post-quantum signature schemes (ML-DSA, SLH-DSA, FN-DSA, XMSS/XMSS^MT, LMS/HSS), classical baselines measured for the deltas, and six composition and integration paths.

https://github.com/bgin-global/pqc-agility-competition/tree/main/evaluation

### The scope rule

Only pre-existing NIST-class schemes are in scope. The competition is not selecting new primitives. Every *integration path*, though, is an explicit committee ruling rather than a default — `C-01` hybrid classical + PQ, `C-02` the Bitcoin P2QRH / BIP-360 direction, `C-03` the Ethereum account-abstraction path, `C-04` consensus-layer BLS to hash-based aggregation, `C-05` ZK-wrapped verification, `C-06` advanced key management. Each needs a decision record with reasons. Arguments for and against any of the six are directly useful now.

Two known soft spots: FN-DSA is carried as FIPS 206 in draft status and the status needs confirming at the ruling; and the Ethereum consensus direction is heading toward XMSS-style hash-based aggregation with Poseidon2 for ZK-friendliness, which is not an SP 800-208 parameterisation — whether that is in scope is a ruling, not a detail.

### Six open questions

Carried from the IKP-WG discussion, all assigned at W2:

1. Is the headline quantity total overhead, or migration speed?
2. Who must upgrade first — node operators or users — and how does a metric reflect the burden split?
3. How is the legitimate-owner-versus-attacker race scored during a migration window?
4. Which reference CPU class, and which reference transaction mix or block, anchor the cost metrics?
5. Are consensus-layer and user-level evidence scored on one rubric or two?
6. Which of the GDC26 attack classes does each metric defend against — on-spend (in flight), at-rest against on-chain keys, or on-setup (a universal exploit manufactured once, before any attack)? The taxonomy is the one in *Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations* (PRX Quantum 7, 031001, https://doi.org/10.1103/j3xf-bw18), which the GDC26 scene-setting was built on.

Question 4 in particular is a decision somebody has to make concretely, and it will be made better with implementers in the thread than without.

### Three September releases that bear on the rulings

Named on the 10 September IKP call; each lands on a specific row rather than on the debate in general.

- **Project Eleven — [key recovery from state reuse](https://www.projecteleven.com/blog/key-recovery-from-state-reuse).** Stateful hash-based signatures (XMSS/XMSS^MT, LMS/HSS — `S-04`, `S-05`) carry an operational failure mode, not only a cryptographic one: sign twice from one state and the key is exposed. The scheme rows already flag state management as the operational risk; this is the demonstrated failure behind that flag, and the Poseidon2-XMSS ruling inherits it.
- **a16z crypto — [Lattice Jolt](https://a16zcrypto.com/posts/article/lattice-snarks-jolt-post-quantum-faster/).** A post-quantum zkVM on a Module-SIS lattice commitment (the ML-DSA / ML-KEM assumption family), proofs under 100 KB. `C-05` ZK-wrapped verification and `M-16` stop being hypothetical and become measurable.
- **[ProveKit](https://provekit.org/)** (World, Atheon, Reilabs, Nethermind). Client-side proving on the phones people own — seconds on recent hardware, under 30 s on a 2 GB Android. Bears on wallet-side verification cost and on where the user-level (`ETH-user`) burden actually falls.

### Anchoring

Comparative evaluation anchors on Bitcoin and Ethereum: `BTC-tx` transaction-level, `ETH-user` user-level, `ETH-cons` consensus-layer. Other-chain and general-purpose work is in scope where its results map to that evidence. This is a measurement decision, not an endorsement — BGIN is ecosystem-neutral and the anchoring is there so numbers can be compared at all.

Comment here, or use the *Metric proposal* and *Scheme proposal* issue templates.
```


---

## Step 6 — testbed node hosts

**Where:** new topic in category 44.

**Title:** `Testbed: expressions of interest for node hosting`


```markdown
The neutral evaluation testbed is what separates this competition from a paper exercise, and it needs hosts. The formal node call is a W3 output (November); this is the expression-of-interest stage, so that W3 starts with a map instead of a blank sheet.

**Offer a node:** the *Node host offer* issue template at https://github.com/bgin-global/pqc-agility-competition/issues/new/choose, or a reply here.

### Shape

The IKP-WG discussion started from ten nodes over six months; the current specification says on the order of 10–15 nodes, multi-region, running over multiple months. What matters is not the count but the two properties the count is a proxy for: **geographic and organisational distribution**, and **reproduction** — the same run, on different hardware in different jurisdictions, agreeing within a stated tolerance.

Reproduction tolerance is calibrated during the W5 pilot with three to five nodes. That calibration is the difference between a number and evidence.

### What hosting involves

- Running the harness described in `testbed/HARNESS.md` against a fixed result schema (`testbed/schema/result.schema.json`).
- Reporting results in that schema, reproducibly, on a schedule.
- Accepting that results tied to a named operator are handled as confidential and that what gets published is the aggregate that identifies no one, unless the operator agrees otherwise.

Both the harness interface and the result schema are draft and adopted at W3. An operator who reads the harness spec now and says what is unworkable is more useful than one who says yes to it as written.

### Open, and better answered by hosts than by conveners

The reference CPU class and the reference transaction mix are undecided — open questions 4 in the metric register. So is the block mix that the per-block overhead metrics anchor to. These are the parameters that decide whether numbers from different nodes can be compared at all, and the people who will actually run the machines should set them.

### Neutrality

Node hosts are not applicants. The testbed measures; it does not compete. Where a host has an interest in an applicant or a scheme, the conflict-of-interest policy applies to the measurement seat as it does to the review seats.
```


---

## Step 7A — reply: A. On the [IKP Post Quantum Cryptography thread 06/26](https://bgin.discourse.group/t/ikp-post-quantum-cryptography-thread-06-26/1001)


```markdown
The crypto-agility competition work now has its own category — **Post-Quantum Crypto Agility Competition** — and a working repository at https://github.com/bgin-global/pqc-agility-competition.

Committee nominations, the metric register, the scheme scope rulings and the testbed node call all move there. This thread keeps its role as the IKP PQC archive: papers, talks, trackers, and the general migration discussion.

Three things open now: committee nominations, comment on the 22 candidate metrics and the six integration-path rulings, and expressions of interest for testbed nodes. All three have issue templates in the repository.
```


---

## Step 7B — reply: B. On the [GDC26 meeting report thread](https://bgin.discourse.group/t/gdc26-meeting-report-published-post-quantum-cryptography-migration-on-dlts/1045)


```markdown
Following the report's invitation for definitional proposals and evaluation-committee participation: both now have a home. The **Post-Quantum Crypto Agility Competition** category carries the competition work, and the repository at https://github.com/bgin-global/pqc-agility-competition carries the record.

The report's two evaluation axes — theoretical security and implementation efficiency — are the frame the metric register is built on, and the "PQC-ready chain" definition it names as a December deliverable is targeted at the SSR co-located workshop on 13 December.

One discrepancy worth flagging rather than quietly resolving: the report targets winner selection for March 2029, while the July community briefing says mid-September 2028. Both are provisional and the host's call text settles it. The repository carries both, attributed.
```


---

## Step 7C — reply: C. On the [IKP Post Quantum Cryptography thread 06/26](https://bgin.discourse.group/t/ikp-post-quantum-cryptography-thread-06-26/1001) — resource reply


```markdown
For the archive: the scene-setting at the GDC26 PQC session was Google Quantum AI's *When ECC and RSA Break: Urgency of Migrating to Post-Quantum Cryptography*, built on *Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations* — PRX Quantum 7, 031001, published 21 August 2026, open access at https://doi.org/10.1103/j3xf-bw18 (also arXiv 2603.28846). The on-spend / at-rest / on-setup attack classes and the secp256k1 resource estimates in it are what the competition's metric register cites for its sixth open question.

The slides are on the BGIN website beside the meeting report: https://bgin-global.org/documents/meeting-reports/gdc26/GDC26_PQC_Migration_DLTs_Slides_GoogleQuantumAI.pdf

The meeting report and the BGIN session deck remain at https://bgin-global.org/news/260903-gdc26-pqc-migration.
```


---

## After posting

- Website: the hub's filled *Work on Discourse* button and the *Competition category on Discourse ↗* links land on the category (site PR `pqc-migration-hub-block15`, staged in `~/bgin-homepage-fork`).
- Repository: `README`, `GOVERNANCE §7`, `CONTRIBUTING`, `SUPPORT`, `resources/README` point at the category (commit `4bd887b` on `docs/communication-channels`, PR #3 — push to update the PR).
- Post a one-line reply on the 10 Sep call thread (1048) only if useful: *the competition category is open — [link]*.
