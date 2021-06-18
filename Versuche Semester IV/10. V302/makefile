all: build/Protokoll_V302.pdf



#hier Python-Skripte


build/plots/plot1.pdf:	|build
	python python/V302.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V302.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plots/plot1.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V302.tex
	biber build/Protokoll_V302.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V302.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_V302.aux Protokoll_V302.bcf Protokoll_V302.log Protokoll_V302.pdf Protokoll_V302.run.xml Protokoll_V302.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean