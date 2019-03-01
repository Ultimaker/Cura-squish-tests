# -*- coding: utf-8 -*-
import names

class Cura():
    BUTTON_AGREEMENT = names.agreementButton
    
    def acceptAgreement(self):
        mouseClick(waitForObject(self.BUTTON_AGREEMENT))