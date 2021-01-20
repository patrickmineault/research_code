OUTDIR := pdf

# This pattern excludes README.md
MD_FILES=$(wildcard *-*.md)
OUT_FILES=$(patsubst %.md, $(OUTDIR)/%.pdf, $(MD_FILES))

all : directories $(OUT_FILES)

.PHONY : clean
clean :
	rm -f $(OUTDIR)/*.pdf

$(OUTDIR)/%.pdf : %.md preamble.tex
	pandoc -t beamer -s $< -o $@ -H preamble.tex

directories : $(OUTDIR)

$(OUTDIR):
	mkdir -p $(OUTDIR)