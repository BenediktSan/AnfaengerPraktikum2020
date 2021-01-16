all: build/Protokoll_V354.pdf



#hier Python-Skripte

build/a.png:	|build
	python python/calculate.py

build/d.png:	|build
	python python/calculate.py


# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V354.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V703.tex
	biber build/Protokoll_V703.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V703.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V703.aux Protokoll_V703.bcf Protokoll_V703.log Protokoll_V703.pdf Protokoll_V703.run.xml Protokoll_V703.toc texput.log

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
	
FORCE:

.PHONY: all clean