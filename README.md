# Writing good research code good

This repo contains example code that illustrates several points in a tutorial on write good research code good.

## Organization

This repo follows the organization of [shablona](https://github.com/uwescience/shablona). It also uses the same setup as this tutorial on [setuptools](https://python-packaging-user-guide.readthedocs.io/tutorials/packaging-projects/).

## To install the package locally in development mode

`cd` into this directory, then run:

```{python}
pip install -e .
```

In Python:

```
import example_pkg
```

## To test

`cd` into the `research_code/tests` directory, then run each file individually, or run `nosetests`.

Under WSL, permissions for files are elevated; you will need to run for nosetests:

```
nosetests --exe
```