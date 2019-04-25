from PageObjects.AddPrinterPage import AddPrinter
from PageObjects.PrinterPage import Printer
from PageObjects.CuraPage import Cura

printer = Printer()
add_printer = AddPrinter()
cura = Cura()


@Step("I can see that a |any| printer has been selected")
def step(context, expected_printer_type):
    actual_printer_type = printer.selectedPrinter()
    test.compare(expected_printer_type, actual_printer_type)


@When("I add a non-networked |any| printer")
def step(context, printer):
    add_printer.addLocalPrinter(printer)


@Step("I want to add a printer from the main menu")
def step(context):
    printer.openPrinterList()


@When("I add a network printer with address |any|")
def step(context, printer_IP):
    add_printer.addNetworkPrinter(printer_IP)
