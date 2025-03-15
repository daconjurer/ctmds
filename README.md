Commodity Trading Market Data Simulator (CTMDS)
================================================

This is a market data simulator for energy commodities with two interfaces:
- a CLI, using Typer
- a REST API, using FastAPI

Currently it can generate prices for a given day considering DST changes for the following
commodities:

- Power (electricity)
- Crude oil
- Natural gas

And the following countries:

- Great Britain (GB)
- Netherlands (NE)
- Germany (DE)
- France (FR)

To see more on the domain modelling, check out the [Domain modelling section](./docs/dm/home.md)

- [Price simulation based on the generation stack](./docs/dm/power.md) for Power (electricity).

The package uses [Poetry 2](https://python-poetry.org/). To install it, run `poetry install`.

Then the data can be generated using either interface as both share the underlying
domain models and business logic.

To see more about the REST API and its endpoints, check out the [API section](./docs/api.md).

To see more about the CLI and its commands, check out the [CLI section](./docs/cli.md).

And to see more about the dev tools available, see the [Dev Tools section](./docs/dev-tools.md).
