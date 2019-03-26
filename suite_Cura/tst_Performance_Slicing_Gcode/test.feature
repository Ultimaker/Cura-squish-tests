Feature: Performance of slicing, and gcode

    Scenario: Save model to gcode and verify size
        Given Cura has been started
        And I load file 'Robot.STL'
        And I select the 'Ultimaker 3' printer and 'fine' profile
        And I slice the object
        When I save a sliced model as 'Robot.gcode'
        Then I can verify the gcode size is greater than 1kb
        And the line size of the gcode is printed

    Scenario Outline: Slicing objects with profile: Fine and printer: UM3
        Given Cura is running
        When I clear the buildplate
        And I load <File> '<FileName>'
        And I select the 'Ultimaker 3' printer and 'fine' profile
        And I slice the object in performance mode
        Then the slice time is retrieved from the log
        And the slice time is printed
        Examples:
            | File    | FileName      |
            | file    | Robot.STL     |
            | project | UM3_Robot.3mf |