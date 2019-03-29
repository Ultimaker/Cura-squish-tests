Feature: Printer management

    Scenario: Add printer from launch
        Given Cura has been started with no configurations
        And I accept the user agreement
        When I add a Ultimaker S5 printer
        And I finish the Add Printer wizard
        Then I can see that a Ultimaker S5 printer has been selected

    Scenario: Add printer from printer preferences
        Given Cura is running
        When I navigate to file menu Preferences and Configure Cura
        And I navigate to Printers in preferences
        And I want to Add a printer from printer preferences
        And I add a Ultimaker 2+ printer
        Then the printer overview contains a Ultimaker 2+ printer
        Then I close the preferences

    Scenario: Add networked printer
        Given Cura is running
        When I navigate to file menu Preferences and Configure Cura
        And I navigate to Printers in preferences
        And I want to Add a printer from printer preferences
        And I add a Ultimaker S5 printer
        And I add a network printer with address 10.183.1.1
        Then the networked printer "10.183.1.1" is available

	Scenario: Customize the printers in printer manager
	    Given Cura has been started with preset configurations
	    When I navigate to file menu Preferences and Configure Cura
	    And I navigate to Printers in preferences
	    And I select printer Ultimaker 2+ from the local printers
	    And I want to Activate a printer from printer preferences
	    And I want to Rename a printer from printer preferences
	    And I give the printer the '-my name' name
	    #TODO: Implement this next step:
	    Then the printer is renamed to '-my name'