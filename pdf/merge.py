#!/usr/bin/python
import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import reportlab

tmp = '__tmp.pdf'

def createPagePdf(fileNames, tmp, pageSize):
    c = canvas.Canvas(tmp)
    for name in fileNames:
        c.setFont("Helvetica", 10)
        c.drawString(2 * mm, 2 * mm, name)
        c.setPageSize(pageSize)
        c.showPage()
    c.save()
    return
    with open(tmp, 'rb') as f:
        pdf = PdfFileReader(f)
        layer = pdf.getPage(0)
    return layer

if len(sys.argv) < 2:
    sys.exit()

fileNames = []
pageSize = (0, 0)
for i in range(1, len(sys.argv)):
    fileNames.append(sys.argv[i])

overlayPDF = ''
writer = PdfFileWriter()
for i in range(1, len(sys.argv)):
    reader = PdfFileReader(open(sys.argv[i],'rb'))
    if i == 1:
        page = reader.getPage(0)
        pageSize = (page.mediaBox[2], page.mediaBox[3])
        createPagePdf(fileNames, tmp, pageSize)

    with open(tmp, 'rb') as ftmp:
        overlayPdf = PdfFileReader(ftmp)
        overlayPage = overlayPdf.getPage(i - 1)
        for p in xrange(reader.numPages):
            page = reader.getPage(p)
            page.mergePage(overlayPage)
            writer.addPage(page)

with open('merged.pdf', 'wb') as f:
    writer.write(f)

os.remove(tmp)
