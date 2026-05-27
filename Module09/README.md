# EX0

```bash
cd ex0/

# Create a virtual environment
python3 -m venv venv

# Enable it (Linux/Mac)
source venv/bin/activate

# Install Pydantic v2
pip install pydantic

# lists all the packages installed in your venv
# and writes them to the file requirements.txt
pip freeze > requirements.txt

deactivate
```

After git clone:
```bash
cd ex0/
python3 -m venv venv
source venv/bin/activate

# -r: read and install
pip install -r requirements.txt
```

> mypy and flake8 are dev tools, install manually if needed:
> `pip install mypy flake8`


# EX1
```bash
cd ../ex1/

# Create a virtual environment specific for ex1
python3 -m venv venv

# Enable it (Linux/Mac)
source venv/bin/activate

# Install Pydantic v2
pip install pydantic

# Lists all the packages installed and writes them to ex1's requirements.txt
pip freeze > requirements.txt

deactivate
```

After git clone:
```bash
cd ex1/
python3 -m venv venv
source venv/bin/activate

# Install the exact same versions for ex1
pip install -r requirements.txt
```

# EX2
```bash
cd ../ex2/
python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt
```

```bash
# Para ver si te has dejado algún espacio raro o línea larga:
flake8 .

# Para verificar que no te falte ningún tipo de dato:
mypy .
```