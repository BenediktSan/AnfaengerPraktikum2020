all: build/Protokoll_V603.pdf



#hier Python-Skripte


build/plots/plot1.pdf:	|build
	python python/V603.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V603.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plots/plot1.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V603.tex
	biber build/Protokoll_V603.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V603.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V603.aux Protokoll_V603.bcf Protokoll_V603.log Protokoll_V603.pdf Protokoll_V603.run.xml Protokoll_V603.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean