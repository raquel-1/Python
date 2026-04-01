# Python

*Este proyecto ha sido creado como parte del currículo de 42 por raqroca-.*

---

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
```

## Resources

##### Inheritance:
- [DataCamp - Python Inheritance](https://www.datacamp.com/tutorial/python-inheritance)

##### @staticmethod and @classmethod:
- [Codefinity - Static and Class Methods](https://codefinity.com/courses/v2/fe5c351e-cb4a-4e9b-b4fc-ce8a7421466f/1d6d34fe-ff2b-49af-96d0-69ccefb7b03c/3e75134e-ca71-4f5f-ba23-c05b9e0a0b39)
---

**School**: 42 MADRID