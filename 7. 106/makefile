all: build/Protokoll_V106.pdf



#hier Python-Skripte


#build/plot1.pdf:	|build
#	python python/c).py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V106.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V106.tex
	biber build/Protokoll_V106.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V106.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V106.aux Protokoll_V106.bcf Protokoll_V106.log Protokoll_V106.pdf Protokoll_V106.run.xml Protokoll_V106.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean