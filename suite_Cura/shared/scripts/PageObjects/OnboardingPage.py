# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
from PageObjects.AddPrinterPage import AddPrinter
import names


class Onboarding(PageObject):
    def __init__(self):
        importSquishSymbols()

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
        # Printer objects in 'Onboarding' and 'Add printer' have different parent containers
        # For the Onboarding flow, change the container to names.mwi (main screen)
        printer_list_objs = [
            names.pdg_btn_add_printer_by_ip, names.pdg_btn_refresh,
            names.pdg_btn_troubleshoot, names.pdg_cbo_network_printer,
            names.pdg_cbo_local_printer]
        
        add_printer = AddPrinter()
        printer_list = [add_printer.replaceOnboardingObjProperty(x) for x in printer_list_objs]
        
        switcher = {
            'Data Collection': [names.onb_btn_next],
            'Changelog': [names.onb_win_changelog, names.onb_btn_next],
            'User Agreement': [names.onb_btn_decline_close, names.onb_btn_accept_agreement],
            'Printer': printer_list,
            'Cloud': [names.onb_btn_create_acc, names.onb_btn_sign_in, names.onb_btn_finish]
        }

        return switcher.get(page)
