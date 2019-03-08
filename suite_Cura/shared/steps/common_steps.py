from pageobjects.page_object import PageObject
from pageobjects.cura_page import Cura

pageObject = PageObject()
cura = Cura()

@Given(r"Cura has been started?(.*)", regexp=True)
def step(context, configurations):
    if "with no configurations" in configurations:     
        pageObject.startCuraNoConfig()
    else:
        pageObject.startCura()

@Given("Cura is running")
def step(context):
    cura.curaIsStarted()

@Step("I accept the user agreement")
def step(context):
    cura.acceptAgreement()
    
@Step("I navigate to |word| and |any|")
def step(context, menuItem, subMenuItem):
    cura.navigateTo(menuItem, subMenuItem)