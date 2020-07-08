Feature: Printer management of local printers

  Scenario: Switching extruders should cause profile change
    Given Cura has been started with preset configurations
    And I select the 'Ultimaker 3' printer with Engineering intent and 'Fine - 0.1 mm' profile
    When the 1 nozzle is of type 'AA 0.4'
    And the 2 nozzle is of type 'AA 0.4'
    And I select the 2 extruder
    And I select printcore 'AA 0.8'
    And I show all settings
    Then the setting 'Layer Height' in 'Quality' is '0.2'
    And the setting 'Line Width' in 'Quality' is '0.75'
    And I close the extruder selector

  Scenario: Add printer from printer preferences
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I select Add printer
    And I add a non-networked Ultimaker 2 Extended+ printer
    Then the printer overview contains a 'Ultimaker 2 Extended+' printer
    And I close the preferences

  Scenario: Activating a printer in printer manager
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I select printer Ultimaker 2+ from the local printers
    And I select Activate printer
    Then The printer is activated
    And I close the preferences

  Scenario: Rename a printer
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I give the printer the 'terri' name
    Then the printer overview contains a 'terri' printer
    And I close the preferences

  Scenario: Delete a printer
  	Given Cura is running
   	When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I select printer terri from the local printers
    And I select Remove printer
    Then the printer 'terri' doesn't exist anymore

