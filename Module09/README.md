<h1><font color="reen">EX0</font></h1>

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