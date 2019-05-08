from PageObjects.CommonPage import PageObject
from PageObjects.MaterialsPage import Materials

page_object = PageObject()
materials = Materials()


@When("I activate material '|any|'")
def step(context, material_type):
    materials.navigateToMaterialsPreferences()
    materials.activateMaterial(material_type)
    cura.pressCloseButton()


@Then("Extruder one makes use of material '|any|'")
def step(context, expected_material):
    actual_material = materials.getExtruderOneMaterial()
    test.compare(expected_material, actual_material.text)
