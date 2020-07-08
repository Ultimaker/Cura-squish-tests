#Copyright (c) 2019 Ultimaker B.V.
#This code is not licensed.

#To get environment variables
import os
#To join paths to get the final path
import os.path
#To detect the current platform
import sys

"""
Class that provides the locations where Cura stores its resources and configuration files.

The class will use the current host operating system to determine where
Cura would store its resources 
"""
class CuraResources:
    """
    Creates the resources instance
    \param cura_version The version that is used in the folder to store
    Cura's resources, such as "4.1".
    """
    def __init__(self, cura_version: str):
        self.cura_version = cura_version

    """
    Get the configuration folder
    
    This contains cura.cfg for the preferences and stderr.log, the log file
    for the latest run of Cura
    """
    @property
    def config(self):
        if sys.platform == "win32":
            config_root = os.getenv("APPDATA")
        elif sys.platform == "darwin":
            config_root = os.path.expanduser("~/Library/Application Support")
        elif sys.platform == "linux":
            try:
                config_root = os.environ["XDG_CONFIG_HOME"]
            except KeyError:
                config_root = os.path.expanduser("~/.config")
        else:
            config_root = "."

        return os.path.join(config_root, "cura", self.cura_version)

    """
    Get the data folder
    
    This contains all of the profiles, scripts, plug-ins and added printers
    """
    @property
    def data(self):
        if sys.platform == "win32":
            data_root = os.getenv("APPDATA")
        elif sys.platform == "darwin":
            data_root = os.path.expanduser("~/Library/Application Support")
        elif sys.platform == "linux":
            try:
                data_root = os.environ["XDG_DATA_HOME"]
            except KeyError:
                data_root = os.path.expanduser("~/.local/share")
        else:
            data_root = "."

        return os.path.join(data_root, "cura", self.cura_version)

    """
    Get the cache folder
    
    The cache folder contains temporary files that make Cura start up faster
    """
    @property
    def cache(self):
        if sys.platform == "win32":
            cache_root = os.getenv("LOCALAPPDATA")
        elif sys.platform == "darwin":
            cache_root = os.path.expanduser("~/Library/Application Support")
        elif sys.platform == "linux":
            try:
                cache_root = os.environ["XDG_CACHE_HOME"]
            except KeyError:
                cache_root = os.path.expanduser("~/.cache")
        else:
            cache_root = "."

        return os.path.join(cache_root, "cura", self.cura_version)