# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import names


class PrintSettings(PageObject):
    def __init__(self):
        importSquishSymbols()

    def enableGradualInfill(self):
        self.click(names.prs_chk_gradual_infill)
