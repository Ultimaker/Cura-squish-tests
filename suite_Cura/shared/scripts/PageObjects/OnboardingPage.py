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

    def navigateNextPage(self):
        self.click(names.onb_btn_next)

    def finishWizard(self):
        self.click(names.onb_btn_finish)

    def fetchPageTitle(self):
        return waitForObject(names.obn_page_title).text

    def verifyPage(self, page):
        [waitForObjectExists(x, 5000) for x in self.getPageObj(page)]

    def getPageObj(self, page):
        switcher = {
            'Data Collection': [names.onb_btn_next, names.onb_img_improve_cura],
            'Changelog': [names.onb_win_changelog, names.onb_btn_next],
            'User Agreement': [names.onb_btn_decline_close, names.onb_btn_accept_agreement],
            'Printer': [names.pdg_btn_add_printer_ip, names.pdg_btn_refresh,
                        names.pdg_btn_troubleshoot, names.pdg_cbo_network_printer,
                        names.pdg_cbo_local_printer],
            'Cloud': [names.onb_btn_create_acc, names.onb_btn_sign_in, names.onb_btn_finish]
        }

        return switcher.get(page)
