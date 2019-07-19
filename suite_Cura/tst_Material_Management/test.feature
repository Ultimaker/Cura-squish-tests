Feature: Material manager

    Scenario: Create material
   	    Given Cura has been started with preset configurations
        When I navigate to menu Preferences and Configure Cura
        And I navigate to Materials in preferences
        And I select Create material
        Then the material 'Custom Custom Material' has been added
        And I close the preferences
        Then Extruder one makes use of material 'Custom Custom Material'


    Scenario: Duplicate material
        Given Cura is running
        When I navigate to menu Preferences and Configure Cura
        And I navigate to Materials in preferences
        And I select Duplicate material
        Then the material 'Custom Custom Material' has been added
        Then I select 'Unlink Material'
        And I close the preferences


    Scenario: Adjust material diameter
        Given Cura is running
        When I navigate to menu Preferences and Configure Cura
        And I navigate to Materials in preferences
        And I select Create material
        Then the material 'Custom Custom Material' has been added
        When I change the material name to 'Diameter Test'
        Then the material 'Custom Diameter Test' has been added
        And the material property 'Diameter' is '2.85 mm'
        When I change the material property 'Diameter' to '3.25'
        Then the material 'Custom Diameter Test' has been added
        And the material property 'Diameter' is '3.25 mm'
        When I change the material property 'Diameter' to '1.75'
        And I deny changing the diameter
        Then the material 'Custom Diameter Test' has been added
        And the material property 'Diameter' is '3.25 mm'
        When I change the material property 'Diameter' to '1.75'
        And I confirm changing the diameter
        Then the material 'Custom Diameter Test' has not been added
        And the material property 'Diameter' is '2.85 mm'
        And the material 'PLA' is selected
        And I close the preferences


	Scenario: Material diameter after restarting
	    Given Cura is running
	    When I navigate to menu Preferences and Configure Cura
	    And I navigate to Materials in preferences
	    And I select Create material
	    Then the material 'Custom Custom Material' has been added
	    When I change the material name to 'Diameter Restart'
	    Then the material 'Diameter Restart' has been added
	    And the material property 'Diameter' is '2.85 mm'
	    When I change the material property 'Diameter' to '3.33'
	    Then the material 'Diameter Restart' has been added
	    And the material property 'Diameter' is '3.33 mm'
	    When I close the preferences
	    And I restart Cura
	    And I navigate to menu Preferences and Configure Cura
	    And I navigate to Materials in preferences
	    Then the material 'Diameter Restart' has been added
	    And the material property 'Diameter' is '3.33 mm'
	    And I close the preferences

    Scenario: Customise a material
        Given Cura is running
        When I navigate to menu Preferences and Configure Cura
        And I navigate to Materials in preferences
        And I select Create material
        Then the material 'Custom Custom Material' has been added
        When I change the material name to 'Customized'
        Then the material 'Customized' has been added
        When I change the material property 'Density' to '2'
        Then the material property 'Density' is '2.00 g/cm³'
        When I change the material property 'Filament Cost' to '45'
        Then the material property 'Filament Cost' is '€ 45.00'
        When I change the material property 'Filament Weight' to '750'
        Then the material property 'Filament Weight' is '750 g'
