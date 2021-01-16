all: build/Protokoll_V311.pdf



#hier Python-Skripte
python/variables/B_abfallend.npy:
	python python/einlesen.py

python/variables/FE_pKupfer.npy:
	python python/einlesen.py

python/variables/param1.npy:
	python python/calculate.py

build/Tabellen/U_Hall_konst_Probe_Zink.txt:
	python python/Tabellen.py


build/plot1.pdf: python/variables/B_abfallend.npy python/variables/param1.npy	|build
	python python/plotten.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/Protokoll_V311.pdf:  latex/auswertung.tex latex/theorie.tex latex/durchf.tex latex/diskussion.tex build/plot1.pdf build/Tabellen/U_Hall_konst_Probe_Zink.txt| build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V311.tex
	biber build/Protokoll_V311.bcf
	lualatex --output-directory=build --interaction=batchmode --halt-on-error latex/Protokoll_V311.tex


build:
	mkdir -p build

clean:
	rm -rf build
	
aux2:
	rm -rf Protokoll_V311.aux Protokoll_V311.bcf Protokoll_V311.log Protokoll_V311.pdf Protokoll_V311.run.xml Protokoll_V311.toc

auxv:
	rm -rf python/variables

auxt:
	rm -rf build/Tabellen

FORCE:

.PHONY: all clean