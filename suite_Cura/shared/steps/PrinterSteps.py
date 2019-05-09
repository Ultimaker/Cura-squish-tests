from PageObjects.AddPrinterPage import AddPrinter
from PageObjects.PrinterPage import Printer
from PageObjects.CuraPage import Cura
from PageObjects.PreferencesPage import Preferences

preferences = Preferences()
printer = Printer()
add_printer = AddPrinter()
cura = Cura()


@Step("An |any| printer has been selected")
def step(context, printer_type):
    actual_printer_type = printer.selectedPrinter()
    test.compare(printer_type, actual_printer_type)


@When(r"I add a non-networked (.*) printer?(.*)", regexp=True)
def step(context, printer_type, location):
    if "onboarding screen" in location:
        add_printer.addLocalPrinterFromOnb(printer_type)
    else:
        add_printer.addLocalPrinter(printer_type)


@Step("I want to add a printer from the main menu")
def step(context):
    printer.openPrinterList()


@When("I add a network printer with address |any|")
def step(context, printer_IP):
    add_printer.addNetworkPrinter(printer_IP)


@Step("|integer| Printers are present")
def step(context, expected_count):
    printer.navigateToPrinterPreferences()
    printer_list = preferences.getPrinterListSize()
    test.compare(expected_count, printer_list)
    cura.pressCloseButton()


@Step("It is possible to switch to single extruder printer |any|")
def step(context, printer_type):
    test.compare(2, printer.getExtruderCount())
    printer.selectPrinter(printer_type)
    test.compare(1, printer.getExtruderCount())
