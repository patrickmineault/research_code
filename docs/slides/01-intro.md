% Intro
% Good research code
% Patrick Mineault

# 

Intro

# Who is this lecture for?

![](../figures/tweet.png)

# Who is this lecture for?

* Most people who do coding-heavy research are not trained in CS or software engineering
* You're probably in this bucket
* Bad consequences:
    * You feel like you don't know what you're doing
    * Imposter syndrome
    * Low productivity
    * Bugs
    * You hate your code and you don't want to work on it
    * You never graduate
    * You have great sadness in your heart
* It doesn't have to be all bad!

# My weird perspective

* Patrick Mineault, PhD in neuroscience
* (wildly underqualified) software engineer at Google
* [Research scientist at Facebook Reality Labs on brain-computer interfaces](https://tech.fb.com/imagining-a-new-interface-hands-free-communication-without-saying-a-word/)
* [Helped build NMA as first year CTO](https://xcorr.net/2021/03/25/building-neuromatch-academy/)
* [Independent researcher](https://xcorr.net/) and technologist
* Occasionally taught CS

# Regrets, I've had a few

* Mostly self-taught in programming
* Didn't study CS until very late
* Wasted months working with bad code of my own making
* Not a great coder, but better than in grad school
* I think you might be curious

# Organization

* Assume that you know a little bit about [Python](https://swcarpentry.github.io/python-novice-inflammation/), [git](http://swcarpentry.github.io/git-novice/) and the [command line](http://swcarpentry.github.io/shell-novice/)
    * You can catch up on these topics via Software Carpentries
    * If you don't, that's ok! This is vertically integrated advice. Get inspired, follow more detailed tutorials after, and come back to this.
* 5 practical tips to better code
    * Concrete examples
    * 5-minute action items
    * Everybody leaves having learned an actionable thing
* Interrupt me and chat!
* But first, I will indulge in theory...

# Open question

Q: What does coding look like in the brain?

# Coding is very working-memory intensive

![Code and working memory in the brain, Ivanova et al. (2020)](../figures/wm-federenko.png)

# Coding is very working-memory intensive

* MD: Multiple-demand system
* CP: code programming
* SP: sentence programming
* SR: sentence reading
* NR: non-word reading

# Consequence

You will get [overloaded](https://imgur.com/gallery/UNhWQiV).

# Principle 1: conserve your WM

- Reduce the cognitive load of understanding your code
- [Simple is better than complex. Complex is better than complicated.](https://zen-of-python.info/simple-is-better-than-complex.html#3)

# Research code is very LTM-intensive

![Theory](../figures/lifecycle_simple.png){height=250px}

# Research code is very LTM-intensive

![Practice](../figures/lifecycle_complex.png){height=250px}

# Research code

- Endpoint is unclear
- Correct can be hard to define
- Lots of exploration and dead ends
- Sometimes, there are manual steps involving human judgement
- You have to remember all the dead ends for the code to even make sense

# Principle 2: write for your future self in mind

- Future you will have forgotten 90% of what you wrote
- Kernighan's Law - Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.

# Thesis

Writing good research code boils down to saving your memory - both working and long-term.

---

# 

Practical Lessons

# Disclaimer: this is a low-judgement zone

- It's ok to write garbage code when you're in a rush
- It's not ok to keep building more and more on top of garbage code
    - sure, there's the moral imperative to create replicable code to bring forward the shining light of science and truth...
    - [and yes, people have messed up the world real bad](https://www.nytimes.com/2013/04/19/opinion/krugman-the-excel-depression.html) by doing things fast and loose
    - but also, do you want to scrap 6 months of research because you forgot to transpose a matrix?
    - you will get bitten back
- Guidelines not rules

# Lesson 1: keep things tidy

![](../figures/mary-kondo.jpg)

# What needs to be tidy

* Project folder structure
* Code style
* Notebooks
* Scripts
* Prereq: Git & Github: if you're going to keep things clean, you will mess up and need a time machine.

# Project folder structure

* Consensus: one repo = one project $\approx$ one paper
* Lots of templates around:
  * [Turing Way](https://the-turing-way.netlify.app/reproducible-research/compendia.html#executable-compendium)
  * [Research Software Engineering with Python](https://merely-useful.github.io/py-rse/getting-started.html#getting-started-structure)
  * [Data science cookiecutter](https://drivendata.github.io/cookiecutter-data-science/)
  * [Shablona](https://github.com/uwescience/shablona)

# Shablona

![Shablona](../figures/shablona.png){height=220px}

# Shablona

* Lightweight, good starter template
* Keeps docs, data, scripts and code tidy and in their own little box
* You can `import shablona` to access the code in the packages
* [Use as a template to start a new project via big green button](https://github.com/uwescience/shablona)
* Or build it from scratch to understand the moving pieces
* **Important**: Is compatible with Python packaging. That means you can install locally with `pip install -e .`, and the code inside the special folder (placeholder: `shablona`) becomes a package `shablona`

# 

Live demo

# Packages, how do they work?

Whatever template you use, make sure it makes a local package for your code that you can `pip install`. That will make it easier to re-use your code in other places.

[If you're curious, I wrote a long-form note on how packages really work](../notes/how_packages_work.md).

# Other conventions

- Notebooks → `Start with a Capital Letter.ipynb`
- Reusable functions and packages, etc. → `snake_case.py`
- Tests under `tests` folder

# Organizing scripts

![From [Van Vliet (2020)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007358)](../figures/pcbi.1007358.g002.PNG_L.png){height=220px}

# Organizing scripts

* Use filenames that indicate hierarchy, e.g. `00_fetch_data.py`
  * One issue: you can't `import` these scripts because you can't start a module name with a digit.
  * Start with an underscore, `_00_fetch_data.py`, or with a prefix, `step_00_fetch_data.py`, those are valid module names
* Figure code separate from processing steps code, e.g. `figure_csd.py`
* Use a master script to bind everything together
  * Plain Python
  * Bash files
  * Build tools: `doit`, `make`
  * Specialized tools like `nipype`

# Code style

* Use a consistent style
* [Python has a style guide - PEP8](https://www.google.com/search?channel=crow2&client=firefox-b-d&q=pep8). 
  * Indentation
  * Line length
  * Spaces
  * Variable names
  * imports
* [Orgs like Google have their even more pedantic style guides](https://google.github.io/styleguide/pyguide.html).
* There are linters and auto-formatters which will catch style issues
  * flake8
  * pylint
  * black
* Install them in VSCode

# Docstrings

[Numpy style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html) or [Google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

```{.python}
def my_doubler(x):
    """Doubles x.

    Args:
        x: the number to double

    Returns:
        Twice x
    """
    return x * 2
```

# IPython notebooks

> If you use notebooks to develop software, you are probably using the wrong tool. -- [Yihui Xie](https://yihui.org/en/2018/09/notebook-war/)

* Notebooks are hard to keep tidy because of nonlinear execution
* Restart and Run All is your friend
* If your notebook doesn't run top to bottom - it's not reproducible
* It's ok to write plotting code in a notebook, but don't write real functions.
* Import the code from your installable package (see `shablona` above)
* You can auto-reload your package code when it changes, makes development easier. In a cell:

```{.python}
%load_ext autoreload
%autoreload 2
```

# Why does this matter?

You don't have to constantly ask yourself where stuff is, how you should do thing X, etc. and that allows you to focus on the stuff that matters.

# Aside: day 3

Everything at Google is one giant monorepo with [billions of lines of code](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext#FNE). By ~day 3, it was time to go do a code. Everything is organized according to strict [conventions](https://github.com/google/styleguide/blob/gh-pages/pyguide.md), so it's not *that bad* to jump in. 

# Lesson 1

* Keep things tidy
* Free your W&LTM from having to remember where stuff is
* Your 5-minute exercise: use the `shablona` template for a project

---