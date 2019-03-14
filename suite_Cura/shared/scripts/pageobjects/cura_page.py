# -*- coding: utf-8 -*-
import names
from pageobjects.common_page import PageObject
import squish_module_helper
import squish
from pageobjects.performance_page import Performance

class Cura(PageObject):
    button_agreement = names.agreementButton
    menu_item = names.menuItem
    main_window = names.mainWindow
    config_cura = names.configureCura
    clear_buildplate = names.clearBuildplate
    menu_open_file = names.mainWindowOpenFile
    filedialog_input = names.fileNameInput
    filedialog_open = names.openFile
    filedialog_save = names.saveFile
    file_type = names.fileType
    button_save_to_file = names.saveToFileButton
    button_preview = names.previewButton
    button_slice = names.sliceButton
    add_networkprinter = names.addNetworkPrinter
    networkprinter_inputfield = names.printerAddressInputField
    networkprinter_ok = names.printerAddressOKButton
    connect_networkprinter = names.connectNetworkPrinter

    def __init__(self):
        PageObject.__init__(self)
        squish_module_helper.import_squish_symbols()

    def acceptAgreement(self):
        squish.mouseClick(waitForObjectExists(self.button_agreement))
        
    def navigateTo(self, menuItem, subMenuItem, property=None):
        menuObject = PageObject.findObjectByText(self.menu_item, menuItem, "plainText")
        squish.mouseClick(menuObject)
        
        if "Configure Cura" in subMenuItem:
            squish.mouseClick(waitForObject(self.config_cura))
        if "Clear Build Plate" in subMenuItem:
            squish.mouseClick(waitForObject(self.clear_buildplate))
            
    def curaIsStarted(self):
        waitForObjectExists(self.main_window)
        
    def loadFile(self, model, trackTime=False):
        squish.mouseClick(waitForObject(self.menu_open_file))
        self.setTextFieldValue(self.filedialog_input, model)
        squish.clickButton(waitForObject(self.filedialog_open))

        if trackTime:
            return Performance.trackFileloadTime()

    def modelIsSliced(self):
        waitForObjectExists(self.button_save_to_file)
        waitForObjectExists(self.button_preview)

    def sliceObject(self, trackTime=False):
        squish.mouseClick(waitForObject(self.button_slice))

        if trackTime:
            return Performance.trackSliceTime()

    def saveToFile(self, fileName):
        squish.mouseClick(waitForObject(self.button_save_to_file))

        self.setTextFieldValue(self.filedialog_input, fileName)

        squish.mouseClick(waitForObject(self.file_type))
        squish.mouseClick(waitForObjectItem(self.file_type, "G-code File (*\\.gcode)"))

        squish.mouseClick(waitForObject(self.filedialog_save))

        return findFile("testdata", fileName)

    def addNetworkPrinter(self, printerIP):
        squish.mouseClick(waitForObject(self.add_networkprinter))
        squish.mouseClick(waitForObject(self.networkprinter_inputfield))
        squish.nativeType(printerIP);
        squish.mouseClick(waitForObject(self.networkprinter_ok))
        squish.mouseClick(waitForObject(self.connect_networkprinter))