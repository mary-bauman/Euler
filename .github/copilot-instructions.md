# Guidance for AI coding agents working on this repository

This repository contains solutions (and work-in-progress) for Project Euler problems. Most solutions are small, self-contained scripts. Below are concise, actionable notes to help an AI be productive immediately.

## Big picture
- Layout: each problem usually lives in its own directory named by problem number (e.g. `82/82.py`, `31/ThirtyOne.java`). Work-in-progress problems are under `unsolved/`.
- Languages: primarily Python (Python 3), with a few Java solutions. There are some committed `.class` files alongside `.java` sources.
- Intent: individual scripts solve a single Euler problem. There is no central app or service boundary — each file is effectively an independent program.

## I/O and run conventions (important)
- Many Python scripts read from files named `in.txt` or `sampleIn.txt` that live in the same directory as the script. Others open specific filenames (check the top of the file for `open("in.txt")` or similar).
- Output is usually printed to stdout or captured in `out.txt` located in the same directory.
- Run scripts from their directory. Example patterns observed:
  - Python: change into the problem folder and run `python3 82.py` (or run the script directly; it commonly opens `in.txt` internally).
  - Java: compile with `javac ThirtyOne.java` then run `java ThirtyOne` from the same folder. If `.class` files are present they may be stale—recompile to be safe.

## Project-specific conventions and patterns
- Filenames and directories: top-level directories named by the problem number. Add new problems using the same structure (e.g., `123/123.py` or `unsolved/719/719.py`).
- Input parsing patterns:
  - CSV grids: several problems load grids with `line.split(",")` into nested lists (see `unsolved/82/82.py`).
  - Sieve/primes patterns: reusable sieve code is commonly embedded inside solution files (see `35/35.py`).
- Hardcoded parameters: many scripts set constants like `size = 80` at the top. Look for and adjust these when changing inputs.

## Integration points & dependencies
- No external package manager files (requirements.txt, package.json) are present. Assume only standard Python and JDK are required.
- No network or external APIs used by the repository.

## Editing and committing guidance
- For Python edits: run the script from its folder to validate. If a script expects `in.txt`, either create that file or modify the script to accept stdin or an argument.
- For Java edits: delete outdated `.class` files before committing, or recompile (`javac`) and commit both `.java` and updated `.class` only if necessary.
- Keep the lightweight scripting style: solutions are small; prefer minimal, single-file changes unless refactoring multiple problems.

## Examples from the codebase (use these as references)
- Grid parsing (unsolved/82/82.py):

  for line in f:
      line = line.strip()
      grid.append([int(x) for x in line.split(",")])

- Sieve example (35/35.py): contains an in-file sieve implementation returning a set of primes for later checks.

## Pitfalls and edge cases for automation
- Many scripts assume current working directory is the script's folder. Automated runners must cd into the folder or set correct paths.
- Some files are incomplete or placeholder (empty `.py` files). Check for basic content before running.
- Watch for hardcoded filenames and magic constants.

## Suggested small improvements (good first PRs)
- Add a short CONTRIBUTING.md or per-directory README describing how to run that problem's script (example I/O files and expected output).
- Normalize input handling: accept stdin or a filename CLI arg instead of always opening `in.txt`.

If anything here looks wrong or you'd like me to include CI instructions or example run scripts, tell me what to add and I'll update this file.
