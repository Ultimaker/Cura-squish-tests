# -*- coding: utf-8 -*-
import json


@OnFeatureEnd
def hook(context):
    for ctx in applicationContextList():
        ctx.detach()


@OnScenarioStart
def hook(context):
    if context.userData:
        context.userData.clear()


@OnScenarioEnd
def hook(context):
    if context.userData:
        performance_results = findFile("scripts", "TestResults/Performance.txt")
        with open(performance_results, "a") as new_file:
            new_file.write(json.dumps(context.title) + "\n")
            new_file.write(json.dumps(context.userData) + "\n")


def init():
    testSettings.logScreenshotOnError = True
    testSettings.logScreenshotOnFail = True
