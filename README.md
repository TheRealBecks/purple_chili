# Purple Chili

Trading software with web UI and Purple Chili flavor!

## Development

Install `uv` as package installer:
```
pip install --user uv
```

### Create a local Development Environment and compile new requirements-dev.txt

Create a new virtual environment with `uv`:
```
uv venv --python 3.12
```

Activate the virtual environment, but check which `activate` file needs to be used, e.g. use `activate.fish` for the `fish` shell:
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

### Install a local Development Environment with existing requirements-dev.txt

Create a new virtual environment with `uv`:
```
uv venv --python 3.12
```

Activate the virtual environment, but check which `activate` file needs to be used, e.g. use `activate.fish` for the `fish` shell:
```
source .venv/bin/activate
```

Install development dependencies:
```
uv pip install -r requirements-dev.txt
```

Or update your already installed dependencies:
```
uv pip sync requirements-dev.txt
```

### Podman

You can use Podman or Docker. For simplicity the commands will be written for Podman. The commands for Docker may differ.

Build and start a new Podman pod:
```
podman compose up --build
```

This will create the pod `pod_purple_chili_dev`

Stop the pod with all containers by pressing `Ctrl-C` or enter:
```
podman pod stop pod_purple_chili_dev
```

Start the pod with all containers again:
```
podman pod start pod_purple_chili_dev
```

### Purple Chili App and Documentation

The Purple Chili app can now be accessed via [http://localhost:8000](http://localhost:8000).

The API endpoint documentations can be found here:
- [Swagger UI](http://localhost:8000/docs)
- [Redoc](http:/localhost:8000/redoc)
- [Logfire](https://logfire.pydantic.dev)
