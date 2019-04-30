# Copyright (c) 2017 Thomas Karl Pietrowski

# Buildins
import os
import tempfile
import threading
import uuid
import platform

# Uranium/Cura
from UM.Application import Application # @UnresolvedImport
from UM.Logger import Logger # @UnresolvedImport
from UM.i18n import i18nCatalog # @UnresolvedImport
from UM.Mesh.MeshReader import MeshReader # @UnresolvedImport
from UM.Message import Message # @UnresolvedImport
from UM.PluginRegistry import PluginRegistry # @UnresolvedImport

if platform.system() == "Windows":
    from .SystemUtils import convertDosPathIntoLongPath

i18n_catalog = i18nCatalog("CadIntegrationUtils")

class CommonReader(MeshReader):
    conversion_lock = threading.Lock()

    def __init__(self,
                 app_friendly_name):
        super().__init__()
        
        # Setting default aka fallback
        self._default_app_friendly_name = app_friendly_name
        
        # By default allow no parallel execution. Just to be failsave...
        self._parallel_execution_allowed = False
        
        # # Start/stop behaviour

        # Technically neither preloading nor keeping the instance up, is possible, since Cura calls the file reader from different/new threads
        # The error when trying to use it here is:
        # > pywintypes.com_error: (-2147417842, 'The application called an interface that was marshalled for a different thread.', None, None)
        self._app_preload = False
        self._app_keep_running = False

        """
        if self._app_preload and not self._app_keep_running:
            self._app_keep_running = True
        """

        # Preparations
        """
        if self._app_preload:
            Logger.log("d", "Preloading %s..." %(self._app_friendlyName))
            self.startApp()
        """
        
        # Quality
        self.quality_classes = None
        
        # Doing some routines after all plugins are loaded
        app_instance = Application.getInstance()
        if "pluginsLoaded" in dir(app_instance):
            Application.getInstance().pluginsLoaded.connect(self._onAfterPluginsLoaded)
        else:
            Application.getInstance().engineCreatedSignal.connect(self._onAfterPluginsLoaded)

    @property
    def _app_names(self):
        return []
    
    @property
    def _prefered_app_name(self):
        return None

    def _onAfterPluginsLoaded(self):
        return None

    def preStartApp(self, options):
        pass

    def getAppVisible(self, state):
        raise NotImplementedError("Toggle for visibility not implemented!")

    def setAppVisible(self, state, options):
        raise NotImplementedError("Toggle for visibility not implemented!")

    def closeApp(self, options):
        raise NotImplementedError("Procedure how to close your app is not implemented!")
    
    def postCloseApp(self, options):
        pass

    def openForeignFile(self, options):
        "This function shall return options again. It optionally contains other data, which is needed by the reader for other tasks later."
        raise NotImplementedError("Opening files is not implemented!")

    def exportFileAs(self, options, quality_enum = None):
        raise NotImplementedError("Exporting files is not implemented!")

    def closeForeignFile(self, options):
        raise NotImplementedError("Closing files is not implemented!")

    def renameNodes(self, options, scene_nodes):
        for scene_node in scene_nodes:
            if not scene_node.hasChildren():
                mesh_data = scene_node.getMeshData()
                Logger.log("d", "File path in mesh was: %s", mesh_data.getFileName())
                mesh_data = mesh_data.set(file_name = options["foreignFile"])
                scene_node.setMeshData(mesh_data)
            else:
                self.renameNodes(options, scene_node.getAllChildren())
        return scene_nodes

    def nodePostProcessing(self, options, scene_nodes):
        self.renameNodes(options, scene_nodes)
        return scene_nodes

    def readCommon(self, file_path):
        "Common steps for each read"

        options = {"foreignFile": file_path,
                   "foreignFormat": os.path.splitext(file_path)[1],
                   "tempFileKeep" : False,
                   "fileFormats" : [],
                   }

        # Let's convert only one file at a time!
        if not self._parallel_execution_allowed:
            self.conversion_lock.acquire()
        
        # Append all formats which are not preferred to the end of the list
        return options
        
    def preRead(self, options):
        return MeshReader.PreReadResult.accepted
        
    def readOnSingleAppLayer(self, options):
        scene_node = None
        
        # Tell the loaded application to open a file...
        Logger.log("d", "... and opening file.")
        options = self.openForeignFile(options)
                   
        # Trying to convert into all formats 1 by 1 and continue with the successful export
        Logger.log("i", "Trying to convert into one of: %s", options["fileFormats"])
        for file_format in options["fileFormats"]:
            Logger.log("d", "Trying to convert <%s>...", os.path.split(options["foreignFile"])[1])
            options["tempType"] = file_format
            
            # Creating a new unique filename in the temporary directory..
            tempdir = tempfile.gettempdir()
            Logger.log("d", "Using suggested tempdir: {}". format(repr(tempdir)))
            if platform.system() == "Windows":
                tempdir = convertDosPathIntoLongPath(tempdir)
            options["tempFile"] = os.path.join(tempdir,
                                               "{}.{}".format(uuid.uuid4(), file_format.upper()),
                                               )
            Logger.log("d", "... into '%s' format: <%s>", file_format, options["tempFile"])
            # Export using quality classes if possible
            if self.quality_classes is None:
                quality_classes = {None : None}
            else:
                quality_classes = self.quality_classes
                
            quality_enums = list(quality_classes.keys())
            quality_enums.sort()
            quality_enums.reverse()
            
            if "app_export_quality" in options.keys():
                quality_enum_target = options["app_export_quality"]
                while quality_enums[0] > quality_enum_target:
                    del quality_enums[0]
            
            for quality_enum in quality_enums:
                try:
                    self.exportFileAs(options, quality_enum = quality_enum)
                except:
                    Logger.logException("e", "Could not export <%s> into '%s'.", options["foreignFile"], file_format)
                    continue
                
                if os.path.isfile(options["tempFile"]):
                    size_of_file_mb = os.path.getsize(options["tempFile"]) / 1024 ** 2 
                    Logger.log("d", "Found temporary file! (size: {}MB)".format(size_of_file_mb))
                    break
                else:
                    Logger.log("c", "Temporary file not found after export! (next quality class..)")
                    continue
            if not os.path.isfile(options["tempFile"]):
                Logger.log("c", "Temporary file not found after export! (next file format..)")
                continue
            
            if "app_export_quality" in options.keys():
                if quality_enum is not quality_enum_target:
                    error_message = Message(i18n_catalog.i18nc("@info:status",
                                                               "Could not export using \"{}\" quality!\nFelt back to \"{}\".".format(self.quality_classes[quality_enum_target],
                                                                                                                                     self.quality_classes[quality_enum]
                                                                                                                                     )
                                                               )
                                            )
                    error_message.show()
                    
            # Opening the resulting file in Cura
            try:
                reader = Application.getInstance().getMeshFileHandler().getReaderForFile(options["tempFile"])
                if not reader:
                    Logger.log("d", "Found no reader for %s. That's strange...", file_format)
                    continue
                Logger.log("d", "Using reader: %s", reader.getPluginId())
                scene_node = reader.read(options["tempFile"])
                if not scene_node:
                    Logger.log("d", "Scene node is {}. Trying next format and therefore other file reader!".format(repr(scene_node)))
                    continue
                break
            except:
                Logger.logException("e", "Failed to open exported <%s> file in Cura!", file_format)
                continue
            finally:
                # Whatever happens, remove the temp_file again..
                if not options["tempFileKeep"]:
                    Logger.log("d", "Removing temporary %s file, called <%s>", file_format, options["tempFile"])
                    os.remove(options["tempFile"])
                else:
                    Logger.log("d", "Keeping temporary %s file, called <%s>", file_format, options["tempFile"])
        
        return scene_node

    def readOnMultipleAppLayer(self, options):
        scene_node = None
        
        list_of_apps = self._app_names
        prefered_app = self._prefered_app_name
        if prefered_app:
            if prefered_app in list_of_apps:
                list_of_apps.remove(prefered_app)
            list_of_apps = [prefered_app,] + list_of_apps
         
        for app_name in list_of_apps:
            if prefered_app and app_name is not prefered_app:
                Logger.log("e", "Couldn't use prefered app. Had to fall back!")
            options["app_name"] = app_name
            
            # Preparations before starting the application
            self.preStartApp(options)
            try:
                # Start the app by its name...
                self.startApp(options)
                
                scene_node = self.readOnSingleAppLayer(options)
                if scene_node:
                    # We don't need to test the next application. The result is already there...
                    break
                
            except Exception:
                Logger.logException("e", "Failed to export using '%s'...", app_name)
                # Let's try with the next application...
                continue
            finally:
                # Closing document in the app
                self.closeForeignFile(options)
                # Closing the app again..
                self.closeApp(options)
                # Nuke the instance!
                if "app_instance" in options.keys():
                    del options["app_instance"]
                # .. and finally do some cleanups
                self.postCloseApp(options)

        if not scene_node:
            Logger.log("d", "Scene node is {}. We had no luck to use any of the readers to get the mesh data!".format(repr(scene_node)))
            return scene_node
        elif not isinstance(scene_node, list):
            # This part is needed for reloading converted files into STL - Cura will try otherwise to reopen the temp file, which is already removed.
            scene_node_list = [scene_node,]
        else:
            # Likely the result of an 3MF conversion
            scene_node_list = scene_node

        self.nodePostProcessing(options, scene_node_list)

        return scene_node
