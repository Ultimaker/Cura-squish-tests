# -*- coding: utf-8 -*-
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