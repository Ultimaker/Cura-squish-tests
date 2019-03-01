Feature: Exruder

    Scenario: Change core of extruder 2
        Given Cura is running
        And I switch to printer: Ultimaker 3
        When I select extruder 2 from the main menu
        And I change the print core to "AA 0.8"
        Then print core "AA 0.8" for extruder 2 is visible in the main menu

    #Possible other check after changing print core