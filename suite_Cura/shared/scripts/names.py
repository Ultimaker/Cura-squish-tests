# encoding: UTF-8
from objectmaphelper import *

# Main window
mainWindow = {"title": "Ultimaker Cura", "type": "MainWindow", "unnamed": 1, "visible": True}
mainWindowPrinter = {"container": mainWindow, "id": "machineSelection", "type": "MachineSelector", "unnamed": 1, "visible": True}
mainWindowSelectedPrinter = {"container": mainWindowPrinter, "type": "Label", "unnamed": 1, "visible": True}

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