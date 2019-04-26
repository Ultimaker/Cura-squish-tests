# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import squish
from PageObjects.PerformancePage import Performance
import names


class Cura(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        importSquishSymbols()

    def pressCloseButton(self):
        self.click(names.btn_close)

    #     Top-level navigation bar
    def navigateTo(self, menu_item, submenu_item, property=None):
        menu_object = PageObject.findObjectByText(names.mnu_item, menu_item, "plainText")
        self.click(menu_object)

        submenu_object = PageObject.findObjectByText(names.sub_mnu_item, submenu_item)
        self.click(submenu_object)

    def navigateToStageMenu(self, stage_item):
        if "Marketplace" in stage_item:
            self.click(names.mwi_btn_marketplace)

    def curaIsStarted(self):
        waitForObjectExists(names.mwi)

    def loadFile(self, model, track_time=False):
        self.click(names.mwi_btn_open_file)

        # Navigate to the correct dir first
        self.setTextFieldValue(names.fdg_input_name, self.testdata_dir)
        squish.clickButton(waitForObject(names.fdg_btn_open))

        self.setTextFieldValue(names.fdg_input_name, model)
        squish.clickButton(waitForObject(names.fdg_btn_open))

        if track_time:
            return Performance.trackFileloadTime()

    def modelIsSliced(self):
        waitForObjectExists(names.mwi_btn_save_to_file)
        waitForObjectExists(names.mwi_btn_preview)

    def sliceObject(self, track_time=False):
        self.click(names.mwi_btn_slice)

        if track_time:
            return Performance.trackSliceTime()

    #     After model has been sliced
    def saveToFile(self, file_name):
        self.click(names.mwi_btn_save_to_file, 40000)

        self.setTextFieldValue(names.fdg_input_name, file_name)

        self.click(names.fdg_cbo_file_type)
        squish.mouseClick(waitForObjectItem(names.fdg_cbo_file_type, "G-code File (*\\.gcode)"))

        self.click(names.fdg_btn_save)

        if object.exists(names.mbo_file_exists):
            self.click(names.mbo_btn_overwrite)

        return findFile("testdata", file_name)

    def openFileAsProject(self):
        self.click(names.btn_open_as_prj)

    def openFileFromSummary(self, track_time=False):
        self.click(names.btn_open_prj_summary)

        if track_time:
            return Performance.trackFileloadTime()

    def saveAsProject(self, track_time):
        self.click(names.btn_save_as_prj)
        self.setTextFieldValue(names.fdg_input_name, "UM3_Robot_SAVE.3mf")
        self.click(names.fdg_btn_save)

        if object.exists(names.mbo_file_exists):
            self.click(names.mbo_btn_overwrite)

        if track_time:
            return Performance.trackFileloadTime()

    def moveModel(self, x_pos):
        self.setTextFieldValue(names.mwi_move_model_x, x_pos)
        self.click(names.mwi)

    def scaleModel(self, size):
        squish.mouseClick(self.findObjectByText(names.mwi_btn_toolbar, "Scale"))

        if not waitForObject(names.mwi_chk_uniform_scaling).checked:
            squish.mouseClick(names.mwi_chk_uniform_scaling)

        self.setTextFieldValue(names.mwi_scale_model_x, size)
        self.click(names.mwi)
