Simple script to generate random decimal numbers in the `[0, 100)` range.
At the minute there is a basic iterator function and a function that uses
Numpy.

The package uses [Poetry](https://python-poetry.org/). To install it, run:

```
poetry install
```

Then run:

```
poetry run python3 generator.py <num-of-elements>
```

where `num-of-elements` is the number of elements to generate (e.g. 100000).

To run the tests:

```
poetry run pytest tests --full-trace
```
