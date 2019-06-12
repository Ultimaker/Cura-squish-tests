from PageObjects.PreferencesPage import Preferences


preferences = Preferences()


@Step("I navigate to |word| in preferences")
def step(context, menu_item):
    preferences.navigateTo(menu_item)


@When("I select |word| printer")
def step(context, action):
    preferences.selectPreferencesMenu(action)

    if action == "Remove":
        preferences.removePrinter()


@Then("the printer overview contains a '|any|' printer")
def step(context, expected_printer):
    actual_printer = preferences.getPrinterFromList(expected_printer)
    test.compare(expected_printer, actual_printer.text)


@Then(r"printer (.*?) is not visible (?:anymore)?", regexp=True)
def step(context, printer):
    test.compare(True, preferences.verifyPrinterDeleted(printer), f"Object {printer} has been deleted")


@When("I select printer |any| from the local printers")
def step(context, printer_type):
    preferences.selectPrinter(printer_type)


@When("I give the printer the '|any|' name")
def step(context, printer_name):
    preferences.selectPreferencesMenu("Rename")
    preferences.renamePrinter(printer_name)


@Then("The printer is activated")
def step(context):
    preferences.verifyPrinterActivated()
    
@Step("I select |word| profile")
def step(context, action):
    preferences.selectPreferencesMenu(action)

@Step("I give the new profile '|word|' name")
def step(context, profile_name):
    preferences.createProfile(profile_name)

@Step("I give the duplicated profile '|word|' name")
def step(context, profile_name):
    preferences.duplicateProfile(profile_name)

@Step("I select the '|word|' profile in preferences")
def step(context, profile_name):
    preferences.selectProfile(profile_name)

@Then("the profile overview contains the profile: '|any|'")
def step(context, expected_profile):
    actual_profile = preferences.getProfileFromList(expected_profile)
    test.compare(expected_profile, actual_profile.text)
    