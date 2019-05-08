from PageObjects.CommonPage import PageObject
from PageObjects.CuraPage import Cura
from PageObjects.PrinterSettingsPage import PrintSettings
from PageObjects.PrinterPage import Printer
from PageObjects.PerformancePage import Performance
from PageObjects.MarketplacePage import Marketplace

page_object = PageObject()
cura = Cura()
print_settings = PrintSettings()
printer = Printer()
performance = Performance()
marketplace = Marketplace()


@Given("Cura has been started")
def step(context):
    page_object.startCura()


@Given("Cura has been started with preset configurations")
def step(context):
    page_object.startCuraWithPresetConfig()


@Given("Cura has been started with no configurations")
def step(context):
    page_object.startCuraNoConfig()


@Given(r"Cura has been started with [+-]?([0-9]*[.][0-9])+ configuration", regexp=True)
def step(context, version):
    cura.startCuraConfigVersion(version)


@Given("Cura is running")
def step(context):
    cura.curaIsStarted()


@Step("A model has been sliced")
def step(context):
    cura.modelIsSliced()


@Step("I navigate to menu |word| and |any|")
def step(context, menu_item, sub_menu_item):
    cura.navigateTo(menu_item, sub_menu_item)


@Step("I navigate to stage menu |word|")
def step(context, stage_item):
    cura.navigateToStageMenu(stage_item)


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
def step(context, printer_type, profile):
    printer.selectPrinter(printer_type)
    print_settings.selectProfile(profile)


@Step("I save a sliced model as '|any|'")
def step(context, file_name):
    context.userData = {}
    context.userData['gcode'] = cura.saveToFile(file_name)


@Then("I close Cura from |any|")
def step(context, location):
    if "Marketplace" == location:
        marketplace.quitCura()
    else:
        test.fail(f"Closing cura from {location} not implemented")


@Given("I slice the object")
def step(context):
    cura.sliceObject()

@Then("I close Cura")
def step(context):
    for ctx in applicationContextList():
        ctx.detach()
@When("I open the settings bar")
def step(context):
    cura.navigateToSettings()

@When("I enable Gradual infill")
def step(context):
    cura.enableGradualInfill()



