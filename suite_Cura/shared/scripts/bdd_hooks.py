# -*- coding: utf-8 -*-

@OnFeatureEnd
def hook(context):
    for ctx in applicationContextList():
        ctx.detach()

# @OnFeatureStart
# def hook(context):
#     pageObject = PageObject()
#     pageObject.presetPreferences()
#     startApplication("Cura")