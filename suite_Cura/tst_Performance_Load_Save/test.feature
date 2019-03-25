Feature: Performance of loading and saving files

    Scenario: Loading file
        Given Cura has been started
        When I load file Robot.STL in performance mode
        Then the file load time is retrieved from the log
        And the file load time is printed

    Scenario: Loading 3MF project
        Given Cura is running
        When I load project UM3_Robot.3mf in performance mode
        Then the file load time is retrieved from the log
        And the file load time is printed

    Scenario: Saving file as project
        Given Cura is running
        When I load file 'Robot.STL'
        And I save the file as a project in performance mode
        Then the writing time is retrieved from the log
        And the writing time is printed