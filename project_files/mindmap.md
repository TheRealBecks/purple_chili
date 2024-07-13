---
title: Purple Chili
markmap:
  colorFreezeLevel: 2
---

# Purple Chili

## Scope

### Custom and standardized technical indicators

### Currencies

### Instruments

### Exchanges

### Algorithmic live trading with strategies

### Multiple time frames (e.g. 1 minute, 1 hour, 1 day)

### Write custom strategies

- Predefined technical analysis functions
- Write Python strategy files
- Future: WYSIWYG editor
- ...with drag and drop blocks

### Example strategies

### Abstract broker APIs

### Web UI

- Fluid design for desktop and mobile devices
- Easy to use for non-technical users
- Data visualization (e.g. plots, charts, dashboards)
- Currently running and historic strategy runs with charts

## Potencial future scope

- Different types of assets (e.g. stocks, options, futures, cryptocurrencies, commodities)
- Different data sources (e.g. Bloomberg, FactSet, Refinitiv, Quandl, Alpha Vantage)
- Advanced analytics (e.g. machine learning, neural networks)
- Risk management
- Additional brokers

## Out of scope

- Backtesting

## Technical requirements

### Use Docker/Podman from day 1

### Write Python test cases from day 1

- Test driven development in the future?

### CI/CD from day 1

### pre-commits from day 1

### Rolling release

- Update packages frequently

### Python packages

#### Development

- [uv](https://github.com/astral-sh/uv): Python virtual environment
- [ruff](https://github.com/astral-sh/ruff): Linting, formatting
- [pyright](https://github.com/microsoft/pyright): Type checking while developing
- [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python): Creates projects from cookiecutters (project templates)
- [perflint](https://github.com/tonybaloney/perflint): Linter for performance anti patterns
- [Writing Faster Python 3](https://github.com/switowski/writing-faster-python3): Code examples for the writing faster Python 3

#### Backend

- [FastAPI](https://github.com/tiangolo/fastapi): Web framework (backend)
- [Pydantic](https://github.com/pydantic/pydantic): Python type checking at runtime
- [SQLModel](https://github.com/tiangolo/sqlmodel): ORM for FastAPI
- [Alembic](https://github.com/sqlalchemy/alembic): database migrations
- [Logfire](https://pydantic.dev/logfire): observability platform, logging, performance metrics
- [Postgres](https://github.com/postgres/postgres): SQL database
- [Redis](https://github.com/redis/redis): in-memory database that persists on disk
- [dolt](https://github.com/dolthub/dolt): Database - git for data 
- [Numba](https://github.com/numba/numba): NumPy aware dynamic Python compiler using LLVM

#### Frontend

- [FastUI](https://github.com/pydantic/FastUI): Build UIs with FastAPI and Pydantic
- [Jinja2](https://github.com/pallets/jinja/): Template engine
- [Bootstrap](https://getbootstrap.com/): Frontend toolkit
- [rich](https://github.com/Textualize/rich): Library for rich text and beautiful formatting in the terminal
- [HTMX](https://htmx.org/): HTML with AJAX, Javascript library

#### Full Stack

- [Full Stack FastAPI Template](https://github.com/tiangolo/full-stack-fastapi-template): Good examples to get FastAPI working with Docker

#### Data analysis

- [Numpy](https://github.com/numpy/numpy): Scientific computing (needed for Pandas)
- [Pandas](https://github.com/pandas-dev/pandas): Dataframes (needs Numpy)
- [Polars](https://github.com/pola-rs/polars): Dataframes
- [Ibis](https://github.com/ibis-project/ibis): Dataframes
- [Scipy](https://github.com/scipy/scipy): Scientific computing

#### Technical analysis libraries

- [TA-Lib](https://github.com/TA-Lib/ta-lib): Technical Analysis Library, C-Code
- [ta-lib-python](https://github.com/ta-lib/ta-lib-python): Official Python wrapper for TA-Lib
- [Pandas TA](https://github.com/twopirllc/pandas-ta): Can be used with or without TA-Lib, OUTDATED
- [ta](https://github.com/bukosabino/ta)

#### Data visualization libraries

- Matplotlib
- Seaborn
- Bokeh
- Plotly

#### Machine learning libraries

- scikit-learn
- TensorFlow
- PyTorch

#### Testing

- [Tox](https://github.com/tox-dev/tox): Unit testing framework
- [Nox](https://github.com/wntrblm/nox): Unit testing framework
- [pytest](https://github.com/pytest-dev/pytest/): testing framework
- [time-machine](https://github.com/adamchainz/time-machine): Travel through time in your tests
- [Faker](https://github.com/joke2k/faker): Generate fake data

### Benchmarking

- [timeit](https://docs.python.org/3/library/timeit.html): Measure execution time of small code snippets
- [pyperf](https://github.com/psf/pyperf): Toolkit to run Python benchmarks
- [pyperformance](https://github.com/python/pyperformance): The Python Benchmark Suite
- [pytest-benchmark](https://github.com/ionelmc/pytest-benchmark): py.test fixture for benchmarking code

#### CI/CD

- [Hatch](https://github.com/pypa/hatch): Modern, extensible Python project management 
- [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)
- [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
- [Latest Changes](https://github.com/tiangolo/latest-changes): https://github.com/tiangolo/latest-changes
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [oss-fuzz](https://github.com/google/oss-fuzz): Continuous Fuzzing for Open Source Software
- [clusterfuzz](https://github.com/google/clusterfuzz): Scalable fuzzing infrastructure

#### Other

- [ffn](https://github.com/pmorissette/ffn): Financial Functions for Python
- [dirty-equals](https://github.com/samuelcolvin/dirty-equals): (mis)uses the `__eq__` method to make python code (generally unit tests) more declarative and therefore easier to read and write
- [pandas_market_calendars](https://github.com/rsheftel/pandas_market_calendars): Market calendars to use with Pandas
- [OpenBBTerminal](https://github.com/OpenBB-finance/OpenBBTerminal)

## Resources

- [Awesome Python](https://github.com/vinta/awesome-python)
- [Youtube: FastAPI Course](https://www.youtube.com/watch?v=Lw-zLopB3o0&list=PL-2EBeDYMIbQghmnb865lpdmYyWU3I5F1)
- [Youtube: Fastapi with FastUI & SQLModel](https://www.youtube.com/watch?v=XTn6esHGwe0&t)
- [Youtube: Fastapi with FastUI & Pydantic](https://www.youtube.com/watch?v=eBWrnSyN2iws)
- [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)
- [uv](https://samedwardes.com/2024/04/21/python-uv-workflow/): Replacing pip with uv for Python projects

## Broker APIs

### [Alpaca](https://alpaca.markets/)

- [alpaca-py](https://github.com/alpacahq/alpaca-py): Official Alpaca Python SDK

### [brokerize](https://brokerize.com/)
### [Lemon Markets](https://www.lemon.markets/)

## Alternate projects

- [Lumibot](https://github.com/Lumiwealth/lumibot)
- [VectorBT and VectorBT Pro](https://github.com/polakowo/vectorbt)
- [nautilus_trader](https://github.com/nautechsystems/nautilus_trader)
- [tradingview-webhooks-bot](https://github.com/robswc/tradingview-webhooks-bot)
- [bt](https://github.com/pmorissette/bt)
- [pysystemtrade](https://github.com/robcarver17/pysystemtrade)
- [backtrader](https://github.com/mementum/backtrader)
- [backtrader2](https://github.com/backtrader2/backtrader)
- [basana](https://github.com/gbeced/basana)
