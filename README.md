*Este proyecto ha sido creado como parte del currículo de 42 por raqroca-.*

# Python  💻 🐍 👍


## Python Script Setup & Execution (Linux)


#### 1. Install flake8
```bash
python3 -m pip install flake8
```

#### 2. Run flake8
```bash
python3 -m flake8
```

#### 3. Run a Python file
```bash
python3 ft_hello_garden.py
```

#### 4. Run as executable

##### Step 1: Add shebang at the top of your file
```python
#!/usr/bin/env python3
```

##### Step 2: Give execution permission
```bash
chmod +x ft_hello_garden.py
```

##### Step 3: Run it
```bash
./ft_hello_garden.py
```

#### 5. Add the main entry point

Make sure your file includes:

```python
if __name__ == "__main__":
    ft_hello_garden()
```
---

## Run mypy
```bash
pip install --user mypy

python3 -m mypy --strict ft_hello_garden.py 

python3 -m mypy --strict .
```

## Virtual Environments

A virtual environment is an isolated Python installation that lives inside a folder in your project. It has its own Python interpreter and its own packages, completely separate from the system. This means you can install whatever you need without affecting the global Python installation or other projects.

#### Test 1: outside the virtual environment

Run the program directly. Python will be the system one and no virtual environment will be detected.

```bash
# Prueba 1: fuera del venv
python3 construct.py
```

#### Test 2: inside the virtual environment

Each command must be executed **one by one** — never paste them all at once.

```bash
# Prueba 2: dentro del venv
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 construct.py
deactivate
```

`python3 -m venv matrix_env` creates the environment inside a folder called `matrix_env/`. `source matrix_env/bin/activate` activates it in your current shell — you will see `(matrix_env)` appear at the start of your prompt as confirmation. After running the program, `deactivate` returns your shell to its normal state.

> **Important:** never commit the `matrix_env/` folder to your repository. Add it to your `.gitignore` and recreate it whenever you need it with the two commands above.

---

## Resources

- [DataCamp - Python Inheritance](https://www.datacamp.com/tutorial/python-inheritance)

- [Codefinity - Static and Class Methods](https://codefinity.com/courses/v2/fe5c351e-cb4a-4e9b-b4fc-ce8a7421466f/1d6d34fe-ff2b-49af-96d0-69ccefb7b03c/3e75134e-ca71-4f5f-ba23-c05b9e0a0b39)

- [Python Tutorial](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)

- [What is __Init__.Py File in Python?](https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/)

- [El Libro De Python](https://ellibrodepython.com/)
---

**School**: 42 MADRID