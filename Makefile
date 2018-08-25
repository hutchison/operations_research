.PHONY: clean

# Löscht alle von LaTeX erzeugten überflüssigen Dateien. Die PDF-Datei bleibt erhalten.
clean:
	$(RM) *.aux *.log *.fls *.out *.fdb_latexmk *.xdv

# Die Mitschrift kann man auf zwei Arten texen: einmal ganz normal mit pdflatex und einmal mit xelatex.
# XeLaTeX nutzt dabei besondere Schriftarten, die man installiert haben muss:
# * Minion Pro
# * Myriad Pro
# * Fira Mono
#
# Willst du die Mitschrift ganz normal texen, dann nutze
# $ make mitschrift_operations_research.pdf
#
# Willst du die Mitschrift ganz normal texen, aber nicht ständig make aufrufen? Dann nutze
# $ make mitschrift_operations_research.pdf-live
# Dann wird die PDF-Datei immer wieder neu generiert, wenn du sie verändert und gespeichert hast.
# Den gleichen Spaß gibt’s auch mit xelatex. Dann nutze
# $ make mitschrift_operations_research_nice.pdf
# bzw.
# $ make mitschrift_operations_research_nice.pdf-live

mitschrift_operations_research.pdf: mitschrift_operations_research.tex packages.tex
	latexmk -pdf -use-make $<

mitschrift_operations_research.pdf-live: mitschrift_operations_research.tex packages.tex
	latexmk -pdf -use-make -pvc $<

mitschrift_operations_research_nice.pdf: mitschrift_operations_research.tex packages.tex
	latexmk -pdf -xelatex -use-make $<

mitschrift_operations_research_nice.pdf-live: mitschrift_operations_research.tex packages.tex
	latexmk -pdf -xelatex -use-make -pvc $<
