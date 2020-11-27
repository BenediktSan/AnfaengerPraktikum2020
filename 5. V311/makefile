all: build/Protokoll_V311.pdf



#hier Python-Skripte


#build/plot1.pdf:	|build
#	python python/c).py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V311.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V311.tex
	biber build/Protokoll_V203.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V311.tex


build:
	mkdir -p build

aux2:
	rm -rf Protokoll_V311.aux Protokoll_V311.bcf Protokoll_V311.log Protokoll_V311.pdf Protokoll_V311.run.xml Protokoll_V311.toc

auxv:
	rm -rf python/variables
FORCE:

.PHONY: all clean