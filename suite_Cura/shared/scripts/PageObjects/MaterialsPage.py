# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import names
from PageObjects.PreferencesPage import Preferences
from Helpers.GetObjectsByProperties import ObjectDescendants

class Materials(PageObject):
    def __init__(self):
        importSquishSymbols()

    def selectExtruders(self):
        self.click(names.mwi_lst_extruders)
        
    def navigateToMaterialsPreferences(self):
        self.selectExtruders()
        self.click(names.mat_btn_selection)

        manage_materials = self.findObjectWithText(names.mat_mnu_manage, "Manage Materials")
        self.click(manage_materials)     
        
    def activateMaterial(self, material_type):
        custom_material = names.mat_cbo_custom
        self.click(custom_material)
        
        # Get grand-parent of custom_material, which is the wrapper of the whole custom section
        wrapper_obj = self.getGrandParentObj(custom_material)
        
        # Get specific grandchild from this
        pla_dropdown = ObjectDescendants.getObjects(objectMap.realName(wrapper_obj), {"text": "PLA"})
        self.click(pla_dropdown[0])
        
        # Select material and activate
        self.click(names.mat_custom_pla)
        Preferences.selectPreferencesMenu("Activate")
        