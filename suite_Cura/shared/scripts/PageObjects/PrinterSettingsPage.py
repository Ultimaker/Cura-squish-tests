# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import names


class PrintSettings(PageObject):
    def __init__(self):
        importSquishSymbols()

    # Note case sensitive, but you only need the first part of the profile name.
    # From Print Settings (not preferences)
    def selectProfile(self, profile):
        self.click(names.mwi_print_settings)
        waitForObject(names.win_print_settings)

        # This check is required, in case custom settings are already opened
        if object.exists(names.prs_btn_custom):
            self.click(names.prs_btn_custom)

        self.click(names.prs_btn_sel_profile)
        self.click(self.findObjectWithText(names.sub_mnu_item, profile))

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
        profiles = self.getChildrenOfType(findObject(names.pfs_profile_list), "QQuickRectangle")
        for rect in profiles:
            profile_obj_list = self.getChildrenOfType(findObject(objectMap.realName(rect)), "QQuickText")
            if len(profile_obj_list) == 1:
                profiles_obj.append(profile_obj_list[0])

        return profiles_obj
        
    # Custom profiles have attribute 'isReadOnly' set to False
    def getCustomProfiles(self, custom_profiles = None, custom_profiles_obj = None):
        all_profiles = self.getAllProfiles(custom_profiles, custom_profiles_obj)
        custom_profiles = []
        for profile in all_profiles:
            rect = object.parent(profile)
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

    def getCurrentPrintProfile(self):
        return waitForObject(names.mwi_mnu_print_settings_profile)

    def gotoCustomSettings(self):
        # This check is required, in case the settings are already opened
        if not object.exists(names.win_print_settings):
            self.click(names.mwi_print_settings)
            waitForObject(names.win_print_settings)

        # This check is required, in case custom settings are already opened
        if object.exists(names.prs_btn_custom):
            self.click(names.prs_btn_custom)

    def showAllSettings(self):
        self.gotoCustomSettings()
        self.click(names.btn_settings_visibility)
        submenu_object = self.findObjectWithText(names.sub_mnu_item, "Show All Settings")
        self.click(submenu_object)

    def checkTextboxSetting(self, tab_name, setting_name, setting_value_str):
        self.gotoCustomSettings()

        # Open tab:
        obj_tab = {"container": names.settings_scrollview, "text": tab_name, "type": "Label", "unnamed": 1, "visible": True}
        waitForObject(obj_tab)
        self.click(obj_tab)

        # Find setting-item:
        obj_label = self.findObjectWithText({"container": names.settings_scrollview, "type": "Label", "unnamed": 1, "visible": True}, setting_name)
        assert(obj_label.text == setting_name)
        child_list = self.getChildrenOfType(object.parent(obj_label), "QQuickTextInput")

        # Close the tab again, so it can be reopened next time (workaround because it's hard to know if it's collapsed or not):
        self.click(obj_tab)

        # Compare and return:
        assert(len(child_list) > 0)
        return (child_list[0].text == setting_value_str)
