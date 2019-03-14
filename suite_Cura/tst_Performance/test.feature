Feature: Performance

  The performance of actions measured through the GUI and through log files

  Scenario: Booting Cura
    Given Cura is being started in performance mode
    Then the boot time is retrieved from the log
    And the boot time is printed

  Scenario: Loading file
    Given Cura is running
    When I load file 'Cat.STL' in performance mode
    Then the file load time is retrieved from the log
    And the file load time is printed

  Scenario: Slicing single object with profile: Fine and printer: UM3
    Given Cura is running
    When I clear the buildplate
    And I load file 'Cat.STL'
    And I select the 'Ultimaker 3' printer and 'fine' profile
    And I slice the object in performance mode
    Then the slice time is retrieved from the log
    And the slice time is printed

  Scenario: Save model to gcode and verify size
    Given Cura is running and a model has been sliced
    When I save a sliced model as cat.gcode
    Then I can verify the gcode size is greater than 1kb
    And the line size of the gcode is printed




