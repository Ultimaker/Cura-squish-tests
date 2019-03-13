# -*- coding: utf-8 -*-
import names
from pageobjects.page_object import PageObject
import squish_module_helper
import squish

class Cura(PageObject):
    BUTTON_AGREEMENT = names.agreementButton
    MENU_ITEM = names.menuItem
    MAIN_WINDOW = names.mainWindow
    CONFIG_CURA = names.configureCura
    BUTTON_PRINTERLIST = names.mainWindowPrinter
    ADD_NETWORKPRINTER = names.addNetworkPrinter
    NETWORKPRINTER_INPUTFIELD = names.printerAddressInputField
    NETWORKPRINTER_OK = names.printerAddressOKButton
    CONNECT_NETWORKPRINTER = names.connectNetworkPrinter
    
    def __init__(self):
        squish_module_helper.import_squish_symbols()

    def acceptAgreement(self):
        squish.mouseClick(waitForObjectExists(Cura.BUTTON_AGREEMENT))
        
    def navigateTo(self, menuItem, subMenuItem, property=None):
        menuObject = PageObject.findObjectByText(Cura.MENU_ITEM, menuItem, "plainText")
        squish.mouseClick(menuObject)
        
        if "Configure Cura" in subMenuItem:
            squish.mouseClick(waitForObject(Cura.CONFIG_CURA))
            
    def curaIsStarted(self):
        waitForObjectExists(Cura.MAIN_WINDOW)
        
    def openPrinterList(self):
        squish.mouseClick(waitForObject(self.BUTTON_PRINTERLIST))
        
    def addNetworkPrinter(self, printerIP):
        squish.mouseClick(waitForObject(self.ADD_NETWORKPRINTER))
        squish.mouseClick(waitForObject(self.NETWORKPRINTER_INPUTFIELD))
        squish.nativeType(printerIP);
        squish.mouseClick(waitForObject(self.NETWORKPRINTER_OK))
        squish.mouseClick(waitForObject(self.CONNECT_NETWORKPRINTER))
        