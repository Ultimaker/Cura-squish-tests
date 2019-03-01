source(findFile("scripts", "pageobjects/page_object.py"))
source(findFile("scripts", "pageobjects/cura_page.py"))

cura = Cura()

@Given("Cura has been started")
def step(context):
    pageObject = PageObject()
    pageObject.startCura()

@Given("I accept the user agreement")
def step(context):
    cura.acceptAgreement()
