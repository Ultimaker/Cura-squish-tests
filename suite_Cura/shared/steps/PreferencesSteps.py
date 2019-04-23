from PageObjects.PreferencesPage import Preferences

preferences = Preferences()


@Step("I navigate to |word| in preferences")
def step(context, menuItem):
    preferences.navigateTo(menuItem)


@When("I |word| a printer from printer preferences")
def step(context, action):
    preferences.pressButton(action)


@Then("the printer overview contains a '|any|' printer")
def step(context, expectedPrinter):
    printerList = preferences.getPrinterList(expectedPrinter)
    if len(printerList) != 0:
        test.compare(expectedPrinter, printerList[0].text)
    else:
        test.fail("Printer %s not found" % expectedPrinter)


@When("I select printer |any| from the local printers")
def step(context, printerType):
    preferences.selectPrinter(printerType)


@When("I give the printer the '|any|' name")
def step(context, printerName):
    preferences.renamePrinter(printerName)


@Then("The printer is activated")
def step(context):
    preferences.verifyPrinterActivated()
