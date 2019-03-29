# -*- coding: utf-8 -*-
import names
import squish_module_helper
import squish

class Marketplace():
    marketplace_install_button = names.marketplaceInstallButton
    plugin_license_accept_button = names.licenseAcceptButton
    auto_orientation_plugin = names.autoOrientationPlugin
    barbarian_units_plugin = names.barbarianUnitsPlugin
    custom_supports_plugin = names.customSupportsPlugin
    quit_cura_button = names.marketplaceQuitCuraButton
    installed_button = names.installedPluginButton
    
    def __init__(self):
        squish_module_helper.import_squish_symbols()
        
    def selectPlugin(self, pluginItem):
        if "Auto-Orientation" in pluginItem:
            squish.mouseClick(waitForObject(self.auto_orientation_plugin))
        if "Barbarian Plugin" in pluginItem:
            squish.mouseClick(waitForObject(self.barbarian_units_plugin))
        if "Custom Supports" in pluginItem:
            squish.mouseClick(waitForObject(self.custom_supports_plugin))
        
    def selectPluginInstall(self):
        squish.mouseClick(waitForObject(self.marketplace_install_button))
        squish.mouseClick(waitForObject(self.plugin_license_accept_button))
        
    def quitCura(self):
        squish.mouseClick(waitForObject(self.quit_cura_button))
        
    def verifyPluginInstalled(self):
        object.exists(self.installed_button)
        