all: build/main.pdf

# hier Python-Skripte:

build/rechteck.pdf: rechteck.py matplotlibrc header-matplotlib.tex csv/rechteck.csv | build
	TEXINPUTS=$$(pwd): python rechteck.py

build/dreieck.pdf: dreieck.py matplotlibrc header-matplotlib.tex csv/dreieck.csv | build
	TEXINPUTS=$$(pwd): python dreieck.py

build/saegezahn.pdf: saegezahn.py matplotlibrc header-matplotlib.tex csv/saegezahn.csv | build
	TEXINPUTS=$$(pwd): python saegezahn.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/saegezahn.pdf build/dreieck.pdf build/rechteck.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
