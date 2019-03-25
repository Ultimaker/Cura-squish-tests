from pageobjects.common_page import PageObject
from pageobjects.cura_page import Cura
from pageobjects.printsettings_page import PrintSettings
from pageobjects.printer_page import Printer
from pageobjects.performance_page import Performance
from pageobjects.marketplace_page import Marketplace

pageObject = PageObject()
cura = Cura()
printSettings = PrintSettings()
printer = Printer()
performance = Performance()
marketplace = Marketplace()

@Given(r"Cura has been started?(.*)", regexp=True)
def step(context, configurations):
    if "with no configurations" in configurations:     
        pageObject.startCuraNoConfig()
    elif "with preset configuration" in configurations:
        pageObject.startCuraWithPresetConfig()
    else:
        pageObject.startCura()

@Given("Cura is running")
def step(context):
    cura.curaIsStarted()

@Step("A model has been sliced")
def step(context):
    cura.modelIsSliced()

@Step("I accept the user agreement")
def step(context):
    cura.acceptAgreement()

@Step("I navigate to file menu |word| and |any|")
def step(context, menuItem, subMenuItem):
    cura.navigateTo(menuItem, subMenuItem)

@Step("I navigate to stage menu |word|")
def step(context, stageItem):
    cura.navigateToStageMenu(stageItem)

@Step("I close the preferences")
def step(context):
    cura.pressCloseButton()

@Step(r"I load (file|project) '(.*)'$", regexp=True)
def step(context, type, model):
    if type == 'project':
        cura.loadFile(model)
        cura.openFileAsProject()
        cura.openFileFromSummary()
    else:
        cura.loadFile(model)

@Step("I clear the buildplate")
def step(context):
    cura.navigateTo("Edit", "Clear Build Plate")

@Step("I select the '|any|' printer and '|word|' profile")
def step(context, printerType, profile):
    printer.selectPrinter(printerType)
    printSettings.selectProfile(profile)

@Step("I save a sliced model as '|any|'")
def step(context, fileName):
    context.userData = {}
    context.userData['gcode'] = cura.saveToFile(fileName)

@Then("I close Cura from |any|")
def step(context, location):
    cura.closeCura(location)

@Given("I slice the object")
def step(context):
    cura.sliceObject()