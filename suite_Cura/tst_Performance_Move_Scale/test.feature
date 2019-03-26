Feature: Performance of movement and scaling

    Scenario: Moving multiple objects
        Given Cura has been started with preset configurations
        And I load project 'UM3_Robot.3mf'
        When I move the model 40 x 60 y
        #TODO: Implement this after log line has been added
        Then the movement time is retrieved from the log
        And the movement time is printed

    Scenario: Scaling single object
        Given Cura is running
        And I clear the buildplate
        And I load file 'Robot.stl'
        When I scale the model to 125% uniformly
        #TODO: Implement this after log line has been added
        Then the scale time is retrieved from the log
        And the scale time is printed