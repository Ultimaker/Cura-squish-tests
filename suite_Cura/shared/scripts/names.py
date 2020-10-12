# encoding: UTF-8
from objectmaphelper import *

# Main Window (mwi)
mwi = {"type": "MainWindow", "unnamed": 1, "visible": True}
mwi_ovl = {"container": mwi, "type": "Overlay", "unnamed": 1, "visible": True}
qqw_qml = {"type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
# Welcome dialog (wel) - on first use
wel_main = {"container": mwi, "id": "welcomeDialogItem", "type": "WelcomeDialogItem", "unnamed": 1, "visible": True}

# Cura Main Page
mwi_btn_open_file = {"checkable": False, "container": mwi, "id": "openFileButton", "type": "Button", "unnamed": 1, "visible": True}

# Printers
mwi_printer = {"container": mwi, "id": "machineSelection", "type": "MachineSelector", "unnamed": 1, "visible": True}
mwi_sel_printer = {"container": mwi_printer, "type": "Label", "unnamed": 1, "visible": True}
mwi_btn_manage_printers = {"checkable": False, "container": mwi_ovl, "id": "managePrinterButton", "type": "ActionButton", "unnamed": 1, "visible": True}
mwi_printer_list = {"container": mwi_ovl, "id": "machineSelectorList", "type": "MachineSelectorList", "unnamed": 1, "visible": True}

# Print Settings
mwi_print_settings = {"container": mwi, "id": "printSetupSelectorItem", "type": "Item", "unnamed": 1, "visible": True}
mwi_mnu_print_settings_profile = {"container": mwi_print_settings, "id": "printSetupSelectorProfileText", "type": "IconWithText", "unnamed": 1, "visible": True}

# Slicing
mwi_btn_slice = {"checkable": False, "container": mwi, "id": "sliceButton", "type": "ActionButton", "unnamed": 1, "visible": True}
mwi_btn_save_to_file = {"checkable": False, "container": mwi, "id": "saveToButton", "type": "ActionButton", "unnamed": 1, "visible": True}
mwi_btn_preview = {"checkable": False, "container": mwi, "id": "previewStageShortcut", "type": "ActionButton", "unnamed": 1, "visible": True}

# Extruders
mwi_lst_extruders = {"container": mwi, "id": "extrudersList", "type": "ListView", "unnamed": 1, "visible": True}
#mwi_item_extruder = {"container": mwi_lst_extruders, "index": 0, "type": "Item", "unnamed": 1, "visible": True}
#mwi_lbl_extruder = {"container": mwi_item_extruder, "type": "Label", "unnamed": 1, "visible": True}
mwi_lbl_extruder = {"container": mwi, "text": "Custom Custom Material", "type": "Label", "unnamed": 1, "visible": True}

# Menu (mnu, top level menu bar)
mnu_bar = {"container": mwi, "id": "menuBarLoader", "type": "Loader", "unnamed": 1, "visible": True}
mnu_item = {"container": mnu_bar, "plainText": "", "type": "StyleItem1", "unnamed": 1, "visible": True}

qqm_mnu_popup = {"type": "QQuickMenuPopupWindow1", "unnamed": 1, "visible": True}
scroll_view = {"container": qqm_mnu_popup, "id": "scrollView", "type": "ScrollView", "unnamed": 1, "visible": True}

# Generic menu item
gen_mnu_item = {"container": scroll_view, "text": "", "type": "StyleItem1", "unnamed": 1, "visible": True}

# Toolbar
mwi_btn_toolbar = {"checkable": True, "container": mwi, "text": "", "type": "ToolbarButton", "unnamed": 1, "visible": True}

mwi_per_model_btn = {"checkable": True, "container": mwi, "text": "Per Model Settings", "type": "ToolbarButton", "unnamed": 1, "visible": True}
mwi_per_model = {"container": mwi, "type": "ScrollView", "unnamed": 1, "visible": True}
field_per_model = {"backgroundcolor": "#ffffff", "container": mwi_per_model, "echoMode": 0, "id": "input", "occurrence": 2, "type": "TextInput", "unnamed": 1, "visible": True}

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
#onb_win_changelog = {"container": onb_panel, "id": "whatsNewTextArea", "type": "ScrollableTextArea", "unnamed": 1, "visible": True}
mwi_changelog = {"container": mwi, "id": "whatsNewTextArea", "type": "ScrollableTextArea", "unnamed": 1, "visible": True}
mwi_changelog_btn_close = {"checkable": False, "container": onb_panel, "id": "getStartedButton", "type": "ActionButton", "text": "Close", "unnamed": 1, "visible": True}

# onb cloud
onb_btn_create_acc = {"checkable": False, "container": mwi, "id": "createAccountButton", "type": "ActionButton", "unnamed": 1, "visible": True}
onb_btn_sign_in = {"container": mwi, "id": "signInButton", "type": "Label", "unnamed": 1, "visible": True}
onb_btn_finish = {"checkable": False, "container": mwi, "id": "finishButton", "type": "ActionButton", "unnamed": 1, "visible": True}
onb_btn_skip = {"container": mwi, "text": "Skip", "type": "Label", "unnamed": 1, "visible": True}

# File Dialog (fdg)
fdg = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
fdg_lbl_name = {"name": "fileNameLabel", "type": "QLabel", "visible": 1, "window": fdg}
fdg_input_name = {"buddy": fdg_lbl_name, "name": "fileNameEdit", "type": "QLineEdit", "visible": 1}
fdg_btn_open = {"text": "Open", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": fdg}
fdg_btn_save = {"text": "Save", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": fdg}
fdg_cbo_file_type = {"name": "fileTypeCombo", "type": "QComboBox", "visible": 1, "window": fdg}
fdg_save_view = {"name": "splitter", "type": "QSplitter", "visible": 1, "window": fdg}
fdg_save_view_sidebar = {"container": fdg_save_view, "name": "sidebar", "type": "QSidebar", "visible": 1}
fdg_save_userfolder = {"container": fdg_save_view_sidebar, "text": "", "type": "QModelIndex"}

mbo_confirm_dialog = {"type": "QMessageBox", "unnamed": 1, "visible": 1}
mbo_btn_confirm = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mbo_confirm_dialog}
mbo_btn_deny = {"text": "No", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mbo_confirm_dialog}
mbo_btn_confirm = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mbo_confirm_dialog}
mbo_btn_OK = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": mbo_confirm_dialog}

# Open 3MF Dialog
btn_open_as_prj = {"container": qqw_qml, "id": "openAsProjectButton", "type": "Button", "unnamed": 1, "visible": True}
btn_open_save_summary = {"container": qqw_qml, "id": "ok_button", "type": "Button", "unnamed": 1, "visible": True}

# Generic sub-menu item
sub_mnu_item = {"container": scroll_view, "text": "", "type": "StyleItem1", "unnamed": 1, "visible": True}
profile_sub_mnu_item = {"checkable": True, "container": mwi_ovl, "id": "button", "text": "", "type": "MenuButton", "unnamed": 1, "visible": True}

# Generic close-button
btn_close = {"container": qqw_qml, "id": "closeButton", "type": "Button", "unnamed": 1, "visible": True}

# Add Printer dialog (pdg)
win_add_printer = {"title": "Add Printer", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
gen_net_printer_view = {"container": win_add_printer, "id": "networkPrinterScrollView", "type": "ScrollView", "unnamed": 1, "visible": True}
btn_net_printer = {"text": "", "checkable": False, "container": gen_net_printer_view, "type": "MachineSelectorButton", "unnamed": 1, "visible": True}
btn_add_printer = {"container": win_add_printer, "text": "Add", "type": "Label", "unnamed": 1, "visible": True}
prs_name_field = {"container": win_add_printer, "echoMode": 0, "id": "printerNameTextField", "type": "TextField", "unnamed": 1, "visible": True}
pdg_btn_add_printer = {"checkable": False, "container": win_add_printer, "id": "nextButton", "type": "ActionButton", "unnamed": 1, "visible": True}

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
pdg_cbo_local_printer = {"container": win_add_printer, "id": "addLocalPrinterDropDown", "type": "DropDownWidget", "unnamed": 1, "visible": True}
pdg_win_local_printer = {"container": win_add_printer, "id": "localPrinterSelectionItem", "type": "Item", "unnamed": 1, "visible": True}
pdg_rbtn_printer = {"checkable": True, "container": pdg_win_local_printer, "id": "radioButton", "text": "", "type": "RadioButton", "unnamed": 1, "visible": True}

# Remove printer dialog (rpd)
rpd_win = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Confirm Remove"}
rpd_btn_confirm = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": rpd_win}

# Preferences
mnu_preferences = {"container": qqw_qml, "id": "pagesList", "type": "TableView", "unnamed": 1, "visible": True}
mnu_item_preferences = {"container": mnu_preferences, "objectName": "label", "text": "", "type": "Text", "visible": True}
prf_mnu_btn = {"container": qqw_qml, "id": "activateMenuButton", "type": "Button", "unnamed": 1, "visible": True}

# Materials preferences (mat)
#mat_base_page = {"container": qqw_qml, "id": "base", "type": "MaterialsPage", "unnamed": 1, "visible": True}
mat_win = {"title": "Preferences", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
mat_panel_details = {"container": mat_win, "id": "materialDetailsView", "type": "MaterialsView", "unnamed": 1, "visible": True}
base_tabbar_TabBar = {"container": mat_panel_details, "objectName": "tabbar", "type": "TabBar", "visible": True}
mat_btn_selection = {"container": mwi_ovl, "id": "materialSelection", "type": "Button", "unnamed": 1, "visible": True}
mat_create_material = {"container": ":win_mps", "iconName": "list-add", "text": "Create", "type": "Button", "unnamed": 1, "visible": True}
mat_btn_unlink = {"container": qqw_qml, "id": "unlinkMaterialButton", "text": "Unlink Material", "type": "Button", "unnamed": 1, "visible": True}
mat_input_name = {"container": mat_panel_details, "id": "displayNameTextField", "type": "ReadOnlyTextField", "unnamed": 1, "visible": True}
mat_input_density = {"container": mat_panel_details, "id": "densitySpinBox", "type": "ReadOnlySpinBox", "unnamed": 1, "visible": True}
mat_input_diameter = {"container": mat_panel_details, "id": "diameterSpinBox", "type": "ReadOnlySpinBox", "unnamed": 1, "visible": True}
mat_input_cost = {"container": mat_panel_details, "id": "spoolCostSpinBox", "type": "SpinBox", "unnamed": 1, "visible": True}
mat_input_weight = {"container": mat_panel_details, "id": "spoolWeightSpinBox", "type": "SpinBox", "unnamed": 1, "visible": True}
mat_material_item = {"container": mat_win, "text": "Custom Custom Material", "type": "Text", "unnamed": 1, "visible": True}
mat_setting_line = {"container": mat_panel_details, "type": "TooltipArea", "unnamed": 1, "visible": True}
mat_printsettings_tab = {"container": base_tabbar_TabBar, "id": "styleitem", "type": "StyleItem1", "unnamed": 1, "visible": True}
mat_input_build_temperature = {"container": mat_panel_details, "index": 1, "type": "TooltipArea", "unnamed": 1, "visible": True}
mat_input_retraction_distance = {"container": mat_panel_details, "index": 2, "type": "TooltipArea", "unnamed": 1, "visible": True}
mat_input_retraction_speed = {"container": mat_panel_details, "index": 3, "type": "TooltipArea", "unnamed": 1, "visible": True}
mat_input_standby_temperature = {"container": mat_panel_details, "index": 4, "type": "TooltipArea", "unnamed": 1, "visible": True}
mat_input_fan_speed = {"container": mat_panel_details, "index": 5, "type": "TooltipArea", "unnamed": 1, "visible": True}
mat_scroll_bar = {"container": qqw_qml, "id": "vscrollbar", "type": "ScrollBar", "unnamed": 1, "visible": True}


# custom brand
mat_cbo_custom = {"container": qqw_qml, "id": "brandSection", "sectionName": "Custom", "type": "MaterialsBrandSection", "unnamed": 1, "visible": True}
mat_ScrollView = {"container": mat_win, "id": "materialScrollView", "type": "ScrollView", "unnamed": 1, "visible": True}
mat_general_category_arrow = {"container": mat_ScrollView, "id": "brand_header", "type": "Row", "unnamed": 1, "visible": True}
# material section of brand
mat_header = {"container": mat_cbo_custom, "id": "material_type_header", "type": "Row", "unnamed": 1, "visible": True}
mat_header_custom = {"container": mat_header, "text": "PLA", "type": "Text", "unnamed": 1, "visible": True}

# material of brand
mat_custom_pla = {"container": mat_cbo_custom, "text": "Custom PLA Custom", "type": "Text", "unnamed": 1, "visible": True}
mat_custom_material = {"container": mat_cbo_custom, "text": "", "type": "Text", "unnamed": 1, "visible": True}

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
win_pfs = {"container": qqw_qml, "id": "base", "type": "ProfilesPage", "unnamed": 1, "visible": True}
win_create_profile = {"title": "Create Profile", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
input_profile_name = {"container": win_create_profile, "id": "nameField", "type": "TextField", "unnamed": 1, "visible": True}
btn_create_profile_confirm = {"container": win_create_profile, "text": "OK", "type": "Button", "unnamed": 1, "visible": True}
win_duplicate_profile = {"title": "Duplicate Profile", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
input_duplicate_profile_name = {"container": win_duplicate_profile, "id": "nameField", "type": "TextField", "unnamed": 1, "visible": True}
btn_duplicate_profile_confirm = {"container": win_duplicate_profile, "text": "OK", "type": "Button", "unnamed": 1, "visible": True}
pfs_profile_list = {"container": win_pfs, "id": "qualityListView", "type": "ListView", "unnamed": 1, "visible": True}
pfs_profile_item = {"container": pfs_profile_list, "text": "", "type": "Text", "unnamed": 1, "visible": True}

# Print Settings (prs)
win_print_settings = {"container": mwi, "type": "PrintSetupSelectorContents", "unnamed": 1, "visible": True}
prs_btn_custom = {"checkable": False, "container": mwi, "id": "customSettingsButton", "type": "ActionButton", "unnamed": 1, "visible": True}
prs_custom_view = {"container": mwi, "id": "customPrintSetup", "type": "CustomPrintSetup", "unnamed": 1, "visible": True}
prs_btn_recommended = {"container": mwi, "text": "Recommended", "type": "Label", "unnamed": 1, "visible": True}
prs_btn_sel_profile = {"container": prs_custom_view, "id": "globalProfileSelection", "type": "Button", "unnamed": 1, "visible": True}
prs_btn_sel_profile = {"checkable": False, "container": mwi, "id": "intentSelection", "type": "Button", "unnamed": 1, "visible": True} # new addition in v4.4 due to the intents
prs_profile_list = {"container": mwi, "type": "PopupItem", "unnamed": 1, "visible": True}
prs_chk_gradual_infill = {"container": mwi, "id": "enableGradualInfillCheckBox", "type": "CheckBox", "unnamed": 1, "visible": True}
prs_intent_name = {"container": mwi_ovl, "text": "", "type": "Label", "unnamed": 1, "visible": True}

# Marketplace (mar)
mwi_btn_marketplace = {"checkable": False, "container": mwi, "id": "marketplaceButton", "type": "Button", "unnamed": 1, "visible": True}
win_marketplace = {"title": "Marketplace", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
mar_downloads = {"container": win_marketplace, "id": "viewDownloads", "type": "ScrollView", "unnamed": 1, "visible": True}
mar_view = {"container": win_marketplace, "type": "ScrollView", "unnamed": 1, "visible": True}
mar_btn_quit_cura = {"checkable": False, "container": win_marketplace, "id": "restartButton", "type": "ActionButton", "unnamed": 1, "visible": True}
mar_btn_install = {"container": mar_view, "id": "installButton", "type": "ToolboxProgressButton", "unnamed": 1, "visible": True}
mar_scroll_bar = {"container": mar_downloads, "type": "ScrollBar", "unnamed": 1, "visible": True}
mar_featured = {"container": mar_downloads, "text": "Featured", "type": "Text", "unnamed": 1, "visible": True}

plugin_auto_orientation = {"container": mar_downloads, "text": "Auto-Orientation", "type": "Text", "unnamed": 1, "visible": True}
plugin_barbarian_units = {"container": mar_view, "text": "Barbarian Units", "type": "Text", "unnamed": 1, "visible": True}
plugin_customer_supports = {"container": mar_view, "text": "Custom Supports", "type": "Text", "unnamed": 1, "visible": True}

# Plugin License Agreement
win_plugin = {"title": "Plugin License Agreement", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
plugin_lcs_btn_accept = {"container": win_plugin, "id": "acceptButton", "type": "Button", "unnamed": 1, "visible": True}
plugin_lcs_btn_agree = {"checkable": False, "container": win_plugin, "text": "Agree", "type": "ActionButton", "unnamed": 1, "visible": True}
plugin_btn_installed = {"checkable": False, "container": mar_view, "id": "installedButton", "type": "ActionButton", "unnamed": 1, "visible": True}

ext_btn_variant = {"container": mwi_ovl, "id": "variantSelection", "type": "Button", "unnamed": 1, "visible": True}
settings_scrollview = {"container": mwi, "id": "scrollView", "type": "ScrollView", "unnamed": 1, "visible": True}
gen_settings_entry = {"container": settings_scrollview, "id": "mouse", "type": "MouseArea", "unnamed": 1, "visible": True}
btn_settings_visibility = {"container": mwi, "id": "settingVisibilityMenu", "type": "Button", "unnamed": 1, "visible": True}

btn_printer_sync = {"container": mwi_ovl, "type": "ConfigurationItem", "unnamed": 1, "visible": True}
btn_to_config = {"container": mwi_ovl, "text": "Configurations", "type": "Label", "unnamed": 1, "visible": True}
mwi_printer_config_drop = {"container": mwi, "id": "printerSetup", "type": "ConfigurationMenu", "unnamed": 1, "visible": True}
mwi_monitor_tab = {"container": mwi, "text": "MONITOR", "type": "Button", "unnamed": 1, "visible": True}
mwi_prepare_tab = {"container": mwi, "text": "PREPARE", "type": "Button", "unnamed": 1, "visible": True}
lbl_in_monitor = {"container": mwi, "text": "", "type": "Label", "unnamed": 1, "visible": True}
open_project_file_QQuickWindowQmlImpl = {"title": "Open project file", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
open_project_file_Remember_my_choice_CheckBox = {"container": open_project_file_QQuickWindowQmlImpl, "id": "rememberChoiceCheckBox", "text": "Remember my choice", "type": "CheckBox", "unnamed": 1, "visible": True}
open_Project_QQuickWindowQmlImpl = {"title": "Open Project", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
ultimaker_Cura_MainWindow = {"title": "Ultimaker Cura", "type": "MainWindow", "unnamed": 1, "visible": True}
ultimaker_Cura_Custom_Custom_Material_Label = {"container": ultimaker_Cura_MainWindow, "text": "Custom Custom Material", "type": "Label", "unnamed": 1, "visible": True}
preferences_base_MaterialsPage = {"container": mat_win, "id": "base", "type": "MaterialsPage", "unnamed": 1, "visible": True}
base_materialScrollView_ScrollView = {"container": preferences_base_MaterialsPage, "id": "materialScrollView", "type": "ScrollView", "unnamed": 1, "visible": True}
materialScrollView_brand_header_Row = {"container": base_materialScrollView_ScrollView, "id": "brand_header", "occurrence": 2, "type": "Row", "unnamed": 1, "visible": True}
