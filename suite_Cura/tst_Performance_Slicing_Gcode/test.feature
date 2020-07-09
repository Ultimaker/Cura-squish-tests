Feature: Performance of slicing, and gcode

  Scenario: Save model to gcode and verify size
    Given Cura has been started with preset configurations
    And I load file 'Robot.stl'
    And I select the 'Ultimaker 3' printer with no intent and 'Fine - 0.1mm' profile
    And I slice the object
    When I save a sliced model as 'Robot.gcode'
    Then I can verify the gcode size of 'Robot.gcode' is greater than 1kb
    And the line size of 'Robot.gcode' is printed

  Scenario Outline: Slicing objects with profile: Fine and printer: UM3
    Given Cura is running
    When I clear the buildplate
    And I load <File> '<FileName>'
    And I select the 'Ultimaker 3' printer with no intent and 'Fine - 0.1mm' profile
    And I slice the object in performance mode
    Then the slice time is retrieved from the log
    And the slice time is printed
    Examples:
      | File    | FileName      |
      | file    | Robot.stl     |
      | project | UM3_Robot.3mf |