from PageObjects.AddPrinterPage import AddPrinter
from PageObjects.PrinterPage import Printer
from PageObjects.CuraPage import Cura

printer = Printer()
add_printer = AddPrinter()
cura = Cura()


@Step("An |any| printer has been selected")
def step(context, expected_printer_type):
    actual_printer_type = printer.selectedPrinter()
    test.compare(expected_printer_type, actual_printer_type)


@When(r"I add a non-networked (.*) printer?(.*)", regexp=True)
def step(context, printer, location):
    if "onboarding screen" in location:
        add_printer.addLocalPrinterFromOnb(printer)
    else:
        add_printer.addLocalPrinter(printer)


@Step("I want to add a printer from the main menu")
def step(context):
    printer.openPrinterList()


@When("I add a network printer with address |any|")
def step(context, printer_IP):
    add_printer.addNetworkPrinter(printer_IP)

@Then("|integer| Printers are present")
def step(context, expected_count):
    printer.navigateToPrinterPreferences()
    test.compare(expected_count, printer.retrievePrinterCount())

@Then("It is possible to switch to a single extruder printer")
def step(context):
    test.warning("TODO implement switching to a single extruder printer succeeds")
