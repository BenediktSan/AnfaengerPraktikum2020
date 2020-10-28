all: build/Protokoll_D206.pdf

# hier Python-Skripte:
build/plot.pdf: D206.py | build
	 python D206.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_D206.pdf: build/plot.pdf auswertung.tex  | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Protokoll_D206.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Protokoll_D206.tex
build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
