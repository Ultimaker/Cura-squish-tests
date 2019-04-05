from PageObjects.CommonPage import PageObject
from PageObjects.CuraPage import Cura
from PageObjects.OnboardingPage import Onboarding

page_object = PageObject()
cura = Cura()
onboarding = Onboarding()


@When("I start the onboarding flow")
def step(context):
    onboarding.startFlow()


@Step("the |any| page is shown with title '|any|'")
def step(context, _, expected_title):
    actual_title = onboarding.fetchPageTitle(title)
    test.compare(expected_title, actual_title)


@Given("I'm on the user agreement page of the onboarding flow")
def step(context):
    test.warning("TODO implement I'm on the user agreement page of the onboarding flow")


@Given("I'm on the changelog page of the onboarding flow")
def step(context):
    test.warning("TODO implement I'm on the changelog page of the onboarding flow")


@When("I confirm the changelog changes")
def step(context):
    test.warning("TODO implement I confirm the changelog changes")


@Given("I'm on the data collection page of the onboarding flow")
def step(context):
    test.warning("TODO implement I'm on the data collection page of the onboarding flow")


@When("I agree to my data being collected")
def step(context):
    test.warning("TODO implement I agree to my data being collected")


@Given("I'm on the printer screen of the onboarding flow")
def step(context):
    test.warning("TODO implement I'm on the printer screen of the onboarding flow")


@When("I add a non-networked Ultimaker S5 printer")
def step(context):
    test.warning("TODO implement I add a non-networked Ultimaker S5 printer")


@Given("I'm on the home page of Cura")
def step(context):
    test.warning("TODO implement I'm on the home page of Cura")


@When("I finish the onboarding flow")
def step(context):
    test.warning("TODO implement I finish the onboarding flow")
