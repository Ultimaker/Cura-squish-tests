from PageObjects.PreferencesPage import Preferences
#To validate exported profiles
import configparser
#To remove the exported profile
import os
#To save exported profiles in the test data directory
import os.path
#To validate exported profiles
import zipfile

preferences = Preferences()


@Step("I navigate to |word| in preferences")
def step(context, menu_item):
    preferences.navigateTo(menu_item)


@When("I select |word| printer")
def step(context, action):
    preferences.selectPreferencesMenu(action)

    if action == "Remove":
        preferences.removePrinter()


@Then("the printer overview contains a '|any|' printer")
def step(context, expected_printer):
    actual_printer = preferences.getPrinterFromList(expected_printer)
    test.compare(expected_printer, actual_printer.text)


@Then(r"the printer (.*?) doesn't exist (?:anymore)?", regexp = True)
def step(context, printer):
    test.compare(True, preferences.verifyPrinterDeleted(printer), f"Object {printer} has been deleted")


@When("I select printer |any| from the local printers")
def step(context, printer_type):
    preferences.selectPrinter(printer_type)


@When("I give the printer the '|any|' name")
def step(context, printer_name):
    preferences.selectPreferencesMenu("Rename")
    preferences.renamePrinter(printer_name)


@Then("The printer is activated")
def step(context):
    preferences.verifyPrinterActivated()
    
    
@Step("I select |word| profile")
def step(context, action):
    preferences.selectPreferencesMenu(action)


@Step("I give the new profile '|word|' name")
def step(context, profile_name):
    preferences.createProfile(profile_name)


@Step("I give the duplicated profile '|word|' name")
def step(context, profile_name):
    preferences.duplicateProfile(profile_name)


@Step("I select the '|word|' profile in preferences")
def step(context, profile_name):
    preferences.selectProfile(profile_name)

<<<<<<< Updated upstream
@Step("I save the profile as '|any|'")
=======

@Step("I save the file as '|any|'")
>>>>>>> Stashed changes
def step(context, file_name):
    preferences.saveAsProfile(os.path.join(preferences.testdata_dir, file_name))

@Step("I confirm the removal")
def step(context):
    preferences.confirmAction()


@Then("the profile overview contains the profile: '|any|'")
def step(context, expected_profile):
    actual_profile = preferences.getProfileFromList(expected_profile)
    test.compare(expected_profile, actual_profile.text)

<<<<<<< Updated upstream
@Then("the file '|any|' is a valid profile")
def step(context, file_name):
    with zipfile.ZipFile(os.path.join(preferences.testdata_dir, file_name)) as archive: #If this raises an exception, the file doesn't exist or is invalid.
        for archived_file in archive.namelist():
            with archive.open(archived_file) as f:
                contents = f.read().decode("utf-8")
                profile = configparser.ConfigParser()
                profile.read_string(contents) #If this raises an exception, the file is invalid.
    test.passes("Profile is valid.") #If it got here, none of the aforementioned exceptions occurred so it is valid.
=======

@Then("the file '|any|' is a valid '|any|'")
def step(context, file_name, type):
    if type == 'profile':
        with zipfile.ZipFile(os.path.join(preferences.testdata_dir, file_name)) as archive: # If this raises an exception, the file doesn't exist or is invalid.
            for archived_file in archive.namelist():
                with archive.open(archived_file) as f:
                    contents = f.read().decode("utf-8")
                    profile = configparser.ConfigParser()
                    profile.read_string(contents) # If this raises an exception, the file is invalid.
        test.passes("Profile is valid.") # If it got here, none of the aforementioned exceptions occurred so it is valid.
    else: 
        preferences.validateExport()
>>>>>>> Stashed changes


@Then(r"the profile '(.*?)' doesn't exist (?:anymore)?", regexp = True)
def step(context, forbidden_profile):
    preferences.verifyProfileDeleted(forbidden_profile)
  
    
<<<<<<< Updated upstream
@Step("I select '|any|' material in preferences")
def step(context, material_name):
    preferences.selectMaterial(material_name)
=======
@Step("I select '|any|' material from the '|any|' brand with the '|any|' type in preferences")
def step(context, material_name, material_brand, material_type):
    brand_object = preferences.selectMaterialBrand(material_brand)
    type_object = preferences.selectMaterialType(material_type, material_brand, brand_object)
    preferences.selectMaterial(material_name, type_object)
    
>>>>>>> Stashed changes
