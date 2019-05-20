# -*- coding: utf-8 -*-
import json
import datetime


@OnFeatureEnd
def hook(context):
    for ctx in applicationContextList():
        ctx.detach()


@OnScenarioStart
def hook(context):
    if context.userData:
        context.userData.clear()


# TODO: Fix when updating Performance tests to export results
@OnScenarioEnd
def hook(context, current_data=None):
    if current_data is None:
        current_data = {}

    if context.userData:
        performance_results = findFile("scripts", "TestResults/Performance.json")

        with open(performance_results, "r") as new_file:
            try:
                current_data = json.load(new_file)
            except Exception as e:
                print(e)

        # Format data so its more readable and easier to analyze
        jsondata = {"data": []}
        content, results = {}, {}

        # Using context.userData in steps to store results that I can extract here
        # TODO: context.userData is sometimes used for things other than performance results. Filter those out!
        results["GUI"] = next(iter(context.userData.values()))

        content["measurements"] = context.title
        now = datetime.datetime.now()
        content["datetime"] = now.strftime("%Y-%m-%d %H:%M:%S")
        content["fields"] = results

        with open(performance_results, "w") as new_file:
            if "data" in current_data:
                current_data['data'].append(content)
                json.dump(current_data, new_file, indent=4)
            else:
                jsondata['data'].append(content)
                json.dump(jsondata, new_file, indent=4)


def init():
    testSettings.logScreenshotOnError = True
    testSettings.logScreenshotOnFail = True
