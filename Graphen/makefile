all: Abgabe_Graphen.pdf

text1.txt Graph1.pdf: Graph1.py 
	python Graph1.py
Uebungsaufgaben.pdf: text1.txt Graph1.pdf
clean:
	rm -f Graph1.pdf text1.txt

.PHONY: all clean