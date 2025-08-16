# concatGitFiles - Repo-to-Text Consolidator
A simple, zero-dependency Python script that consolidates all relevant files in a repository into a single `.txt` file. This is useful for providing the full context of a codebase to Large Language Models (LLMs) or for creating a single-file archive.

## Quick Start

1.  **Create a sub-directory** in the root of the repository you want to process. For example:
    ```bash
    mkdir .repo_to_text
    ```

2.  **Place the script** (`consolidate_repo.py`) inside this new directory.

3.  **Run the script** from within that directory:
    ```bash
    cd .repo_to_text
    python consolidate_repo.py
    ```

4.  **Done!** An `output.txt` file containing the entire repository's text content will be created in the same directory.

## How It Works

The script scans its parent directory (the project root) and recursively walks through all subdirectories. It reads the content of each file and appends it to a single `output.txt` file, separated by a header indicating the original file path.

It automatically ignores:
* Common unnecessary directories (`.git`, `node_modules`, `venv`, etc.).
* The directory the script itself is in.
* Binary files and compiled objects (`.pyc`, `.dll`, `.exe`, etc.).
* The script file and its output file.

---

## Optional: Customization & Best Practices

### Customizing Ignores

You can easily customize what gets ignored by editing the lists at the top of the `consolidate_repo.py` script:
* `ignore_dirs`: Add any directory names you want to skip.
* `ignore_extensions`: Add any file extensions to exclude.
* `ignore_files`: Add specific file names to ignore.

### Git Integration

To prevent the large `output.txt` file from being committed to your project's repository, add the script's directory to your project's main `.gitignore` file.

**Example `.gitignore` entry:**
