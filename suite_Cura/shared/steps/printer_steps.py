source(findFile("scripts", "pageobjects/printer_page.py"))
source(findFile("scripts", "pageobjects/add_printer_page.py"))
printer = Printer()
addPrinter = AddPrinter()

@Step("I add a |any| printer")
def step(context, printerType):
    addPrinter.select(printerType)
    addPrinter.add()

@Then("I can see that a |any| printer has been selected")
def step(context, expectedPrinterType):
    actualPrinterType = printer.selectedPrinter()
    test.compare(expectedPrinterType, actualPrinterType)
