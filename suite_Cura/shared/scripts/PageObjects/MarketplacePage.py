# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
import SquishModuleHelper


class Marketplace(PageObject):
    def __init__(self):
        SquishModuleHelper.importSquishSymbols()

    def selectPlugin(self, plugin_item):
        plugin = self.getPlugin(plugin_item)
        self.click(plugin)

    def getPlugin(self, plugin):
        switcher = {
            'Auto-Orientation': names.plugin_auto_orientation,
            'Barbarian Plugin': names.plugin_barbarian_units,
            'Custom Supports': names.plugin_customer_supports
        }

        return switcher.get(plugin)

    def selectPluginInstall(self):
        self.click(names.mar_btn_install)
        self.click(names.plugin_lcs_btn_accept)

    def quitCura(self):
        self.click(names.mar_btn_quit_cura)

    def verifyPluginInstalled(self):
        object.exists(names.plugin_btn_installed)
