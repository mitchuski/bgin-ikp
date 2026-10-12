# BGIN SR 0011

## Study Report: Zero-Knowledge Proofs (ZKPs) – Technology and Applications

**Author**: Leona Hioki (BGIN) and contributors  
**Editor**: Mitchell Travers (BGIN)  
**Working Group**: IAM, Key Management and Privacy Working Group

---

*This study is a work product of the IAM, Key Management and Privacy Working Group of BGIN.*

©2025 BGIN (Blockchain Governance Initiative Network) is registered as BN Association, a Japanese general association with its principal place of business at Shiba Building, 704, 4-7-6, Shiba, Minato-ku, Tokyo. All rights reserved.

---

## Executive Summary

This report consolidates modern zero-knowledge proof (ZKP) practice for blockchain applications, examining arithmetization choices (R1CS, Plonkish, AIR, CCS), proving backends (pairing/KZG, IPA, FRI/STARK, sumcheck-centric), recursion and folding/IVC (Nova/SuperNova/HyperNova), zkVMs, and post-EIP-4844 rollup economics. It provides concrete derivations (Groth16/QAP, KZG, sumcheck, FRI), proof size and cost estimates, and security considerations for production deployments.

Zero-knowledge proofs enable one party (the prover) to convince another party (the verifier) that a statement is true without revealing any information beyond the validity of the statement itself. Since their theoretical foundation in 1985 and practical implementation beginning in 2013, ZKPs have evolved from academic curiosity to production-ready technology powering privacy-preserving transactions, scalable blockchain infrastructure, and verifiable computation systems.

**Key Capabilities:**
- **Privacy Enhancement**: Privacy-preserving transactions and identity verification without exposing sensitive data
- **Scalability Solutions**: zkRollups enable thousands of off-chain transactions while maintaining on-chain security
- **Verifiable Computation**: Verification of complex computations with minimal overhead

---

## Table of Contents

1. [Scope and Audience](#1-scope-and-audience)
2. [Conventions and Notation](#2-conventions-and-notation)
3. [Terms and Definitions](#3-terms-and-definitions)
4. [Abbreviations and Symbols](#4-abbreviations-and-symbols)
5. [Definition and History of ZKP](#5-definition-and-history-of-zkp)
6. [ZKP Technology Architecture](#6-zkp-technology-architecture)
7. [Frontend Systems: Arithmetization](#7-frontend-systems-arithmetization)
8. [Backend Systems: Proving Mechanisms](#8-backend-systems-proving-mechanisms)
9. [Polynomial Commitment Schemes](#9-polynomial-commitment-schemes)
10. [Recursion and Folding](#10-recursion-and-folding)
11. [Applications](#11-applications)
12. [Programming Languages and Libraries](#12-programming-languages-and-libraries)
13. [Performance Trade-offs](#13-performance-trade-offs)
14. [Security Considerations](#14-security-considerations)
15. [Mathematical Derivations](#15-mathematical-derivations)
16. [Measurements and Representative Sizes](#16-measurements-and-representative-sizes)
17. [Choosing a Stack](#17-choosing-a-stack)
18. [Ecosystem Snapshot](#18-ecosystem-snapshot)
19. [References](#19-references)
20. [Appendices](#20-appendices)

---

## 1. Scope and Audience

**Scope**: Practical non-interactive proofs in production—zkSNARKs, zkSTARKs, and folding-based IVC—and their use in privacy, scalability, and proofs of computation.

**Audience**: Protocol engineers, auditors, product teams, blockchain developers, security professionals, and policy makers working with or evaluating ZKP systems.

---

## 2. Conventions and Notation

We write fields as 𝔽_q (q=p^k), elliptic-curve groups as G1/G2/G_T, and use CRS/SRS for reference strings. Standard cryptographic notation applies throughout.

---

## 3. Terms and Definitions

### 3.1 Zero-Knowledge Proof (ZKP) & NIZK

**ZKP**: A cryptographic protocol satisfying three properties:
- **Completeness**: If the statement is true, an honest prover convinces an honest verifier
- **Soundness** (or knowledge soundness for SNARKs): If the statement is false, no prover can convince the verifier except with negligible probability
- **Zero-knowledge**: The verifier learns nothing beyond the truth of the statement

**NIZK**: Non-interactive zero-knowledge proof, obtained natively or via Fiat-Shamir transformation (ROM).

### 3.2 Finite Fields, Groups, Curves

**Finite field** 𝔽_q has q=p^k elements where:
- characteristic(𝔽_q)=p
- Every non-zero element has a multiplicative inverse

**Elliptic curves** over 𝔽_q form abelian groups:
- Identity element 𝒪
- For finite group order n: n·P=𝒪 for any point P
- **Important**: Group order ≠ field characteristic

**Elliptic Curve**: An equation that can be represented as y² = x³ + ax + b over a finite field. Points P and Q on the elliptic curve have a defined addition operation, making P + Q = R. While direct multiplication P × Q isn't defined, scalar multiplication like P+P=2P and nP (n times P) is defined. Due to the discrete logarithm problem, it's computationally infeasible to derive n from nP.

**Order**: The order of the finite field that defines the elliptic curve.

**Characteristic**: The total number of points on that curve given an elliptic curve's functions and its order. If the characteristic is q, then for any point P on that curve, qP equals P.

### 3.3 Commitments, Hashes, Vector Commitments

**Commitment**: A cryptographic primitive providing:
- **Binding**: Cannot change the committed value
- **Hiding**: The committed value remains unknown until revealed

Includes Polynomial Commitment Schemes (PCS) such as KZG/IPA/FRI.

**Hash function**: A function that:
- Ensures different outputs with high probability for different inputs
- Makes it computationally infeasible to discern the input from its output
- Always produces the same output for the same input
- Provides preimage/second-preimage/collision resistance
- Uses domain separation for transcripts

### 3.4 Arithmetic Circuit

A circuit that performs arithmetic operations on the input (not a digital circuit). The operation receiving each input is called a **gate**, and in the context of ZKP, this operation's equation becomes a **constraint**. In many NIZK systems, there's a strong positive correlation between the number of constraints and the proof generation time.

### 3.5 Polynomial Problem

The problem of whether one knows a polynomial that meets certain conditions. In many cases of ZKP, knowing certain input eventually gets converted or reduced to a polynomial problem.

### 3.6 Witness

A value needed for proof that can be obtained during the calculation process when input into a circuit. The witness represents the private inputs and intermediate values.

### 3.7 Instance

The public dataset where the witness is actually substituted for the gate, representing the public inputs and outputs of the computation.

### 3.8 Fiat-Shamir Transformation

A method to convert interactive ZKP into a non-interactive format using a random oracle (typically implemented with a hash function). The prover side can produce a value that they cannot control during the computation process, allowing the verifier side's random oracle role to be transferred to the prover side.

---

## 4. Abbreviations and Symbols

**AIR** — Algebraic Intermediate Representation  
**CCS** — Customizable Constraint Systems  
**CRS** — Common Reference String  
**DA** — Data Availability  
**FFT** — Fast Fourier Transform  
**FRI** — Fast Reed-Solomon Interactive Oracle Proof  
**IPA** — Inner Product Argument  
**IVC** — Incrementally Verifiable Computation  
**KZG** — Kate-Zaverucha-Goldberg (polynomial commitment)  
**MSM** — Multi-Scalar Multiplication  
**NIZK** — Non-Interactive Zero-Knowledge  
**PCS** — Polynomial Commitment Scheme  
**QAP** — Quadratic Arithmetic Program  
**R1CS** — Rank-1 Constraint System  
**ROM** — Random Oracle Model  
**SRS** — Structured Reference String  
**STARK** — Scalable Transparent ARgument of Knowledge  
**zkEVM** — Zero-Knowledge Ethereum Virtual Machine  
**zkML** — Zero-Knowledge Machine Learning  
**zkRollup** — Zero-Knowledge Rollup  
**ZKP** — Zero-Knowledge Proof  
**zkSNARK** — Zero-Knowledge Succinct Non-interactive ARgument of Knowledge  
**zkVM** — Zero-Knowledge Virtual Machine  

---

## 5. Definition and History of ZKP

### 5.1 Origins

The invention and explicit mention of Zero-Knowledge Proof (ZKP) was first demonstrated in 1985 in "The Knowledge Complexity of Interactive Proof Systems" by Shafi Goldwasser, Silvio Micali, and Charles Rackoff. This foundational paper established the theoretical framework for protocols where one party can prove knowledge without revealing the knowledge itself.

### 5.2 Evolution to Practical Systems

**1985-2012**: Theoretical development period, establishing foundations but lacking practical implementations.

**2013**: Groth16 and earlier SNARK systems begin practical deployment, starting with ZCash development.

**2016**: ZCash launches as the first major production deployment of zkSNARKs (using Groth16), enabling completely private transactions on a public blockchain.

**2018**: Vitalik Buterin conceives zkRollup concept for Ethereum scaling. Barry Whitehat implements MVP of Plasma with zkp (Plasma snap).

**2019**: Loopring launches the first DEX using zkRollup technology.

**2020**: zkSync launches zkSync v1, a remittance network using zkSNARK validity proofs.

**2021**: StarkWare introduces Cairo and production STARKs. Nova folding scheme proposed.

**2023**: Multiple zkEVMs launch (Polygon zkEVM, Scroll, zkSync Era), offering Ethereum-compatible scaling with different levels of EVM equivalence.

**2024-2025**: Maturation of zkVMs, folding schemes (SuperNova, HyperNova, MicroNova), and Plonky3. EIP-4844 (Proto-Danksharding) activates, dramatically improving zkRollup economics.

---

## 6. ZKP Technology Architecture

### 6.1 Two-Layer Architecture

Modern ZKP systems are typically organized across two layers:

**Frontend (Arithmetization)**: Converts computational statements into mathematical constraints
- Defines how computations are represented
- Determines constraint format and structure
- Affects circuit design and optimization strategies

**Backend (Proving System)**: Generates and verifies proofs from those constraints
- Implements the cryptographic protocol
- Determines proof size, generation time, and verification cost
- Affects security assumptions and setup requirements

### 6.2 Key Properties

Different ZKP systems optimize for different properties:

**Proof Size**: From ~128 bytes (Groth16) to 100-250 KB (typical STARK)

**Prover Time**: Computational cost to generate proof, typically O(n log n) or better

**Verifier Time**: Cost to verify proof, ranging from constant (pairings) to logarithmic (FRI queries)

**Setup Requirements**: Trusted setup, universal setup, or transparent (no setup)

**Post-Quantum Security**: Hash-based systems (STARK/FRI) offer quantum resistance; pairing-based systems do not

**Recursion Support**: Ability to efficiently prove statements about other proofs

---

## 7. Frontend Systems: Arithmetization

### 7.1 R1CS (Rank-1 Constraint System)

**Structure**: Constraints of the form a × b = c where a, b, c are linear combinations of variables.

**Characteristics**:
- Simple and well-understood
- Foundational format for early SNARKs (Groth16, original ZCash)
- Each constraint represents one multiplication gate
- Addition and linear operations are "free"

**Limitations**:
- Bit operations costly (require many constraints)
- Limited expressiveness compared to modern systems
- No native lookup support

**Use Cases**: Early SNARK systems, simple circuits where tooling maturity matters more than efficiency.

### 7.2 Plonkish Gates

**Structure**: Polynomial constraints with custom gates and lookup tables.

**Characteristics**:
- Custom gates can encode multiple operations efficiently
- Native lookup table support (PlonKup, Halo2)
- More flexible than R1CS while maintaining efficient proving
- Supports range checks, bit decomposition, and table lookups efficiently

**Advantages**:
- Efficient hashing (can use lookup tables for S-boxes)
- Better performance for real-world applications
- Universal setup possible (reusable across different circuits)

**Complexity**: Higher design complexity; requires understanding of polynomial constraints.

**Use Cases**: Modern SNARKs (PLONK, Halo2), applications requiring efficient hashing or range proofs.

### 7.3 AIR (Algebraic Intermediate Representation)

**Structure**: Time-step state transition constraints for STARKs.

**Characteristics**:
- Optimized for sequential computation traces
- Natural fit for VM execution
- Constraints verify state transitions at each time step
- Execution trace represented as polynomials over time

**Advantages**:
- Excellent for VM traces and sequential programs
- Scales efficiently with trace length
- Natural representation for iterative computations

**Use Cases**: STARK-based systems, zkVMs, Cairo, long computational traces.

### 7.4 CCS (Customizable Constraint Systems)

**Structure**: Unified framework supporting multiple constraint formats.

**Characteristics**:
- Generalizes R1CS, Plonkish, and other systems
- Designed for folding schemes and IVC
- Flexible constraint representation

**Use Cases**: Nova, HyperNova, and other folding-based IVC systems.

---

## 8. Backend Systems: Proving Mechanisms

### 8.1 Pairing-Based Systems (Groth16, PLONK)

**Mechanism**: Uses elliptic curve pairings for succinct verification.

**Setup**: Requires trusted setup ceremony:
- Circuit-specific (Groth16): New setup for each circuit
- Universal (PLONK): Single setup works for all circuits up to a size

**Proof Size**: Smallest available (~128-192 bytes for Groth16)

**Verification**: Constant time (2-3 pairings), efficient on-chain

**Security**: Based on discrete log assumptions; not post-quantum secure

**Prover Cost**: FFT and MSM operations dominate; O(n log n) typical

**Best For**: On-chain verification, applications requiring minimal proof size, mature production deployments.

### 8.2 IPA (Inner Product Argument / Bulletproofs)

**Mechanism**: Logarithmic-size proofs via inner product arguments.

**Setup**: Transparent or universal (no trusted setup)

**Proof Size**: O(log n) group elements

**Verification**: O(n) but can be batched; MSM-heavy

**Security**: Discrete log assumption; not post-quantum secure

**Recursion**: Excellent recursion properties (Halo, Halo2)

**Best For**: Recursive proofs, applications avoiding trusted setup, moderate proof sizes acceptable.

### 8.3 FRI / STARK

**Mechanism**: Fast Reed-Solomon Interactive Oracle Proof; hash-based polynomial commitment.

**Setup**: Completely transparent (no setup required)

**Proof Size**: Larger (100-250 KB typical)

**Verification**: Logarithmic number of queries; hash operations

**Security**: Post-quantum secure (based on collision-resistant hashing and low-degree testing)

**Prover**: Scales well for very large computations; highly parallelizable

**Best For**: Large computational traces, zkVMs, post-quantum security requirements, transparent systems.

### 8.4 Folding / IVC (Nova, HyperNova)

**Mechanism**: Incrementally verifiable computation through folding schemes.

**Concept**: Instead of proving each step separately, "fold" multiple proof instances into one.

**Characteristics**:
- Low per-step prover cost
- Aggregated proof verification
- Natural for streaming or long-running computations
- Supports recursive composition

**Variants**:
- **Nova**: Original folding for R1CS
- **SuperNova**: Multiple circuits (non-uniform IVC)
- **HyperNova**: CCS-based with sumcheck protocol
- **MicroNova**: Extremely small proofs for sequential computation

**Best For**: Incremental computation, proofs of correctness for long-running programs, proof aggregation.

---

## 9. Polynomial Commitment Schemes

### 9.1 KZG (Kate-Zaverucha-Goldberg)

**Mechanism**: Pairing-based polynomial commitment with constant-size proofs.

**Properties**:
- Commitment: c = g^{φ(τ)} for polynomial φ
- Opening: Prove φ(a) = y with π = g^{q(τ)} where q(X) = (φ(X) - y)/(X - a)
- Verification: Single pairing check

**Setup**: Trusted setup required; universal (powers of τ up to degree bound)

**Proof Size**: Single group element (~48 bytes on BLS12-381)

**Verification**: Constant time (one pairing)

**Use Cases**: PLONK, modern SNARKs, EIP-4844 KZG commitments for blob data.

### 9.2 IPA (Inner Product Argument)

**Mechanism**: Logarithmic-size commitments via recursive halving.

**Properties**:
- No trusted setup
- Proof size O(log n)
- Verification cost O(n) or O(log n) with preprocessing

**Use Cases**: Bulletproofs, Halo, Halo2.

### 9.3 FRI

**Mechanism**: Hash-based low-degree testing.

**Properties**:
- Transparent (no setup)
- Post-quantum secure
- Larger proof size
- Query-based verification

**Use Cases**: STARKs, Cairo, hash-based zkVMs.

---

## 10. Recursion and Folding

### 10.1 Recursive Proof Composition

**Concept**: Proving statements about other proofs—a proof verifies another proof's correctness.

**Applications**:
- Proof aggregation (many proofs → one proof)
- Unbounded computation (streaming proofs)
- Cross-system bridges (prove STARK inside SNARK)

**Challenges**:
- Non-native field arithmetic (proving over different curves)
- Circuit size for verifier
- Cycle of curves (Halo approach)

### 10.2 Folding Schemes (Nova Family)

**Nova (2021)**:
- Fold two R1CS instances into one
- Low per-step cost
- Proof-carrying data (PCD) support

**SuperNova (2022)**:
- Multiple circuit support (non-uniform IVC)
- Prove execution of different programs

**HyperNova (2023)**:
- CCS-based (more expressive than R1CS)
- Sumcheck protocol integration
- Better for complex constraint systems

**MicroNova (2024)**:
- Extremely small proofs for sequential computation
- Optimized for specific use cases

**Use Cases**: Long-running computations, zkVMs, proof aggregation, incremental verification.

---

## 11. Applications

### 11.1 Privacy-Preserving Transactions

**ZCash**: Uses Groth16 to completely conceal:
- Sender address
- Receiver address
- Transfer amount

While maintaining verifiability of:
- No double-spending
- Conservation of value
- Proper authorization

**Tornado Cash**: Privacy mixer using zkSNARKs for:
- Breaking on-chain transaction graphs
- Proving withdrawal rights without revealing deposit
- Selective disclosure capabilities

### 11.2 zkRollups

**Definition**: Layer 2 scaling solution where:
- Transactions executed off-chain
- State transitions proven with validity proofs (zkSNARKs/STARKs)
- Proof and minimal data posted to Layer 1
- Inherits Layer 1 security guarantees

**History**: Conceived by Vitalik Buterin in 2018. Barry Whitehat performed MVP implementation (Plasma snap). Loopring launched first production DEX (2019). zkSync v1 launched (2020). Multiple zkEVMs launched (2023).

**Classification by State Management**:

1. **Stateful zkRollup**: Manages state commitments on Layer 1 smart contracts
   - Examples: Starknet, zkSync Era, Polygon zkEVM, Scroll, Taiko, Loopring

2. **Succinct zkRollup**: Anyone can calculate state from Layer 1 data
   - Example: Sovereign Rollup

3. **Stateless zkRollup**: Users compute only their own state
   - Example: Intmax

**Classification by zkEVM Type**:

- **Type 1**: Exactly equivalent to Ethereum Network
  - Example: Taiko
  - Perfect compatibility, slowest proving

- **Type 2**: Fully EVM bytecode compatible
  - Example: Scroll
  - Minor modifications for proving efficiency

- **Type 3**: Mostly EVM compatible
  - Example: Polygon zkEVM
  - Some Solidity code portable

- **Type 4**: Custom VM, limited EVM compatibility
  - Examples: StarkNet (Cairo), zkSync (custom VM)
  - Best performance, requires code porting

### 11.3 Related zkp Solutions (Not zkRollups)

**zkPorter** (zkSync proposal):
- Sacrifices some zkRollup security for scalability
- Offloads DA cost to token-carrying network
- 2/3 token holder coalition could freeze (but not confiscate) assets
- Does not fully inherit Layer 1 security

**Validium** (zkSync):
- Trusts validator group for DA
- No Layer 1 DA cost
- Lower security than zkRollup

**Volition** (Starkware):
- User-selectable security/cost trade-off
- Choose DA storage trustlessness level
- Balance between price and security

### 11.4 Identity and Credentials

**Selective Disclosure**: Prove attributes without revealing full credentials:
- Age verification without birthdate
- Citizenship without passport details
- Credentials without identity linkage

**Applications**:
- Privacy-preserving KYC
- Anonymous voting with eligibility proof
- Regulatory compliance with minimal disclosure

### 11.5 Verifiable Machine Learning (zkML)

**Capabilities**:
- Prove model trained on specific dataset
- Verify inference ran with specific weights
- Demonstrate model properties without revealing model

**Use Cases**:
- Trustworthy AI attestation
- Private inference
- Model provenance
- Regulatory compliance for AI

### 11.6 Cross-Chain Bridges

**ZK-enabled bridges**:
- Prove state on source chain
- Verify proof on destination chain
- Eliminate trusted intermediaries

**Advantages**:
- Trustless cross-chain transfers
- No validator set reliance
- Cryptographic security guarantees

---

## 12. Programming Languages and Libraries

### 12.1 Domain-Specific Languages

**Circom** (iden3):
- JavaScript-like syntax
- R1CS circuit generation
- Mature toolchain and ecosystem
- Used in production (Tornado Cash, Hermez)

**Cairo** (StarkWare):
- Designed for STARKs
- AIR-based constraints
- Turing-complete STARK-friendly CPU architecture
- Powers Starknet

**Noir** (Aztec):
- Rust-like syntax
- Multiple backend support
- Focus on developer experience
- Universal verifier approach

**Leo** (Aleo):
- Type-safe functional language
- SNARK-optimized
- Integrated with Aleo platform

### 12.2 Libraries and Frameworks

**Bellman** (Rust):
- Groth16 implementation
- Used in ZCash
- Mature and audited

**Halo2** (Rust):
- PLONK-based with lookup arguments
- No trusted setup (IPA)
- Excellent recursion
- Used in ZCash Orchard, Scroll

**Plonky2/Plonky3** (Rust):
- Fast PLONK implementation
- FRI-based (Plonky2) or flexible PCS (Plonky3)
- >2M Poseidon2 hashes/s on M3 Max
- Powers SP1, Valida

**arkworks** (Rust):
- Comprehensive cryptographic primitives
- Multiple curve implementations
- Modular proving system components

**gnark** (Go):
- Go-based SNARK library
- Groth16, PLONK support
- Production-ready

**Winterfell** (Rust):
- STARK prover and verifier
- AIR-based
- Used in Polygon Miden

### 12.3 zkVMs

**SP1** (Succinct Labs):
- RISC-V zkVM
- Plonky3-based
- Supports Rust programs

**Risc Zero**:
- RISC-V zkVM
- STARK-based
- Mature tooling

**zkMIPS**:
- MIPS architecture zkVM
- EVM compatibility focus

**Valida**:
- Custom ISA zkVM
- Plonky3-based
- Performance-optimized

---

## 13. Performance Trade-offs

### 13.1 Fundamental Trade-offs

**Proof Size vs. Prover Time**:
- Groth16: Tiny proofs (~128 B), slow proving, requires trusted setup
- STARK: Large proofs (100-250 KB), fast proving at scale, transparent

**Verification Cost vs. Proof Size**:
- Pairing-based: Constant verification, smallest proofs, on-chain friendly
- FRI-based: Logarithmic queries, larger proofs, post-quantum secure

**Setup Requirements vs. Flexibility**:
- Circuit-specific setup: Best performance, new ceremony per circuit
- Universal setup: One ceremony for all circuits, slightly larger proofs
- Transparent: No setup, larger proofs or higher verification cost

### 13.2 Recursion Capabilities

**Native recursion** (Halo2, Plonky2):
- Efficient proof-of-proof verification
- Enables proof aggregation
- Critical for zkVMs and unbounded computation

**Cross-system recursion**:
- Prove STARK inside SNARK (on-chain verification)
- Requires non-native field arithmetic
- Higher overhead but enables best-of-both-worlds

### 13.3 Practical Considerations

**Hardware acceleration**:
- GPU acceleration for MSM operations
- ASIC development for high-throughput
- Critical for production zkRollup sequencers

**Parallelization**:
- STARKs: Highly parallelizable
- Folding schemes: Sequential by nature
- Circuit partitioning strategies

**Memory requirements**:
- Large circuits require significant RAM
- FFT operations memory-intensive
- Proof aggregation reduces peak memory

---

## 14. Security Considerations

### 14.1 Trusted Setup

**Circuit-Specific Setup (Groth16)**:
- New ceremony required for each circuit
- "Toxic waste" (secret randomness) must be destroyed
- If τ is recovered, soundness breaks (false proofs accepted)
- Multi-party computation (MPC) ceremonies mitigate risk

**Universal Setup (PLONK, Halo2)**:
- Single ceremony for all circuits up to size bound
- Reusable across different applications
- Significantly improves practical security
- Still requires secure ceremony execution

**Transparent Systems (STARK, Bulletproofs)**:
- No setup required
- Eliminates trusted setup risk entirely
- Trade-off: Typically larger proofs

### 14.2 Parameter Selection

**Security levels**:
- Curve choice affects security (BN254 ~100-128 bit, BLS12-381 ~128 bit)
- Field size must exceed security parameter
- Binding factor selection in FRI
- Soundness error must be negligible

**Common mistakes**:
- Insufficient constraint randomization
- Weak Fiat-Shamir hash function
- Improper domain separation
- Inadequate field size for operations

### 14.3 Circuit Design Vulnerabilities

**Under-constrained circuits**:
- Missing constraints allow invalid proofs
- Similar to smart contract logic bugs
- Requires careful auditing

**Arithmetic errors**:
- Overflow/underflow in finite fields
- Division by zero handling
- Range constraint violations

**Nondeterminism**:
- Witnesses must be deterministic from public inputs
- Prover-chosen values must be properly constrained

### 14.4 Implementation Vulnerabilities

**Historical vulnerabilities**:
- **Frozen Heart (Bulletproofs)**: Soundness break via malformed proof
- **Groth16 verification**: Incorrect pairing check implementation
- **zkSNARK setup**: Parameter generation issues

**Common issues**:
- Fiat-Shamir transcript errors
- Incorrect subgroup checks
- Malleability attacks
- Memory safety in proof generation

### 14.5 Audit Requirements

**Circuit audits**:
- Constraint completeness verification
- Arithmetic correctness
- Witness generation review

**Cryptographic audits**:
- Parameter selection validation
- Setup ceremony review (if applicable)
- Implementation correctness

**Best practices**:
- Formal verification where possible
- Extensive testing with edge cases
- Independent security reviews
- Bug bounty programs

---

## 15. Mathematical Derivations

### 15.1 Groth16 via QAP (Quadratic Arithmetic Program)

**Setup**: Given R1CS constraints, construct polynomials:
- Let A_w(X) = ∑ w_i A_i(X)
- Let B_w(X) = ∑ w_i B_i(X)  
- Let C_w(X) = ∑ w_i C_i(X)
- Let t(X) = ∏(X - r_j) be the target polynomial

**Requirement**: A_w(τ)·B_w(τ) - C_w(τ) = h(τ)·t(τ)

This means the polynomial on the left vanishes at all roots of t(X), which happens if and only if all constraints are satisfied.

**Proof Structure** = (A∈G1, B∈G2, C∈G1)

**Verification**: Three pairing checks confirm the QAP relationship holds.

### 15.2 KZG Evaluation Proof

**Commitment**: c = g^{φ(τ)} for polynomial φ

**Opening at point a with claimed value y = φ(a)**:
1. Compute quotient q(X) = (φ(X) - y)/(X - a)
2. Generate proof π = g^{q(τ)}
3. Verification: e(c/g^y, g) = e(π, g^{τ}/g^{a})

**Result**: Constant-size proof (one group element) proves polynomial evaluation.

### 15.3 Sumcheck Protocol (Sketch)

**Goal**: Prove S = ∑_{x∈{0,1}^n} g(x) for multivariate polynomial g

**Method**:
1. Prover sends univariate h_1(X_1) = ∑_{x_2,...,x_n} g(X_1, x_2, ..., x_n)
2. Verifier checks h_1(0) + h_1(1) = S and sends random r_1
3. Recurse with g'(x_2, ..., x_n) = g(r_1, x_2, ..., x_n) and claim S' = h_1(r_1)
4. After n rounds, verifier checks final evaluation directly

**Result**: Reduces sum verification to polynomial evaluation, logarithmic communication.

### 15.4 FRI Low-Degree Test

**Goal**: Prove committed polynomial has degree ≤ d

**Method**:
1. Commit to polynomial evaluations on domain
2. Apply random linear combination and domain reduction
3. Repeat folding with fresh randomness
4. Final polynomial is constant (degree 0)
5. Verification: Query random positions, check consistency

**Result**: Logarithmic rounds, query-based verification, post-quantum secure.

---

## 16. Measurements and Representative Sizes

### 16.1 Proof Sizes (Typical Configurations)

| System | Curve / Security | Proof contents | Compressed size | Uncompressed size (on-chain) |
|:---:|:---:|:---:|:---:|:---:|
| Groth16 | BN254 (~100–128-bit) | A∈G1, B∈G2, C∈G1 | ~128 B (32+64+32) | ≈256 B (64+128+64) |
| Groth16 | BLS12-381 (128-bit+) | A∈G1, B∈G2, C∈G1 | ~192 B (48+96+48) | ≈384 B (96+192+96) |
| KZG eval proof | BLS12-381 | π∈G1 | 48 B | 96 B (uncompressed) |
| IPA PC (poly eval) | Curve-group | O(log n) elements | logarithmic | logarithmic |
| STARK/FRI | Hash-based | Queries + commitments | 100–250 KB (typical) | same |

### 16.2 EIP-4844 Blob Economics

| Parameter | Symbol | Value |
|:---:|:---:|:---:|
| Bytes per field element | BYTES_PER_FIELD_ELEMENT | 32 |
| Field elements per blob | FIELD_ELEMENTS_PER_BLOB | 4096 |
| Bytes per blob | — | 131,072 bytes |
| Blob gas per blob | GAS_PER_BLOB | 2^17 = 131,072 |
| Target / Max blobs per block | — | 3 target / 6 max |

**Cost calculation**: cost per blob = base_fee_per_blob_gas × GAS_PER_BLOB

Example: At 1 gwei per blob gas ⇒ 131,072 gwei per blob (≈1.31e-4 ETH)

**Significance**: EIP-4844 (activated 13-Mar-2024) dramatically reduced zkRollup data posting costs by introducing dedicated blob storage with separate fee market.

---

## 17. Choosing a Stack

**For minimal proof size & fast on-chain verification**: 
- Pairing/KZG-based (Groth16/PLONK)
- Mature Solidity verifiers
- Best for frequent on-chain verification

**For transparent systems & long traces**: 
- FRI/STARK
- No trusted setup
- Post-quantum security
- Best for zkVMs and large computations

**For flexible recursion/folding**: 
- Halo2, Plonky2/3, Nova/HyperNova
- Efficient proof composition
- Best for incremental computation

**For zkRollups**:
- Type 1-3 zkEVM: Groth16 or PLONK with KZG
- Type 4: STARK-based (Cairo for Starknet)
- Consider blob availability post-EIP-4844

---

## 18. Ecosystem Snapshot (2024-2025)

**Plonky3**: >2M Poseidon2 hashes/s on M3 Max (reported); powering SP1/Valida

**Nova/HyperNova/MicroNova**: Advancing folding/IVC with on-chain verification improvements

**zkVMs**: Maturing rapidly; universal verifiers and aggregation becoming standard

**EIP-4844**: Proto-Danksharding live since March 2024; blob fee market significantly improves zkRollup economics

**zkEVM Competition**: Multiple implementations (Polygon zkEVM, zkSync Era, Scroll, Taiko) racing toward full EVM equivalence

**Post-Quantum Transition**: Growing attention to FRI-based systems and quantum resistance roadmaps

---

## 19. References

### Foundational Papers

[1] Goldwasser, S., Micali, S., & Rackoff, C. (1985). "The Knowledge Complexity of Interactive Proof Systems." *STOC 1985*.

[2] Blum, M., Feldman, P., & Micali, S. (1988). "Non-Interactive Zero-Knowledge and Its Applications." *STOC 1988*.

[3] Groth, J. (2016). "On the Size of Pairing-based Non-interactive Arguments." *EUROCRYPT 2016* (ePrint 2016/260).

[4] Ben-Sasson, E., Bentov, I., Horesh, Y., & Riabzev, M. (2018). "Scalable, transparent, and post-quantum secure computational integrity." *IACR ePrint 2018/046*.

### Modern Systems

[5] Gabizon, A., Williamson, Z.J., & Ciobotaru, O. (2019). "PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge." *IACR ePrint 2019/953*.

[6] Bowe, S., Grigg, J., & Hopwood, D. (2019). "Recursive Proof Composition without a Trusted Setup." *IACR ePrint 2019/1021* (Halo).

[7] Kothapalli, A., Setty, S., & Tzialla, I. (2021). "Nova: Recursive Zero-Knowledge Arguments from Folding Schemes." *IACR ePrint 2021/370*.

[8] Kothapalli, A., & Setty, S. (2022). "SuperNova: Proving universal machine executions without universal circuits." *IACR ePrint 2022/1758*.

[9] Kothapalli, A., Setty, S., & Tzialla, I. (2023). "HyperNova: Recursive arguments for customizable constraint systems." *IACR ePrint 2023/573*.

[10] Boyle, E., et al. (2024). "MicroNova: Extremely Small Proofs for Sequential Computation." *IACR ePrint 2024/2099*.

[11] Polygon Labs (2024). "Plonky3: The Next Generation of ZK Proving Systems."

### Polynomial Commitments

[12] Kate, A., Zaverucha, G.M., & Goldberg, I. (2010). "Constant-Size Commitments to Polynomials and Their Applications." *ASIACRYPT*.

[13] Bünz, B., Bootle, J., Boneh, D., Poelstra, A., Wuille, P., & Maxwell, G. (2018). "Bulletproofs: Short Proofs for Confidential Transactions and More." *IEEE S&P*.

### zkRollups and Scaling

[14] Buterin, V. (2018). "On-chain scaling to potentially ~500 tx/sec through mass tx validation." *Ethereum Research*.

[15] Ethereum Foundation (2024). "EIP-4844: Shard Blob Transactions (Proto-Danksharding)."

[16] Ethereum.org (2024). "Dencun Upgrade FAQ" (activation 13-Mar-2024; blob lifetime).

[17] Blocknative (2024). "Blob congestion event analysis; still cheaper than calldata in practice."

### Security

[18] Trail of Bits (2022). "The Frozen Heart: ZK Proof Vulnerability." *Blog post on Bulletproofs vulnerability*.

[19] OpenZeppelin (2023). "Auditing Zero-Knowledge Circuits."

[20] Consensys Diligence (2024). "zkSNARK Security Best Practices."

### Online Resources

[21] ZK Whiteboard Sessions. https://www.youtube.com/@zk-learning

[22] IACR ePrint Archive. https://eprint.iacr.org/

[23] Ethereum Research Forum. https://ethresear.ch/

[24] ZKProof Standards. https://zkproof.org/

[25] BGIN Resources. https://bgin-global.org/

---

## 20. Appendices

### Appendix A: Glossary

**AGM** — Algebraic Group Model  
**AIR** — Algebraic Intermediate Representation  
**CCS** — Customizable Constraint Systems  
**CRS** — Common Reference String  
**DA** — Data Availability  
**FFT** — Fast Fourier Transform  
**FRI** — Fast Reed-Solomon Interactive Oracle Proof  
**IPA** — Inner Product Argument  
**IVC** — Incrementally Verifiable Computation  
**KZG** — Kate-Zaverucha-Goldberg polynomial commitment  
**MSM** — Multi-Scalar Multiplication  
**NIZK** — Non-Interactive Zero-Knowledge  
**PCS** — Polynomial Commitment Scheme  
**QAP** — Quadratic Arithmetic Program  
**R1CS** — Rank-1 Constraint System  
**ROM** — Random Oracle Model  
**SRS** — Structured Reference String  
**STARK** — Scalable Transparent ARgument of Knowledge  
**zkEVM** — Zero-Knowledge Ethereum Virtual Machine  
**zkML** — Zero-Knowledge Machine Learning  
**zkRollup** — Zero-Knowledge Rollup  
**ZKP** — Zero-Knowledge Proof  
**zkSNARK** — Zero-Knowledge Succinct Non-interactive ARgument of Knowledge  
**zkVM** — Zero-Knowledge Virtual Machine  

### Appendix B: System Comparison Tables

**Backend System Comparison**

| Family | Setup | Assumptions | Proof size | Verify time | Prover cost | Notes |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Pairing/KZG | SRS (circuit/universal) | AGM/ROM, DLOG | Smallest | Few pairings | FFT+MSM heavy | Mature on-chain |
| IPA | Transparent/universal | DLOG | O(log n) | MSMs | Moderate–High | Good recursion |
| FRI/STARK | Transparent | Hash/LDT | 100–250 KB+ | Queries | Scales well | VM traces |
| Folding/IVC | Depends on PCS | Sumcheck + PCS | Aggregated | Succinct | Low per-step | Streaming/PCD |

**Frontend System Comparison**

| Front-End | Primary use | Lookups | Trace style | Strengths | Considerations |
|:---:|:---:|:---:|:---:|:---:|:---:|
| R1CS | Early SNARKs | Limited | Gate constraints | Simple | Bit ops costly |
| Plonkish | SNARKs w/ custom gates | Native | Polynomial constraints | Efficient hashing/lookups | Design complexity |
| AIR | STARK systems | Common | Time-step transitions | VM traces | Larger proofs |
| CCS | Unified | Via gadgets | Flexible | IVC-friendly | Advanced tooling |

### Appendix C: On-Chain Verification Notes

**Groth16 on BN254**:
- Mature Solidity verifiers available
- Uses pairing precompiles (EIP-197)
- ~300k gas typical verification cost
- Most widely deployed for on-chain verification

**KZG on BLS12-381**:
- Point-evaluation precompile (EIP-4844)
- Designed for blob verification
- Can be used for general polynomial commitments
- ~50k gas for single evaluation proof

**IPA verifiers**:
- Cost dominated by multi-scalar multiplications (MSMs)
- Batch openings strongly recommended
- Higher gas cost than pairing-based
- Benefits from EIP-2537 (BLS12-381 operations)

### Appendix D: zkRollup Considerations

**Decentralization of Block Producers**:
Many zkRollups have not yet fully decentralized block producers due to:
- High computational cost of proof generation
- Risk of bugs in new systems
- While this doesn't compromise security (inherited from Layer 1), it raises concerns about service continuity

**Proto-danksharding/Danksharding Security Implications**:
Time-limited data (e.g., one month via proto-danksharding) represents a novel approach:
- Enables 1/N security assumption (one honest node prevents DA attack)
- When writing to Layer 1 calldata: N ≈ 5000 (Ethereum node count)
- When using proto-danksharding: N ≈ 20-100 (rollup node count)
- Major Layer 2s can maintain large N
- Smaller "Rollup-as-a-Service" deployments may have limited N

**zkRollup ≠ Zero-Knowledge?**:
Most zkRollups are not confidential. The "zero-knowledge" property is used primarily for:
- Hiding intermediate computation details for efficiency
- Not for privacy (data is public)
- Some argue "validity rollup" is more accurate terminology

**Does zkRollup = Bridge?**:
Tokens natively issued on Layer 2 that are not bridged from Layer 1 may not fully inherit Layer 1 security if they conduct independent governance or forks. However, this mirrors existing Layer 1 tokens with governance or limited liquidity. Currently considered a non-critical concern.

---

**Disclaimer**: The views expressed in this document are personal views of the participating members of the BGIN community and should not be seen as the official views or recommendations of the institutions with which they are affiliated.

The technology described in this document was made available from contributions from various sources, including members of BGIN and others. Although BGIN has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this document or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights.

---

**END OF DOCUMENT**

BGIN SR 0011 – Zero-Knowledge Proofs (ZKPs): Technology and Applications Study Report

Version: 1.0 Consolidated  
Date: 2025  
© 2025 BGIN (Blockchain Governance Initiative Network)  
All Rights Reserved
