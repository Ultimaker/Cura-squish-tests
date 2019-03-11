# -*- coding: utf-8 -*-
import os

# @OnFeatureStart
# def hook(context):
# #     Set the CWD to the testdata folder
#     configFile = findFile("testdata", "WindowsConfig/4.0/cura.cfg")
#     testdataDir = os.getcwd() + "\\" +findFile("testdata","")
#
#     with open(configFile, "r+") as infile:
#         for line in infile:
#             if "local_file" in line:
#                 infile.write("\n"+testdataDir)

@OnFeatureEnd
def hook(context):
    for ctx in applicationContextList():
        ctx.detach()

@OnScenarioStart
def hook(context):
    if context.userData:
        context.userData.clear()
    
def init():
    testSettings.logScreenshotOnError = True;
    testSettings.logScreenshotOnFail = True;
    
# @OnFeatureStart
# def hook(context):
#     pageObject = PageObject()
#     pageObject.presetPreferences()
#     startApplication("Cura")