# PQC Migration on Bitcoin — Bitcoin Core edition of the GDC26 breakout deck

Source: `ORIGINAL_GDC26_PQC_Migration_DLTs_Slides.pdf` (BGIN — Mitchell Travers & Shin'ichiro Matsuo, 3 Sep 2026; no LaTeX source on disk, so this is a fresh Beamer reproduction).
Build: `latexmk -pdf GDC26_PQC_Migration_Bitcoin_Core_Slides.tex` (MiKTeX; needs beamer, booktabs, fontawesome5, tikz, qrcode).

## What changed vs the original (17 slides, same order and look)
- Title / slide 2: "on DLTs" -> "on Bitcoin"; audience line "Bitcoin Core & Bitcoin infrastructure community | October 2026" (PLACEHOLDER: set the real venue and date); GDC26 co-organizers moved to a "where this frame comes from" list.
- Slides 3, 4, 6, 11, 12, 14, 15, 16: DLT-generic wording made Bitcoin-specific (soft-fork activation, classical UTXOs, P2PK / reused-address exposure, vbytes / validation time / UTXO growth, Lightning, signing devices, "what stays outside Bitcoin Core's remit").
- Slide 5: Google Quantum AI resource numbers (PRX Quantum 7, 031001) and the P2QRH / BIP-360 reference mapping named explicitly.
- Slide 7: adds the public coordination repository line.
- Slide 8: adds "Nothing here asks Bitcoin Core to adopt anything."
- Slides 9 and 10: the original PDF rendered these diagrams BLANK (caption only). Drawn here: three lanes + candidates + BTC-tx metrics (from testbed/SCHEMES.md and evaluation/METRICS.md), and the Sep 2026 -> 2028 timeline (from workshops/ROADMAP.md).
- Slide 13-16 (Matsuo's discussion starter): kept near-verbatim; only Bitcoin object names added. Confirm with him before presenting.
- Slide 17: venue updated to Georgetown University Capitol Campus, 111 Massachusetts Ave NW (per the current Block 15 record); fourth QR for the competition repo.

Facts follow bgin-global/pqc-agility-competition draft v0; everything remains ecosystem-neutral (no chain / scheme endorsement).
