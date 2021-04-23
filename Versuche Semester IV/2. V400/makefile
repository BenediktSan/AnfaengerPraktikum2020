all: build/Protokoll_V400.pdf



#hier Python-Skripte


build/plot1.pdf:	|build
	python python/V400.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V400.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plot1.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V400.tex
	biber build/Protokoll_V400.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V400.tex


build:
	mkdir -p build

clean:
	rm -rf build


txt:
	python python/einlesen.py

#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V400.aux Protokoll_V400.bcf Protokoll_V400.log Protokoll_V400.pdf Protokoll_V400.run.xml Protokoll_V400.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean