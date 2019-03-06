from pageobjects.preferences_page import Preferences

preferences = Preferences()

@Step("I navigate to |word| in preferences")
def step(context, menuItem):
    preferences.navigateTo(menuItem)
    
@When("I want to |word| a printer from |any|")
def step(context, action, location):
    if "printer preferences" == location:
        preferences.pressButton(action)
        
@Then("the printer overview contains a |any| printer")
def step(context, printerType):
    printerList = preferences.getPrinterList()
    test.compare(expectedPrinterType, printerList)