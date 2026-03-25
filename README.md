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

con el mypy:
instalar : pip install --user mypy
ejecutar : python3 -m mypy --strict ft_hello_garden.py 

---

**School**: 42 MADRID