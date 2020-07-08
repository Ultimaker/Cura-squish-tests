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


@Step("I restart Cura")
def step(context):
    page_object.restartCura()
<<<<<<< Updated upstream
=======
  
    
@Step("I restart Cura with a project file as argument")
def step(context):
    page_object.restartCuraWithArguments()

>>>>>>> Stashed changes

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


@Step("I select the '|any|' printer with |word| intent and '|any|' profile")
def step(context, printer_type, intent, profile):
    printer.selectPrinter(printer_type)
    print_settings.selectProfile(intent, profile)


@Step("I save a sliced model as '|any|'")
def step(context, file_name):
    cura.saveToFile(file_name)


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


@When("I open Print Settings")
def step(context):
    cura.openPrintSettings()

@Step("I close the extruder selector")
def step(context):
    cura.selectExtruderTab("0") # NOTE: Only if already open!

# @Then("I select the [1-8] extruder", regexp=True)
@When("I select the |any| extruder")
def step(context, extruder_nr):
    cura.selectExtruderTab(extruder_nr)

@Step("the |any| nozzle is of type '|any|'")
def step(context, extruder_nr, nozzle_type):
    assert(cura.checkNozzleTypeText(extruder_nr, nozzle_type))

<<<<<<< Updated upstream
=======

@Then("the |any| nozzle is of type '|any|'")
def step(context, extruder_nr, nozzle_type):
    assert(cura.checkNozzleTypeText(extruder_nr, nozzle_type))

>>>>>>> Stashed changes
@When("I select printcore '|any|'")
def step(context, print_core):
    cura.selectPrintCore(print_core)

@Then("the setting '|any|' in '|any|' is '|any|'")
def step(context, setting_name, setting_tab, setting_value):
    print_settings.checkTextboxSetting(setting_tab, setting_name, setting_value)

@When("I show all settings")
def step(context):
    print_settings.showAllSettings()
    
@Step("I select the models")
def step(context):
    cura.navigateTo("Edit", "Select All Models")

@Step("I navigate to Recommended settings")
def step(context):
    cura.openRecommendedView()

@Step("I choose to load '|any|'")
def step(context, filename):
<<<<<<< Updated upstream
    cura.loadOtherTypeFiles(filename)        
=======
    cura.loadOtherTypeFiles(filename)
 
    
@Step("I check the Remember my choice checkbox")
def step(context):
    cura.rememberMyChoice()
  
    
@Step("I select open as project")
def step(context):
    cura.openFileAsProject()
    cura.openFileFromSummary()

    
@Then("the open as project window does not appear")
def step(context):
    #test.compare(None, names.open_project_file_Remember_my_choice_CheckBox, f"The Open as Project Window does not appear anymore")
    try:
        names.open_project_file_Remember_my_choice_CheckBox
    except NameError:
        pass

>>>>>>> Stashed changes
