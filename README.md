## What's `pymd2googleslides`?

This is a pet-project trying to re-implement
[md2googleslides](https://github.com/googleworkspace/md2googleslides) in Python.
It's not official by any chance, and at the time of writing this, it's in
development and is not yet working. 

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
