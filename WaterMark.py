import PyPDF2
import sys
input = PyPDF2.PdfFileReader(open("super.pdf", 'rb'))
watermark= PyPDF2.PdfFileReader(open("wtr.pdf", 'rb'))

writer = PyPDF2.PdfFileWriter()
for i in range(input.getNumPages()):
    print(i)
    page = watermark.getPage(0)
    wage = input.getPage(i)
    wage.mergePage(page)
    writer.addPage(wage)
with open('watermark_file.pdf', 'wb') as file:
    writer.write(file)
