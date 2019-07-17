# Copyright (c) 2019 Ultimaker B.V.

from PageObjects.PPAPage import PPA

#Steps that can be executed on the PPA.

ppa = PPA()

@Given("the PPA plug-in is installed")
def step(context):
    ppa.install()