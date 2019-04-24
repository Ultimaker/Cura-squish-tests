from PageObjects.PreferencesPage import Preferences

preferences = Preferences()


@Step("I navigate to |word| in preferences")
def step(context, menu_item):
    preferences.navigateTo(menu_item)


@When("I |word| a printer from printer preferences")
def step(context, action):
    preferences.selectPrinterMenu(action)


@Then("the printer overview contains a '|any|' printer")
def step(context, expected_printer):
    printer_list = preferences.getPrinterList(expected_printer)
    if len(printer_list) != 0:
        test.compare(expected_printer, printer_list[0].text)
    else:
        test.fail("Printer %s not found" % expected_printer)


@When("I select printer |any| from the local printers")
def step(context, printer_type):
    preferences.selectPrinter(printer_type)


@When("I give the printer the '|any|' name")
def step(context, printer_name):
    preferences.renamePrinter(printer_name)


@Then("The printer is activated")
def step(context):
    preferences.verifyPrinterActivated()
