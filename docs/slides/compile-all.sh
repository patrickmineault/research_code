#!/bin/bash
pandoc -t beamer -s 01-intro.md -o 01-intro.pdf -H preamble.tex
pandoc -t beamer -s 02-decouple.md -o 02-decouple.pdf -H preamble.tex
pandoc -t beamer -s 03-testing.md -o 03-testing.pdf -H preamble.tex
pandoc -t beamer -s 04-docs.md -o 04-docs.pdf -H preamble.tex
pandoc -t beamer -s 05-social.md -o 05-social.pdf -H preamble.tex