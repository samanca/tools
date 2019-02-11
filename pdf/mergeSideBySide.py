#!/usr/bin/python
import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

if len(sys.argv) != 4:
    sys.exit()

in1,in2,out = sys.argv[1:]

output = PdfFileWriter()
input1 = PdfFileReader(file(in1, 'rb'))
input2 = PdfFileReader(file(in2, 'rb'))

m = min(input1.getNumPages(),input2.getNumPages())
print('common pages', m)
for i in range(0, m):
    print('adding common page',i)
    p1 = input1.getPage(i)
    p2 = input2.getPage(i)
    offset_x = p1.mediaBox[2]
    offset_y = 0
    p1.mergeTranslatedPage(p2, offset_x, offset_y, expand=True)
    output.addPage(p1)

print('adding non-common pages')
for j in range(i + 1, input1.getNumPages()):
    print('adding', j, 'from first')
    output.addPage(input1.getPage(j))
for j in range(i + 1, input2.getNumPages()):
    print('adding', j, 'from second')
    p0 = output.addBlankPage(p1.mediaBox[2], p1.mediaBox[3])
    offset_x = p1.mediaBox[2]
    offset_y = 0
    p0.mergeTranslatedPage(input2.getPage(j), offset_x, offset_y)

outputStream = file(out, 'wb')
output.write(outputStream)
outputStream.close()
