#!/bin/bash
pandoc -t beamer -s 01-intro.md -o 01-intro.pdf
pandoc -t beamer -s 02-decouple.md -o 02-decouple.pdf
pandoc -t beamer -s 03-testing.md -o 03-testing.pdf