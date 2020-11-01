all: build/Protokoll_D206.pdf

# hier Python-Skripte:
build/plot1.pdf: D206.py | build
	 python D206.py

build/plot2.pdf: D206.py | build
	 python D206.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_D206.pdf: build/plot1.pdf build/plot2.pdf auswertung.tex theorie.tex  | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Protokoll_D206.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Protokoll_D206.tex
build:
	mkdir -p build

clean:
	rm -rf build

aux:
	rm -rf Protokoll_D206.aux Protokoll_D206.bcf Protokoll_D206.log Protokoll_D206.pdf Protokoll_D206.run.xml Protokoll_D206.toc

FORCE:

.PHONY: all clean
