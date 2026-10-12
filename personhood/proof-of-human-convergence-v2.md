# Proof of Human: Overlap and Convergence Analysis

**Status:** Working note v2 for discussion
**Prepared for:** BGIN IKP Working Group and World Foundation
**Date:** August 2026
**Author:** [Mitchell Travers — privacymage] · Co-chair, BGIN IKP Working Group

*The author is also **co-chair of the DTG ZKP Task Force**, a task force of the ToIP Decentralized Trust Graph Working Group (DTGWG) at Linux Foundation Decentralized Trust. Observations about DTGWG work here are personal and drawn from public materials only — the published Credentials Core Specification, the published proof-of-liveness requirements v0.3, the published drafting rules, and open discussions on the public task force repository. They are not positions of the DTGWG, the ZKP Task Force, ToIP, or BGIN.*

*Revision note (v2): corrects v1, which assessed the World Foundation framework against the DTG **Credentials** specification alone and treated the DTG **ZKP Task Force** as an empty downstream consumer. The ZKP Task Force has published predicate semantics that already occupy part of the layer v1 offered to World Foundation. Sections 1, 2, 3.2, 4.1–4.4, 5.1–5.3, 7, 8, 9 and Appendix A are revised accordingly. The convergence finding is unchanged and, properly stated, stronger.*

---

## 0. Why this note exists

Three efforts are converging on the same problem from three directions, and they are not yet in contact with each other's current work.

- **World Foundation** has drafted a *Proof of Human Conceptual Standards Framework* (v0.13, 13 August 2026) defining ten assurance categories with a four-dimension decomposition.
- **ToIP DTGWG** works across two relevant workstreams. The **Credentials** workstream published *DTG Core Credentials V1.0, Working Draft 01*, defining six normative W3C VC types that construct and annotate a decentralized trust graph. The **ZKP Task Force** published *Privacy-Preserving Proof of Liveness — Requirements* v0.3, which defines predicate semantics, a per-predicate disclosure column, and an explicit assurance boundary for the proof layer the Credentials spec deliberately leaves open.
- **BGIN IKP** is preparing its proof of personhood paper toward Block 15 (Washington DC, October 2026) and publication at Block 16, with a stated ambition to reach formal standards venues.

These efforts arrived at compatible structures independently, and that is worth stating plainly at the outset: independent convergence is the strongest available evidence that the problem is real and that the way these efforts are cutting it is sound. It is also a reminder of how quickly parallel work can drift apart without an explicit map between the layers.

*A note on chronology, since v1 leaned on it too heavily.* The Credentials specification carries a generator build stamp rather than a publication date, and its Working Draft 01 content was in place well before that stamp. The convergence claim therefore rests on **structural correspondence**, not on a coincidence of dates. That is the more durable claim in any case, and it is the one this note makes.

This note is that map. It identifies where each effort is strongest, where they reinforce each other, where the seams need work, and which gaps remain unclaimed by anyone. The aim is a division of labour, not a ranking.

A framing point that runs through the whole analysis: a taxonomy whose categories land on existing standards is **succeeding at its stated aim**. Common semantics across a mature ecosystem is the goal; novelty for its own sake would be the failure mode. The question worth asking of the Proof of Human framework is not how much of it is new, but whether it makes the existing pieces composable — and on that test it does real work.

A second framing point, added in v2: the same test must be applied in both directions. Where the DTG ZKP Task Force has already published predicate semantics, a parallel World Foundation vocabulary would be a **second** vocabulary for the same object — which is the failure mode this note exists to prevent. Section 4 is revised to state precisely which parts of the framework are additive and which must land inside existing DTG structures rather than beside them.

---

## 1. The layers

The clearest way to see the relationship is as a stack. Each effort occupies a different layer, and the friction is almost entirely at the seams. v1 collapsed two distinct semantic layers into one; they are separated here, because the distinction is where the division of labour actually falls.

| Layer | Question it answers | Who is working here |
|---|---|---|
| **Assurance semantics (cross-ecosystem)** | What class of claim is this, at what strength, on what class of evidence, and how does that map onto other ecosystems' scales? | WF Proof of Human taxonomy; NIST xAL and ISO 29115 as the vocabularies it must map onto |
| **Predicate semantics** | What proposition does a proof establish, what does it explicitly *not* establish, what does it disclose, to whom, against which adversary, for how long? | DTG ZKP Task Force — requirements v0.3; v0.4 draft under discussion; Predicate & Assurance-Boundary decision document in preparation (v0.3 §14) |
| **Mechanism** | What credential, protocol and proof construction carries the claim? | ToIP DTG Core Credentials WD01; First Person Network |
| **Formal security** | What does the claim provably guarantee against a defined adversary? | Adler et al. (2024); *A Cryptographic Framework for Proof of Personhood* (ePrint 2026/333) — adopted as the ZKP Task Force's normative reference |
| **Governance & policy** | Who may assert this, within what domain, under what regulatory consequence? | BGIN IKP; ToIP Governance Metamodel; trust registry frameworks |

**The convergence thesis (revised):** the WF taxonomy is most valuable as a **cross-ecosystem assurance-semantics layer** that populates fields the DTG ZKP predicate semantics already reserve — assurance class, policy identifier, accreditation reference — carried by DTG mechanisms, formalised against ePrint 2026/333, and governed through BGIN and ISO. Published standalone it becomes a fourth competing vocabulary. Published as a layer, bound to the predicate register beneath it, it becomes the thing that makes the others interoperable.

The distinction matters practically. "WF supplies the semantics layer" is false as an unqualified claim, because the ZKP Task Force publishes predicate semantics. "WF supplies the assurance-class vocabulary those predicates disclose, and the mapping to NIST and ISO scales" is true, additive, and unclaimed.

---

## 2. Category-by-category convergence matrix

WF's ten assurance categories, mapped against DTG normative and published draft content. The DTG column now covers both workstreams; v1 covered only Credentials, which produced three false gap findings. The right-hand column records where each layer is load-bearing — not a scoring of originality.

| # | WF category | DTG position (Credentials WD01 · ZKP TF v0.3) | Where the value sits |
|---|---|---|---|
| 1 | **Identity assurance** | **Cred:** IDVCs explicitly *not* DTG credential subtypes. Any W3C VC satisfying a VTC/VTN's identity-proofing requirement. Issuers, assurance levels and requirements delegated to VTC/VTN policy and trust registries. **ZKP:** the biometric provider's signed determination is a defined input contract. | **Deliberate gap in Credentials.** WF fills it — but with NIST/ISO material, so the contribution is the bridge, not the content. |
| 2 | **Humanity assurance** | **Cred:** a PHC is a VMC issued by a VTC whose governance enforces real human personhood. No additional schema fields; optional `PersonhoodCredential` type string explicitly non-authoritative. **ZKP:** decomposed into two predicates — liveness-attestation possession and personhood-policy satisfaction — each with a stated negative meaning. | **Strong convergence, with a caution.** DTG carries the mechanism. WF's strength vocabulary is wanted — but "humanity" is not a single predicate on the DTG side, so a single ordinal for it will not bind. See §4.1. |
| 3 | **Uniqueness assurance** | **Cred:** same PHC construct: exactly one membership per person, scoped to the issuing VTC. VTN-level policy may enforce network-wide qualification. **ZKP:** narrowed to *scoped reuse detection* — a nullifier over enrolment root, scope, purpose and epoch; three distinct uniqueness claims on an explicit Sybil/unlinkability **trade curve**, of which only the first is cryptographic. | **Strong convergence, and the sharpest correction available to WF.** "Unique within a declared domain" must be parameterised by context, scope, purpose *and* epoch — not by ecosystem. See §7. |
| 4 | **Credential control assurance** | **Cred:** standard W3C VC proof verification, DID resolution, verification-method validation; key compromise in Security Considerations. **ZKP:** holder binding proves key control and explicitly does **not** establish non-transfer of the key or agent authority. | Covered by baseline VC machinery, with the negative space already written on the ZKP side. No conflict, no novelty. |
| 5 | **Human presence assurance** | **Cred:** VWC attests conditions of edge formation — both parties at the same event, or proof of biometric liveness at the time of relationship formation. `witnessContext` carries event, sessionId, method. Bound via `taskContext` and a JCS-canonicalised SHA-256 digest. **ZKP:** freshness binds a canonical transcript, not a bare nonce. | WF states the principle; DTG has a working implementation on both sides. WF can cite it as an existence proof that the category is implementable. |
| 6 | **Human continuity assurance** | **Cred:** nothing. M-DID reuse is *intentional correlation*, not continuity; no enrolment-anchor primitive. **ZKP:** claimed. "Same-human-as-enrolment" is a named predicate of the Extended Personhood Profile, appears as a required predicate for the login/re-authentication context, and the enrolment root/population is a mandatory nullifier input; enrolment controls are an open question. | **Not a joint gap** — v1 was wrong here. The predicate is claimed at the proof layer. The two real gaps are a *credential-layer carrier* and the *governance of enrolment controls* that determines what the predicate is worth. See §4.3. |
| 7 | **Attribute assurance** | **Cred:** IDVC and VEC, both explicitly outside normative scope. Endorsement vocabulary defined by VTC/VTN. **ZKP:** demographic range is an explicit **extension**, not core. | Complementary. ISO 27551/27565/27566 already own the privacy-preserving side. |
| 8 | **Role assurance** | **Cred:** trust registries are the authoritative source for roles, mapping DIDs to roles and policies. Open editor's question on whether role/access-control data belongs in the VIC. | Partial. WF's role semantics could inform an open DTG question — a concrete entry point. |
| 9 | **Action assurance** | **Cred:** out of scope. Planned *DTG Core Trust Task Protocols* covers offer/issue/request/present/revoke of credentials, not human approval of an external transaction. **ZKP:** named as a non-establishment — holder-key control is not consent or human intent, and conflating them is on the ruled-out list. | **Still a gap, but a named one.** Nobody establishes it; the ZKP side has at least fenced it. The unclaimed work is the governance and liability framing. |
| 10 | **Agent authority assurance** | **Cred:** DTG nodes include AI agents; a VTA may represent an agent. An **Agent card** VDS modelled on the A2A AgentCard is planned but unpublished. **ZKP:** delegation is claimed as in scope and specified as *separate structured evidence* carrying principal, agent, scope, duration and revocation; two agent contexts are enumerated — day-zero authorisation, and step-up on intent drift, new permission or new environment. | **Co-authorship, not a vacuum** — v1 was wrong to call this an empty vessel. The field list exists. WF's contribution is what is missing from it, and the governance of who may delegate. See §4.4. |

**Summary (revised):** four categories map onto mature standards work — which is the point, since those are the categories where common semantics is most needed and least available. Three converge closely with DTG, where the layers are complementary rather than competing. One — action assurance — remains a genuine gap on all sides, though the ZKP work has fenced it as a non-establishment. Two — continuity and agent authority — were reported as gaps in v1 and are not: both are claimed at the DTG proof layer, and the available contribution is joint work inside an existing structure rather than a new work item. One — role assurance — is an open editor's question the WF semantics could answer directly.

---

## 3. Where DTG has already built the mechanism

Three places where the WF draft states as principle something DTG has expressed in normative text. In each case the framework gets stronger by citing the implementation rather than restating the principle — it turns an assertion into a demonstrated capability.

### 3.1 The credential/artifact boundary

DTG applies an explicit test: a **credential** is a durable claim about the graph that is true standing alone and outlives the exchange; an **artifact** is a work-product of a trust task, meaningful only inside its exchange, correlated by `threadId`, with terminal state expressed at the trust task layer.

WF's *human presence assurance* and *action assurance* fall on the artifact side of that line. The draft does not say so. If it ships as written, implementers will attempt to mint presence credentials — precisely what DTG designed against, with **context collapse** named as an attack class in Security Considerations and a normative rule that a verifier must not treat a `taskContext`-bearing credential as proof of ceremony completion unless matching outcome evidence is present and verified.

**Recommendation:** WF section 2.5 (temporal and contextual scope) should cite the DTG boundary test directly and classify each of its ten categories as durable or task-bound.

### 3.2 Linkability scope — adopt the architecture, but parameterise the dimension

The disclosure/linkability dimension the WF framework lacks has a partial answer in the Credentials spec, expressed as four identifier types:

| Identifier | Scope | Correlation property |
|---|---|---|
| **R-DID** (relationship) | Pairwise, one per counterparty (normative MUST) | Unlinkable beyond the two peers |
| **P-DID** (persona) | Holder-asserted persona | Intentional, holder-controlled correlation |
| **M-DID** (membership) | Per-VTC, may be reused across VTCs by choice | Deliberate cross-community correlation |
| **C-DID** (community) | Public community identifier | Fully public |

DTG's Privacy Considerations state the governing rule: correlation across relationships should occur **only** through the holder's deliberate assertion of a persona or M-DID, never as a side effect of credential structure. Implementations should make ZKP presentation the default so privacy does not require opt-in.

**Recommendation (revised).** WF should adopt this as the **identifier-layer instantiation** of a fifth dimension — *disclosure profile* — rather than inventing a parallel model. But the dimension itself must not be a fixed four-point taxonomy, and v1's recommendation was under-specified on exactly this point.

The reason is a rule the ZKP Task Force has publicly adopted: **every privacy claim names its adversary, and every privacy claim names its horizon.** A four-value enumeration cannot express "unlinkable against a colluding issuer and verifier, for epoch E" — and per ePrint 2026/333, full unlinkability is not reachable alongside Sybil resistance, so an unparameterised linkability label will overstate what it delivers. The dimension therefore needs to carry, at minimum: the **context** the claim is scoped to, the **epoch** over which it holds, and the **adversary** it holds against — with the four DID types as the concrete identifier-layer realisation.

Stated that way this remains the most persuasive available evidence that WF is building on the DTG work rather than around it, and it now also satisfies the drafting discipline the receiving group applies to itself.

### 3.3 Verifiability vs. truth

DTG's VEC definition draws the distinction in one sentence: verifiability applies to cryptographic assurance in the issuer's signature, not to the truth of the assertions, which must be evaluated independently. That is the category/strength separation WF argues for across several pages, already stated compactly and normatively — and stated again, in assurance-boundary form, in ZKP requirements v0.3.

---

## 4. Where WF genuinely adds value

Five contributions. Three are revised from v1, where the value was correctly identified but mislocated: the framework's contribution is narrower and lands *inside* existing DTG structures rather than filling empty ones. Narrower and load-bearing is a stronger position than broad and displaced.

### 4.1 Strength expression — the headline gap, correctly located

The **Credentials specification** has no vocabulary for assurance strength. A VMC from a local chess club and a VMC from a government identity-verification provider are structurally identical; PHC qualification is a governance determination carried in a trust registry, in prose. There is no way for a verifier to programmatically distinguish weak from strong personhood, and no way for a VTC to declare its identity-proofing requirement in a portable form. The DTGWG has surfaced this internally — task force discussion has flagged the spread from a local sports league to personhood trusted by major platforms as an unresolved design question.

**What v1 got wrong:** it reported this as an absence across DTG. It is not. ZKP requirements v0.3 already states, per predicate, that the disclosure to the verifier is *assurance class, policy version, accreditation framework* — and it already allocates assurance to the accreditation layer rather than the cryptography: the cryptography carries the privacy, the accreditation framework carries the assurance. A WF strength vocabulary therefore arrives **second**, into fields that already exist.

**What follows.** The contribution is not the existence of a strength dimension; it is the **content** of one — a portable, cross-ecosystem vocabulary of assurance classes and evidence classes that can populate `assurance class` and `policy identifier` where the DTG proof layer already discloses them, together with the mapping to NIST xAL and ISO 29115 that neither DTG workstream will produce. Delivered that way it is additive. Delivered as a standalone strength model it collides with the attestation-schema work and becomes a second vocabulary for one field.

Two constraints the framework must respect, both public:

- **It cannot be a single ordinal for "humanity".** On the DTG side humanity decomposes into liveness-attestation possession and personhood-policy satisfaction, which have different negative meanings and different accountable parties. Strength attaches per predicate.
- **It cannot be a maturity ladder.** v0.3 states the Sybil/unlinkability relationship as a **trade curve**, not a ladder: stronger deduplication is bought by spending unlinkability, and "the strongest one we can implement" is explicitly not an available strategy. A scale implying that higher is uniformly better contradicts a constraint the receiving group has already accepted.

**Prior art worth borrowing from:** Common Criteria Protection Profiles and Security Targets solve a structurally identical problem in a different domain — expressing "what assurance, at what level, against what threat model" in a portable, evaluable artifact, with profiles authored by communities of interest rather than by the standard itself. BGIN's wallet security assurance work (ST/PP and convergence) is already engaged with this from the wallet side. A trust registry publishing something PP-shaped for its personhood governance would give WF's strength dimension a concrete carrier and give DTG verifiers something machine-processable. This is a stronger move than inventing a new levels scheme, and it connects two BGIN workstreams that are currently separate. Unchanged from v1, and still the best single idea in the note.

### 4.2 Separating humanity from uniqueness

The Credentials spec bundles both into one credential as two governance conditions on a VMC. But a relying party may legitimately want one without the other: a forum may need humanity without one-per-person; an airdrop needs uniqueness and may not care about civil identity at all. WF splitting these into independently requestable predicates is a real improvement and maps cleanly onto ZKP predicate design.

Note that the ZKP work has already made this split at the proof layer — liveness, personhood policy and scoped uniqueness are three separate predicates with three separate negative meanings. WF's contribution is therefore **agreement that reinforces an existing split**, plus the argument for carrying it up into the credential and governance layers where it has not yet been made. Worth saying explicitly: convergent independent derivation of the same split is evidence, and it is cheap to cite.

### 4.3 Continuity — the carrier and the controls, not the primitive

**What v1 got wrong:** it called continuity a gap neither body had addressed, and proposed it as the best single new work item. At the proof layer it is claimed. "Same-human-as-enrolment" is a named predicate of the Extended Personhood Profile, it appears as a required predicate for the login/re-authentication context, and the enrolment root/population is a mandatory nullifier input.

**What is actually missing** — and these are real:

1. **A credential-layer carrier.** The Credentials spec has no enrolment-anchor primitive, and M-DID reuse is intentional correlation rather than continuity. A predicate with no credential to stand on cannot be requested through the DTG credential flow. This is a concrete, filable Credentials issue.
2. **The governance of enrolment controls.** The ZKP requirements ask, as an open question, what enrolment controls are needed to support the second point on the trade curve and how strong a guarantee they give. The answer is not cryptographic — it is re-enrolment resistance, recovery and exception rules, issuer coordination, and deduplication quality. That is a governance and accreditation question, which is BGIN's competence and explicitly not the ZKP Task Force's.
3. **A reference-event model** that names what continuity is measured *from*, which the WF draft supplies and neither DTG document does.

Reframed this way it is a better contribution than v1 claimed, because it is joint work with a named counterpart rather than a new work item competing for the same ground.

### 4.4 Agent authority semantics — the field list exists; complete it

**What v1 got wrong:** it described the planned DTG Agent card as an empty vessel with nothing written yet and nothing to displace, and recommended entering there because the door was open. The door is open, but the room is not empty. ZKP requirements v0.3 specifies agent authorisation as "separate, structured delegation evidence (principal, agent, scope, duration, revocation)"; establishes that key control is not agent authority; enumerates two agent contexts — day-zero authorisation and step-up on intent drift, new permission or new environment; and states that delegation is probably in scope for the task force because the cryptographic literature reaches this point and stops.

**What follows.** WF's category 10 should be checked *against* that list rather than offered *into* a vacuum. On a reading of both, the plausible additions are:

- **conditions and limits** — value ceilings, rate limits, environment constraints — which the current list does not carry;
- **step-up requirements** as structured data rather than a described context;
- **evidence that the current action is covered** by the delegation, which is the predicate a verifier actually needs and the hardest one to express;
- **escalation and revocation-propagation** semantics;
- and the governance question underneath all of it: **who is permitted to delegate what**, which no cryptographic layer can answer.

The Agent card remains the lowest-friction entry point, and it remains true that nothing is yet published there. The correct framing is co-authorship with a task force that has already staked the ground — not occupation of empty space. Getting this wrong in a note that will be read by that task force is a needless cost.

### 4.5 Bridging to formal standards vocabularies

DTG is a Linux Foundation JDF deliverable; ISO and NIST are separate universes. Someone has to write the mapping that lets a VTC governance framework state its requirements in 29115 or 800-63-4 terms. Nobody currently is. Unchanged from v1, and now the clearest single instance of the §4.1 pattern: the contribution is the bridge, and the bridge is unclaimed.

---

## 5. Gaps nobody owns

These are the strongest candidates for BGIN IKP work items, because they are unclaimed by ToIP, unaddressed by NIST, and directly in BGIN's competence. Three are revised where the ZKP work has partially claimed the ground.

### 5.1 Coercion, duress and credential rental

A human can be present, live, unique, continuous with enrolment and cryptographically flawless — and still be operating as a rented proxy for an AI system or a farm operator. Every deployed personhood system faces this.

**Revised from v1**, which called this an unnamed failure mode with no vocabulary on either side. It is named on the DTG proof layer, as an explicit non-establishment: the ZKP requirements separate key control from non-transfer and from agent authority, and place "conflating holder-key control with human continuity or agent authority" on the ruled-out list. The Credentials spec has nothing.

**The substantive point survives intact, and it is important:** naming coercion as something a proof does not establish is not the same as having vocabulary for the risk, allocating liability, or telling a relying party what to do about it. Fencing is not treatment. Any humanity or uniqueness claim made without this caveat **overstates what it delivers**, and this should be an explicit limitation section in any taxonomy rather than an afterthought.

It is a governance and economics problem more than a cryptographic one, which is why BGIN is the right venue — and the ZKP Task Force has formally disclaimed the adjacent layer, stating that accreditation frameworks are depended on but not defined by it. That disclaimer is better evidence for BGIN's role than an assertion of a gap, and it should be cited rather than argued.

### 5.2 Threat model per assurance category

For ISO SC 27 to take a taxonomy seriously it needs an adversary column: Sybil (uniqueness), injection and deepfake (presence), enrolment poisoning (continuity), credential theft (control), duress (action), farming (uniqueness + continuity). Conformance cannot be evaluated against a claim whose adversary is unstated.

**Revised from v1:** the discipline this asks for already exists in public, adopted form, and does not need proposing. The DTG ZKP Task Force's published drafting rules require that every privacy claim names its adversary — verifier, issuer, or the two colluding, which are three different specifications — that every claim names its horizon, that every predicate states what it does not establish, and that conjecture is labelled as conjecture. They exist to prevent one specific failure: a specification whose privacy claims are unfalsifiable.

The work item is therefore not the discipline but its **application**: running WF's ten categories through it and producing the adversary-and-horizon column per category. The template is published and citable, which makes this cheap to do and hard to argue with. *(Disclosure: those rules were proposed by the author of this note and adopted by that group; they are cited here as published material, not as a personal position.)*

### 5.3 Governance of the domain

"Unique within a declared domain" is only meaningful if someone is authorised to declare and govern the domain.

**Narrowed from v1.** The Credentials spec answers the structural question (VTC governance, VTN trust anchors, trust registries), and the redress and appeal path is in scope for the Predicate & Assurance-Boundary decision document the ZKP Task Force has committed to drafting — so it should not be reported as unowned. What remains genuinely unanswered, by any document in either workstream, is the **institutional** question: **who accredits a VTN?** What happens when two VTNs disagree about the same human? On what authority does a context authority hold its mandate, and who supervises it? That is a political and regulatory question, it is unclaimed, and it is BGIN's.

### 5.4 Regulatory interface

The AML/CTF, sanctions and travel-rule interaction with pseudonymous uniqueness is unexamined in both documents. A personhood credential that is unlinkable by design and a sanctions-screening obligation that presumes identifiability are on a collision course. **This is BGIN's sharpest comparative advantage** and the part neither ToIP nor World Foundation will produce. Unchanged from v1, and the strongest item in the note.

### 5.5 The global registry harms case

A uniqueness assertion that survives across domains is a correlation key. The harms analysis — exclusion, coercion by states, irreversibility of biometric enrolment, function creep — belongs alongside the technical work, not after it. DTGWG has a Risk Assessment and Harms Prevention Task Force; BGIN can bring the regulatory and political-economy dimension it lacks.

---

## 6. Terminology reconciliation

Collisions to resolve before any joint publication. Every WF term should be checked against the DTG Glossary, the ToIP main glossary, and the ZKP requirements vocabulary.

| Term | Current conflict | Proposed resolution |
|---|---|---|
| **context** | WF uses it as one of four dimensions. Credentials has `taskContext` with precise normative meaning, plus "context collapse" as a named attack. The ZKP work treats *context* as the governed linkability domain that parameterises every construction — its open foundational question. | WF should rename its dimension (e.g. **scope**), and must not use *context* for a linkability boundary without the parameters §7 sets out. This is now the highest-risk collision of the five. |
| **domain** | WF's "declared domain" for uniqueness scope. Credentials has VTC and VTN with formal definitions; the ZKP work scopes uniqueness by context, scope, purpose and epoch — explicitly not by ecosystem. | Do not introduce a parallel term, and do not equate a declared domain with a VTN. See §7. |
| **VTC** | Verifiable Trust *Community* (DTG Glossary) vs. Verifiable Trust *Circles* (Herman, IETF draft). Pre-existing collision inside ToIP. | Flag to DTGWG; avoid the acronym in cross-body documents until resolved. |
| **credential control** | WF category name vs. DTG/SSC controller layers (beneficial, intermediate, technical). | Align, or state the relationship explicitly. |
| **assurance strength** | WF term. NIST uses xAL; ISO 29115 uses LoA. The ZKP work discloses *assurance class* and *policy version*. | Define the mapping in a normative annex rather than a third scale, and align the field name with the disclosure the proof layer already makes. |

---

## 7. The ZKP seam

This section is substantially rewritten. v1 described the seam correctly and then expressed it in a form the published ZKP requirements rule out. The corrected version is more useful, because it is the form the receiving task force can act on.

### 7.1 What the Credentials spec provides

DTG WD01 is deliberately **format-agnostic** — no binding to BBS+, SD-JWT-VC or any specific scheme — and defines two proof constructions:

1. **Pairwise ZKP** — available to any two VRC holders regardless of shared community. Demonstrates possession of a valid VRC with selective disclosure over attributes, subject DIDs or predicates. Common application: disclose both parties' P-DIDs while hiding the underlying R-DIDs, proving two known personas have a relationship without exposing the private pairwise channel or enabling cross-presentation correlation. Confers no community-level assurance by itself.

2. **Community-anchored ZKP** — available when both parties hold VMCs from the same VTC. Demonstrates possession of the VRC, possession of the underlying VMC, and that the VRC issuer holds a VMC from the same C-DID. Whatever assurance the community's trust registry attaches to its VMCs carries forward into the proof.

The spec keeps schemas deliberately minimal to enable common predicates, and states explicitly that detailed ZK protocols and registry–ZK interactions are left to future work.

### 7.2 The seam

"Whatever assurance the trust registry attaches carries forward into the proof" is doing enormous unexamined work. There is no way, in the Credentials spec, to express *what* assurance at *what strength* inside the proof. A ZKP that proves "holder has a valid VMC from a recognised VTC" proves membership; it does not prove the VTC's personhood governance met any particular bar. That finding stands.

What v1 missed is that the ZKP Task Force has already begun closing this from its side, and has established three constraints that any taxonomy handed to it must satisfy:

- **The assurance boundary.** A ZKP proves possession of, and selected properties about, *an attestation*. It does not prove the underlying biometric determination was correct. The cryptography carries the privacy; the accreditation framework carries the assurance. A strength vocabulary is therefore a statement about accreditation, not about the proof.
- **The trade curve.** Sybil resistance and full unlinkability cannot both be promised. What is reachable is context-dependent unlinkability — linkable within a context, unlinkable across contexts — and stronger deduplication is bought by spending unlinkability (following ePrint 2026/333).
- **The foundational boundary question.** What counts as a context, and must a context boundary survive the issuer and the verifier acting together? Every candidate construction is parameterised by the answer, and until it is answered a construction table "looks specific but is underdetermined."

### 7.3 What the taxonomy must supply — and in what form

A predicate vocabulary that is (a) expressible as a ZK statement, (b) compositional, and (c) carries strength. v1 rendered that as:

> ~~`prove(humanity ≥ strength_S) ∧ prove(unique_within(VTN_X)) ∧ ¬disclose(identity) ∧ linkability = pairwise`~~

That expression should not be circulated. Five faults, each traceable to published material:

1. **`unique_within(VTN_X)` scopes uniqueness by ecosystem**, which is the specific shortcut the ZKP work rules out. Scoped uniqueness is parameterised by context, scope, purpose *and* epoch; an ecosystem is none of these, and "one enrolment per issuer or ecosystem" sits at the second point of the trade curve — a governance and biometrics property, not a cryptographic one.
2. **`humanity ≥ strength_S` presumes a single ordinal over a single predicate.** Humanity decomposes into liveness-attestation possession and personhood-policy satisfaction, with different negative meanings; and the trade curve is not a ladder, so `≥` is the wrong relation. This note's own §9 asks whether humanity is even a primitive claim — v1 asserted the predicate and questioned its existence in the same document.
3. **`¬disclose(identity)` is not a predicate.** It is a property of the disclosure boundary, and it is defeasible by derived disclosure, field combination, registry lookup patterns and observable events. It cannot be asserted as a conjunct of the statement being proved.
4. **`linkability = pairwise` conflates two layers.** Pairwise is an identifier-layer property (one R-DID per counterparty). A linkability context is a governed domain that may legitimately span several verifiers performing the same purpose. And conjoining strong uniqueness with pairwise unlinkability treats as independent two things the trade curve makes coupled.
5. **It names no adversary, no horizon and no transcript** — failing all three of the published drafting rules, and omitting the epoch and the collusion target that make the claim testable.

**The corrected form.** A show over the published predicate set, every parameter bound, stated with its adversary and horizon:

> **Show:**
> `liveness_attestation(policy P, assurance class A)`
> `∧ issuer_accreditation(framework F, concealment mode m)`
> `∧ personhood_policy(policy Q)`
> `∧ scoped_uniqueness(context C, scope S, purpose U, epoch E)`
> `∧ holder_binding(transcript T)`
> `∧ freshness(transcript T)`
>
> **Asserted against** adversary 𝒜 ∈ {honest-but-curious verifier; verifiers colluding across contexts; issuer colluding with verifier} — with the target stated, not assumed.
>
> **For horizon** H, bounded by the earliest of attestation validity, epoch rollover, enrolment-root cryptoperiod, status freshness and profile lifetime.
>
> **Alongside** the declared disclosure set: assurance class, policy version, accreditation framework, and a context-scoped pseudonym.
>
> **Does not establish:** correctness of any underlying determination; one natural person globally; one enrolment per issuer or ecosystem; non-transfer of the holder key; absence of coercion or account sharing; consent; agent authority.

Where an agent presents, delegation evidence is composed as a **separate** structured artefact bound to the same transcript — never inferred from `holder_binding`.

Two properties of this form matter more than its notation. It **degrades honestly**: a deployment that cannot resist issuer–verifier collusion states so and declares a different profile, rather than carrying the stronger claim silently. And it **resists composition failure**: proofs that are individually sound can leak jointly, so the show is specified as a whole with a single declared disclosure set, not assembled from independently-specified conjuncts.

This is the join between the assurance-semantics layer and the DTG mechanism layer, and it is the natural joint deliverable. It is also the point at which the taxonomy stops being a document and starts being a circuit specification — but only in this form. In v1's form it would not survive construction selection.

### 7.4 The genuinely open research item

v1 named registry–ZK interaction as the open cryptographic question. That framing should be retargeted: the interaction itself has candidate constructions — set-membership over the accredited-issuer set, with an accumulator or vector commitment where the set churns — and issuer concealment is already treated as a per-profile choice rather than a universal requirement, so the specific issuer may be concealed within a named accredited set while the accreditation framework, policy version and assurance class are disclosed.

The hard problem is narrower and better stated as: **is issuer–verifier collusion resistance achievable at all**, given issuer-held enrolment data, schema field rarity, status and registry traffic, network observability and presentation timing? That is construction-specific, it is not answered by the nullifier alone, and it is the right joint problem for BGIN and the ZKP Task Force. Adjacent and equally open: how biometric-derived secrets can be rotated for recovery and epoch rollover without creating a reusable biometric correlator.

---

## 8. BGIN IKP positioning

### What BGIN uniquely brings

1. **Multi-stakeholder legitimacy** — regulators, academics and industry in one room. A World Foundation-authored personhood taxonomy will be read by some as standard-shaping around a specific biometric uniqueness product, however technology-neutral the text. Routing it through BGIN neutralises that.
2. **Regulatory interface** — AML/CTF, sanctions, travel rule, and the tension between unlinkable uniqueness and identifiability obligations.
3. **Political economy** — who governs personhood domains, who accredits the accreditors, and what happens when personhood becomes a precondition for participation.
4. **Cross-venue brokerage** — IKP sits adjacent to ISO, IEEE, ToIP, DIF and LFDT simultaneously. Few groups do.

### Sequencing

v1's table omitted the ZKP Task Force's own calendar, which contains the nearest hard deadline for the deliverable §7 describes. Added below.

| When | What |
|---|---|
| **Now** | Reply to WF with the convergence finding, the Credentials WD01 reference **and the ZKP requirements v0.3 reference**. Introduce them to the DTGWG Credentials TF; the spec is at Working Draft 01 with an open issue tracker and conformance tests undefined — the window is open. Flag the ZKP TF's September interim target so the taxonomy can be an input to it rather than a comment on it. |
| **1–3 Sept, GDC Geneva** | **BGIN co-organises "The Decentralized Trust Graph: A Unified Trust Infrastructure for the Internet of Humans and the Internet of Agents", day 2, 16:00–16:50** — the natural venue to introduce the convergence, with DTG participants present. BGIN also hosts workshops on post-quantum migration on DLTs, vulnerability handling in the agentic AI era, and wallet security assurance (ST/PP and convergence). Chatham House applies throughout. Corridor targets: ISO SC 27 WG 5 contacts, DTGWG editors, EUDI/ARF participants, OpenID Foundation, NIST agent-identity people. |
| **September** | **ZKP TF interim milestone** — a shareable strawman of the proof-of-liveness requirements, to put in front of the cryptography teams. First point at which an assurance-class vocabulary can land in the attestation-schema discussion rather than after it. |
| **September** | File targeted issues against `trustoverip/dtgwg-cred-spec`: (i) strength expression for PHC-qualifying VMCs, aligned to the assurance class the proof layer already discloses; (ii) humanity/uniqueness as separable predicates; (iii) **an enrolment-anchor primitive to carry the same-human-as-enrolment predicate**; (iv) assurance semantics for the planned Agent card, checked against the existing delegation field list. |
| **September** | **IKP working group community session** — invite World Foundation to present the taxonomy to the IKP community, straight after Geneva and while the paper is still open. First public test of the merged framing, and where contributions get sourced. |
| **September, topic call** | Public IKP call on biometrics, ZKPs and proof of personhood, co-hosted with World Foundation, going deeper than the community session allows. |
| **September–October** | **Incorporate the assurance decomposition into the IKP proof of personhood paper as a contributed section**, with the convergence mapping as an annex. WF contributes the assurance-class semantics; BGIN supplies the governance and regulatory framing around it. |
| **October, Linux Plumbers / OpenVTC** | LFDT and UC Berkeley ZKP work is a build priority for this track, and the ZKP TF aims to keep its proof definitions in sync with it. Same month as Block 15 — worth deconflicting travel, and more importantly making sure the predicate vocabulary reaches both venues in the same form. |
| **October, Block 15 (DC)** | IKP session, with the taxonomy already carried in the paper rather than proposed alongside it. Session output feeds the final revision. |
| **3–5 November, IIW #43** | **The ZKP Task Force's Working Draft milestone.** This is the operative deadline for the §7 deliverable: a predicate vocabulary that is ZK-expressible, compositional and carries strength has to exist in usable form by here, or the Working Draft ships without it and the seam sets. Nearer, harder and more consequential than any ISO date. |
| **Beyond** | ISO SC 27 WG 5 study period → NWIP. Realistically 3–4 years. Faster citable outputs: ToIP deliverable, W3C CG note, or IETF Internet-Draft. |

### Expectation management on the standards endgame

World Foundation's stated goal is formal adoption by applicable SDOs. Worth being candid: ISO SC 27 WG 5 — where 27551, 27565 and 27566 live — moves on a multi-year cycle and will not adopt a taxonomy that has not already demonstrated multi-party implementation consensus. The realistic path is: the DTG deliverables establish the mechanism and the predicate semantics, the BGIN paper establishes the governance framing, and *then* an ISO study period has something to standardise. Attempting ISO first inverts the order and stalls.

---

## 9. Open questions to pressure-test at GDC

Take these into the corridors rather than a position. (Numbering corrected from v1, which had two items at 3.)

1. Should assurance strength be a single ordinal scale, per-category scales, or a profile-defined vector? What does a relying party actually consume?
2. Can the Common Criteria ST/PP model carry personhood assurance profiles, or does the community-authored profile pattern break down when the "product" is a governance framework rather than a device?
3. Where should a cross-ecosystem assurance-class vocabulary live — in the issuer attestation schema, in the trust registry record, or in both — and what does that choice cost in issuer fingerprinting?
4. Can a ZK predicate carry strength without leaking the issuer's identity — and is issuer–verifier collusion resistance achievable at all once schema rarity, status traffic and timing are counted?
5. Is "humanity" a primitive claim, or the union of liveness plus presence plus absence-of-automation? Is the third even provable? If it decomposes, strength attaches per component — what does a relying party do with a vector?
6. How does any personhood claim survive coercion and credential rental — and if it cannot, how should the taxonomy say so?
7. Who accredits a VTN? What is the appeal path when a human is falsely denied uniqueness, and who supervises the context authority?
8. Does EUDI ARF's pseudonym/PID model already occupy this space in the EU, and how does a personhood taxonomy interact with it?
9. For agent authority: does the human principal need to be *identified*, or only *assured as human with delegated scope*?

---

## 10. Recommended immediate actions

1. **Reply to World Foundation** with the convergence finding, both DTG references — Credentials WD01 *and* ZKP requirements v0.3 — and an offer to introduce them to the DTGWG Credentials Task Force.
2. **Encourage the framework to be positioned as a cross-ecosystem assurance-semantics layer** with an explicit mapping annex, binding to the predicate semantics already published beneath it, rather than as a standalone end-to-end framework. That is a stronger claim, not a smaller one — it makes the taxonomy adoptable by every body it maps to, and it avoids becoming a second vocabulary for a field that already exists.
3. **Secure GDC registration** via the co-organiser link — free but mandatory, and two weeks out. Anchor the conversation to the day 2 DTG session BGIN co-organises rather than leaving it to corridors.
4. **Invite World Foundation to present at the September IKP community session** — the concrete near-term slot, and the basis for incorporating the assurance decomposition into the proof of personhood paper. Table this analysis alongside it.
5. **Surface the strength-expression gap** in the ZKP and credentials discussions as a candidate joint deliverable, in the §7.3 form and against the IIW #43 deadline.

---

## Appendix A: Reference set

**Normative / published**
- ToIP, *Decentralized Trust Graph Credentials — Core Specification*, v1.0 Working Draft 01. https://trustoverip.github.io/dtgwg-cred-spec/
- ToIP DTGWG ZKP Task Force, *Privacy-Preserving Proof of Liveness — Requirements*, v0.3 — assurance boundary, Sybil/unlinkability trade curve, foundational context question, per-predicate disclosure table, profile split. https://github.com/trustoverip/dtgwg-zkp-tf
- ToIP DTGWG ZKP Task Force, *Drafting rules* — name the adversary; name the horizon; state what each predicate does not establish; label conjecture as conjecture. Published in the same repository.
- W3C, *Verifiable Credentials Data Model v2.0*; *Decentralized Identifiers v1.0*
- NIST SP 800-63-4 family
- ISO/IEC 29115:2013; ISO/IEC TS 29003:2018
- ISO/IEC 27551:2021 (unlinkable attribute authentication); 27565:2026 (ZKP privacy preservation); 27566-1:2025 (age assurance); 29100:2024
- ISO/IEC 30107-3:2023; 30108-1:2026; 19795-10:2024; 24745:2022

**Research**
- *A Cryptographic Framework for Proof of Personhood*, IACR ePrint 2026/333 — Choudhuri, Garg, Lee, Montgomery, Policharla, Sinha. **Adopted as the normative reference of the DTG ZKP Task Force**, not merely cited literature: it is the source of the trade-curve constraint in §7.2.
- Adler et al., *Personhood Credentials*, arXiv:2408.07892 (2024, rev. Jan 2025) — also cited by the Credentials spec.
- Borge et al. (2017) and the pseudonym-party literature, for the physical-uniqueness baseline

**In progress**
- ToIP DTGWG ZKP TF: *Predicate & Assurance-Boundary decision document* (in preparation, per requirements v0.3 next steps) — the document that will resolve the foundational context question. A v0.4.0 requirements draft with stable requirement identifiers and the minimum-liveness / extended-personhood profile model is under discussion in the public repository. **Working Draft milestone: IIW #43, 3–5 November 2026.**
- ToIP DTGWG: *DTG Core Trust Task Protocols* (planned); *DTG Verifiable Data Structures* (planned, includes r-card and Agent card)
- ToIP DTGWG Risk Assessment and Harms Prevention Task Force
- LFDT / UC Berkeley ZKP work — build priority for the October Linux Plumbers / OpenVTC track; the ZKP TF aims to keep proof definitions in sync with it
- First Person Project / First Person Network (LFDT, Ayra, ToIP, DIF, OWF)
- NIST AI Agent Standards Initiative; NCCoE Software and AI Agent Identity and Authorization
- World Foundation, *Proof of Human Conceptual Standards Framework*, v0.13

**Not currently referenced by either draft — should be**
- EU Digital Identity Wallet Architecture and Reference Framework (pseudonym and PID model)
- OpenID for Agents; GNAP; IETF Web Bot Auth
- euCONSENT / AgeAware, as prior art for attribute assurance with strength

*(v1 listed the A2A AgentCard here in error — the Credentials spec's planned Agent card is explicitly modelled on it, as §2 row 10 of this note records.)*

---

## Appendix B: IKP paper integration points

*The proof of personhood paper is open, so the assurance decomposition can be incorporated directly rather than proposed alongside it. Slots to complete against the current draft:*

- Which of the ten assurance categories the paper already addresses, and under what terminology — reconcile before importing WF's vocabulary wholesale
- Where the paper's regulatory analysis attaches to the DTG governance layer (VTC governance frameworks, VTN trust anchors, trust registries)
- Whether the paper's treatment of biometrics maps onto WF's evidence classes or needs its own
- The paper's position on coercion, rental and duress — still the strongest available differentiator; fenced as a non-establishment on the DTG proof layer, but unclaimed as a governance and liability question (§5.1)
- The institutional accreditation question — who accredits a VTN, who supervises a context authority (§5.3) — which no document in either DTG workstream answers
- Whether the convergence mapping rides as an annex or is cited as a separate note
- What the paper needs from the ZKP side: the predicate vocabulary in the §7.3 form — every parameter bound, adversary and horizon declared, negative space written — against the IIW #43 deadline

---

*This is a working note for discussion, not a position of BGIN, ToIP or World Foundation. Critical feedback welcome.*
