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
    menu_config_cura = names.configureCura
    menu_clear_buildplate = names.clearBuildplate
    menu_open_file = names.mainWindowOpenFile
    menu_save = names.saveAsProjectMenuItem
    filedialog_input = names.fileNameInput
    filedialog_open = names.openFile
    filedialog_save = names.saveFile
    file_type = names.fileType
    button_save_to_file = names.saveToFileButton
    button_preview = names.previewButton
    button_slice = names.sliceButton
    file_exists_dialog = names.fileAlreadyExistsDialog
    overwrite_file = names.overwriteFile
    button_open_as_project = names.openFileAsProject
    button_summary_open = names.openProjectFromSummary
    button_summary_save = names.saveFileAsProject
    
    def __init__(self):
        PageObject.__init__(self)
        squish_module_helper.import_squish_symbols()

    def acceptAgreement(self):
        squish.mouseClick(waitForObjectExists(self.button_agreement))
        
    def navigateTo(self, menuItem, subMenuItem, property=None):
        menuObject = PageObject.findObjectByText(self.menu_item, menuItem, "plainText")
        squish.mouseClick(waitForObject(menuObject))
        
        if "Configure Cura" in subMenuItem:
            squish.mouseClick(waitForObject(self.menu_config_cura))
        if "Clear Build Plate" in subMenuItem:
            squish.mouseClick(waitForObject(self.menu_clear_buildplate))
        if "Save" in subMenuItem:
            squish.mouseClick(waitForObject(self.menu_save))
            
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

#     After model has been sliced
    def saveToFile(self, fileName):
        squish.mouseClick(waitForObject(self.button_save_to_file, 50000))

        self.setTextFieldValue(self.filedialog_input, fileName)

        squish.mouseClick(waitForObject(self.file_type))
        squish.mouseClick(waitForObjectItem(self.file_type, "G-code File (*\\.gcode)"))

        squish.mouseClick(waitForObject(self.filedialog_save))
        
        if object.exists(self.file_exists_dialog):
            squish.mouseClick(waitForObject(self.overwrite_file))

        return findFile("testdata", fileName)
    
    def openFileAsProject(self):
        squish.mouseClick(waitForObject(self.button_open_as_project))
        
    def openFileFromSummary(self, trackTime=False):
        squish.mouseClick(waitForObject(self.button_summary_open))
        
        if trackTime:
            return Performance.trackFileloadTime()
        
    def saveAsProject(self, trackTime):
        squish.mouseClick(waitForObject(self.button_summary_save))
        self.setTextFieldValue(self.filedialog_input, "UM3_Robot_SAVE.3mf")
        squish.mouseClick(waitForObject(self.filedialog_save))
        
        if object.exists(self.file_exists_dialog):
            squish.mouseClick(waitForObject(self.overwrite_file))
            
        if trackTime:
            return Performance.trackFileloadTime()