all: build/Protokoll_V702.pdf



#hier Python-Skripte


#build/plot1.pdf:	|build
#	python python/c).py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V702.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V354.tex
	biber build/Protokoll_V354.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V354.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V702.aux Protokoll_V702.bcf Protokoll_V702.log Protokoll_V702.pdf Protokoll_V702.run.xml Protokoll_V702.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean