all: build/Graphen.pdf

#Python Skripte
build/Graph1.pdf: Graph1.py | build
	python Graph1.py

build/Graph2.pdf: Graph2.py | build
	python Graph2.py

#finale Pdf
build/Graphen.pdf: build/Graph1.pdf build/Graph2.pdf Graphen.tex | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Graphen.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error Graphen.tex

#Build Ordner
build:
	mkdir -p build

#delete
clean:
	rm -rf build

.PHONY: all clean