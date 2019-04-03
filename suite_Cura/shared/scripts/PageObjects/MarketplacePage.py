# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
import SquishModuleHelper


class Marketplace(PageObject):
    def __init__(self):
        SquishModuleHelper.importSquishSymbols()
        
    def selectPlugin(self, pluginItem):
        if "Auto-Orientation" in pluginItem:
            self.click(names.autoOrientationPlugin)
        if "Barbarian Plugin" in pluginItem:
            self.click(names.barbarianUnitsPlugin)
        if "Custom Supports" in pluginItem:
            self.click(names.customSupportsPlugin)
        
    def selectPluginInstall(self):
        self.click(names.marketplaceInstallButton)
        self.click(names.licenseAcceptButton)

    def quitCura(self):
        self.click(names.marketplaceQuitCuraButton)
        
    def verifyPluginInstalled(self):
        object.exists(names.installedPluginButton)
        