
# combinePDFs.py - Combine all PDFs in the current working directory into one PDF

import os, PyPDF2

pdfFiles = []
for fname in os.listdir():
    if fname.endswith(".pdf"):
        pdfFiles.append(fname)

pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
for fname in pdfFiles:
    pdfFileObj = open(fname, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages except the first one and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
pdfOutput = open("allminutes.pdf", "wb")
pdfWriter.write(pdfOutput)
pdfWriter.close()

