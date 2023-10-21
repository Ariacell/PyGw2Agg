# Setup

Start a venv python -m venv venv

Activate the venv with ./venv/Scripts/activate

poetry install

# Building a release

```
pyinstaller --onefile pygw2agg/main.py
```

This will create a /dist/main/main.exe file that can be executed to run the application in standalone mode.
