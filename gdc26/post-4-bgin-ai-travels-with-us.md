# BGIN AI Travels With Us: Interactive Infrastructure for GDC, Block 15, and Beyond

Companion post to the GDC 2026 session proposals thread. Feedback wanted by **Friday 10 July**, alongside the session agenda deadline.

## The premise

BGIN sessions describe systems: threat sharing, credential ceremonies, machine-readable terms, trust graphs, PQC evaluation. At GDC and at Block 15 we will stand in rooms full of policymakers and standards people and describe them again. This post proposes that we stop only describing and start letting the room *touch* the work, and that the infrastructure we build for it travels with us from event to event. Hence the name. This is easier to do than it sounds; most of the pieces already exist.

I host bgin.ai, and I am offering to use it as the vehicle.

## What I am proposing to build

### 1. A live demo surface per session, or one consolidated BGIN interface

Two options, and I want the community's preference:

- **Per-session:** each Block 15 / GDC session gets an updated demo of the relevant working group's current output, hosted at bgin.ai and shown live in the room.
- **Consolidated:** a single **BGIN at GDC** interface, one front door for the three sessions, with each session's demo behind it.

My lean is consolidated for GDC (one URL a policymaker can remember from a slide) and per-session for Block 15 (working group depth). Both are cheap once the first is built.

### 2. A MyTerms primitive at the front door

When someone visits the BGIN interface, they should not meet a cookie banner. They should meet an **agreement ceremony**: the visitor's side presents machine-readable terms, ours responds, and the agreement is recorded before anything else happens. This is IEEE P7012 made tactile. Fifty people in a Geneva breakout room experiencing the contractual privacy paradigm at the door, instead of hearing the phrase "notice and consent" one more time, is worth more than a slide deck. It also gives Session 3 (wallet assurance and certification) a live artefact to point at.

### 3. Trust graph formation as the room participates

Each visit, each agreement, each gate opened (see below) forms an edge. Over the days of the event, the room grows a visible trust graph of its own making. We display it at the close: this is what the community built by showing up and agreeing to terms with each other. The graph is the demo. Nothing teaches relationship-based identity faster than watching your own edge appear.

### 4. Federated wiki as the system of record

For record keeping and exploration of the sessions, I propose forming a **federated local wiki**: each session's notes, artefacts, and follow-ups live as wiki pages that can be forked, annotated, and carried home by participants, in the lineage of the federated wiki work already running in the Hitchhiker timeline project. The record does not sit in one silo owned by one host. It federates, which is the point: BGIN's outputs behave the way BGIN says infrastructure should behave.

### 5. The Gatehouse: encrypted document access as a shared ceremony

I have just built an encrypted wiki sharing system at [guide.agentprivacy.ai/gates](https://guide.agentprivacy.ai/gates). A gate opens with two factors that are useless alone: a **sigil** (an emoji string) and a **proverb** (a spoken line). Trace one, speak the other, and the gate opens to a unique set of documents.

Here is how it plays in a session room:

1. At the close of the session, the proverb is spoken aloud from the front of the room. If you were there, you heard it.
2. The sigil drops into the session group chat that formed during the hour. If you joined, you can copy it.
3. Each attendee casts both at the gate and receives access to a unique document set: the session's deep materials, the drafts, the references, the follow-up pathway.
4. They can point their own agent at those documents afterwards. The session does not end when the room empties; it ends when their agent has finished reading.
5. Soulbae, the first mage, saves the moment: the ceremony is recorded as an event in the record, an edge in the trust graph, a page in the wiki.

Presence plus participation as the access credential. No account creation, no email harvesting, no badge scan. You had to be in the room and in the conversation. That is the whole authentication model, and it is a better demonstration of "understanding as key" than any talk about it.

### 6. The threat system demo (Session 1 decision)

Cross-referencing the GDC thread: if we choose to demo the working group threat system in Session 1, it becomes the sixth surface in this stack, sharing the front door, the terms ceremony, and the record keeping. The open question there stands: what specifically do we build for a 50-minute policy audience, and who builds it? Concrete suggestions welcome in either thread; I will consolidate.

## Why this is worth the build

GDC's audience decides on certifications, standards, and regulatory posture. Most of them have never watched a machine-readable terms agreement complete, never seen a trust graph grow from their own participation, and never opened an encrypted resource with a spoken proverb instead of a password. Every one of those experiences argues for BGIN's positions more efficiently than the accompanying paper does. And because the infrastructure federates and travels, whatever the Geneva room builds is waiting in Washington when Block 15 opens.

## Asks

1. **Preference:** consolidated BGIN at GDC interface vs. per-session demos, or the hybrid proposed above.
2. **Session 1:** yes or no on the threat system demo, and if yes, the specific build scope and builder(s).
3. **Content owners:** one volunteer per session to curate what goes behind that session's gate.
4. **A dry run:** I propose we rehearse the full loop (terms ceremony, gate, wiki, graph) at the public IKP session on biometric ZKP before September, so GDC gets the second performance, not the first.
5. **Naming and blessing:** if the Steering Committee wants this branded and reviewed before it stands under bgin.ai, say so early. I would rather adjust in July than in August.

Reply here by 10 July. The pieces exist; the assembly is the work of weeks, not months.
