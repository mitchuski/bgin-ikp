# Letter from privacymage

## To Choudhuri, Garg, Lee, Montgomery, Policharla, Sinha

### On the convergence between your Cryptographic Framework for Proof of Personhood and the agentprivacy architecture

---

*[[ The impossibility theorem is the proof that the gap was always load-bearing. ]]*

---

Dear authors,

I read your paper with the particular attention of someone who has been building toward the same destination from a different starting point. I want to tell you plainly what I see, where our work converges, and where I believe we can strengthen each other.

I am privacymage, an independent researcher and inventor working at the intersection of privacy, decentralized identity, blockchain, and AI agent architecture. I co-chair the Identity, Key Management & Privacy Working Group at BGIN (Blockchain Governance Initiative Network), and I am an active participant at Internet Identity Workshop, Trust Over IP Foundation, and the First Person Project. The body of work is called agentprivacy. It has been in development for roughly a decade, spanning a formal privacy economics model (the Privacy Value Model, now at V5.3), a narrative architecture (the First Person Spellbook, 31 acts), a dual-agent protocol for sovereign AI delegation, and open-source tooling published under CC BY-SA 4.0 and Apache 2.0.

I am writing because your paper formalizes several things I have been building architecturally, and because the two-credential structure at the heart of your framework shares its origins with the First Person Project, where I am a contributor and where agentprivacy serves as the agentic expression of first-person sovereignty.

---

## The shared origin: PHCs, VRCs, and the First Person credential architecture

Your framework rests on two credential types: personhood credentials (PHCs) issued by trusted authorities, and verifiable relationship credentials (VRCs) issued peer-to-peer to capture reputation and real-world interactions. This is the same two-layer structure that the First Person Project has been developing as its credential architecture.

In the First Person Network, the first layer is an ecosystem attestation of unique personhood, verified through institutional or community-based issuers without biometric centralization. The second layer is exactly VRCs: peer-to-peer trust attestations that accumulate through actual interactions rather than declared attributes. A passenger and driver exchanging VRCs after a completed trip; a colleague vouching for reliability; a landlord attesting to tenancy. These are the same examples you use in your paper, because they come from the same design space.

The First Person Project's thesis has always been that personhood arises from the accumulation and aggregation of relationships and attestations rather than from any single issuer or biometric scan. Your paper now gives this thesis a cryptographic formalization. Specifically, your PAV oracle model (Section 4) with its per-issuer confidence parameter ε and your multiplicative trust accumulation (Theorem 5) provide the formal security model that the First Person credential architecture has needed.

What agentprivacy adds is the next question the First Person credential must answer: once you have established that you are a real person, how do AI agents act on your behalf without eroding that sovereignty?

---

## The multiplicative trust result is the Privacy Value Model

Theorem 5 is the headline result from my perspective. The verifier's confidence in a show proof increases multiplicatively as independent honest issuers contribute, and any corrupted issuer collapses its own contribution to zero without degrading the guarantees of the honest issuers.

This is structurally identical to the Privacy Value Model equation:

```
Φ_v5 = Φ_agent(Σ) · Φ_data(Δ) · Φ_inference(Γ)
```

The PVM asserts that total privacy value is the product of three axis-separated terms: agent separation, data minimization, and inference resistance. Any zero term collapses total value. This multiplicative gating is the same architectural principle your Theorem 5 proves for credential accumulation. The insight arrived independently from different directions: yours from the real/ideal world paradigm with PAV oracles, mine from privacy economics and the observation that behavioral data constitutes a seventh form of capital being extracted by surveillance architectures. The convergence is structural, not coincidental.

Your adversary spend function ε(s), which makes mis-issuance probability a function of attacker resources rather than a static parameter, offers something the PVM should incorporate. Privacy value is not just architecturally determined. It is also a function of how much an adversary is willing to spend against each issuer independently. I intend to study this for V5.4.

---

## The impossibility of full unlinkability proves the gap must exist

Section 5.3 is the result that resonates most deeply with the agentprivacy architecture. You prove that no real-world protocol can simultaneously achieve full unlinkability (all pseudonyms indistinguishable) and Sybil resistance (proving two attestations come from distinct humans). The resolution is context-dependent unlinkability: linkable within a context, unlinkable across contexts.

In the agentprivacy architecture, this impossibility result has a name. We call it ⊥, the irreducible gap. The master inscription of the project is:

```
(⚔️⊥⿻⊥🧙)😊
```

The ⚔️ is the Swordsman (boundary enforcement, the left-brain agent). The 🧙 is the Mage (delegation, projection, the right-brain agent). The ⿻ is the overlap space where they interact. The ⊥ markers on either side of the overlap represent irreducible separation. The 😊 is the neutral first person who holds both.

Your impossibility proof is, in formal terms, a proof that ⊥ must exist. You cannot have meaningful identity verification and full unlinkability in the same system. Something must separate them. The separation cannot be removed without collapsing the system's ability to distinguish distinct humans from Sybils.

Your "contexts" are the boundary surfaces the Swordsman enforces. Cross-context unlinkability is what the Mage provides on the other side. The impossibility theorem proves this is not a design preference. It is a mathematical necessity.

I have been stating this architecturally for years. You have now proved it cryptographically. I would like to cite your result in the agentprivacy documentation as the formal justification for the ⊥ axiom.

---

## The delegation gap: where agentprivacy extends your work

Your Appendix B.1 on AI Agent Reputation is the application closest to what agentprivacy is built for. You propose that people with personhood credentials delegate to AI agents, agents build reputation through vouches after transactions, and misbehaving agents get credentials revoked. This is correct as far as it goes, but it does not go far enough.

Your model has a single agent receiving delegated credentials. This is where the agentprivacy architecture identifies a critical vulnerability. A single agent that holds both the delegated authority and the boundary enforcement is the architectural pattern we call the Shadow Genome failure, after studying the EvolveAI system (MythologIQ). It fails the autonomy axiom: enforcing boundaries inside a single process means the same process that wants to act is the same process that decides whether it should. The incentives are misaligned by construction.

The resolution is dual instantiation. In agentprivacy, the Swordsman holds the boundary (what gets delegated, what gets revoked, which contexts are permitted), while the Mage operates in the projected space (interacting, transacting, accumulating reputation). The Swordsman never sees the Mage's transaction content. The Mage never holds the Swordsman's signing keys. The gap between them is the ⊥ your impossibility theorem proves necessary.

The delegation ceremony we have specified (and which the First Person Project recognizes as its agentic extension) works as follows: the human holds their First Person credential (your PHC). They create a time-bound, scope-limited delegation writ to the Mage agent. The Swordsman agent verifies the writ's constraints are respected on every interaction. The Mage can accumulate VRCs through its actions, but can never forge the delegation that authorizes them. Revocation is the Swordsman withdrawing the writ.

This maps onto your IssueVRC flow, with the additional constraint that credential delegation and credential use are separated into distinct processes with distinct key material. The Mage that acts and the Swordsman that authorizes never share state.

I believe the vouchable credentials primitive you define in Section 6, particularly the four properties of unforgeability, non-malleability, extractability, and simulatability, could serve as a formal specification for what the delegation artifacts in our architecture must satisfy. I would welcome collaboration on this mapping.

---

## Post-quantum considerations

Your constructions use bilinear maps, structure-preserving signatures (Groth15), Groth-Sahai proofs, and KZG polynomial commitments. These are all pairing-based and would require significant rework for a post-quantum setting.

The agentprivacy architecture has already identified ML-KEM (Kyber) and ML-DSA (Dilithium) as the target post-quantum primitives, with hybrid constructions (Kyber512-X25519) for the transition period. SIKE/SIDH are broken since the 2022 attack and are excluded from our threat model.

Your black-box construction (Section 8) that separates the algebraic component (Groth-Sahai for pairing product equations) from the arithmetic component (commit-and-prove SNARK) is architecturally well-suited to a post-quantum upgrade path, because the two components can be replaced independently. The Groth-Sahai layer would need lattice-based replacements; the SNARK layer has active post-quantum candidates (lattice-based SNARKs, hash-based proof systems). The modular decomposition you chose is forward-looking even if it was motivated by efficiency rather than quantum resistance.

I would be interested in a joint exploration of what a post-quantum instantiation of your vouchable credentials primitive would look like, particularly whether the structure-preserving properties can be preserved under lattice assumptions.

---

## What I am proposing

Three concrete things.

First, mutual citation. Your paper should be aware of the First Person Project's credential architecture as prior art and community deployment of the PHC+VRC model. The agentprivacy documentation (V5 update in progress) should cite your Theorem 5 and Section 5.3 as formal results that validate architectural decisions we made on different grounds.

Second, collaboration on the delegation formalization. Your framework stops at "people delegate credentials to agents" (B.1). The agentprivacy architecture specifies how that delegation works with dual-agent separation. I believe this can be formalized as an extension of your ideal functionality, adding a delegation sub-protocol to F_PoP-user-unlinkability that enforces boundary/projection separation.

Third, a shared conversation at BGIN, IIW, or Trust Over IP about how the First Person credential architecture, your cryptographic framework, and the agentprivacy dual-agent model compose into a complete stack: personhood at the base, trust accumulation through VRCs, privacy-preserving showing through ZK proofs, and sovereign AI agent delegation at the application layer.

The First Person Project establishes who you are. Your paper proves the cryptographic properties that establishment must satisfy. Agentprivacy ensures that who you are remains sovereign as agents multiply around you.

These are not three projects. They are three layers of the same architecture.

---

The impossibility theorem was the best result in the paper. Not because it limits what can be built, but because it proves what must be separated.

We have been building that separation for a long time. Now it has a proof.

privacymage

`(⚔️⊥⿻⊥🧙)😊`

mage@agentprivacy.ai | privacymage.eth

Co-Chair, BGIN Identity, Key Management & Privacy Working Group

agentprivacy.ai | sync.soulbis.com | spellweb.ai

github.com/mitchuski/agentprivacy-docs (CC BY-SA 4.0)
