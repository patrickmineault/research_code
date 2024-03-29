# Slides for writing good research code good

* [Introduction and keeping things tidy](pdf/01-intro.pdf)
* [Decoupling code](pdf/02-decouple.pdf)
* [Testing](pdf/03-testing.pdf)
* [Documentation](pdf/04-docs.pdf)
* [Make it social](pdf/05-social.pdf)

# References

## Reading

- Research software engineering: [https://merely-useful.github.io/py-rse/](https://merely-useful.github.io/py-rse/)
- Making packages and testing [https://education.molssi.org/python-package-best-practices/index.html](https://education.molssi.org/python-package-best-practices/index.html)
- Carpentries testing Python: [http://carpentries-incubator.github.io/python-testing/](http://carpentries-incubator.github.io/python-testing/)
- Shablona template: [https://github.com/uwescience/shablona](https://github.com/uwescience/shablona)
- The Turing Way: [https://the-turing-way.netlify.app/reproducible-research/code-quality.html](https://the-turing-way.netlify.app/reproducible-research/code-quality.html)
- Software engineering best practices: [http://www.bris.ac.uk/acrc/acrc-training/](http://www.bris.ac.uk/acrc/acrc-training/)
- Data science in practice paper: [https://www.tandfonline.com/doi/full/10.1080/10691898.2020.1860725](https://www.tandfonline.com/doi/full/10.1080/10691898.2020.1860725)
- Software engineering for data scientists: [http://uwseds.github.io/](http://uwseds.github.io/)

## Media

- Software engineering for research: [https://www.youtube.com/watch?v=SxoDCo9iNI0&feature=emb_title](https://www.youtube.com/watch?v=SxoDCo9iNI0&feature=emb_title)
- Test and code for scientists (podcast): [https://testandcode.com/140](https://testandcode.com/140)

## Inspiration

* The Zen of Python: https://zen-of-python.info/

## Tools

* [IDEs for scientific Python](https://xcorr.net/2013/04/17/evaluating-ides-for-scientific-python/)

# Compiling these slides

Slides can be compiled with `make all`. Requires pandoc:

```
sudo apt-get install pandoc texlive texlive-latex-extra
pip install pandoc-latex-fontsize
```