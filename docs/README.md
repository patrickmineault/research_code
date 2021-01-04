# Docs

This contains the documentation (including what I used to create slides) for my tutorial on writing good research software good.

To compile the Markdown for the slides into a slide deck, pandoc:

```
sudo apt-get install pandoc texlive-latex-base texlive-latex-recommended texlive-latex-extra
pip install pandoc-latex-fontsize
pandoc -t beamer -s slides-lecture1.md -o slides-lecture1.pdf
```