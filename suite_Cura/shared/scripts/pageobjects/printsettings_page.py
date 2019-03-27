# -*- coding: utf-8 -*-
import names
from pageobjects.common_page import PageObject
import squish_module_helper
import squish

class PrintSettings(PageObject):
    menu_printsettings = names.mainWindowPrintSettings
    button_custom_printsettings = names.printSettingsCustomButton
    button_printsettings_profile = names.printSettingsProfileSelection
    printsettings_fine_profile = names.printSettingsFineProfile
    printsettings_content = names.printSettingsContent
    
    def __init__(self):
        squish_module_helper.import_squish_symbols()
    
    def selectProfile(self, profile):
        squish.mouseClick(waitForObject(self.menu_printsettings))
        waitForObject(self.printsettings_content)
        
#         This check is required, in case custom settings are already opened
        if object.exists(self.button_custom_printsettings):
            squish.mouseClick(self.button_custom_printsettings)
        
        squish.mouseClick(waitForObject(self.button_printsettings_profile))    
        squish.mouseClick(waitForObject(self.printsettings_fine_profile))
        
#         Close print settings in case it interferes with other steps
        squish.mouseClick(waitForObject(self.menu_printsettings))