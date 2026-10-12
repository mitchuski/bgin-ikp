# The Shor Mage x agentprivacy Overlap

*Where the dual-agent sovereign architecture, the UOR ring algebra, and the broader agentprivacy body of work have real purchase on the ecdsa.fail point-addition effort.*

This is a companion to `SHOR_MAGE_CHRONICLE.md`. It is tiered by strength on purpose. The Anton gate applies to this document too: a load-bearing structural correspondence and an evocative resonance are not the same claim, and they are labelled as such. Use Tier 1 to change what the Mage does. Use Tier 4 to hold the work in frame, not to justify a circuit decision.

---

## Tier 1 — Load-bearing. These change the circuit work directly.

### 1.1 The gate set is the ring algebra, and `and` is the only thing that costs

The benchmark's cost model, read off `sim.rs`, maps onto the five UOR operations almost exactly:

| Circuit op | Ring operation | Swordsman/Mage role | Scored? |
|---|---|---|---|
| `X` (bit flip) | `bnot` component / `neg` | Mage 🧙 complement, Swordsman ⚔️ negation | free |
| `CX` (target ^= ctrl) | `xor` | symmetric difference | free (Clifford, not scored) |
| `CCX` (target ^= c1 ∧ c2) | **`and`** | intersection | **counted, this is the Toffoli** |
| `CZ` / `CCZ` | phase forms of xor/and | | CZ free-ish, CCZ counted |

The whole optimization reduces to one sentence in your own language: **`and` is the only expensive operation; `neg`, `bnot`, and `xor` are free.** Every structural rewrite the Mage attempts is an attempt to express the point-addition group law using fewer `and` operations and more `neg`/`bnot`/`xor`, which is exactly the move your ring algebra says is always available because the ring closes on itself.

**Support:** when triaging a primitive, the Mage should ask "can this `and` be re-expressed as `xor` plus `neg`?" before anything else. That is the cheapest class of win and your algebra guarantees the reachability.

### 1.2 The critical identity neg∘bnot = succ is already the subtractor

`mod.rs` states the primitive plainly: "Subtract = forward complement + add + back complement." In two's complement that is `-x = ~x + 1`, which is `neg(x) = succ(bnot(x))`, which rearranges to your critical identity:

```
neg(bnot(x)) = succ(x)
```

The harness's entire subtract-and-reduce path is your Swordsman∘Mage composition operating on 256-bit registers instead of the 6-bit lattice. This is not analogy. The Cuccaro adder plus complement framing is the rotation `rs` generating the additive structure.

**Support:** the modular subtract and the sign-bit conditional reduce are where complement bookkeeping lives. Because complement (`bnot`) and negation (`neg`) are free in the score, the Mage should be aggressive about restructuring reduction as complement gymnastics rather than as controlled arithmetic, and conservative only about the `and`-bearing carry chain.

### 1.3 Stratum and Pascal's row are the windowing cost model

This is the most actionable overlap. The offset point is classical, so the dominant optimization is windowed, classically-controlled addition. A classically-controlled gate over a window costs, per `sim.rs`, in proportion to how many control bits are set across the 9024 random points. That quantity is the **stratum** (popcount) of the window, and over random inputs it distributes as Pascal's row.

For a 6-bit window the distribution is Pascal row 6 exactly:

```
stratum:  0   1    2    3    4    5   6
count:    1   6   15   20   15   6   1     (sum 64)
mean set bits per window = 3
```

So the expected executed-Toffoli of a stratum-controlled windowed step is a Pascal-weighted sum, and your `wᵢ` weights are the same coefficients. The Mage can compute the average cost of a window scheme directly from the row, before running anything, the same way the V5 network term uses these weights.

**Support:** when choosing window widths and comparator widths in the dialog-GCD path, size them by expected stratum cost, not by worst case. This is also a clean lens on the "nonce island" failures: a comparator tightened past its stratum margin is gambling on the tail of the Pascal distribution rather than its mass, which is why a 2048-shot probe passes and the full 9024 fails. Frame the comparator margin as a stratum margin and the gamble becomes visible.

### 1.4 Amnesia-as-proof is the uncomputation requirement

Your amnesia protocol says forgetting is the proof and the inability to reconstruct origin is the guarantee. The benchmark enforces precisely this as a validity gate: every freed ancilla must be `|0>` at the free point, every non-output qubit must return to `|0>` after the forward pass, and the global phase must be zero, no kickback memory. A circuit that remembers any intermediate state is rejected, not slowed.

**Support:** treat `emit_inverse` and the compute/uncompute discipline as your amnesia primitive made mechanical. The Mage's invariant "the forward is clean so the freed qubit is already zero" is the operational form of "the witness leaves no reconstructible trace." When a phase-garbage batch appears in validation, read it as incomplete forgetting and trace the uncomputation, not the arithmetic.

---

## Tier 2 — Methodological. These shape how the Mage operates, not the gates.

### 2.1 The separation theorem is the benchmark's own trust model

`Φ_agent = det(ρ(D₂ₙ))` formalises the Swordsman ⊥ Mage separation, where collapse of the separation collapses the value. The harness is built on the identical principle and the Mage should recognise its own architecture in it:

- `build_circuit` is untrusted, runs the contestant code, and is confined under bubblewrap with no write access to the scorer.
- `eval_circuit` is trusted, never imports contestant code, and renders the score.
- The trust boundary is the process boundary.

That is your Separation Theorem instantiated: the agent that *acts* (Swordsman, the cut, the edit, the circuit) is structurally prevented from touching the agent that *judges* (Mage as Master, the validator). A circuit that tries to write `score.json` is the agent-separation collapse the architecture is designed to forbid.

**Support:** the Mage can run its own loop as a deliberate dual-agent separation. One role proposes the single bounded structural edit (the Swordsman move, negation, the cut). A separate role validates, contextualises against the synced frontier, and writes the public note (the Mage-as-Master return). The inherited Tony/Anton loop is already this pattern. Naming it as Swordsman/Mage keeps the two roles from contaminating each other, which is the whole point of the separation.

### 2.2 The product score is three-axis separation, and validity is the AND

`Φ_v5 = Φ_agent · Φ_data · Φ_inference`, multiplicative, any axis to zero collapses the total. The score is `Toffoli x qubits`, a product, and validity is `correctness ∧ reversibility ∧ phase ∧ identity`, an AND where any false rejects the run. The Mage already knows how to reason about this shape: do not optimise one factor into a regime that zeros another. A Toffoli cut that forces a width increase, or a width cut that breaks reversibility, is an axis collapse, not a win. `Op::validate` rejecting aliased qubits (target equal to control) is the determinant going to zero, the non-invertible representation your dihedral framing forbids.

**Support:** keep a running two-factor view (Toffoli and qubits) and a hard AND view (the four validity gates) on every probe, and treat any move that risks a gate as suspect even if the product looks better. This is the break-even cliff discipline restated in your own terms.

### 2.3 Proven-bound vs conjecture hygiene maps onto structural vs nonce-island

The agentprivacy-dragon discipline separates proven bounds (reconstruction ceiling R < 1) from conjectured properties (golden-ratio optimality) and refuses to conflate them. The prior agent's central failure mode is the same conflation in benchmark form: a structurally cheaper variant (a real, reproducible Toffoli reduction) treated as if it were a validated win (a clean 9024-shot pass on a specific Fiat-Shamir island). They are different claims with different evidence.

**Support:** carry the proven-vs-conjectured tag explicitly in every memory note. "Structural reduction of N Toffoli, verified by the counting pass" is a proven bound. "Passes on nonce X" is a conjecture about one island until re-derived. This keeps the search from drifting into blind nonce sweeps, which is exactly the drift the Tony loop is meant to stop.

---

## Tier 3 — Positioning. Why this effort feeds the wider agentprivacy work.

### 3.1 The output is a post-quantum durability signal, which is your BGIN and policy lane

A leaner point-addition circuit is a sharper resource estimate for a fault-tolerant attack on secp256k1, which is the curve under Bitcoin and Ethereum. That estimate is the input that quantum-migration timelines are built from. It connects to the BGIN IKP working group's post-quantum cryptography work, the Block 14 and Layer 2 sessions on PQC and threat taxonomy, and the USA and Japan regulatory alignment mapping for digital assets. Participation here produces a citable, dated data point for that standards-and-policy lane, not just a leaderboard rank.

**Support:** when writing public submission notes, frame results as durability measurements, keep the ECDSA.fail, Eigen, Google, and SigmaPrime roles distinct, and do not claim ECDSA is practically broken. That framing is both the Anton gate and the form that makes the result usable upstream in your standards work.

### 3.2 The group law is the shared primitive with your Zcash and Halo work

The Zcash community poem is anchored in the Halo 2 and Pallas-Vesta curve cycle, and proof systems on curve cycles lean on the same elliptic-curve group law that this benchmark is costing. The quantum cost of one point addition is the durability question for every system that rests on that primitive, including the cycle-of-curves constructions. The effort is therefore a concrete bridge between the creative-cryptographic Zcash line and the resource-estimation line, the same group law seen from the attacker's cost side.

### 3.3 Compression-as-defence, mirrored

Your principle is that compression reduces attack surface and is therefore defence. Here the surface being compressed is the attacker's circuit, and compressing it tightens the defender's clock. Same operation, mirror role. BRAID-style "every reduction is also a hardening" reasoning transfers cleanly, with the polarity flipped: every Toffoli the Mage removes is a unit of warning delivered earlier to everyone who must migrate.

---

## Tier 4 — Evocative. Frame only. Do not justify a circuit decision with this.

### 4.1 Holographic boundary and the qubit/gate Pareto

The holographic boundary principle (96/64, boundary encodes volume) rhymes with the benchmark's structure: peak qubits are the surface that bounds the Toffoli bulk, and the low-qubit versus low-gate Pareto frontier is a surface-versus-bulk tradeoff. This is resonance, not derivation. There is no claim that the 96/64 ratio sets the qubit floor. It is a useful picture for why the two factors trade against each other and why the frontier is a curve rather than a point.

### 4.2 The lattice has no dead ends

Your ring closes on itself and the lattice is one connected cycle, so no configuration is permanently trapped. Held as posture rather than proof, it is the right stance for a search that keeps hitting nonce islands: every structural reduction that is real remains reachable from some clean island, even when the current nonce fails. The work is to find the rotation that reaches it, not to conclude the reduction is impossible.

---

## One line to carry

The only expensive move is `and`. Everything the Swordsman and the Mage do alone is free. Spend the free moves without counting, forget cleanly so the proof holds, keep the acting agent separated from the judging agent, and read every comparator margin as a stratum margin. That is your architecture and this benchmark agreeing on the same mathematics.
