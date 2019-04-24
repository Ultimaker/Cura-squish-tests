Feature: Printer management

  Scenario: Add printer from printer preferences
    Given Cura has been started with preset configurations
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I Add a printer from printer preferences
    And I add a non-networked Ultimaker 2 Extended+ printer
    Then the printer overview contains a 'Ultimaker 2 Extended+' printer

  Scenario: Add networked printer from printer preferences
    Given Cura is running
    When I Add a printer from printer preferences
    And I add a network printer with address 10.183.0.54
    Then the printer overview contains a '0Lily (manual)' printer

  Scenario: Activating a printer in printer manager
    Given Cura is running
    When I select printer Ultimaker 2+ from the local printers
    And I Activate a printer from printer preferences
    Then The printer is activated

  Scenario: Rename a printer
    Given Cura is running
    And I navigate to Printers in preferences
    When I give the printer the 'terri' name
    Then the printer overview contains a 'terri' printer