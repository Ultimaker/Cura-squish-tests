# encoding: UTF-8
from objectmaphelper import *

# Main window
mainWindow = {"title": "Ultimaker Cura", "type": "MainWindow", "unnamed": 1, "visible": True}

# Cura Menu
mainWindowPrinter = {"container": mainWindow, "id": "machineSelection", "type": "MachineSelector", "unnamed": 1, "visible": True}
mainWindowSelectedPrinter = {"container": mainWindowPrinter, "type": "Label", "unnamed": 1, "visible": True}
mainWindowOpenFile = {"checkable": False, "container": mainWindow, "id": "openFileButton", "type": "Button", "unnamed": 1, "visible": True}

# File Dialog
fileDialog = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
fileNameLabel = {"name": "fileNameLabel", "type": "QLabel", "visible": 1, "window": fileDialog}
fileNameInput = {"buddy": fileNameLabel, "name": "fileNameEdit", "type": "QLineEdit", "visible": 1}
openFile = {"text": "Open", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": fileDialog}

# Menu (top-level)
menuBar = {"container": mainWindow, "id": "menuBarLoader", "type": "Loader", "unnamed": 1, "visible": True}
menuItem = {"container": menuBar, "plainText": "", "type": "StyleItem1", "unnamed": 1, "visible": True}

o_QQuickMenuPopupWindow = {"type": "QQuickMenuPopupWindow1", "unnamed": 1, "visible": True}
scrollView = {"container": o_QQuickMenuPopupWindow, "id": "scrollView", "type": "ScrollView", "unnamed": 1, "visible": True}
configureCura = {"container": scrollView, "text": Wildcard("Configure Cura*"), "type": "StyleItem1", "unnamed": 1, "visible": True}

# Changelog
changelogWindow = {"title": "Changelog", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
changelogClose = {"container": changelogWindow, "text": "Close", "type": "Button", "unnamed": 1, "visible": True}

# Agreement
agreementDialog = {"title": "User Agreement", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
agreementButton = {"container": agreementDialog, "text": "I understand and agree", "type": "Button", "unnamed": 1, "visible": True}

# Printer dialog
addPrinterDialog = {"title": "Add Printer", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
addPrinter = {"container": addPrinterDialog, "id": "addPrinterButton", "text": "Add Printer", "type": "Button", "unnamed": 1, "visible": True}
addPrinterFinish = {"container": addPrinterDialog, "id": "nextButton", "text": "Finish", "type": "Button", "unnamed": 1, "visible": True}

printerView = {"container": addPrinterDialog, "id": "machinesHolder", "type": "ScrollView", "unnamed": 1, "visible": True}
printerList = {"container": printerView, "id": "machineList", "type": "ListView", "unnamed": 1, "visible": True}
selectedPrinter = {"container": printerList, "id": "machineButton", "text": "", "type": "AbstractCheckable", "unnamed": 1, "visible": True}

# Preferences
preferenceWindow = {"title": "Preferences", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
preferencesMenu = {"container": preferenceWindow, "id": "pagesList", "type": "TableView", "unnamed": 1, "visible": True}
preferencesMenuItem = {"container": preferencesMenu, "objectName": "label", "text": "", "type": "Text", "visible": True}

# Printer preferences
preferencesMenuButton = {"container": preferenceWindow, "text": "", "type": "Button", "unnamed": 1, "visible": True}
printerListView = {"container": preferenceWindow, "id": "objectList", "type": "ListView", "unnamed": 1, "visible": True}
printerListItem = {"container": printerListView, "text": Wildcard("*"), "type": "Text", "unnamed": 1, "visible": True}

# Slice button
sliceButton = {"checkable": False, "container": mainWindow, "id": "sliceButton", "text": "Slice", "type": "ActionButton", "unnamed": 1, "visible": True}
