# Duck typing : It is concept where the type of an object is determined
#               by its behaviouor(function),not by its class

class InkjetPrinter:
    def printdocument(self,document):
        print("Inkjet printer printing : ",document)

class LaserPrinter:
    def printdocument(self,document):
        print("Laser printer printing : ",document)

class PDFWriter:
    def printdocument(self,document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.printdocument("Marvllous Notes")  

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()          




# desgin pattern