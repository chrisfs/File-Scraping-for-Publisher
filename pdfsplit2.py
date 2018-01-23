'''
 This script I did for a publshing company. It looks through a 2000 page report on author royalties and separates it into many different documents one for each author paid during that month. The former process was to copy and paste by hand so this script speed up the process immensely
'''  

from pyPdf import PdfFileReader, PdfFileWriter
input = PdfFileReader(file("2016RoyaltyStatements0221.pdf","rb"))
current=[]
for pagenum in range(input.numPages):
    page = input.getPage(pagenum)
    current.append(page)
    text = page.extractText()
    vendorstart = text.find("As Of:")+6
    vendorend = text.find("2/21/17")
    vendor = text[vendorstart:vendorend]
    if "Total Payment Due" in text:
        output = PdfFileWriter()
        outputfile = file(vendor+".pdf","wb")
        for eachpage in current:
            output.addPage(eachpage)
        output.write(outputfile)
        outputfile.close()
        current = []


##output.addPage(input.getPage(0))
##outputStream = file("output.pdf","wb")
##output.write(outputStream)
##outputStream.close()

