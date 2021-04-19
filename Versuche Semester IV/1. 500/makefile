all: build/Protokoll_500.pdf



#hier Python-Skripte


build/gelb.pdf:	|build
	python python/calculate.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_500.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex latex/auswertung.tex build/gelb.pdf| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_500.tex
	biber build/Protokoll_500.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_500.tex


build:
	mkdir -p build

clean:
	rm -rf build


#Zusätzliche Ordner/Dateien löschen
aux2:
	rm -rf Protokoll_500.aux Protokoll_500.bcf Protokoll_500.log Protokoll_500.pdf Protokoll_500.run.xml Protokoll_500.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen	
FORCE:

.PHONY: all clean