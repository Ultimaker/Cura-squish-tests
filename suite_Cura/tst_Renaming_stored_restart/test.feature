# This is a sample .feature file
# Squish feature files use the Gherkin language for describing features, a short example
# is given below. You can find a more extensive introduction to the Gherkin format at
# https://github.com/cucumber/cucumber/wiki/Gherkin
Feature: Verify that printers, materials and profile keep their name after restarting Cura



    Scenario: Renaming a printer and restarting Cura
        Given Cura has been started with preset configurations
        When I navigate to menu Preferences and Configure Cura
        And I navigate to Printers in preferences
        And I give the printer the 'andreea' name
        Then the printer overview contains a 'andreea' printer
        And I close the preferences
        When I restart Cura
        Then the printer overview contains a 'andreea' printer


    Scenario: This is a second sample scenario

        ...
