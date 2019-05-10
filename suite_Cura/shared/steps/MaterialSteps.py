from PageObjects.MaterialsPage import Materials
from PageObjects.CuraPage import Cura

materials = Materials()
cura = Cura()

@When("I activate material '|any|'")
def step(context, material_type):
    materials.navigateToMaterialsPreferences("nl")
    materials.activateMaterial(material_type)
    cura.pressCloseButton()


@Then("Extruder one makes use of material '|any|'")
def step(context, expected_material):
    actual_material = materials.getExtruderOneMaterial()
    test.compare(expected_material, actual_material.text)
