all: build/Protokoll_V203.pdf

# hier Python-Skripte:
python/variables/T_1.npy:
	python python/einlesen.py

python/variables/T_2.npy:
	python python/einlesen.py

python/variables/p_1.npy:
	python python/einlesen.py

python/variables/p_2.npy:
	python python/einlesen.py

build/plot1.pdf: python/variables/p_2.npy python/variables/T_2.npy	|build
	python python/1bar.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V203.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchfuehrung.tex latex/disskusion.tex build/plot1.pdf | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Protokoll_V203.tex
	biber build/Protokoll_D206.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Protokoll_V203.tex
build:
	mkdir -p build

clean:
	rm -rf build

aux:
	rm -rf latex/Protokoll_V203.aux latex/Protokoll_V203.bcf latex/Protokoll_V203.log latex/Protokoll_V203.pdf latex/Protokoll_V203.run.xml latex/Protokoll_V203.toc

FORCE:

.PHONY: all clean
