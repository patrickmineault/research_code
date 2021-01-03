# Packaging user guide

Running the https://python-packaging-user-guide.readthedocs.io/tutorials/packaging-projects/ as a tutorial.

## To install this package locally in development mode

`cd` into this directory, then run:

```{python}
pip install -e .
```

In Python:

```
import example_pkg
```

## To test

`cd` into the `tests` directory, then run each file individually, or run `nosetests`.

Under WSL, permissions for files are elevated; you will need to run:

```
nosetests --exe
```

