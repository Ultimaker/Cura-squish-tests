Feature: Performance of loading and saving files

    Scenario: Loading file
        Given Cura has been started
        When I load file 'Cat.STL' in performance mode
        Then the file load time is retrieved from the log
        And the file load time is printed