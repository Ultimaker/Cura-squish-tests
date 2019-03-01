Feature: Materials

    Scenario: Create material
        Given Cura is running
        When I navigate to material preferences
        And I create a new material with the following properties
            | Display Name       | Brand |
            | CustomCuraMaterial | ABC   |
        And I exit material preferences
        Then material "CustomCuraMaterial" is selected

    Scenario: Duplicate material
        Given Cura is running
        When I navigate to material preferences
        And I duplicate "Generic PLA" with the following properties
            | Display Name       	 | Brand |
            | DuplicatedCuraMaterial | ABCD  |
        And I navigate to Print settings
        Then print settings contains the following properties
            | Default Printing Temperature | Fan Speed |
            | 265C						   | 7%		   |

    Scenario: Export, delete and Re-import material
        Given Cura is running
        When I navigate to material preferences
        And I activate "Generic ABS"
        And I export "Generic PLA" with the name "ExportedPLA"
        And I delete "Generic PLA"
        And I import "ExportedPLA"
        Then the material "ExporterPLA" is available