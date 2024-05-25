---
title: Purple Chili
markmap:
  colorFreezeLevel: 2
---

# Purple Chili

## Scope

### Algotithmic trading (with strategies)

### Write custom strategies

- Predefined technical analysis functions
- Write Python strategy files
- Future: WYSIWYG editor
- ...with drag and drop blocks

### Abstract broker APIs

### Web UI

- Fluid design for desktop and mobile devices
- Easy to use for non-technical users

## Out of scope

- Backtesting

## Technical requirements

### Use Docker/Podman from day 1

### Write Python test cases from day 1

### CI/CD from day 1

### pre-commits from day 1

### Rolling release

- Update packages frequently

### Python packages

#### Mandatory

- [uv](https://github.com/astral-sh/uv): Python virtual environment
- [ruff](https://github.com/astral-sh/ruff): linting, formatting
- [FastAPI](https://github.com/tiangolo/fastapi): Web framework (backend)
- [Pydantic](https://github.com/pydantic/pydantic): Python type checking at runtime
- [pyright](https://github.com/microsoft/pyright): Type checking while developing
- [SQLModel](https://github.com/tiangolo/sqlmodel): ORM for FastAPI
- [FastUI](https://github.com/pydantic/FastUI): Build UIs with FastAPI and Pydantic
- [Jinja2](https://github.com/pallets/jinja/): Template engine
- [Bootstrap](https://getbootstrap.com/): Frontend toolkit
- [Logfire](https://pydantic.dev/logfire): observability platform, logging, performance metrics
- [Postgres](https://github.com/postgres/postgres): SQL database

#### Optional / to be discussed / needs to be evaluated

- [Full Stack FastAPI Template](https://github.com/tiangolo/full-stack-fastapi-template): Good examples to get FastAPI working with Docker
- [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)
- [perflint](https://github.com/tonybaloney/perflint)
- [Writing Faster Python 3](https://github.com/switowski/writing-faster-python3)
- [Numba](https://github.com/numba/numba)
- [Redis](https://github.com/redis/redis)
- [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)
- [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- HTMX
- [Tox](https://github.com/tox-dev/tox): Unit testing framework
- [Nox](https://github.com/wntrblm/nox): Unit testing framework

## Resources

- [Awesome Python](https://github.com/vinta/awesome-python)

## Broker APIs

- [Alpaca](https://alpaca.markets/)
- [brokerize](https://brokerize.com/)
- [Lemon Markets](https://www.lemon.markets/)