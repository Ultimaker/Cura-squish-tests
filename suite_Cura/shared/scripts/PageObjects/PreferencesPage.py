# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.GetObjectsByProperties import ObjectDescendants
from Helpers.SquishModuleHelper import importSquishSymbols
import names
# Needed for the scrolling
import pynput
from pynput.mouse import Controller


class Preferences(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        importSquishSymbols()

    def navigateTo(self, menu_item, lang=None):
        menu_object = self.findObjectWithText(names.mnu_item_preferences, menu_item, lang=lang)
        self.click(menu_object)

    def selectPreferencesMenu(self, action):
        button = self.replaceObjectProperty(names.prf_mnu_btn, self.getMenuBtn(action), 'id')
        self.click(button)
        
    def getMenuBtn(self, menu_action):
        switcher = {
            'Add': 'addMenuButton',
            'Activate': 'activateMenuButton',
            'Remove': 'removeMenuButton',
            'Rename': 'renameMenuButton',
            'Create': 'createMenuButton',
            'Duplicate': 'duplicateMenuButton',
            'Import': 'importMenuButton',
            'Export': 'exportMenuButton'
        }

        return switcher.get(menu_action)

    def removePrinter(self):
        self.click(names.rpd_btn_confirm)

    def confirmAction(self):
        self.click(names.mbo_btn_confirm)

    def verifyPrinterDeleted(self, printer):
        obj = self.replaceObjectProperty(names.pps_printer_item, printer)
        return self.verifyObjDeleted(obj)

    def verifyProfileDeleted(self, profile):
        obj = self.replaceObjectProperty(names.pfs_profile_item, profile)
        return self.verifyObjDeleted(obj)

    def getPrinterListSize(self):
        """
        This list contains non-printer objects, such as 'Local printers' and 'Network printers'
        As they are the same object type
        """
        printer_list = len(self.getChildrenOfType(findObject(names.pps_printer_list), "QQuickRectangle"))

        # Check if 'Local/Network printers' exists, if so extract one item from the printer list
        if object.exists(self.getObjByLang(names.pps_local_printers)):
            printer_list -= 1
        if object.exists(self.getObjByLang(names.pps_network_printers)):
            printer_list -= 1

        return printer_list

    def getPrinterFromList(self, printer):
        printer_obj = self.replaceObjectProperty(names.pps_printer_item, printer)
        return waitForObject(printer_obj, 5000)

    def selectPrinter(self, printer_type):
        printer_obj = self.getPrinterFromList(printer_type)
        self.click(printer_obj)

    def selectProfile(self, profile_name):
        profile_obj = self.getProfileFromList(profile_name)
        self.click(profile_obj)
      
    def renamePrinter(self, printer_name):
        self.click(names.input_printer_name)
        self.setTextFieldValue(names.input_printer_name, printer_name)
        self.click(names.btn_rename_confirm)

    def verifyPrinterActivated(self):
        object.exists(names.pps_btn_machine_settings)

    # Fills in a name in the "create profile" dialog and clicks OK
    def createProfile(self, profile_name):
        self.click(names.input_profile_name)
        self.setTextFieldValue(names.input_profile_name, profile_name)
        self.click(names.btn_create_profile_confirm)

    # Fills in a name in the "duplicate profile" dialog and clicks OK
    def duplicateProfile(self, profile_name):
        self.click(names.input_duplicate_profile_name)
        self.setTextFieldValue(names.input_duplicate_profile_name, profile_name)
        self.click(names.btn_duplicate_profile_confirm)

    # Navigates the save file dialogue to export a profile
    def saveAsProfile(self, file_name = "output.curaprofile"):
        self.setTextFieldValue(names.fdg_input_name, file_name)
        self.click(names.fdg_btn_save)

        if object.exists(names.mbo_confirm_dialog):
            self.click(names.mbo_btn_confirm)
        
    def getProfileFromList(self, profile):
        profile_obj = self.replaceObjectProperty(names.pfs_profile_item, profile)
        return waitForObject(profile_obj, 5000)
    
    def createMaterial(self):
        self.click(names.mat_create_material)
           
    def getMaterialFromList(self, material, type):
        material_obj = self.replaceObjectProperty(names.mat_material_item, material)
            
        try:
            waitForObject(material_obj, 500).visible
            self.click(material_obj)
        except LookupError:
            waitForObject(names.mat_scroll_bar, 500).visible
            self.click(names.mat_scroll_bar)   
            
            # Do the actual scroll
            mousecheck = Controller()
            mousecheck.scroll(0, -5)
            self.getMaterialFromList(material, brand)
            
        return material_obj
    
<<<<<<< Updated upstream
    def selectMaterial(self, material_name):
        material_obj = self.getMaterialFromList(material_name)
        self.click(material_obj)   
=======
    def selectMaterial(self, material_name, type_object):
        material_obj = self.getMaterialFromList(material_name, type_object)
        self.click(material_obj)
        
    def selectMaterialBrand(self, material_brand):
        """
        This function is used to select the brand of the desired material
        (e.g., Ultimaker, DSM, Fishy Filaments, etc.)
        """
        brand_obj = self.findObjectWithText(names.mat_cbo_custom, material_brand, 'sectionName', exact_match=True)
        
        """
        Get all the properties of the brand object in order to check
        whether the the brand list is expanded (i.e., open) and its 
        materials are, thus, visible
        """
        brand_properties = object.properties(brand_obj)
        if 'expanded' in brand_properties.keys():
            isExpanded = brand_properties['expanded']
            if not isExpanded:
                try:
                    waitForObject(brand_obj, 200).visible
                    self.click(brand_obj)
                except LookupError:
                    waitForObject(names.mat_scroll_bar, 100).visible
                    self.click(names.mat_scroll_bar)   
            
                    # Do the actual scroll
                    mousecheck = Controller()
                    mousecheck.scroll(0, -5)
                    selectMaterialBrand(material_brand)
        else:
            test.fail("The object does not have an 'expanded' property!")
        
        return brand_obj
    
            
    def selectMaterialType(self, material_type, material_brand, brand):
        """
        This function is used to click on the material name (e.g., PLA) of the brand
        selected in the selectBrand() function above. NOTE: the name meant here is not
        the full material name as in Ultimaker Blue PLA, but rather the sub-list of the
        desired brand. The full material name will be returned using the selectMaterial()
        function above
        """
        
        type_obj = ObjectDescendants.getObjects(brand, {"materialName": material_brand})
        try:
            waitForObject(type_obj, 200).visible
            self.click(type_obj)
        except LookupError:
            # Do the actual scroll
            mousecheck = Controller()
            mousecheck.scroll(0, -5)
            selectMaterialType(material_type, material_brand, brand)
        
        return type_obj
            
>>>>>>> Stashed changes
