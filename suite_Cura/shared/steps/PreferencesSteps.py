from PageObjects.PreferencesPage import Preferences

preferences = Preferences()


@Step("I navigate to |word| in preferences")
def step(context, menu_item):
    preferences.navigateTo(menu_item)


@When("I select |word| printer")
def step(context, action):
    preferences.selectPrinterMenu(action)

    if action == "Remove":
        preferences.removePrinter()


@Then("The printer overview contains a '|any|' printer")
def step(context, expected_printer):
    actual_printer = preferences.getPrinterFromList(expected_printer)
    test.compare(expected_printer, actual_printer['text'])


@Then(r"Printer (.*?) is not visible (?:anymore)?", regexp=True)
def step(context, printer):
    test.compare(True, preferences.verifyPrinterDeleted(printer), f"Object {printer} has been deleted")


@When("I select printer |any| from the local printers")
def step(context, printer_type):
    preferences.selectPrinter(printer_type)


@When("I give the printer the '|any|' name")
def step(context, printer_name):
    preferences.selectPrinterMenu("Rename")
    preferences.renamePrinter(printer_name)


@Then("The printer is activated")
def step(context):
    preferences.verifyPrinterActivated()
