# Git Guide — AI Engineer Bootcamp

This project is **already** a Git repository connected to GitHub
(`origin` → `github.com/hemant237/Fastapi-project`, branch `main`).

You do **NOT** need to:

- create a new GitHub repository
- run `git init` again
- add the remote again (`git remote add ...`)
- push `.venv` (it's ignored on purpose)
- upload files manually on the GitHub website

## Daily workflow

```powershell
cd C:\AI-Engineer-Bootcamp

git status                         # 1. what changed?
git add .                          # 2. stage everything (ignored files are skipped automatically)
git status                         # 3. review what's staged...
git diff --cached                  #    ...and the exact changes (press q to quit)
git commit -m "Describe the change"   # 4. commit
git push                           # 5. send to GitHub
```

Before `git commit`, glance at the staged list. If you see `.env`, `.venv`, passwords, keys or
database dumps, **stop** (see "A secret was accidentally staged" below).

## The Python environment is NOT on GitHub

`.venv` is large and machine-specific, so it's ignored. `requirements.txt` is committed instead.
On another computer (or after deleting `.venv`), recreate it with Python 3.12:

```powershell
git clone https://github.com/hemant237/Fastapi-project.git AI-Engineer-Bootcamp
cd AI-Engineer-Bootcamp
py -3.12 -m venv .venv            # or: python -m venv .venv  (if python is 3.12)
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

After installing a new package, update the list and commit it:

```powershell
python -m pip install package_name
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
```

Secrets live in `.env` files, which are ignored. On a new computer, create them again by hand.
Never commit them.

## Common situations

**See what changed**
```powershell
git status              # which files
git diff                # exact line changes (not staged yet)
git diff --cached       # exact line changes (staged)
```

**See previous commits**
```powershell
git log --oneline -10
git show <commit-hash>      # details of one commit
```

**Branch is behind** ("Your branch is behind 'origin/main'"): someone (or you, on another
computer or on the GitHub website) pushed changes. Get them first:
```powershell
git pull
```

**`git push` is rejected** ("Updates were rejected... fetch first"): same cause.
```powershell
git pull
git push
```
Never use `git push --force` to "fix" this. It can delete work on GitHub.

**Merge conflicts** (after `git pull`, Git says CONFLICT):
1. `git status` shows the conflicted files.
2. Open each one in VS Code. It highlights the conflict and lets you choose
   *Accept Current* / *Accept Incoming* / *Accept Both*.
3. Save, then:
```powershell
git add .
git commit -m "Resolve merge conflict"
git push
```
If you'd rather back out of the merge completely: `git merge --abort`.

**A file was accidentally staged** (not committed yet):
```powershell
git restore --staged path\to\file
```
The file stays on disk; it's just no longer staged. Add it to `.gitignore` if it should never be committed.

**A secret was accidentally staged** (not committed yet):
```powershell
git restore --staged path\to\secret_file
```
Then add the file to `.gitignore`. If it was already **committed or pushed**, removing it in a new
commit is not enough, because it stays in the history. **Change the password or key immediately**, then
ask for help cleaning the history.

**Accidentally modified many files** (and want to throw those edits away):
```powershell
git status                      # look first!
git diff                        # make sure you really don't want these changes
git restore path\to\file        # discard changes in one file
git restore .                   # discard ALL unstaged changes (cannot be undone)
```
Brand-new untracked files are not affected by `git restore`. Delete them yourself if needed.

**Create a new branch** (to try something without touching `main`):
```powershell
git switch -c my-experiment            # create and switch
git push -u origin my-experiment       # first push of the new branch
git switch main                        # go back to main
```
