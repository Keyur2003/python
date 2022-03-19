#practical 10
from PyPDF2 import PdfFileReader as rs
myPdf = rs(r"D:\SEM 4\python\program\University_Result.pdf")
print(myPdf.getNumPages())
print(myPdf.documentInfo)
for p in myPdf.pages:
    print(p.extractText())
print("id:20ce122")
print('name:keyur sanghani')
