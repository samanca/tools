#!/usr/bin/python
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject

if len(sys.argv) < 2:
    sys.exit()

writer = PdfFileWriter()
for i in range(1, len(sys.argv)):
    reader = PdfFileReader(open(sys.argv[i],'rb'))
    for p in xrange(reader.numPages):
        page = reader.getPage(p)
        writer.addPage(page)
with open('merged.pdf', 'wb') as f:
    writer.write(f)
