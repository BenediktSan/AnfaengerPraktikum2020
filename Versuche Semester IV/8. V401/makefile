all: build/Protokoll_V401.pdf



#hier Python-Skripte


build/plot1.pdf:	|build
	python python/V401.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V401.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plot1.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V401.tex
	biber build/Protokoll_V401.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V401.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V401.aux Protokoll_V401.bcf Protokoll_V401.log Protokoll_V401.pdf Protokoll_V401.run.xml Protokoll_V401.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean