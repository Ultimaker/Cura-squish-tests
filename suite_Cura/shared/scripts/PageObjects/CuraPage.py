# -*- coding: utf-8 -*-
import names
from PageObjects.CommonPage import PageObject
import SquishModuleHelper
import squish
from PageObjects.PerformancePage import Performance


class Cura(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        SquishModuleHelper.importSquishSymbols()

    def acceptAgreement(self):
        self.click(names.agreementButton)

    def pressCloseButton(self):
        self.click(names.closeButton)

#     Top-level navigation bar
    def navigateTo(self, menu_item, submenu_item, property=None):
        menu_object = PageObject.findObjectByText(names.menuItem, menu_item, "plainText")
        self.click(menu_object)

        submenu_object = PageObject.findObjectByText(names.submenuItem, submenu_item)
        self.click(submenu_object)
            
    def navigateToStageMenu(self, stage_item):
        if "Marketplace" in stage_item:
            self.click(names.marketplaceButton)

    def curaIsStarted(self):
        waitForObjectExists(names.mainWindow)
        
    def loadFile(self, model, track_time=False):
        self.click(names.mainWindowOpenFile)
        self.setTextFieldValue(names.fileNameInput, model)
        squish.clickButton(waitForObject(names.openFile))

        if track_time:
            return Performance.trackFileloadTime()

    def modelIsSliced(self):
        waitForObjectExists(names.saveToFileButton)
        waitForObjectExists(names.previewButton)

    def sliceObject(self, track_time=False):
        self.click(names.sliceButton)

        if track_time:
            return Performance.trackSliceTime()

#     After model has been sliced
    def saveToFile(self, file_name):
        self.click(names.saveToFileButton, 50000)

        self.setTextFieldValue(names.fileNameInput, file_name)

        self.click(names.fileType)
        squish.mouseClick(waitForObjectItem(names.fileType, "G-code File (*\\.gcode)"))

        self.click(names.saveFile)
        
        if object.exists(names.fileAlreadyExistsDialog):
            self.click(names.overwriteFile)

        return findFile("testdata", file_name)
    
    def openFileAsProject(self):
        self.click(names.openFileAsProject)
        
    def openFileFromSummary(self, track_time=False):
        self.click(names.openProjectFromSummary)
        
        if track_time:
            return Performance.trackFileloadTime()
        
    def saveAsProject(self, track_time):
        self.click(names.saveFileAsProject)
        self.setTextFieldValue(names.fileNameInput, "UM3_Robot_SAVE.3mf")
        self.click(names.saveFile)
        
        if object.exists(names.fileAlreadyExistsDialog):
            self.click(names.overwriteFile)
            
        if track_time:
            return Performance.trackFileloadTime()
        
    def moveModel(self, x_pos):
        self.setTextFieldValue(names.moveModelXaxis, x_pos)
        self.click(names.mainWindow)
        
    def scaleModel(self, size):
        squish.mouseClick(self.findObjectByText(names.toolbarButton, "Scale"))
        
        if not waitForObject(names.uniformScaling).checked:
            squish.mouseClick(names.uniformScaling)
        
        self.setTextFieldValue(names.scaleModelXaxis, size)
        self.click(names.mainWindow)