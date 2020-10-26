all: build/Graph1.pdf 

build/text1.txt build/Graph1.pdf: Graph1.py |build
	python Graph1.py

#Uebungsaufgaben.pdf: text1.txt Graph1.pdf
build:
	mkdir -p build

clean:
	#rm -f Graph1.pdf text1.txt
	rm -rf build

.PHONY: all clean