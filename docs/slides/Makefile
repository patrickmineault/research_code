OUTDIR := pdf

all : directories $(OUTDIR)/01-intro.pdf $(OUTDIR)/02-decouple.pdf $(OUTDIR)/03-testing.pdf $(OUTDIR)/04-docs.pdf $(OUTDIR)/05-social.pdf

.PHONY : clean
clean :
	rm -f $(OUTDIR)/*.pdf

$(OUTDIR)/01-intro.pdf : 01-intro.md preamble.tex
	pandoc -t beamer -s 01-intro.md -o $(OUTDIR)/01-intro.pdf -H preamble.tex

$(OUTDIR)/02-decouple.pdf: 02-decouple.md preamble.tex
	pandoc -t beamer -s 02-decouple.md -o $(OUTDIR)/02-decouple.pdf -H preamble.tex

$(OUTDIR)/03-testing.pdf: 03-testing.md preamble.tex
	pandoc -t beamer -s 03-testing.md -o $(OUTDIR)/03-testing.pdf -H preamble.tex

$(OUTDIR)/04-docs.pdf: 04-docs.md preamble.tex
	pandoc -t beamer -s 04-docs.md -o $(OUTDIR)/04-docs.pdf -H preamble.tex

$(OUTDIR)/05-social.pdf: 05-social.md preamble.tex
	pandoc -t beamer -s 05-social.md -o $(OUTDIR)/05-social.pdf -H preamble.tex

directories : $(OUTDIR)

$(OUTDIR):
	mkdir -p $(OUTDIR)