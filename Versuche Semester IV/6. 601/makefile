all: build/Protokoll_V601.pdf



#hier Python-Skripte


#build/plot1.pdf:	|build
#	python python/V601.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V601.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plot1.pdf | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V601.tex
	biber build/Protokoll_V601.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V601.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V601.aux Protokoll_V601.bcf Protokoll_V601.log Protokoll_V601.pdf Protokoll_V601.run.xml Protokoll_V601.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean