# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import names
# Needed for the scrolling
import pynput
from pynput.mouse import Controller


class Marketplace(PageObject):
    def __init__(self):
        importSquishSymbols()

    def selectPlugin(self, plugin_item):
        plugin = self.getPlugin(plugin_item)

        try:
            findObject(plugin)
            waitForObject(plugin, 500)
            self.click(plugin)
        except LookupError:
            """
            Make sure that our mouse is within has focus on the marketplace window, 
            but ONLY the first time (i.e., once it's opened
            """
            try:
                waitForObject(names.mar_featured, 500).visible
                self.click(names.mar_featured)
            except LookupError:
                pass
            
            # Do the actual scroll
            mousecheck = Controller()
            mousecheck.scroll(0, -3)
            self.selectPlugin(plugin_item)
            
        

    def getPlugin(self, plugin):
        switcher = {
            'Auto-Orientation': names.plugin_auto_orientation,
            'Barbarian Plugin': names.plugin_barbarian_units,
            'Custom Supports': names.plugin_customer_supports
        }

        return switcher.get(plugin)

    def selectPluginInstall(self):
        self.click(names.mar_btn_install)
        self.click(names.plugin_lcs_btn_agree)

    def quitCura(self):
        self.click(names.mar_btn_quit_cura)

    def verifyPluginInstalled(self):
        object.exists(names.plugin_btn_installed)
