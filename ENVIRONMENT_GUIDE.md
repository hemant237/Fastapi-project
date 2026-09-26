# Environment Guide — AI Engineer Bootcamp

## 1. Which Python does this project use?

**One environment for the whole project:**

```
C:\AI-Engineer-Bootcamp\.venv\Scripts\python.exe      (Python 3.12)
```

Every `.py` file, notebook, test and FastAPI app in this folder uses it. It was built from the
standard python.org Python 3.12 (`C:\Users\heman\AppData\Local\Programs\Python\Python312`).

Your other Pythons (Anaconda, Python 3.13) are still installed and untouched. This project just doesn't use them.

## 2. Activate it

```powershell
cd C:\AI-Engineer-Bootcamp
.\.venv\Scripts\Activate.ps1
```

You'll see `(.venv)` at the start of your prompt. New terminals opened *inside VS Code* do this automatically.

## 3. Deactivate it

```powershell
deactivate
```

## 4. Install a new package

```powershell
python -m pip install package_name
```

Then save it to the requirements file so it can be recreated later:

```powershell
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
```

## 5. Why `python -m pip` instead of `pip`?

`pip` is just "whichever pip.exe Windows finds first", and that might belong to Python 3.13 or Anaconda.
`python -m pip` means "the pip that belongs to **this** python". The package always lands in
the same Python that will run your code. That mismatch is exactly what caused your old problems.

## 6. Check which Python is running

```powershell
python -c "import sys; print(sys.executable)"
```

It must print `C:\AI-Engineer-Bootcamp\.venv\Scripts\python.exe`. In a notebook, run `import sys; print(sys.executable)` in a cell.

## 7. Check where a package is installed

```powershell
python -m pip show catboost          # look at the "Location:" line
python -c "import catboost; print(catboost.__file__)"
```

Both paths should contain `C:\AI-Engineer-Bootcamp\.venv\`.

## 8. Create a new Python file

Just create it anywhere in the project, e.g. `practice\new_model.py` or `projects\new_project.py`.
**No setup needed.** It automatically uses `.venv`. Don't create a new environment.

## 9. Run a Python script

```powershell
python practice\new_model.py
```

Or press the ▶ Run button in VS Code.

## 10. Run pytest

```powershell
cd C:\AI-Engineer-Bootcamp\projects\01-Hello-FastAPI
python -m pytest tests
```

Or use the Testing (flask icon) panel in VS Code, which is already configured to run these tests.
(The tests use the remote database in `projects\01-Hello-FastAPI\.env`, so they can be slow.)

## 11. Start FastAPI

```powershell
cd C:\AI-Engineer-Bootcamp\projects\01-Hello-FastAPI
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## 12. Use Jupyter

- **In VS Code:** open a `.ipynb` file → click the kernel name (top-right) → *Select Another Kernel* →
  *Jupyter Kernel* → **AI-Engineer-Bootcamp (.venv)**. (Picking *Python Environments* → `.venv` works too.)
- **In the browser:** `python -m jupyter notebook`

Older notebooks may remember a kernel called "base" (Anaconda) or ".venv (3.14…)". Switch those to
**AI-Engineer-Bootcamp (.venv)** once and save the notebook.

## 13. Select the correct VS Code interpreter

This is normally automatic (`.vscode\settings.json` points at `.venv`). To check or fix it:
`Ctrl+Shift+P` → **Python: Select Interpreter** → choose `.\.venv\Scripts\python.exe`.
The bottom-right status bar should show `3.12.x ('.venv')`.

## 14. I see `ModuleNotFoundError`

1. Check which Python is running (section 6). If it isn't `.venv`, fix the interpreter/kernel (sections 12–13).
2. If it *is* `.venv`, the package simply isn't installed: `python -m pip install package_name`.
3. For notebooks: restart the kernel after installing.

## 15. pip says a package is installed, but `import` fails

That means pip and your code are using **different Pythons**. Compare:

```powershell
python -m pip --version                              # which Python pip belongs to
python -c "import sys; print(sys.executable)"        # which Python runs your code
```

Get both pointing at `.venv` (activate it, and select the `.venv` interpreter/kernel), then install
again with `python -m pip install package_name`.

## 16. Recreate the environment (if `.venv` gets deleted or broken)

```powershell
cd C:\AI-Engineer-Bootcamp
Remove-Item -Recurse -Force .venv          # only if a broken one is still there
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name ai-engineer-bootcamp --display-name "AI-Engineer-Bootcamp (.venv)"
```

---

## ⛔ DO NOT DO THIS

- **Don't create a new environment for every `.py` file.** One `.venv` serves the whole project.
- **Don't install packages into Anaconda** (`conda install ...` or Anaconda's pip) for this project.
- **Don't install packages into Python 3.13** (plain `pip install` from a non-activated terminal does this!).
- **Don't pick a different VS Code interpreter or kernel per file.** Always `.venv`.
- **Don't use bare `pip`.** Always `python -m pip`.
- **Don't delete Python installations to fix one project.** Fix the interpreter selection instead.
