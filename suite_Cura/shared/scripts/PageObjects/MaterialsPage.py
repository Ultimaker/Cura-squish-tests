# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import squish
import names
import test
from PageObjects.PreferencesPage import Preferences

class Materials(PageObject):
    property_name_to_obj = {
        "Name": names.mat_input_name,
        "Density": names.mat_input_density,
        "Diameter": names.mat_input_diameter,
        "Filament Cost": names.mat_input_cost,
        "Filament Weight": names.mat_input_weight,
        "Default Printing Temperature": names.mat_setting_line,
        "Default Build Plate Temperature": names.mat_input_build_temperature,
        "Retraction Distance": names.mat_input_retraction_distance,
        "Retraction Speed": names.mat_input_retraction_speed,
        "Standby Temperature": names.mat_input_standby_temperature,
        "Fan Speed": names.mat_input_fan_speed,
    }

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
        self.findObjectWithText(names.mat_custom_material, material_name, delay = 1000) #Delay is required because the materials list updates asynchronously.

    def verifyMaterialNotPresent(self, material_name):
        if self.objectWithTextExists(names.mat_custom_material, material_name, pause = 1000):
            test.fail(f"Material {material_name} was present.")

    def verifyMaterialSelected(self, material_name):
        actual_material_name = self.getProperty("Name")
        if actual_material_name != material_name:
            test.fail(f"The material {actual_material_name} was active instead of {material_name}.")

    def selectButton(self, action):
        self.click(names.mat_btn_unlink)
        
    def selectTab(self, tabname):
        self.click(self.findObjectWithText(names.mat_printsettings_tab, tabname, exact_match=True))

    def renameMaterial(self, new_name):
        textbox = waitForObject(names.mat_input_name)
        input = self.getChildrenOfType(textbox, "TextInputWithHandles")[0] #Should only be one TextInputWithHandles in here.
        self.clear(input)
        self.write(input, "<Ctrl+A>")
        self.write(input, new_name)
        self.write(input, "<Return>") #Clear the focus.
        
    def setPrintSettingsProperty(self, property_name, property_value):
        tooltip_area = waitForObject(self.replaceObjectProperty(names.mat_setting_line, property_name))
        input = self.getChildrenOfType(tooltip_area, "TextInputWithHandles")[0] #Should only be one Spinbox in here.      
        self.clear(input)
        self.write(input, property_value)
        self.write(input, "<Return>") #Clear the focus.


    def getProperty(self, property_name):
        spinbox = waitForObject(self.property_name_to_obj[property_name])
        input = self.getChildrenOfType(spinbox, "TextInputWithHandles")[0] #Should only be one TextInputWithHandles in here.

        #These property spinboxes are localised, annoyingly, which makes them sometimes use periods and sometimes use commas as radix.
        return str(input.text).replace(",", ".") #Our code must always work with periods as radix.

    def setProperty(self, property_name, property_value):
        spinbox = waitForObject(self.property_name_to_obj[property_name])
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

    def denyDialog(self):
        self.click(names.mbo_btn_deny)