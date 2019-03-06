from pageobjects.add_printer_page import AddPrinter
from pageobjects.printer_page import Printer

printer = Printer()
addPrinter = AddPrinter()

@Step("I add a |any| printer")
def step(context, printerType):
    addPrinter.select(printerType)
    addPrinter.add()

@Step("I can see that a |any| printer has been selected")
def step(context, expectedPrinterType):
    actualPrinterType = printer.selectedPrinter()
    test.compare(expectedPrinterType, actualPrinterType)
    
@Step("I finish the Add Printer wizard")
def step(context):
    addPrinter.finish()

