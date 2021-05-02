all: build/Protokoll_V353.pdf



#hier Python-Skripte

python/variables/f1.npy: 
	python python/einlesen.py

build/plots/plot1.pdf:	python/variables/f1.npy	|build
	python python/V353.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V353.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plots/plot1.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V353.tex
	biber build/Protokoll_V353.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V353.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V353.aux Protokoll_V353.bcf Protokoll_V353.log Protokoll_V353.pdf Protokoll_V353.run.xml Protokoll_V353.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean