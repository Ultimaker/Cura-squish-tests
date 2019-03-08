from pageobjects.preferences_page import Preferences

preferences = Preferences()

@Step("I navigate to |word| in preferences")
def step(context, menuItem):
    preferences.navigateTo(menuItem)
    
@When("I want to |word| a printer from printer preferences")
def step(context, action):
    preferences.pressButton(action)
        
@Then("the printer overview contains a |any| printer")
def step(context, expectedPrinterType):
    printerList = preferences.getPrinterList(expectedPrinterType)
    if len(printerList) != 0:
        for n in printerList:
            test.compare(expectedPrinterType, printerList)