# encoding: UTF-8
from objectmaphelper import *

# Main Window (mwi)
mwi = {"title": "Ultimaker Cura", "type": "MainWindow", "unnamed": 1, "visible": True}
mwi_ovl = {"container": mwi, "type": "Overlay", "unnamed": 1, "visible": True}
qqw_qml = {"type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}

# Cura Main Page
mwi_btn_open_file = {"checkable": False, "container": mwi, "id": "openFileButton", "type": "Button", "unnamed": 1, "visible": True}

# Printers
mwi_printer = {"container": mwi, "id": "machineSelection", "type": "MachineSelector", "unnamed": 1, "visible": True}
mwi_sel_printer = {"container": mwi_printer, "type": "Label", "unnamed": 1, "visible": True}
mwi_btn_manage_printers = {"checkable": False, "container": mwi_ovl, "id": "managePrinterButton", "type": "ActionButton", "unnamed": 1, "visible": True}
mwi_printer_list = {"container": mwi_ovl, "id": "machineSelectorList", "type": "MachineSelectorList", "unnamed": 1, "visible": True}

# Print Settings
mwi_print_settings = {"container": mwi, "id": "printSetupSelectorItem", "type": "Item", "unnamed": 1, "visible": True}

# Slicing
mwi_btn_slice = {"checkable": False, "container": mwi, "id": "sliceButton", "type": "ActionButton", "unnamed": 1, "visible": True}
mwi_btn_save_to_file = {"checkable": False, "container": mwi, "id": "saveToButton", "type": "ActionButton", "unnamed": 1, "visible": True}
mwi_btn_preview = {"checkable": False, "container": mwi, "id": "previewStageShortcut", "type": "ActionButton", "unnamed": 1, "visible": True}

# Extruders
mwi_lst_extruders = {"container": mwi, "id": "extrudersList", "type": "ListView", "unnamed": 1, "visible": True}
mwi_item_extruder = {"container": mwi_lst_extruders, "index": 0, "type": "Item", "unnamed": 1, "visible": True}
mwi_lbl_extruder = {"container": mwi_item_extruder, "type": "Label", "unnamed": 1, "visible": True}

# Menu (mnu, top level menu bar)
mnu_bar = {"container": mwi, "id": "menuBarLoader", "type": "Loader", "unnamed": 1, "visible": True}
mnu_item = {"container": mnu_bar, "plainText": "", "type": "StyleItem1", "unnamed": 1, "visible": True}

qqm_mnu_popup = {"type": "QQuickMenuPopupWindow1", "unnamed": 1, "visible": True}
scroll_view = {"container": qqm_mnu_popup, "id": "scrollView", "type": "ScrollView", "unnamed": 1, "visible": True}

# Toolbar
mwi_btn_toolbar = {"checkable": True, "container": mwi, "text": "", "type": "ToolbarButton", "unnamed": 1, "visible": True}

# Move Model
mwi_move_model_x = {"container": mwi, "id": "xTextField", "type": "TextField", "unnamed": 1, "visible": True}

# Scale Model
mwi_scale_model_x = {"container": mwi, "id": "xPercentage", "type": "TextField", "unnamed": 1, "visible": True}
mwi_chk_uniform_scaling = {"container": mwi, "id": "uniformScalingCheckbox", "type": "CheckBox", "unnamed": 1, "visible": True}

# Onboarding (onb)
onb_panel = {"container": mwi, "id": "wizardPanel", "type": "WizardPanel", "unnamed": 1, "visible": True}
obn_page_title = {"container": onb_panel, "type": "Label", "unnamed": 1, "visible": True}
onb_btn_next = {"checkable": False, "container": onb_panel, "id": "getStartedButton", "type": "ActionButton", "unnamed": 1, "visible": True}

# onb landing
onb_btn_get_started = {"checkable": False, "container": onb_panel, "id": "getStartedButton", "type": "ActionButton", "unnamed": 1, "visible": True}

# onb licence
onb_btn_accept_agreement = {"checkable": False, "container": onb_panel, "id": "agreeButton", "type": "ActionButton", "unnamed": 1, "visible": True}
onb_btn_decline_close = {"checkable": False, "container": mwi, "id": "declineButton", "type": "ActionButton", "unnamed": 1, "visible": True}

# onb changelog
onb_win_changelog = {"container": onb_panel, "id": "whatsNewTextArea", "type": "ScrollableTextArea", "unnamed": 1, "visible": True}

# onb data collection
onb_img_improve_cura = {"container": onb_panel, "id": "curaImage", "type": "Image", "unnamed": 1, "visible": True}

# onb cloud
onb_btn_create_acc = {"checkable": False, "container": mwi, "id": "createAccountButton", "type": "ActionButton", "unnamed": 1, "visible": True}
onb_btn_sign_in = {"container": mwi, "id": "signInButton", "type": "Label", "unnamed": 1, "visible": True}
onb_btn_finish = {"checkable": False, "container": mwi, "id": "finishButton", "type": "ActionButton", "unnamed": 1, "visible": True}

# File Dialog (fdg)
fdg = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
fdg_lbl_name = {"name": "fileNameLabel", "type": "QLabel", "visible": 1, "window": fdg}
fdg_input_name = {"buddy": fdg_lbl_name, "name": "fileNameEdit", "type": "QLineEdit", "visible": 1}
fdg_btn_open = {"text": "Open", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": fdg}
fdg_btn_save = {"text": "Save", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": fdg}
fdg_cbo_file_type = {"name": "fileTypeCombo", "type": "QComboBox", "visible": 1, "window": fdg}

mbo_file_exists = {"type": "QMessageBox", "unnamed": 1, "visible": 1}
mbo_btn_overwrite = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mbo_file_exists}

# Open 3MF Dialog
btn_open_as_prj = {"container": qqw_qml, "id": "openAsProjectButton", "type": "Button", "unnamed": 1, "visible": True}
btn_open_save_summary = {"container": qqw_qml, "id": "ok_button", "type": "Button", "unnamed": 1, "visible": True}

# Generic sub-menu item
sub_mnu_item = {"container": scroll_view, "text": "", "type": "StyleItem1", "unnamed": 1, "visible": True}

# Generic close-button
btn_close = {"container": qqw_qml, "id": "closeButton", "type": "Button", "unnamed": 1, "visible": True}

# Add Printer dialog (pdg)
pdg_btn_add_printer = {"checkable": False, "container": qqw_qml, "id": "nextButton", "type": "ActionButton", "unnamed": 1, "visible": True}

# network
pdg_cbo_network_printer = {"container": qqw_qml, "id": "addNetworkPrinterDropDown", "type": "DropDownWidget", "unnamed": 1, "visible": True}
pdg_win_network_printer = {"container": qqw_qml, "id": "networkPrinterScrollView", "type": "AddNetworkPrinterScrollView", "unnamed": 1, "visible": True}
pdg_btn_troubleshoot = {"container": pdg_win_network_printer, "id": "troubleshootingButton", "type": "Item", "unnamed": 1, "visible": True}
pdg_btn_refresh = {"checkable": False, "container": pdg_win_network_printer, "id": "refreshButton", "type": "ActionButton", "unnamed": 1, "visible": True}
pdg_btn_add_printer_by_ip = {"checkable": False, "container": pdg_win_network_printer, "id": "addPrinterByIpButton", "type": "ActionButton", "unnamed": 1, "visible": True}
pdg_input_address = {"container": qqw_qml, "echoMode": 0, "id": "hostnameField", "type": "TextField", "unnamed": 1, "visible": True}
pdg_btn_add_ip_printer = {"checkable": False, "container": qqw_qml, "id": "addPrinterButton", "type": "ActionButton", "unnamed": 1, "visible": True}
pdg_btn_connect = {"checkable": False, "container": qqw_qml, "id": "connectButton", "type": "ActionButton", "unnamed": 1, "visible": True}

# local
pdg_cbo_local_printer = {"container": qqw_qml, "id": "addLocalPrinterDropDown", "type": "DropDownWidget", "unnamed": 1, "visible": True}
pdg_win_local_printer = {"container": qqw_qml, "id": "localPrinterSelectionItem", "type": "Item", "unnamed": 1, "visible": True}
pdg_rbtn_printer = {"checkable": True, "container": pdg_win_local_printer, "id": "radioButton", "text": "", "type": "RadioButton", "unnamed": 1, "visible": True}

# Remove printer dialog (rpd)
rpd_win = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Confirm Remove"}
rpd_btn_confirm = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": rpd_win}

# Preferences
mnu_preferences = {"container": qqw_qml, "id": "pagesList", "type": "TableView", "unnamed": 1, "visible": True}
mnu_item_preferences = {"container": mnu_preferences, "objectName": "label", "text": "", "type": "Text", "visible": True}
prf_mnu_btn = {"container": qqw_qml, "id": "activateMenuButton", "type": "Button", "unnamed": 1, "visible": True}

# Materials preferences (mat)
mat_btn_selection = {"container": mwi_ovl, "id": "materialSelection", "type": "Button", "unnamed": 1, "visible": True}
mat_mnu_manage = {"container": scroll_view, "text": "Manage Materials...", "type": "StyleItem1", "unnamed": 1, "visible": True}

# custom brand
mat_cbo_custom = {"container": qqw_qml, "id": "brandSection", "sectionName": "Custom", "type": "MaterialsBrandSection", "unnamed": 1, "visible": True}

# material section of brand
mat_header = {"container": mat_cbo_custom, "id": "material_type_header", "type": "Row", "unnamed": 1, "visible": True}
mat_header_custom = {"container": mat_header, "text": "PLA", "type": "Text", "unnamed": 1, "visible": True}

# material of brand
mat_custom_pla = {"container": mat_cbo_custom, "text": "Custom PLA Custom", "type": "Text", "unnamed": 1, "visible": True}

# Printer preferences (pps)
win_pps = {"container": qqw_qml, "id": "base", "type": "MachinesPage", "unnamed": 1, "visible": True}
pps_printer_list = {"container": win_pps, "id": "objectList", "type": "ListView", "unnamed": 1, "visible": True}
pps_printer_item = {"container": pps_printer_list, "text": "", "type": "Text", "unnamed": 1, "visible": True}
pps_local_printers = {"container": pps_printer_list, "text": "Local printers", "type": "Text", "unnamed": 1, "visible": True}
pps_network_printers = {"container": pps_printer_list, "text": "Network printers", "type": "Text", "unnamed": 1, "visible": True}
win_rename_printer = {"title": "Rename", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
input_printer_name = {"container": win_rename_printer, "id": "nameField", "type": "TextField", "unnamed": 1, "visible": True}
btn_rename_confirm = {"container": win_rename_printer, "text": "OK", "type": "Button", "unnamed": 1, "visible": True}
pps_btn_machine_settings = {"container": qqw_qml, "text": "Machine Settings", "type": "Button", "unnamed": 1, "visible": True}

# Profile preferences (pfs)
win_create_profile = {"title": "Create Profile", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
input_profile_name = {"container": win_create_profile, "type": "Column", "unnamed": 1, "visible": True}
btn_create_profile_confirm = {"container": win_create_profile, "type": "Button", "unnamed": 1, "visible": True}

# Print Settings (prs)
win_print_settings = {"container": mwi, "type": "PrintSetupSelectorContents", "unnamed": 1, "visible": True}
prs_btn_custom = {"checkable": False, "container": mwi, "id": "customSettingsButton", "type": "ActionButton", "unnamed": 1, "visible": True}
prs_custom_view = {"container": mwi, "id": "customPrintSetup", "type": "CustomPrintSetup", "unnamed": 1, "visible": True}
prs_btn_sel_profile = {"container": prs_custom_view, "id": "globalProfileSelection", "type": "Button", "unnamed": 1, "visible": True}
prs_chk_gradual_infill = {"container": mwi, "id": "enableGradualInfillCheckBox", "type": "CheckBox", "unnamed": 1, "visible": True}

# Marketplace (mar)
mwi_btn_marketplace = {"checkable": False, "container": mwi, "id": "marketplaceButton", "type": "Button", "unnamed": 1, "visible": True}
win_marketplace = {"title": "Marketplace", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
mar_downloads = {"container": win_marketplace, "id": "viewDownloads", "type": "ScrollView", "unnamed": 1, "visible": True}
mar_view = {"container": win_marketplace, "type": "ScrollView", "unnamed": 1, "visible": True}
mar_btn_quit_cura = {"checkable": False, "container": win_marketplace, "id": "restartButton", "type": "ActionButton", "unnamed": 1, "visible": True}
mar_btn_install = {"container": mar_view, "id": "installButton", "type": "ToolboxProgressButton", "unnamed": 1, "visible": True}

plugin_auto_orientation = {"container": mar_downloads, "text": "Auto-Orientation", "type": "Text", "unnamed": 1, "visible": True}
plugin_barbarian_units = {"container": mar_view, "text": "Barbarian Units", "type": "Text", "unnamed": 1, "visible": True}
plugin_customer_supports = {"container": mar_view, "text": "Custom Supports", "type": "Text", "unnamed": 1, "visible": True}

# Plugin License Agreement
win_plugin = {"title": "Plugin License Agreement", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
plugin_lcs_btn_accept = {"container": win_plugin, "id": "acceptButton", "type": "Button", "unnamed": 1, "visible": True}
plugin_btn_installed = {"checkable": False, "container": mar_view, "id": "installedButton", "type": "ActionButton", "unnamed": 1, "visible": True}
