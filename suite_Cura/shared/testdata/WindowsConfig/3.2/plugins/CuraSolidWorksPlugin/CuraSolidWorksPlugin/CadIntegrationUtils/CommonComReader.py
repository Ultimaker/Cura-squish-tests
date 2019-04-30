# Copyright (c) 2017 Thomas Karl Pietrowski

# Uranium/Cura
from UM.i18n import i18nCatalog # @UnresolvedImport
i18n_catalog = i18nCatalog("CuraSolidWorksIntegrationPlugin")
from UM.Logger import Logger # @UnresolvedImport

# Trying to import one of the COM modules
from .ComFactory import ComConnector
from .CommonReader import CommonReader

class CommonCOMReader(CommonReader):
    def __init__(self,
                 app_friendly_name,
                 app_com_service_family):
        CommonReader.__init__(self, app_friendly_name)
        self._default_app_name = app_com_service_family
        self._default_app_friendly_name = app_friendly_name
    
    @property
    def _app_names(self):
        return [self._default_app_name, ]
    
    def startApp(self, options):
        Logger.log("d", "Calling %s...", options["app_name"])
        
        Logger.log("d", "CreateActiveObject..")
        options["app_was_active"] = True
        try:
            options["app_started_with_coinit"] = False
            options["app_instance"] = ComConnector.CreateActiveObject(options["app_name"])
            return options
        except:
            Logger.logException("d", "Getting active object without Coinit failed")
        
        try:
            Logger.log("d", "CoInit..")
            ComConnector.CoInit()
            options["app_started_with_coinit"] = True
            options["app_instance"] = ComConnector.CreateActiveObject(options["app_name"])
            return options
        except:
            Logger.logException("d", "Getting active object with Coinit failed")
        
        if options["app_started_with_coinit"]:
            Logger.log("d", "UnCoInit..")
            ComConnector.UnCoInit()
        
        Logger.log("d", "Trying to get new class object..")
        options["app_was_active"] = False
        try:
            
            options["app_started_with_coinit"] = False
            options["app_instance"] = ComConnector.CreateClassObject(options["app_name"])
            return options
        except:
            Logger.logException("d", "Getting object without Coinit failed")
        
        try:
            Logger.log("d", "CoInit..")
            ComConnector.CoInit()
            options["app_started_with_coinit"] = True
            options["app_instance"] = ComConnector.CreateClassObject(options["app_name"])
            return options
        except:
            Logger.logException("d", "Getting object with Coinit failed")

        raise Exception("Could not start service!")
    
    def postCloseApp(self, options):
        Logger.log("d", "postCloseApp..")
        if "app_started_with_coinit" in options.keys():
            if options["app_started_with_coinit"]:
                Logger.log("d", "UnCoInit..")
                ComConnector.UnCoInit()
        
    def read(self, file_path):
        options = self.readCommon(file_path)
        result = self.readOnMultipleAppLayer(options)
        
        # Unlock if needed
        if not self._parallel_execution_allowed:
            self.conversion_lock.release()
        
        return result
    
