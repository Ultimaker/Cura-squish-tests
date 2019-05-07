from PageObjects.CommonPage import PageObject
from PageObjects.CuraPage import Cura
from PageObjects.PrinterSettingsPage import PrintSettings
from PageObjects.PrinterPage import Printer
from PageObjects.PerformancePage import Performance
from PageObjects.MaterialsPage import Materials

page_object = PageObject()
cura = Cura()
print_settings = PrintSettings()
printer = Printer()
performance = Performance()
marketplace = Marketplace()
materials = Materials()

@When("I activate material '|any|'")
def step(context, material_type):
    materials.navigateToMaterialsPreferences()
    materials.activateMaterial(material_type)
    cura.pressCloseButton()

@Then("Extruder one makes use of material '|any|'")
def step(context, material_type):
    material_used = materials.getExtruderOneMaterial()
    test.compare(material_type, material_used)