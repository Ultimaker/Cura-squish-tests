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

    def getAllProfiles(self, profiles = None, profiles_obj = None):
        if profiles is None:
            profiles = []
        if profiles_obj is None:
            profiles_obj = []

        #Get all descendants of type QQuickRectangle.
        profiles = self.getChildrenOfType(findObject(names.pfd_profile_list), "QQuickRectangle")
        for rect in profiles:
            profile_obj_list = self.getChildrenOfType(findObject(objectMap.realName(rect)), "QQuickText")
            if len(profile_obj_list) == 1:
                profiles_obj.append(profile_obj_list[0])

        return profile_obj_list
        
    # Custom profiles have attribute 'isReadOnly' set to False
    def getCustomProfiles(self, custom_profiles = None, custom_profiles_obj = None):
        all_profiles = self.getAllProfiles(custom_profiles, custom_profiles_obj)
        custom_profiles = []
        for profile in all_profiles:
            rect = profile.parent()
            if hasattr(rect, "isReadOnly") and not rect.isReadOnly:
                custom_profiles.append(profile)

        return custom_profiles

    def getDefaultProfiles(self, default_profiles = None, default_profiles_obj = None):
        all_profiles = self.getAllProfiles(default_profiles, default_profiles_obj)
        default_profiles = []
        for profile in all_profiles:
            rect = profile.parent()
            if not hasattr(rect, "isReadOnly") or rect.isReadOnly:
                default_profiles.append(profile)

        return default_profiles
    
    def selectProfileFromPreferences(self, profile_list, profile):
        for x in profile_list:
            if x.text == profile:
                self.click(x)
                break