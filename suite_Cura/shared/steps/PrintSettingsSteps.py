from PageObjects.PrinterSettingsPage import PrintSettings
from PageObjects.CuraPage import Cura
from PageObjects.PreferencesPage import Preferences
from collections import Counter

preferences = Preferences()
print_settings = PrintSettings()
cura = Cura()

@When("I enable Gradual infill")
def step(context):
    print_settings.enableGradualInfill()

@Step("The following custom profiles are available")
def step(context):
    # Navigate to Preferences > Profiles
    cura.navigateTo("Preferences", "Configure Cura", "nl")
    preferences.navigateTo("Profiles", "nl")
    
    expected_profiles = context.table
    # Drop initial row with column headers
    expected_profiles.pop(0)
    
    # getCustomProfiles return QQuickText objects
    # This statement retrieves the text, which is a QString obj, and converts it to a String obj
    actual_profile_objs = print_settings.getCustomProfiles()
    profile_list = [str(x.text) for x in actual_profile_objs]
    
    
    # The list of profile objects will be used in later steps
    context.userData = {}
    context.userData['profiles'] = actual_profile_objs
    
    # context.table creates lists for each row. This statement merges them together
    expected_profiles = [item for sublist in expected_profiles for item in sublist]

    test.compare(Counter(profile_list), Counter(expected_profiles))
    
@When("I |word| profile '|any|'")
def step(context, action, profile):
    print_settings.selectProfileFromPreferences(context.userData['profiles'], profile)
    preferences.selectPreferencesMenu(action)
    cura.pressCloseButton()

@Then("The print settings display profile '|any|'")
def step(context, expected_profile):
    # The print settings menu contains the layer height aswell. We only want the profile name.
    current_profile = str(print_settings.getCurrentPrintProfile().text).split()[0]
    test.compare(expected_profile, current_profile)