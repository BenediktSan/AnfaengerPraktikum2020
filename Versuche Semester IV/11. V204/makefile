all: build/Protokoll_V204.pdf



#hier Python-Skripte


#build/plot1.pdf:	|build
#	python python/c).py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V204.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V204.tex
	biber build/Protokoll_V204.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V204.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V204.aux Protokoll_V204.bcf Protokoll_V204.log Protokoll_V204.pdf Protokoll_V204.run.xml Protokoll_V204.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean