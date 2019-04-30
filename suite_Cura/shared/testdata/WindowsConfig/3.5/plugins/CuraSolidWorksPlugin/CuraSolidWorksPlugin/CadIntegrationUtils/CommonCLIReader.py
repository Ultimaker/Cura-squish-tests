# Copyright (c) 2017 Thomas Karl Pietrowski

# Uranium
from UM.Platform import Platform # @UnresolvedImport
from UM.Logger import Logger # @UnresolvedImport

# CIU
from .CommonReader import CommonReader # @UnresolvedImport

# built-ins
import os
import subprocess

# OS dependent
if Platform.isWindows():
    import winreg

class CommonCLIReader(CommonReader):
    def __init__(self, 
                 app_friendly_name):
        super().__init__(app_friendly_name)
        self._parallel_execution_allowed = True
    
    def preStartApp(self):
        # Nothing needs to be prepared before starting
        pass
    
    def startApp(self, options):
        # No start needed..
        return options
    
    def openForeignFile(self, options):
        # We open the file, while converting.. No actual opening of the file needed..
        return options
    
    def read(self, file_path):
        options = self.readCommon(file_path)
        result = super().readOnSingleAppLayer(options)
        
        # Unlock if needed
        if not self._parallel_execution_allowed:
            self.conversion_lock.release()
        
        return result
    
    def executeCommand(self, command, cwd = os.path.curdir):
        environment_with_additional_path = os.environ.copy()
        if self._additional_paths:
            environment_with_additional_path["PATH"] = os.pathsep.join(self._additional_paths) + os.pathsep + environment_with_additional_path["PATH"]
        Logger.log("i", "Executing command: {}".format(command))
        p = subprocess.Popen(command,
                             cwd = cwd,
                             env = environment_with_additional_path,
                             shell = True,
                             )
        p.wait()
        
    def scanForAllPaths(self):
        self._additional_paths = []
        if Platform.isWindows():
            for file_extension in self._supported_extensions:
                path = self._findPathFromExtension(file_extension)
                Logger.log("d", "Found path for {}: {}".format(file_extension, path))
                if path:
                    self._additional_paths.append(path)
    
    def _findPathFromExtension(self, extension):
        try:
            file_class = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, extension)
            file_class = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, os.path.join(file_class,
                                                                                  "shell",
                                                                                  "open",
                                                                                  "command",
                                                                                  )
                                           )
            file_class = file_class.split("\"")
            while "" in file_class:
                file_class.remove("")
            file_class = file_class[0]
            path = os.path.split(file_class)[0]
            if os.path.isdir(path):
                return path
        except:
            Logger.logException("e", "Could not find PATH for extension: {}".format(extension))
        return