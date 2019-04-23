Feature: Printer management

#  Scenario: Add printer from printer preferences
#    Given Cura has been started with preset configurations
#    When I navigate to menu Preferences and Configure Cura
#    And I navigate to Printers in preferences
#    And I want to Add a printer from printer preferences
#    And I add an Ultimaker 2+ Extended printer
#    Then the printer overview contains a Ultimaker 2+ Extended printer
#    Then I close the preferences

#  Scenario: Add networked printer
#    Given Cura is running
#    When I navigate to menu Preferences and Configure Cura
#    And I navigate to Printers in preferences
#   And I want to Add a printer from printer preferences
#    And I add an Ultimaker Ultimaker 3 Extended printer
#    And I add a network printer with address 10.183.1.1
#    Then the networked printer "10.183.1.1" is available

  Scenario: Activating a printer in printer manager
    Given Cura has been started with preset configurations
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I select printer Ultimaker 2+ from the local printers
    And I Activate a printer from printer preferences
    Then The printer is activated

  Scenario: Rename a printer
    Given Cura is running
    And I navigate to Printers in preferences
    When I give the printer the 'terri' name
    Then the printer overview contains a 'terri' printer