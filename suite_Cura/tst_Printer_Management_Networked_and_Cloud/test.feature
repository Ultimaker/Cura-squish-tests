Feature: Printer management of networked and cloud printers

  Scenario: Add detected networked printer from printer preferences
    Given Cura has been started with preset configurations
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I select Add printer
    And I add a network printer with name '0Dany-Cura'
    Then the printer overview contains a '0Dany-Cura' printer
    And I close the preferences

  Scenario: Check if networked printers show up in the monitor page
    Given Cura is running
    And I select the '0Dany-Cura' printer with Normal intent and 'Fine - 0.1 mm' profile
    And I synchronize with the printers configuration
    Then I observe '0Dany-Cura' in the monitor page

  Scenario: Add networked printer via IP from printer preferences
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I select Add printer
    And I add a network printer with address 10.183.1.225
    Then the printer overview contains a '0Dany-Cura' printer
    And I close the preferences

