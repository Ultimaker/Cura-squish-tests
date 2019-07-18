# Copyright (c) 2019 Ultimaker B.V.

import os #To install the PPA plug-in.
import os.path #To install the PPA plug-in.
import shutil #To install the PPA plug-in.

from PageObjects.CommonPage import PageObject

##  Interacts with the PPA sidebar.
class PPA(PageObject):
    ##  Installs the PPA plug-in in the user's configuration.
    #
    #   The plug-in will be copied from the folder next to the
    #   Cura-squish-tests repository. If you want the repository to contain a
    #   specific branch or commit, please check that branch out in the
    #   repository before running the test.
    def install(self):
        source_location = os.path.abspath(os.path.join(__file__, "..", "..", "..", "..", "..", "..", "CuraPrintProfileCreator"))
        target_location = os.path.join(self.cura_resources.data, "plugins", "CuraPrintProfileCreator")
        if os.path.exists(target_location):
            os.remove(target_location) #Copytree fails if it already exists. Remove first so we guarantee that it copies properly.
        shutil.copytree(source_location, target_location)