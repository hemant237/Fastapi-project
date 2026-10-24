#!/data/data/com.termux/files/usr/bin/bash

# Safe Git push helper for Termux
# Usage: bash run.sh
# This script commits local changes, rebases onto origin/main, then pushes.

set -Eeuo pipefail

BRANCH="main"
REMOTE="origin"

fail() {
  echo
  echo "ERROR: $1"
  echo "No force-push was attempted. Your local commits should remain intact."
  exit 1
}

# Make sure we're running inside a Git repository.
git rev-parse --show-toplevel >/dev/null 2>&1 || fail "This folder is not inside a Git repository."
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

echo "Repository: $ROOT"
echo "Branch target: $REMOTE/$BRANCH"
echo

# Check branch.
CURRENT_BRANCH="$(git branch --show-current)"
if [[ "$CURRENT_BRANCH" != "$BRANCH" ]]; then
  fail "Current branch is '$CURRENT_BRANCH', not '$BRANCH'. Switch to main first with: git switch main"
fi

# Ensure the remote exists.
git remote get-url "$REMOTE" >/dev/null 2>&1 || fail "Git remote '$REMOTE' is not configured."

# Stage and commit tracked/new/deleted changes, including this script.
git add -A
if ! git diff --cached --quiet; then
  echo "Creating commit..."
  if ! git commit -m "Update code from Termux"; then
    fail "Could not create a commit. Check the message above."
  fi
else
  echo "No local changes to commit."
fi

echo
echo "Fetching latest remote changes..."
git fetch "$REMOTE" "$BRANCH" || fail "Fetch failed. Check your internet connection and GitHub authentication."

# Rebase local commits onto the latest remote branch.
echo
echo "Rebasing onto $REMOTE/$BRANCH..."
if ! git rebase "$REMOTE/$BRANCH"; then
  echo
  echo "Rebase stopped, usually because of a merge conflict."
  echo "Resolve the files marked by Git, then run:"
  echo "  git add <resolved-file>"
  echo "  git rebase --continue"
  echo "Then rerun: bash run.sh"
  echo
  echo "To cancel this rebase instead, run: git rebase --abort"
  exit 1
fi

# Push only after rebase succeeds.
echo
echo "Pushing to GitHub..."
git push "$REMOTE" "$BRANCH" || fail "Push failed. Check the error above; no force-push was attempted."

echo
echo "SUCCESS: Code pushed to $REMOTE/$BRANCH."
git status --short
