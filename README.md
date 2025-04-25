## Running in venv

Create the venv:

```
python -m venv .venv
```

Activate venv:
```
source .venv/bin/activate
```

After activation, your shell will indicate that you're running inside a venv:
```
(.venv) $
```

Install the development dependencies
```
pip install -e .[dev]
```

Deactivate the venv:
```
deactivate
```
