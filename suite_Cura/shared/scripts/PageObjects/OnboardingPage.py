# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
import SquishModuleHelper


class Onboarding(PageObject):
    def __init__(self):
        SquishModuleHelper.importSquishSymbols()

    def startFlow(self):
        self.click(names.onb_btn_get_started)

    def acceptAgreement(self):
        self.click(names.onb_btn_accept_agreement)
        
    def fetchPageTitle(self, title):
        return self.findObjectByText(names.obn_page_title, title).text