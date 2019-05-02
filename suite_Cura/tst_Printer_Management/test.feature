Feature: Printer management

  Scenario: Add printer from printer preferences
    Given Cura has been started with preset configurations
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I select Add printer
    And I add a non-networked Ultimaker 2 Extended+ printer
    Then The printer overview contains a 'Ultimaker 2 Extended+' printer
    And I close the preferences

  Scenario: Add networked printer from printer preferences
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I select Add printer
    And I add a network printer with address 10.183.0.54
    Then The printer overview contains a '0Lily' printer
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
    Then The printer overview contains a 'terri' printer
    And I close the preferences

  Scenario: Delete a printer
  	Given Cura is running
   	When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I select printer terri from the local printers
    And I select Remove printer
    Then Printer terri is not visible anymore
