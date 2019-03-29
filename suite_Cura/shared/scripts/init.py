# -*- coding: utf-8 -*-

# Load this file at the beginning of each test case' test.py via...
#    
#  source(findFile("scripts", "init.py"))
#
# It makes custom python modules possible (pageobjects) that are not in sys.path

import os.path
import sys

paths = []
for p in sys.path:
    # Remove all shared/scripts:
    if p.endswith("/shared/scripts"):
        sys.path.remove(p)
    if p.endswith("\\shared\\scripts"):
        sys.path.remove(p)

    # Remove duplicates:
    if p not in paths:
        paths.append(p)
    else:
        sys.path.remove(p)

# Add our shared/scripts:
sys.path.insert(0, os.path.join(squishinfo.testCase + "/../shared/scripts"))
