from PyPDF2 import PdfFileWriter, PdfFileReader
#import funkcji
output= PdfFileWriter()
#pobranie danych z plikow
plik=PdfFileReader(open('doc.pdf', 'rb'))
watermarkReader = PdfFileReader(open('watermark.pdf', 'rb'))
wm = watermarkReader.getPage(0)
#pętla
for pages in range (plik.getNumPages()):
    strona = plik.getPage(pages)
    strona.mergePage(wm)
    output.addPage(strona)
#tworzenie nowego pliku
with open ('gotowe.pdf', 'wb') as gotowe:
    output.write(zrobione)
