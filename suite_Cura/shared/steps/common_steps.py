from pageobjects.common_page import PageObject
from pageobjects.cura_page import Cura
from pageobjects.printsettings_page import PrintSettings
from pageobjects.printer_page import Printer
from pageobjects.performance_page import Performance

pageObject = PageObject()
cura = Cura()
printSettings = PrintSettings()
printer = Printer()
performance = Performance()

@Given(r"Cura has been started?(.*)", regexp=True)
def step(context, configurations):
    if "with no configurations" in configurations:     
        pageObject.startCuraNoConfig()
    else:
        pageObject.startCura()

@Given("Cura is running")
def step(context):
    cura.curaIsStarted()

@Given("Cura is running and a model has been sliced")
def step(context):
    cura.curaIsStarted()
    cura.modelIsSliced()

@Step("I accept the user agreement")
def step(context):
    cura.acceptAgreement()

@Step("I navigate to |word| and |any|")
def step(context, menuItem, subMenuItem):
    cura.navigateTo(menuItem, subMenuItem)

@Step("I load file '|any|'")
def step(context, model):
    cura.loadFile(model)   

@When("I clear the buildplate")
def step(context):
    cura.navigateTo("Edit", "Clear Build Plate")

@When("I select the '|any|' printer and '|word|' profile")
def step(context, printerType, profile):
    printer.selectPrinter(printerType)
    printSettings.selectProfile(profile)
    
@When("I save a sliced model as |any|")
def step(context, fileName):
    context.userData['gcode'] = cura.saveToFile(fileName)
    