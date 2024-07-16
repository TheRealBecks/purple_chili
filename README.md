# Purple Chili

Trading software with web UI and Purple Chili flavor!

# Development

Install `uv` as package installer:
```
pip install --user uv
```

## Create a local Development Environment and compile requirements-dev.txt

Create a new virtual environment with `uv`:
```
uv venv --python 3.12
```

Activate the virtual environment:
```
source .venv/bin/activate
```

Compile the development dependencies:
```
uv pip compile pyproject.toml --quiet --extra dev -o requirements-dev.txt
```

Install development dependencies:
```
uv pip install -r requirements-dev.txt
```

## Install a local Development Environment with existing requirements-dev.txt

Create a new virtual environment with `uv`:
```
uv venv --python 3.12
```

Activate the virtual environment:
```
source .venv/bin/activate
```

Install development dependencies:
```
uv pip install -r requirements-dev.txt
```
