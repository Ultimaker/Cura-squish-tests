from PageObjects.PrintSettings import PrintSettings
from PageObjects.CommonPage import PageObject

print_settings = PrintSettings()
page_object = PageObject()


@When("I enable Gradual infill")
def step(context):
    print_settings.enableGradualInfill()
