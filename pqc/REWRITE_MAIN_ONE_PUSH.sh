#!/usr/bin/env bash
# One-time: replace the four GitHub-signed squash commits on main with the signed history (branch main-signed,
# identical tree, 17 commits all signed + DCO). Lifts the main ruleset to "evaluate" for ONE push, then restores it.
set -euo pipefail
export PATH="/c/Program Files/GitHub CLI:$PATH"
cd ~/pqc-agility-competition
R=repos/bgin-global/pqc-agility-competition/rulesets/22344044
[ "$(git rev-parse origin/main)" = "$(git rev-parse e277269)" ] || { echo "origin/main moved — re-check before rewriting"; exit 1; }
gh api -X PUT "$R" --input ~/BGIN_IKP/pqc/main_ruleset_evaluate_ONE_PUSH.json -q '"main ruleset enforcement: \(.enforcement)"'
git push --force-with-lease=main:e277269 origin main-signed:main
ORG=bgin-global bash scripts/bootstrap-github.sh rulesets | grep "'main'"
gh api "$R" -q '"main ruleset enforcement: \(.enforcement) rules: \([.rules[].type] | join(","))"'
git fetch origin && git checkout main && git reset --hard origin/main
scripts/verify-history.sh 31fcf5b..origin/main
git push origin --delete main-signed && git branch -D main-signed
