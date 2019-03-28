Feature: Performance of moving multiple objects

    Scenario: Moving multiple objects
        Given Cura has been started with preset configurations
        And I load project 'UM3_MultipleRobots.3mf'
        When I move the model 100 x
        Then the movement time is retrieved from the log