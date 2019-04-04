# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
import SquishModuleHelper


class PrintSettings(PageObject):
    def __init__(self):
        SquishModuleHelper.importSquishSymbols()

    def selectProfile(self, profile):
        self.click(names.mwi_print_settings)
        waitForObject(names.win_print_settings)

        # This check is required, in case custom settings are already opened
        if object.exists(names.prs_btn_custom):
            self.click(names.prs_btn_custom)

        self.click(names.prs_btn_sel_profile)

        if "fine" in profile:
            self.click(self.findObjectByText(names.sub_mnu_item, "Fine - 0.1mm"))

        # Close print settings in case it interferes with other steps
        self.click(names.mwi_print_settings)
