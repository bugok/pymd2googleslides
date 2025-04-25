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

## Run tests

Once you're in a venv, you can run the tests like so:

```
testslide tests/*.py
```

## Run the CLI

Authenticate to Google:
```
./pymd2googleslides/main.py auth
```

Authenticate to Google, allow the app to perform actions on Google slides.
After this completes, you should have a `token.json` file available
