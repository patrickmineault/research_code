# Writing good research code good

TODO: Make a Jupyterbook out of this

- Who am I?
    - Open source experiences
    - No formal CS training
    - Google SWE and Facebook research scientist
    - Organizer of NMA
    - Occasionally taught CS
- Writing research code

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled.png)

- Who is this for?
    - Not CS students
    - People who picked up programming more or less by accident
- Inspirations
    - Zen of Python
    - data scientist as scientist
    - move fast and break things
    - 12 factors
    - full stack deep learning
    - anti-patterns
- Why is research code hard to write
    - Endpoint is unclear
    - "correct" can be hard to define
    - Lots of exploration and dead ends
    - Sometimes, there are manual steps involving human judgement
    - Many people that do code for research are not trained in CS or programming
- Low judgement zone
    - It's ok to write garbage code when you're in a rush
    - It's not ok to keep building more and more on top of garbage code
        - sure, there's the moral imperative to create replicable code to bring forward the shining light of science and truth...
        - ...but also, do you want to have to scrap 6 months of research because your awful code does something silly?
            - "[https://en.wikipedia.org/wiki/Growth_in_a_Time_of_Debt](https://en.wikipedia.org/wiki/Growth_in_a_Time_of_Debt)" - Reinhart–Rogoff

            ![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%201.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%201.png)

            ![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%202.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%202.png)

        [https://www.bbc.com/news/magazine-22213219](https://www.bbc.com/news/magazine-22213219)

        ![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%203.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%203.png)

        - I've wasted months of my life cursing my own bad code, don't be like me
    - When I say "you should" or "you shouldn't", those are just recommendations, maybe you know better, or maybe you have a deadline to hit
    - Clean things up later!

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%204.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%204.png)

## Grand scheme of things

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%205.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%205.png)

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%206.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%206.png)

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%207.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%207.png)

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%208.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%208.png)

- Lifecycle of research code
    - Create data
        - Psychophysics, EEG, ECoG, fMRI, ephys, calcium imaging, human labeling, simulations, etc.
        - Towards the goal of testing a hypothesis or something
    - Ingest the data
    - Apply transformations to the data
    - Fit models to the data
    - Test hypotheses
    - Generate plots
    - Write the paper
    - (receive the reviews and rewrite the paper)
    - (pass down the code to the next grad student down the pipe)

0. Principles [Ev Federenko]

Ivanova et al. [2020]

CP: code programming

SP: sentence programming

SR: sentence reading

NR: non-word reading

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%209.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%209.png)

- You have to write for your future self in mind
    - Future you will have forgotten 90% of what you wrote
    - You have to be twice as smart to debug code as to write it
        - Never write code that's as a smart as you can make it
- You need to conserve your working memory
    - Reduce the cognitive load of understanding your code
    - mental model for understanding and debugging code:
        - cognitive task in which you have to juggle lots of things in your WM
        - when there's too many pieces of information you have to keep in working memory, you start to lose track of other important pieces of information
        - you then have to refer to non-WM (i.e. stackoverflow, your codebase) to get back on track
        - eventually your productivity trends towards zero
        - e.g. [https://imgur.com/gallery/UNhWQiV](https://imgur.com/gallery/UNhWQiV)
    - simple is better than complex, but complex is better than complicated
        - cyclomatic complexity (number of linearly independent paths in a program)
    - Don't optimize code

1. Organize different code projects according to a convention

I was given the swim test: everything at Google is one giant monorepo with billions of lines of code ([https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext#FNE](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext#FNE)). Everything is organized according to strict (sometimes downright pedantic) conventions, such that "it's not that bad" to jump. [https://github.com/google/styleguide/blob/gh-pages/pyguide.md](https://github.com/google/styleguide/blob/gh-pages/pyguide.md). Also, to become a reviewer, you need to obtain readability ([https://www.pullrequest.com/blog/google-code-review-readability-certification/](https://www.pullrequest.com/blog/google-code-review-readability-certification/)), which is a kind of ritualized hazing in which one is taught the ways of Google-y-ness. To this day, I manually alphabetically sort my imports.

Suggested by Turing Way:

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2010.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2010.png)

Suggested by Research Software Engineering with Python (originally from Noble 2009):

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2011.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2011.png)

[https://github.com/uwescience/shablona](https://github.com/uwescience/shablona)

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2012.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2012.png)

- Convention over configuration
- E.g. React project:
    - lots of code, always in the same folders
- One project → one git repo
    - If you don't use git yet, start doing it now
    - Take a weekend to learn it
- Analysis → Start with a Capital Letter.ipynb
- Reusable functions and packages, etc. → lower letter with underscores .py
- Tests under tests folder
- Extends beyond just project organization
    - Consistency of style (PEP8)
        - flake8 vs. pylint (vscode)
    - Consistency of documentation style (Google vs. numpy)
        - Preference for Google
- Checks off future you and WM
- Exercise: let's create a project with the right structure

2. Avoid the great mush

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2013.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2013.png)

- Maybe your code is written in a way where you're doing a little bit of everything all at once

e.g `wave_clus` 

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2014.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2014.png)

This is a callback for a function in a GUI for spike sorting.

- Does many things at once
    - Manipulates the GUI
    - Modifies data
    - Reads a jpg file?
- Uses magic numbers and magic columns
- Various string formatting and exec
- Big function
- Not complex, but it's complicated
- That's bad because your code becomes really hard to reason about
    - Tightly coupled
- Are the results weird because:
    - the data is bad
    - you're loading the data wrong
    - your model is incorrectly implemented
    - your model is inappropriate for the data
    - you statistical tests are inappropriate for the data distribution
- Are your results good because...
- Keep each of the boxes separate with minimal interface
    - Separation of concerns:
        - example: your data loading function should just load data
        - Your computation functions shouldn't load data, they should just compute
- Make each of the boxes small
    - don't make giant monolithic functions
    - Make functions which are small
        - a screen's worth
            - 80 columns, 50 lines
- Avoid side effects, prefer pure functions
    - What's a side effect?
    - In computer science, an operation, function or expression is said to have a side effect if it modifies some state variable value(s) outside its local environment, that is to say has an observable effect besides returning a value (the main effect) to the invoker of the operation. State data updated "outside" of the operation may be maintained "inside" a stateful object or a wider stateful system within which the operation is performed. Example side effects include modifying a non-local variable, modifying a static local variable, modifying a mutable argument passed by reference, performing I/O or calling other side-effect functions.
    - Example: fib
- Learn more about your language
    - Sometimes (but not always!), code smells come from lack of knowledge
    - E.g. using magic column numbers in a raw numpy array rather than named columns in pandas because you don't know pandas
    - Using unnamed dimensions in numpy rather than xarray
    - Using + and bespoke code rather than the one true solution, the f-string
- E.g. implementing CKA
- Checks off WM

3. Build around testing

Ariel Rokem

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2015.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2015.png)

- Oftentimes we write code to convince ourselves that our other code works
- E.g. I write a spiffy function that fits a GLM with Tikhonov regularization
    - I make up some test data
    - I run my model
    - It gives me the correct outputs
- At the end, I either delete that code (if it's a tiny amount of tests) or I let it rot in a notebook somewhere.
    - Don't do that!
- 70% of bugs will be old bugs that keep reappearing
- Formalize how you write your code through tests
    - Unit tests
        - micro tests
            - inline `assert`
        - unit tests
            - unittest
            - pytest
            - nose
        - Integration tests
            - "big tests"
- How to use a test runner
- Run them periodically
- Lesson: tested code is low-stress code
- Just learned recently:
    - You can even test figures! pytest-mpl
- Practical assignment:
    - 10 next times you comment out a print statement: transform it into an assert
- Checks off WM

4. Make notes to future yourself

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2016.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2016.png)

- Documentation
    - docstrings
        - Controversial opinion: docstrings are overrated. Tests often form better documentation.
    - README.md
    - tests
    - Keep a lab book
        - Notion
- Checks off future self

5. Work with better people than you

- Maybe you're the best coder in your lab so you don't have opportunities for growth
    - Contribute to open source projects
        - NMA & NMC are always happy to have more people!
    - Join a community or hackerspace
- Maybe you're starting out
    - Pair programming!
    - Actively seek resources
        - Julia Evans @b0rk
- Two anecdotes
    - Ctrl+R
    - Michael Waskom's CI for NMA
- Checks off future self

6. Use good tools

- You won't become proficient without actively seeking for it
    - E.g. navigational queries on Google
- Take off days where you learn tool X

# Examples list

precision = 1000

x0 = (self.wx[mask].reshape(-1, 1, 1) +

torch.randn(len(mask), precision, 1) * self.wsigmax[mask].reshape(-1, 1, 1))

y0 = (self.wy[mask].reshape(-1, 1, 1) +

torch.randn(len(mask), precision, 1) * self.wsigmax[mask].reshape(-1, 1, 1))

## Advanced topics

- Configuration and .env
- Environments
- Dockerfiles
- CI
- Packaging
- Cloud stuff
- Reproducibility

# Resources

- Data science in practice paper: [https://www.tandfonline.com/doi/full/10.1080/10691898.2020.1860725](https://www.tandfonline.com/doi/full/10.1080/10691898.2020.1860725)
- Making packages and testing [https://education.molssi.org/python-package-best-practices/index.html](https://education.molssi.org/python-package-best-practices/index.html)
- Carpentries testing Python: [http://carpentries-incubator.github.io/python-testing/](http://carpentries-incubator.github.io/python-testing/)
- Software engineering for research: [https://www.youtube.com/watch?v=SxoDCo9iNI0&feature=emb_title](https://www.youtube.com/watch?v=SxoDCo9iNI0&feature=emb_title)
- Computer code and the brain: [https://twitter.com/neuranna/status/1251589731932135425](https://twitter.com/neuranna/status/1251589731932135425)
- Software engineering best practices: [http://www.bris.ac.uk/acrc/acrc-training/](http://www.bris.ac.uk/acrc/acrc-training/)
- The Turing Way: [https://the-turing-way.netlify.app/reproducible-research/code-quality.html](https://the-turing-way.netlify.app/reproducible-research/code-quality.html)
- Software engineering for data scientists: [http://uwseds.github.io/](http://uwseds.github.io/)
- Test and code for scientists (podcast): [https://testandcode.com/140](https://testandcode.com/140)
- Research software engineering: [https://merely-useful.github.io/py-rse/](https://merely-useful.github.io/py-rse/)
- Shablona template: [https://github.com/uwescience/shablona](https://github.com/uwescience/shablona)

![Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2017.png](Writing%20good%20research%20code%20good%20981f87fd9a8d4b6b9499195e98e55b08/Untitled%2017.png)