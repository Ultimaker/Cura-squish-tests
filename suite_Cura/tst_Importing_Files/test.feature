Feature: Importing files

    Scenario: Open 3MF project
        Given Cura is running
        When I open project "X.3mf" and select "open as project"
        Then a summary of project "X" is shown
        And I open the project from the summary page
        Then I'm able to slice the loaded models

    Scenario: Open STL file
        Given Cura is running
        When I open file "X.STLC"
        Then I'm able to slice the loaded models