# -*- coding: utf-8 -*-
import os
from PageObjects.CommonPage import PageObject
from Helpers.SquishModuleHelper import importSquishSymbols
import squish
from PageObjects.PerformancePage import Performance
import names
# For casting to int, since Squish defines its own int()
import builtins
import sys

class Cura(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        importSquishSymbols()

    def pressCloseButton(self):
        self.click(names.btn_close)
        waitForObject(names.mwi)

    #     Top-level navigation bar
    def navigateTo(self, menu_item, submenu_item, lang=None):
        menu_object = self.findObjectWithText(names.mnu_item, menu_item, "plainText", lang=lang)
        self.click(menu_object)

        submenu_object = self.findObjectWithText(names.sub_mnu_item, submenu_item, lang=lang)
        self.click(submenu_object)

    def navigateToStageMenu(self, stage_item):
        if "Marketplace" in stage_item:
            self.click(names.mwi_btn_marketplace)
            waitForObject(names.mar_scroll_bar)

    def selectExtruderTab(self, extruder_nr_str):
        self.click(names.mwi_printer_config_drop)  # NOTE: Only if not open yet!
        extruder_nr = builtins.int(extruder_nr_str)
        if extruder_nr > 0:
            self.click({"checkable": True, "container": names.mwi_ovl, "occurrence": extruder_nr, "type": "TabButton", "unnamed": 1, "visible": True})

    def checkNozzleTypeText(self, extruder_nr_str, nozzle_text):
        #extruder_nr = builtins.int(extruder_nr_str)
        #obj_extruder_container = {"container": names.mwi}
        obj_nozzle_label = {"container": names.mwi, "text": nozzle_text, "type": "Label", "unnamed": 1, "visible": True}
        #self.click(obj_nozzle_label)
        return object.exists(obj_nozzle_label)

    def selectPrintCore(self, print_core):
        self.click(names.ext_btn_variant)
        btn_print_core = self.findObjectWithText(names.gen_mnu_item, print_core)
        self.click(btn_print_core)

    def openPrintSettings(self):
        if not object.exists(names.win_print_settings):
            self.click(names.mwi_print_settings)

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
        self.setTextFieldValue(names.fdg_input_name, self.testdata_dir + '\\' + file_name)

        self.click(names.fdg_cbo_file_type)
        squish.mouseClick(waitForObjectItem(names.fdg_cbo_file_type, "G-code File (*\\.gcode)"))

        self.click(names.fdg_btn_save)

        if object.exists(names.mbo_confirm_dialog):
            self.click(names.mbo_btn_confirm)

        return findFile("testdata", file_name)

    def openFileAsProject(self):
        self.click(names.btn_open_as_prj)

    def openFileFromSummary(self, track_time=False):
        self.click(names.btn_open_save_summary)

        if track_time:
            return Performance.trackFileloadTime()

    def saveAsProject(self, track_time):
        self.click(names.btn_open_save_summary)
        self.click(self.findObjectWithText(names.fdg_save_userfolder, os.getlogin()))
        self.setTextFieldValue(names.fdg_input_name, "UM3_Robot__Saved.3mf")
        self.click(names.fdg_btn_save)

        if object.exists(names.mbo_confirm_dialog):
            self.click(names.mbo_btn_confirm)

        if track_time:
            return Performance.trackFileloadTime()

    def moveModel(self, x_pos):
        self.setTextFieldValue(names.mwi_move_model_x, x_pos)
        self.click(names.mwi)

    def scaleModel(self, size):
        squish.mouseClick(self.findObjectWithText(names.mwi_btn_toolbar, "Scale"))

        if not waitForObject(names.mwi_chk_uniform_scaling).checked:
            squish.mouseClick(names.mwi_chk_uniform_scaling)

        self.setTextFieldValue(names.mwi_scale_model_x, size)
        self.click(names.mwi)
    
    def openPOS(self):
        squish.mouseClick(names.mwi_per_model_btn)
    
    def modifyPOSSetting(self, infill_density):
        squish.mouseClick(names.field_per_model)
        self.setTextFieldValue(names.field_per_model, infill_density)

    def openRecommendedView(self):
        self.click(names.prs_btn_recommended)
    
    def loadOtherTypeFiles(self, filename):
        # Navigate to the correct dir first
        self.setTextFieldValue(names.fdg_input_name, self.testdata_dir)
        squish.clickButton(waitForObject(names.fdg_btn_open))

        self.setTextFieldValue(names.fdg_input_name, filename)
        squish.clickButton(waitForObject(names.fdg_btn_open))
        squish.clickButton(waitForObject(names.mbo_btn_OK))
        
        
    def closeGenericCategory(self):
        squish.mouseClick(names.mat_general_category_arrow)
        
    
    def rememberMyChoice(self):
        checkBoxToVerify = waitForObject(names.open_project_file_Remember_my_choice_CheckBox)
        if checkBoxToVerify.checked == False:
            test.log("Checkbox already checked")
            self.click(checkBoxToVerify)
        else:
            return

