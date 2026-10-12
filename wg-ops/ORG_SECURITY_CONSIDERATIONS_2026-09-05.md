# bgin-global organization security — considerations for the owners

Private working note (BGIN_IKP KB, not in any repo). Written 2026-09-05 by the IKP-WG co-chair's assistant after standing up `bgin-global/pqc-agility-competition`. Purpose: give the eight owners a measured picture and a set of options to decide **together**. Nothing here has been enacted at organization level; the one repository this concerns carries its own controls.

## What was measured (2026-09-05, via the GitHub API as an owner)

| Item | State |
|---|---|
| Plan | Free (no organization-level rulesets, no GitHub Advanced Security on private repos) |
| Owners | 8 — BGIN-Admin, mitchuski, RoM46, rushida, shigeya, shmatsuo, SogoHosomi, tkns1192 |
| Members | 12 total; base permission for members = read; members may create repositories |
| Two-factor authentication | **Not required.** Two owners (rushida, tkns1192) and five outside collaborators (ayako-y, henryhobin24, Siddhart-Yadav, Takaya9512, tomoy0922) have no 2FA on their accounts |
| Organization defaults for new repositories | secret scanning, push protection, Dependabot alerts, Dependabot security updates, dependency graph, web-commit sign-off: **all off** |
| Existing repositories (13 besides pqc-agility-competition) | no secret scanning, no push protection, no Dependabot alerts, no private vulnerability reporting |
| Actions policy | any action allowed in any repository; `GITHUB_TOKEN` defaults to write; Actions may approve pull requests |
| Workflows in use | only `BGIN-Agent-Framework/.github/workflows/ci.yml` (private) beyond pqc-agility-competition; it uses aquasecurity/trivy-action@master, docker/*, github/codeql-action@v2 and has no `permissions:` block |
| GitHub Apps installed | vercel only (no DCO app) |

## What was briefly changed and then reverted the same day

On 2026-09-05 the assistant enabled the six organization defaults for new repositories and turned on secret scanning, push protection, private vulnerability reporting (public repos) and Dependabot alerts (all repos). On the co-chair's instruction these were **reverted to the prior state within the hour** because organization-wide changes should be an owners' decision. Side effect that cannot be undone: any Dependabot alert emails sent during that window.

`bgin-global/pqc-agility-competition` keeps its own settings (scanning, push protection, private reporting, restricted Actions, signed commits, rulesets). Four teams were created for it (`pqc-conveners`, `pqc-maintainers`, `pqc-evaluation`, `pqc-testbed`); they touch nothing else.

## The 2FA question — considered, not enacted

- **What enforcement does:** GitHub removes every member and outside collaborator without 2FA from the organization at the moment it is switched on; they can rejoin after enabling 2FA. Today that would remove two owners and five collaborators.
- **Why it matters here:** an owner account without 2FA is the single biggest risk to every BGIN repository, including the competition record; a compromised owner can rewrite settings, rulesets and history.
- **What is already true without enforcement:** GitHub requires 2FA for anyone who contributes code on github.com (rolled out 2023–2024), so most active contributors have it. The pqc-agility-competition repository additionally requires signed commits from registered keys, which an attacker without the key cannot produce.
- **Suggested path if the owners agree:** (1) message the seven people by name with a date at least 30 days out; (2) confirm on the day with `gh api "orgs/bgin-global/members?filter=2fa_disabled"` and the outside-collaborators variant that the list is empty; (3) enable "Require two-factor authentication" in Organization settings → Authentication security; (4) record the decision in BGIN's own governance minutes.
- **Alternative if not yet:** ask the two owners individually to enable 2FA now; no organization setting changes.

## Other options for the owners (each one call, each reversible, none enacted)

| Option | Effect | Risk / who is affected |
|---|---|---|
| Organization defaults for **new** repositories (scanning, push protection, Dependabot, dependency graph) | future repos start protected | none for existing repos |
| Secret scanning + push protection on existing **public** repos | blocks pushes that contain a detected secret; alerts on ones already committed | contributors to those repos see a block on a bad push; that is the intended behaviour |
| Dependabot alerts on existing repos | emails to admins about vulnerable dependencies | noise on old repos (several last pushed 2020–2021); consider archiving those instead |
| Actions allow-list (GitHub-owned + verified creators + `aquasecurity/*`, `docker/*`, `ossf/*`) | third-party actions outside the list cannot run | measured: nothing currently in use would break |
| `GITHUB_TOKEN` default read-only | workflows must declare the permissions they need | **would break** BGIN-Agent-Framework CI's SARIF upload until its workflow gets a `permissions:` block |
| Actions may not approve pull requests | closes a known bypass of review rules | none measured |
| Members cannot create repositories (owners can) | repositories go through owners, as Trust over IP does by ruleset | four non-owner members lose self-service creation |
| Install the DCO GitHub App | independent sign-off check on any repo that opts in | none |
| Archive dormant repositories (genesis-documents, sgip, igwg, meeting-materials-and-miniutes, bgin-shared-templates, github-playground, bgin-global-web-at-github-io; last pushed 2020–2023) | read-only, no more alerts or pushes | none if they are truly dormant |

## Commands (for whoever the owners delegate)

```bash
export PATH="/c/Program Files/GitHub CLI:$PATH"
# defaults for new repos
gh api -X PATCH orgs/bgin-global -F secret_scanning_enabled_for_new_repositories=true -F secret_scanning_push_protection_enabled_for_new_repositories=true -F dependabot_alerts_enabled_for_new_repositories=true -F dependabot_security_updates_enabled_for_new_repositories=true -F dependency_graph_enabled_for_new_repositories=true
# actions allow-list + no PR approvals by the token (token default left at write on purpose)
gh api -X PUT orgs/bgin-global/actions/permissions --input - <<<'{"enabled_repositories":"all","allowed_actions":"selected"}'
gh api -X PUT orgs/bgin-global/actions/permissions/selected-actions --input - <<<'{"github_owned_allowed":true,"verified_allowed":true,"patterns_allowed":["aquasecurity/*","docker/*","ossf/*"]}'
gh api -X PUT orgs/bgin-global/actions/permissions/workflow --input - <<<'{"default_workflow_permissions":"write","can_approve_pull_request_reviews":false}'
# owners-only repository creation
gh api -X PATCH orgs/bgin-global -F members_can_create_repositories=false
# who still lacks 2FA (run before any enforcement)
gh api "orgs/bgin-global/members?filter=2fa_disabled" -q '.[].login'
gh api "orgs/bgin-global/outside_collaborators?filter=2fa_disabled" -q '.[].login'
```
