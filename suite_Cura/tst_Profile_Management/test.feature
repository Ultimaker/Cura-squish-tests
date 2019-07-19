Feature: Profile Management

  Scenario: Creating Profile
    Given Cura has been started with preset configurations
    When I open Print Settings
    And I navigate to Recommended settings
    And I enable Gradual infill
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Profiles in preferences
    And I select Create profile
    And I give the new profile 'custom' name
    Then the profile overview contains the profile: 'custom #2'
	And I close the preferences

  Scenario: Duplicating Profile
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Profiles in preferences
    Then the profile overview contains the profile: 'Fine'
    When I select the 'Fine' profile in preferences
    And I select Duplicate profile
    And I give the duplicated profile 'DuplicateOfFine' name
    Then the profile overview contains the profile: 'DuplicateOfFine'
    And I close the preferences

  Scenario: Deleting Profile
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Profiles in preferences
    Then the profile overview contains the profile: 'Fine'
    When I select the 'Fine' profile in preferences
    And I select Duplicate profile
    And I give the duplicated profile 'ToDelete' name
    Then the profile overview contains the profile: 'ToDelete'
    When I select the 'ToDelete' profile in preferences
    And I select Remove profile
    And I confirm removing the profile
    Then the profile 'ToDelete' doesn't exist anymore
    And I close the preferences

  Scenario: Exporting Profile
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Profiles in preferences
    Then the profile overview contains the profile: 'Fine'
    When I select the 'Fine' profile in preferences
    And I select Duplicate profile
    And I give the duplicated profile 'ToExport' name
    Then the profile overview contains the profile: 'ToExport'
    When I select the 'ToExport' profile in preferences
    And I select Export profile
    And I save the profile as 'ToExport.curaprofile'
    Then the file 'ToExport.curaprofile' is a valid profile

#    Scenario: Importing Profile
#       When I give the printer the '|any|' name