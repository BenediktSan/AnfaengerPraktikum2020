all: build/Protokoll_V203.pdf

# hier Python-Skripte:

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V203.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchfuehrung.tex latex/disskusion.tex | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Protokoll_V203.tex
	biber build/Protokoll_D206.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Protokoll_V203.tex
build:
	mkdir -p build

clean:
	rm -rf build

aux:
	rm -rf Protokoll_V203.aux Protokoll_V203.bcf Protokoll_V203.log Protokoll_V203.pdf Protokoll_V203.run.xml Protokoll_V203.toc

FORCE:

.PHONY: all clean
