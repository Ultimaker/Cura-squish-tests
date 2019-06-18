Feature: Performance of moving multiple objects

  Scenario: Moving multiple objects
    Given Cura has been started with preset configurations
    And I load project 'UM3_MultipleRobots.3mf'
    When I move the model 100 x
    Then the movement time is retrieved from the log

  Scenario: POS Slicing
    Given Cura is running
    When I clear the buildplate
    And I load project 'POS.3mf'
    And I slice the object in performance mode
    And I select the models
    And I open POS tool
    And I modify the setting Infill Density to '99'
    And I slice the object in performance mode
    Then the slice time is retrieved from the log
    And the slice time is printed
