from pageobjects.add_printer_page import AddPrinter
from pageobjects.printer_page import Printer
from pageobjects.cura_page import Cura

printer = Printer()
addPrinter = AddPrinter()
cura = Cura()

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
    
@Step("I want to add a printer from the main menu")
def step(context):
    printer.openPrinterList()

@When("I add a network printer with address |any|")
def step(context, printerIP):
    addPrinter.addNetworkPrinter(printerIP)

@Then("the networked printer \"10.183.1.1\" is available")
def step(context):
    test.warning("TODO implement the networked printer \"10.183.1.1\" is available")