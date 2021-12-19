# Writing good research code

This repo contains the slides and code for a presentation on writing research software I first gave in January 2021 to the PhD students in neuro at Harvard. It's a compendium of 5 lessons I learned the hard way about writing research code that won't bite back.

* [The slides are here](https://github.com/patrickmineault/research_code/tree/main/docs/slides)
* The rest of the repo contains supporting code in the format advocated in the first lesson.
* You can see the full presentation recorded at [NMA 2021](https://www.crowdcast.io/e/nma2021/29) and a short version focused on testing recorded at [Brainhack MTL 2021](https://www.youtube.com/watch?v=gfPP2pQ8Rms&feature=youtu.be&ab_channel=OHBMOpenScienceSIG).

For the book version of these slides, see [goodresearch.dev](https://goodresearch.dev/).

## Organization

This repo follows the organization of [shablona](https://github.com/uwescience/shablona). All the code and tests are under `research_code`. `research_code` is itself a Python package.

For the package, we use the same setup as this tutorial on [setuptools](https://python-packaging-user-guide.readthedocs.io/tutorials/packaging-projects/), and is compatible with it - this repo is publishable to PyPI directly!

## To install the package locally in development mode

`cd` into this directory, then run:

```
pip install -e .
```

In Python:

```{python}
import research_code
```

## To test

`cd` into the `research_code/tests` directory, then run each file individually, or run `nose2`.

## CI

While shablona recommended the use of Jenkins for continuous integration (CI), we showcase instead Github actions, which don't require additional accounts/software. The workflow, which runs tests, is located in `.github/workflows/ci.yml`.

