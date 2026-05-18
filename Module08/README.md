## Virtual Environments

A virtual environment is an isolated Python installation that lives inside a folder in your project. It has its own Python interpreter and its own packages, completely separate from the system. This means you can install whatever you need without affecting the global Python installation or other projects.

#### Test 1: outside the virtual environment

Run the program directly. Python will be the system one and no virtual environment will be detected.

```bash
# test 1: outside venv
python3 construct.py
```

#### Test 2: inside the virtual environment

Each command must be executed **one by one** — never paste them all at once.

```bash
# test 2: inside venv
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 construct.py
deactivate
```

`python3 -m venv matrix_env` creates the environment inside a folder called `matrix_env/`. `source matrix_env/bin/activate` activates it in your current shell — you will see `(matrix_env)` appear at the start of your prompt as confirmation. After running the program, `deactivate` returns your shell to its normal state.

> **Important:** never commit the `matrix_env/` folder to your repository. Add it to your `.gitignore` and recreate it whenever you need it with the two commands above.

---
# Exercise 1: The Matrix Data Loader & Dependency Management

This project demonstrates how to set up, isolate, and manage external Python dependencies using two different ecosystems: the traditional approach (`pip` + `requirements.txt`) and the modern approach (`Poetry` + `pyproject.toml`).

The script `loading.py` safely verifies the environment, handles missing package errors gracefully without crashing, generates 1000 synthetic data points using **NumPy**, processes them into a **Pandas** DataFrame, and outputs a statistical plot called `matrix_analysis.png` via **Matplotlib**.

---

## STEP-BY-STEP TESTING WORKFLOW

To fully test this exercise, follow **Method 1**, then perform the **Reset/Clean** step, and finally execute **Method 2**.

---

## Method 1: Traditional Environment Management (pip)

This method uses standard Python virtual environments (`venv`) to isolate packages locally inside a folder.

### 1. Navigate to the Exercise Folder

Make sure your terminal is inside the correct directory:

```bash
cd Module08/ex1

```

### 2. Create the Virtual Environment

This creates a local folder called `matrix_env` containing a clean Python interpreter:

```bash
python3 -m venv matrix_env

```

### 3. Activate the Virtual Environment

This isolates your current terminal session so any package you install stays inside the bubble.

```bash
source matrix_env/bin/activate

```

### 4. Install Dependencies
Install the required packages by reading the classic requirements file:
```bash
pip install -r requirements.txt

```

### 5. Run the Script

Execute the program within the active environment:

```bash
python3 loading.py

```

### 6. Deactivate the Environment

Exit the virtual environment bubble safely:

```bash
deactivate

```

---

## RESET STEP: How to wipe everything clean

Before testing the modern Poetry approach, you must delete the environment and the generated image to simulate a completely fresh installation.

Run these commands in your terminal (macOS/Linux):

```bash
# 1. Delete the traditional virtual environment folder
rm -rf matrix_env/

# 2. Delete the generated output image
rm -f matrix_analysis.png

```

---

## Method 2: Modern Environment Management (Poetry)

INSTALL POETRY IN 42
```bash
curl -sSL https://install.python-poetry.org | python3 -

```

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc

```
---

This method uses Poetry to automatically handle environment creation, precise dependency locking, and package execution without manual activation.

### 1. Install Dependencies and Create Environment

Poetry reads the `pyproject.toml` file, creates its own isolated environment hidden in the system, and generates a precise lock file (`poetry.lock`). Run:

```bash
poetry install

```

### 2. Run the Script via Poetry

You do not need to manually activate any folder. Just instruct Poetry to execute the script inside its managed environment bubble:

```bash
poetry run python loading.py

```

---

## Expected Output

### When Environment is Ready (Successful Run):

When dependencies are properly loaded via `pip` or `Poetry`, the console will output:

```text
LOADING STATUS: Loading programs...
Checking dependencies:
[OK] pandas (2.3.3) - Data manipulation ready
[OK] numpy (2.2.6) - Numerical computation ready
[OK] matplotlib (3.10.8) - Visualization ready

Analyzing Matrix data...
Processing 1000 data points...
Generating visualization...
Analysis complete!
Results saved to: matrix_analysis.png

```

### When Dependencies are Missing (Safe Interception):

If you try to run the script outside an active environment or after running the reset step, the script will gracefully intercept the error and print:

```text
LOADING STATUS: Loading programs...
Checking dependencies:
[MISSING] pandas - Not found
[MISSING] numpy - Not found
[MISSING] matplotlib - Not found

ERROR: Missing dependencies detected.
To fix with pip:    pip install -r requirements.txt
To fix with Poetry: poetry install

```
