# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
import SquishModuleHelper


class PrintSettings(PageObject):
    def __init__(self):
        SquishModuleHelper.importSquishSymbols()
    
    def selectProfile(self, profile):
        self.click(names.mainWindowPrintSettings)
        waitForObject(names.printSettingsContent)
        
#         This check is required, in case custom settings are already opened
        if object.exists(names.printSettingsCustomButton):
            self.click(names.printSettingsCustomButton)
        
        self.click(names.printSettingsProfileSelection)
        
        if "fine" in profile:
            self.click(self.findObjectByText(names.submenuItem, "Fine - 0.1mm"))
        
#         Close print settings in case it interferes with other steps
        self.click(names.mainWindowPrintSettings)