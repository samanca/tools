#!/usr/bin/python
import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

if len(sys.argv) < 1:
    sys.exit()

for i in range(1, len(sys.argv)):
    writer = PdfFileWriter()
    reader = PdfFileReader(sys.argv[i])
    for p in xrange(reader.numPages):
        page = reader.getPage(p)
        page.compressContentStreams()
        writer.addPage(page)

    fileName = os.path.splitext(sys.argv[i])[0] + '-compressed.pdf'
    with open(fileName, 'wb') as f:
        writer.write(f)
