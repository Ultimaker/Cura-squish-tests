Feature: Profile Management
    Scenario: Creating Profile
        Given Cura has been started with preset configurations
    	When I open the settings bar
    	And I enable Gradual infill
    	When I navigate to menu Preferences and Configure Cura
    	And I navigate to Profiles in preferences
    	And I select Create profile
    	And I give the new profile 'custom' name
    	Then the profile overview contains 'custom' profile



#    Scenario: Duplicating Profile
#       When I give the printer the '|any|' name
#
#    Scenario: Exporting Profile
#       When I give the printer the '|any|' name
#
#    Scenario: Deleting Profile
#       When I give the printer the '|any|' name
#
#    Scenario: Importing Profile
#       When I give the printer the '|any|' name