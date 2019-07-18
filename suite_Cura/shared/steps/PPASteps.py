# Copyright (c) 2019 Ultimaker B.V.

from PageObjects.PPAPage import PPA

#Steps that can be executed on the PPA.

ppa = PPA()

@Given("the PPA plug-in is installed")
def step(context):
    ppa.install()

@When("I create a new PPA experiment called '|any|'")
def step(context, experiment_name):
    ppa.new_experiment(experiment_name)

@When("I set the PPA experiment configuration '|any|' to '|any|'")
def step(context, configuration_name, value):
    ppa.set_configuration(configuration_name, value)