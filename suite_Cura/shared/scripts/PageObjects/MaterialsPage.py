# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import squish
import names
from PageObjects.PreferencesPage import Preferences

class Materials(PageObject):
    def __init__(self):
        importSquishSymbols()

    def selectExtruders(self):
        self.click(names.mwi_lst_extruders)
        
    def navigateToMaterialsPreferences(self, lang=None):
        self.selectExtruders()
        self.click(names.mat_btn_selection)

        manage_materials = self.findObjectWithText(names.gen_mnu_item, "Manage Materials", lang=lang)
        self.click(manage_materials)
        
    def activateMaterial(self, material_type):
        # Custom
        self.click(names.mat_cbo_custom)
        # Custom > PLA
        self.click(names.mat_header_custom)
        # Custom > PLA > Custom PLA Custom
        self.click(names.mat_custom_pla)
        
        preferences = Preferences()
        preferences.selectPreferencesMenu("Activate")
        
    def getExtruderOneMaterial(self):
        return waitForObject(names.mwi_lbl_extruder)
    
    def verifyMaterialPresent(self, material_name):
        self.findObjectWithText(names.mat_custom_material, material_name)
        
    def unlinkMaterial(self, action):
        self.click(names.mat_btn_unlink)

    def renameMaterial(self, new_name):
        textbox = waitForObject(names.mat_input_name)
        input = self.getChildrenOfType(textbox, "TextInputWithHandles")[0] #Should only be one TextInputWithHandles in here.
        self.clear(input)
        self.write(input, new_name)
        squish.keyPress("<Return>") #Clear the focus.
        squish.keyRelease("<Return>")

    def setProperty(self, property_name, property_value):
        property_name_to_obj = {
            "Density": names.mat_input_density,
            "Diameter": names.mat_input_diameter,
            "Filament Cost": names.mat_input_cost,
            "Filament Weight": names.mat_input_weight,
        }
        spinbox = waitForObject(property_name_to_obj[property_name])
        input = self.getChildrenOfType(spinbox, "TextInputWithHandles")[0] #Should only be one TextInputWithHandles in here.

        #These property spinboxes are localised, annoyingly, which makes them sometimes use periods and sometimes use commas as radix.
        if "," in str(input.text): #Naively detect if the localisation is using commas. Doesn't work if the current value happens to have round numbers.
            property_value = property_value.replace(".", ",")
        else:
            property_value = property_value.replace(",", ".")

        self.write(input, property_value)
        squish.keyPress("<Return>") #Clear the focus.
        squish.keyRelease("<Return>")

    def confirmDialog(self):
        self.click(names.mbo_btn_confirm)