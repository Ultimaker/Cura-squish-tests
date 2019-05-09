# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import names


class PrintSettings(PageObject):
    def __init__(self):
        importSquishSymbols()

    # From Print Settings (not preferences)
    def selectProfile(self, profile):
        self.click(names.mwi_print_settings)
        waitForObject(names.win_print_settings)

        # This check is required, in case custom settings are already opened
        if object.exists(names.prs_btn_custom):
            self.click(names.prs_btn_custom)

        self.click(names.prs_btn_sel_profile)

        if "fine" in profile:
            self.click(self.findObjectWithText(names.sub_mnu_item, "Fine - 0.1mm"))

        # Close print settings in case it interferes with other steps
        self.click(names.mwi_print_settings)

    def enableGradualInfill(self):
        self.click(names.prs_chk_gradual_infill)
        
    # Custom profiles have attribute 'isReadOnly' set to False
    def getCustomProfiles(self, custom_profiles=None, custom_profiles_obj=None):
        if custom_profiles is None:
            custom_profiles = []
        if custom_profiles_obj is None:
            custom_profiles_obj = []

        # Get all descendants of type QQuickRectangle
        profiles = self.getChildrenOfType(findObject(names.pfs_profile_list), "QQuickRectangle")     
        # Of all these types, add them to the list if property 'isReadOnly' is false    
        [custom_profiles.append(x) for x in profiles if hasattr(x, 'isReadOnly') and not x.isReadOnly]
        
        # Get the QQuickText objects that are children of the custom profile objects
        # They contain the actual name of the profiles
        for x in custom_profiles:
            profile_obj_list = self.getChildrenOfType(findObject(objectMap.realName(x)), "QQuickText")
            if len(profile_obj_list) == 1:
                custom_profiles_obj.append(profile_obj_list[0])
            
        return custom_profiles_obj
    
    def selectProfileFromPreferences(self, profile_list, profile):
        for x in profile_list:
            if x.text == profile:
                self.click(x)
                break