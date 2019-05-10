# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
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