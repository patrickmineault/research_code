# How packages actually work

Pip and packages are wonderful, but they can obscure what's going on behind the 
scenes. How do packages actually work?

## Packages and modules

Let's say we have a directory `mylib` with one module inside (a module is a normal Python file with functions):

```
mylib/
|- code.py
```

Inside `code.py`, there's a function:

```{.python}
def the_fun():
    print("Hello world")
```

Now let's assume the base directory `.` is on Python's search path. This creates the implicit package `mylib`. Hence, you can import code like so:

```{.python}
from mylib.code import the_fun
```

## Python's search path

But wait, where does Python search for code? Several places:

* The current directory `os.getcwd()`
* Directories listed in `sys.path`
* Directories listed in the environment variable `PYTHONPATH`

When you install a package listed in PyPI with `pip`, it puts a copy of that folder somewhere that's on the path. For example, when I use the conda environment 
`py3`, it puts new packages in:

`/home/pmin/anaconda3/envs/py3/lib/python3.8/site-packages`

This location is listed in `sys.path`. Hence, if I `pip install seaborn`, I will find a copy of seaborn inside that directory:

```{.shell}
(py3) pmin@desktop:~/anaconda3/envs/py3/lib/python3.8/site-packages/seaborn$ ls -al
total 780
drwxr-xr-x   6 pmin pmin   4096 Dec 28 16:21 .
drwxr-xr-x 438 pmin pmin  20480 Jan  8 14:00 ..
-rw-r--r--   1 pmin pmin    744 Dec 28 16:21 __init__.py
drwxr-xr-x   2 pmin pmin   4096 Dec 28 16:21 __pycache__
-rw-r--r--   1 pmin pmin  52671 Dec 28 16:21 _core.py
-rw-r--r--   1 pmin pmin   2126 Dec 28 16:21 _decorators.py
-rw-r--r--   1 pmin pmin   5861 Dec 28 16:21 _docstrings.py
-rw-r--r--   1 pmin pmin  14699 Dec 28 16:21 _statistics.py
-rw-r--r--   1 pmin pmin   2139 Dec 28 16:21 _testing.py
-rw-r--r--   1 pmin pmin   4483 Dec 28 16:21 algorithms.py
...
```

## What if I want to use my homebrew library somewhere else?

Let's say your `mylib` code is in `/path/to/mylib/code.py`. You want to import it from `/home/me/projecto/script.py`. You need to figure out a way to place it on Python's search path. Before we discuss the ideal solution, let's make sure we understand what's going on by discussing other partial solutions.

### (bad) copy `code.py` to `/home/me/projecto/mylib/code.py`

This works, but then you have two copies of your code, and it can rapidly become a maintenance nightmare. 

### (not great) create a symlink

A better idea is to create a symlink from `/home/me/projecto/mylib -> /path/to/mylib`. You can do 

`ln -s /path/to/mylib /home/me/projecto/mylib`

This works, but it can be a pain to manage if you use multiple computers or you're sharing your code with somebody else.

### (not great) Change `sys.path` during execution

Add your library code to `sys.path` temporarily. At the top of your script, use:

```{.python}
import sys
# Assuming the code is in /my/great/library/code.py
sys.path.append('/my/great/') 

from library import code
```

Note that once you exit the script, `sys.path` will return to its original value.

This works, but it will mess up code completion and linting in your favorite editor, because the dependency is injected at runtime. 

## Create a package and install it in development mode

We can create a package and install in development mode (`pip install -e`). For that, we need a few files:

```
setup.py
mylib/
|- __init__.py
|- code.py
```

* `setup.py` contains minimal code to setup a package. This will suffice:

```{.python}
from setuptools import setup

setup(
    name='minipkg',
    version='0.0.1',
    author='An Awesome Coder',
    author_email='patty.mcgoo@example.com',
    packages=setuptools.find_packages(),
    scripts=[],
    url='https://github.com/patrickmineault/minimal-package',
    license='LICENSE.txt',
    description='An awesome package that does nothing',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)
```

* Finally, the existence of an empty `__init__.py` tells setuptools that there's a package in that directory.

When you `pip install -e .`, it will add the current directory `.` to sys.path. Hence, you can now import the package from anywhere. The name of the folder (in this case `mylib`) determines the name of the package. 

## Removing one level from imports

It may feel a bit unwieldy to have to have to write `from mylib.code import the_fun`. We can shorten that to `from mylib import the_fun` by changing the contents of `__init__.py` to:

```{.python}
from .code import *
```

This will lift the symbols inside of code, including `the_fun`, to a package-level symbol. This is a [common pattern in Python packages](https://github.com/mwaskom/seaborn/blob/master/seaborn/__init__.py).

## `src` and all that

Some authors prefer putting the package code two levels down, i.e. inside `src/mylib`. This prevents polluting the package namespace with unnecessary symbols; see [this blog post for an explanation](https://blog.ionelmc.ro/2014/05/25/python-packaging/).

# Further reading

* http://andrewsforge.com/article/python-new-package-landscape/
* https://blog.ionelmc.ro/2014/05/25/python-packaging/