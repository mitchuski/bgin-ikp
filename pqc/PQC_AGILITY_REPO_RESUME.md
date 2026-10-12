# RESUME — bgin-global/pqc-agility-competition

Local working note. **Not tracked** (listed in `.git/info/exclude`); canonical copy also at `~/BGIN_IKP/pqc/PQC_AGILITY_REPO_RESUME.md`. Written 2026-09-05 at the end of the founding session. Read this first when you come back.

## -2. 2026-09-16 — Block 15 opening keynote: SITE session page only + Discourse reader (nothing in this repo)

**Keynote:** *Crypto Agility in the Quantum and AI Era* — Alex Pruden, CEO & Co-Founder, Project Eleven; 15 Oct 09:20–09:50, Room A (session 1-2). Abstract + bio + headshot supplied 2026-09-16.

- **Scope ruling (Mitch):** a descriptive fill of `bgin-global.org/events/20261015-block15/sessions/1-2` + announce on the Discourse threads. **No change to this repository** — the outreach branch I had made was dropped; the calendar rows still say "PQC keynote 09:20" (fine).
- **Website** `~/bgin-homepage-fork` branch `block15-pqc-keynote` (off upstream `7186471`): **COMMITTED `19b8c6a` + PUSHED to bgin-global, PR #107 OPEN https://github.com/bgin-global/bgin-homepage/pull/107 (mergeable; Vercel preview building at 13:20Z). Merge = Mitch.** Content — `contents/block15Promo.ts` `BLOCK15_KEYNOTE` record, `lib/block15-program-data.ts` 1-2 (title/summary/speaker/agenda), session page speaker card (headshot, bio, links) + abstract as overview, `lib/block15-hub-meetings.ts` 1-2 plan text, `public/images/Events/person/AlexPruden.jpeg`. tsc/build green. The wider version (home band row, event-page spotlight, news post) is saved as `~/BGIN_IKP/block15/block15-keynote-full-site-diff_2026-09-16.patch` (`git apply` if wanted).
- **Discourse reader (served: `cd ~/BGIN_IKP/readers/2026-09-16-block15-keynote-pack && python -m http.server 8794` → http://127.0.0.1:8794/):** `index.html` (+ `pack.md`, builder beside it) = 3 replies (1054 · 1012 · 1001) + optional standalone topic in *Block Meetings*. **Post after the site merge** — every post links the session page.

## -1. 2026-09-13 — MAIN REWRITTEN AND CLEAN (read first)

**DONE 00:40Z:** `REWRITE_MAIN_ONE_PUSH.sh` ran — main = `f70dad5`, 19 commits all signed by mitchuski + DCO, `verify-history` clean, ruleset restored active (deletion, linear history, signatures, PR-only w/ 0 approvals + rebase-only merge methods, checks, non_fast_forward); CI on main green; `main-signed` deleted; #2/#3 closed; #1 (Dependabot) rebase requested. Local `main` = origin/main; `~/pqc_harness` synced @ f70dad5. **Merge method from now on: `git push origin <branch>:main` after checks pass — never the buttons.** Restore approvals to 1 when the second convener is seated. The rest of this section is history:

### (superseded) MERGES DONE, ONE PUSH LEFT FOR MITCH

- Harness origin `main` PUSHED (`ea25f42`, draw v2). Ruleset lever pulled by Mitch's decision: approvals 0, code-owner/last-push off, **merge_methods = rebase only** (GitHub refuses to sign rebases ⇒ no button merge can land). PRs #4 #5 #6 #7 merged (squash), #8 merged by **fast-forward push of the signed head** (`git push origin <branch>:main` — WORKS, keeps the author's signature + DCO; now the documented merge method in CONTRIBUTING). #2 #3 still OPEN, superseded by #5 — close them.
- **PROBLEM FOUND:** the four squash merges are GitHub-signed, authored "privacymage", 3 without DCO → `verify-history.sh` FAILS on main. **FIX PREPARED:** branch `main-signed` (pushed) = identical tree rebuilt from the PRs' signed heads + one doc commit, 17 commits, all G + DCO. Replacing it needs ONE force-push under a temporarily lifted ruleset (the pull_request rule blocks non-PR pushes even with non_fast_forward lifted); the agent's tool guard refused the enforcement change → **Mitch runs `~/BGIN_IKP/pqc/REWRITE_MAIN_ONE_PUSH.sh`** (evaluate → push → restore → verify → delete main-signed). Mitch approved the rewrite 2026-09-13.
- After that: close #2/#3; `~/pqc_harness/sync-from-repo.sh`; restore approvals to 1 when the second convener is seated.

## 0. 2026-09-11 — where things stand now

- **Website live:** bgin-global.org/projects/pqc-migration carries the competition (repo CTA, category 44 as the Discourse door, GDC26 scene-setting deck + PRX Quantum paper) — bgin-homepage PR #106 merged 13:22Z. No Claude attribution in BGIN commits/PRs (Mitch's rule).
- **Discourse category 44 is live:** About description edited; launch **1053**, workshop series **1054** (not yet pinned), nominations **1055**; replies 1001/2 and 1045/2. **Held to the week of 14 Sep:** metrics (`03`), testbed (`04`). **7C** (deck reply) waits on the speaker's clearance. The launch post still has three *separate topic to follow* lines — the replacement text is in the posting-pack reader.
- **PR #5** `docs/record-2026-09-11` (7 signed commits; dco/signatures/validate green) = the consolidated record: stacks #2 + #3, adds `docs/CONFIDENTIALITY.md`, `outreach/` (drafts + posted-links table), resources (paper DOI/arXiv/ePrint, hosted deck, launch/roadmap/CoDecFin threads), open question 6 taxonomy + source, S-05/C-05 September evidence, Block 15 venue + sessions, CoDecFin 2027 as W6 anchor; **Trust over IP framing removed** everywhere. **Close #2 and #3 when #5 merges.** #4 (DCO bot fix) stays, then #1.
- **Merge blocker unchanged (§2):** REVIEW_REQUIRED — a second convener with a signing key, or temporarily `required_approving_review_count: 0` in `.github/rulesets/main.json` + `ORG=bgin-global scripts/bootstrap-github.sh rulesets`.
- **PR #6** `plan/autoresearch` (stacked on #5; base retargets to main when #5 merges; dco/signatures/validate green) = `docs/AUTORESEARCH.md` (open-benchmark model for calibration tracks; §5b proposers ⊥ provers with the draw as the Gap) + `decisions/0001` (proposed) + `testbed/tracks/` (contract + T1 verify-single manifest/RULES/runner/fixtures + note template) + schema `runner`/`draw`, METRICS directions, COI measurement seat, HARNESS §5 promotion rule. Internal review: `~/BGIN_IKP/pqc/PQC_REVIEW_AND_YUKON_2026-09-11.md`. **Chronicle + build handoff for the PQC dual-agent harness instance: `~/BGIN_IKP/chronicles/2026-09-12_the-prover-and-the-proposer.md` §5** (scaffold `~/pqc_harness` with `new_instance.mjs --prover <other model>`; assay seat = a node; salt per round not per proposal; four conform checks; harness v0 of HARNESS §7 is the critical path).
- **PR #7** `harness/instance` (stacked on #6; CI green incl. `scripts/ci/check-harness.sh`) = the calibration harness IN the record: `harness/upstream/` = agentprivacy dual-agent harness default dist vendored at origin commit `790a3b7` (`UPSTREAM.json` 111 sha256; `scripts/sync-harness.sh <checkout>` / `--verify`), `harness/instance/` = pqc-calibration instance (config: Gap = fixture draw, sourceFile = T1 manifest, sample 10k/65,536, 4 lenses, node-as-prover, 4 conformChecks; `tools/measure.mjs` = UNMEASURED honestly; stub round on record, verify_run green). **Conform fails on the unmeasured baseline BY DESIGN** (OT-1 = build harness v0). **D-1/D-2 FIXED upstream `ea25f42` (draw v2, drawVersion in gap.json, v1 legacy replay) — origin `main` is UNPUSHED (Mitch pushes); re-vendored (`sync-harness.sh` now generates dist in a clean worktree at the pinned commit — dist/ is gitignored upstream); smoke-v2 max idx 65,527/65,536; D-3 = template ENTRY.md link nit; CI link check excludes harness/upstream.** **Local lineage copy `~/pqc_harness`** (scaffolded from the origin with `--source`, `connection.local.json`, `sync-from-repo.sh` repo→local, `README.local.md`).
- **Posting-pack reader:** `~/BGIN_IKP/readers/2026-09-11-discourse-posting-pack/index.html` · https://claude.ai/code/artifact/9900f5bb-6c53-4985-90fe-b5ce249e993d (regenerate: scratchpad `build_reader.py`, which reads `outreach/discourse/`).
- Local branches: `docs/record-2026-09-11` (= PR #5, checked out) · `outreach/discourse-launch` and `docs/communication-channels` are now contained in it (delete after merge).

## 1. Where things stand (2026-09-05, end of day)

| Thing | State |
|---|---|
| Canonical repo | https://github.com/bgin-global/pqc-agility-competition — public, in the org, you are ADMIN |
| Local clone | `C:\Users\mitch\pqc-agility-competition` on `main`, clean, origin = the org repo |
| History on `main` | 3 signed + signed-off commits, all `verified=true` on GitHub: `31fcf5b` Charter the repository · `50219d2` Record the staging location · `bb9d99e` bootstrap: resolve the Python interpreter on Windows |
| Open PRs | **#2** `chore/transfer-complete` (`2801a59`, drops the README staging note, records the transfer) · **#3** `docs/communication-channels` (`6c969e8`, GOVERNANCE §7 channels table: public Discourse · private participants' Discourse · this repo as the only record; CONTRIBUTING/SUPPORT/README aligned) · **#4** `fix/dco-bot-signoff` (CI: the `dco` job rejected Dependabot because it signs off as support@github.com while its author email is a noreply address; bot authors now need a Signed-off-by naming the bot, humans unchanged) · **#1** Dependabot: codeql-action upload-sarif 3.37.9 → 4.37.9 (major bump; its `dco` check fails until #4 merges and the PR is rebased/re-run; check the v4 changelog before approving). All wait on a second reviewer (§2). Merge order: #4 → #2 → #3 → #1 |
| Rulesets (live, tested) | `#22344043` all branches: signed commits only · `#22344044` main: deletion + non_fast_forward + linear history + signatures + PR (1 approval, code owners, last-push approval, threads resolved, squash/rebase) + checks dco/signatures/validate · `#22344045` tags: admin-only, signed. **No bypass actors.** Server tests passed: unsigned push REJECTED, direct push to main REJECTED |
| Repo settings | web sign-off required · merge commits off · wiki/projects/discussions off · secret scanning + push protection ON · Dependabot alerts + security updates ON · private vulnerability reporting ON · Actions = GitHub-owned + verified creators only · GITHUB_TOKEN read-only |
| CI | `provenance.yml` (dco, signatures, validate) green on every push so far · `scorecard.yml` green once, one transient artifact-upload failure re-run |
| Teams (bgin-global) | `pqc-conveners` (maintain) · `pqc-maintainers` (maintain) · `pqc-evaluation` (push) · `pqc-testbed` (push). You are team maintainer of the first two; the others are empty |
| Org (measured, **nothing org-wide enacted**) | plan **free** (no org-level rulesets) · 8 owners / 12 members · 2FA **not** enforced (2 owners + 5 outside collaborators lack it — **considered, not enacted; owners decide together**) · default permission read · members can create repos · org Actions = all allowed, token default write · apps: vercel only. **2026-09-05: org defaults + other repos' scanning/alerts were switched on and then REVERTED the same hour on your instruction** (only Dependabot alert emails from that window cannot be undone). The four `pqc-*` teams are the only org-level footprint. Full picture + options + commands: `~/BGIN_IKP/wg-ops/ORG_SECURITY_CONSIDERATIONS_2026-09-05.md` |
| Your account | bgin-global **owner** (invitation was pending; accepted 2026-09-05) · signing key registered on GitHub ("pqc-agility signing 2026-09-05") · gh token scopes: repo, workflow, admin:org, admin:ssh_signing_key, gist |

## 2. The one blocker: a solo convener cannot merge

The main ruleset needs one approving review from a code owner **other than the author**, bound to the last push, and there is no admin bypass. You are the only member of `pqc-conveners`, so PR #1 and PR #2 wait. Two ways out — pick one:

1. **Seat the second convener** (intended path): they run `scripts/setup-signing.sh`, register the key on GitHub, open a PR adding their `.allowed_signers` line; you add them to `pqc-conveners` (`gh api -X PUT orgs/bgin-global/teams/pqc-conveners/memberships/<login> -f role=maintainer`). Then they approve #2 and #1.
2. **Temporarily run at ToIP's level**: in `.github/rulesets/main.json` set `"required_approving_review_count": 0`, then `ORG=bgin-global scripts/bootstrap-github.sh rulesets`. Everything else (PR-only, signatures, DCO, checks, no force-push) stays. Put it back to 1 when the second convener is seated. Note: the JSON edit itself lands via a PR, so apply the ruleset change from the local file first, merge, and the record catches up.

## 3. This machine

```bash
export PATH="/c/Program Files/GitHub CLI:$PATH"     # gh is installed but not on Git Bash's PATH
cd /c/Users/mitch/pqc-agility-competition
gh auth status                                       # mitchuski, keyring
```

- Signing key: `~/.ssh/pqc_signing_ed25519` (Ed25519, dedicated). **No passphrase yet.** Git now signs through **Windows OpenSSH 9.5** (`gpg.ssh.program = C:/Windows/System32/OpenSSH/ssh-keygen.exe`, tested: sign + verify + history OK) so the Windows agent can hold the key once unlocked. Finish in this order (needs you — elevation and the passphrase):

  ```powershell
  # 1. elevated PowerShell (Run as administrator) — the session shell was denied:
  Set-Service ssh-agent -StartupType Automatic; Start-Service ssh-agent
  ```
  ```bash
  # 2. Git Bash: add the passphrase, load the key, prove a commit still signs
  ssh-keygen -p -f ~/.ssh/pqc_signing_ed25519
  /c/Windows/System32/OpenSSH/ssh-add.exe ~/.ssh/pqc_signing_ed25519
  /c/Windows/System32/OpenSSH/ssh-add.exe -l
  cd ~/pqc-agility-competition && git commit --allow-empty -m "signing probe" && git log -1 --format=%G? && git reset -q --hard HEAD~1
  ```
  Your older `~/.ssh/id_ed25519` (auth key) also has no passphrase; same `ssh-keygen -p` applies.
- Repo-local git config: `gpg.format ssh`, `user.signingkey` = the .pub above, `commit.gpgsign true`, `tag.gpgsign true`, `gpg.ssh.allowedSignersFile` = repo `.allowed_signers`, `core.hooksPath .githooks`.
- Identity used in commits: `mitchuski <mitchuski@users.noreply.github.com>` (this is also your principal line in `.allowed_signers`).
- Hooks: `commit-msg` adds the DCO trailer; `pre-push` refuses unsigned or un-signed-off commits. `git commit -m "..."` is enough; the trailer and signature are automatic.
- If account-level reads 404 (emails, memberships), the token lacks `user`: `gh auth refresh -h github.com -s user`.
- Bash-tool gotcha for the agent: heredoc scripts over ~10 KB fail to parse here; use the Write tool or keep writes under ~8 KB.

## 4. Day-to-day loop

```bash
git checkout -b <topic> origin/main
# edit
git commit -m "..."                       # hook signs off; config signs
scripts/verify-history.sh origin/main..HEAD
git push -u origin <topic>                # pre-push re-checks; server requires signatures on every branch
gh pr create --fill                       # template checklist applies; needs a convener review (see §2)
```

Cut a deliverable (e.g. W4 call-text package): `git tag -s v0.1-call-text -m "..."` then `git push origin v0.1-call-text` (admin-only, signed, by ruleset).

## 5. Cleanup and collaborator edits (the "soon" list)

Placeholders and drafts that real people need to touch, roughly in order:

1. **Merge PR #4, #2, #3** then re-run and decide PR #1 (Dependabot major bump) — needs §2 resolved.
2. **MAINTAINERS.md / COMMITTEE.md**: name the second convener; roster rows as nominations land (issue template *Committee nomination* + COI disclosure). Conveners "to be named on ratification at W1" appears in COMMITTEE.md and GOVERNANCE.md §3.
3. **CODE_OF_CONDUCT.md**: the enforcement contact currently points to conveners + "BGIN administration at the address published on bgin-global.org". Put a real mailbox if BGIN has a conduct contact.
4. **OUTCOMES.md, GOVERNANCE.md, evaluation/*, testbed/*, workshops/ROADMAP.md** are all `draft v0` written from the July briefing, the GDC26 report and the IKP-WG transcript — collaborators should red-pen them before W1. Specific soft spots: composition table sizes (12–18), quorum rule, the 20 metrics' units and reference CPU/block-mix choices (open questions 1–6 in METRICS.md), scheme rows S-03 FN-DSA "draft status — confirm", S-04 Poseidon2-XMSS scope ruling, C-01…C-06 all need rulings; W1 date is only "late Sep".
5. **resources/README.md**: the IKP-WG meeting report `.docx` (with transcript, names) is **not copied** — decide whether it can be cited; link the SSR CfP, EF Quantum Retreat outputs, CSS/BWS outputs as they appear; add Discourse links for the workshops.
6. **README.md** is long (~120 lines with the calendar); consider moving the calendar into `workshops/ROADMAP.md` and keeping the README to purpose, map, how to engage. Badges: Scorecard badge only renders after a successful publish run.
7. **LICENSE holders**: files say contributors hold copyright; if BGIN wants a BGIN copyright line (ToIP's "work license, clarify copyright holders" pattern) add a NOTICE file.
8. **CITATION.cff** author is the WG; add named conveners if that is how BGIN wants citations.
9. **.github/rulesets/README.md** and `docs/SECURITY_MODEL.md` §5 mention org-level rulesets — mark "not available on the free plan" or upgrade the org.
10. **bootstrap-github.sh** `push` step uses an interactive prompt (won't run unattended) and `teams` needs owner — fine now, but tidy if collaborators will use it.
11. `docs/SECURITY_MODEL.md` §5 and `.github/rulesets/README.md`: reword org-level items as owners' decisions; note the free plan has no org rulesets.
12. Merge PR #3 (channels) before announcing. Announce on Discourse: reply on the IKP PQC thread (`/t/ikp-post-quantum-cryptography-thread-06-26/1001`) and the GDC26 report thread (`/t/…/1045`) with the repo link and the three ways to engage (nominate, propose a metric/scheme, offer a node).

Onboarding a collaborator = `docs/SIGNING.md` §1–3 (2FA, signing key registered as a *signing* key, `scripts/setup-signing.sh`, PR adding their `.allowed_signers` line), then a team membership.

## 6. Organization-level items — owners' decisions, not yours alone

You are one of eight owners and new. Rule from 2026-09-05: **no organization-wide change from this lane**; the repository carries its own controls, and organization posture goes to the owners as a proposal. The proposal, with the measured facts, the 2FA impact list, the options table, and the exact commands for whoever the owners delegate, is `~/BGIN_IKP/wg-ops/ORG_SECURITY_CONSIDERATIONS_2026-09-05.md`.

Headlines to raise (nothing enacted):

| Item | Status | Note |
|---|---|---|
| Require 2FA org-wide | off — **considered, not enacted** | would remove 2 owners + 5 outside collaborators today; path = named notice with a 30-day date, confirm the list is empty, then enable; alternative = ask the two owners privately to turn 2FA on now |
| Org defaults for new repos, scanning on existing repos, Actions allow-list, owners-only repo creation | off — options in the note | each one call, each reversible; measured that the Actions allow-list would break nothing; token read-only **would** break BGIN-Agent-Framework CI |
| DCO GitHub App | not installed | org-level install; harmless; then add `DCO` to `main.json` required checks |
| Archive dormant repos (7 last pushed 2020–2023) | idea | reduces surface and alert noise |

Repo-scoped items that remain yours (no owners' vote needed):

- Key passphrase + agent (§3), then `gh auth refresh -h github.com -r admin:org,gist` to downscope the CLI token.
- Second convener with a signing key (§2), or temporarily 0 approvals.
- `docs/SECURITY_MODEL.md` §5 currently phrases the org items as instructions; reword them as owners' decisions in a cleanup PR.

## 7. Decisions made 2026-09-05 (so nobody relitigates them)

- Repo name `pqc-agility-competition`, org `bgin-global`; staged under `mitchuski/` for a few hours only because the owner invite was pending; transferred same day.
- Licenses: CC BY 4.0 for documents, Apache-2.0 for code (ToIP convention). DCO, no CLA.
- Security posture = measured ToIP baseline **plus** required signatures on every branch and tag, code-owner review, last-push approval, no bypass. "Signed push" on GitHub = every commit signed + client pre-push hook.
- Scope rule for the testbed: pre-existing NIST-class schemes only; every integration path (C-01…C-06) is a committee ruling, not a default.
- The IKP-WG `.docx` transcript is referenced, not published.

## 8. Sources

- `resources/NEDO_PQC_Competition_Briefing_EN.pdf` + `resources/briefing-digest.md` (July 2026 community briefing; winners mid–Sep 2028 per briefing vs **March 2029** per GDC26 report — both provisional).
- GDC26 meeting report: https://bgin-global.org/news/260903-gdc26-pqc-migration · slides + MR PDFs under `/documents/meeting-reports/gdc26/`.
- Discourse: IKP PQC thread `/t/ikp-post-quantum-cryptography-thread-06-26/1001`, GDC26 report `/t/…/1045` and `/t/…/1046`, GDC 2026 thread `/t/gdc-2026-thread/1011`.
- Calendar anchors: CBT ~Sep 17 · EF Quantum Retreat Oct 9–12 · **Block 15 Oct 15–16 (PQC keynote 09:20, IKP sessions 09:50–13:00)** · CSS/BWS Oct 19–23 · **SSR co-located workshop Dec 13 (call text + "PQC-ready chain" definition)** · applications open Jan 2027 (planned).
- Trust over IP measurement (what "mirror ToIP" meant): `trustoverip/dtgwg-zkp-spec` — DCO app + EasyCLA checks, PR-only main (0 approvals), no force-push/deletion, web sign-off, org "no creations" ruleset, SHA-pinned actions, Dependabot; **no** signature requirement.
