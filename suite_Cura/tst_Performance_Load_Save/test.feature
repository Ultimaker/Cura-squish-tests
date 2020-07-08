Feature: Performance of loading and saving files

  Scenario: Loading File
    Given Cura has been started with preset configurations
    When I load file Robot.stl in performance mode
    Then the file load time is retrieved from the log
    And the file load time is printed

  Scenario: Loading 3MF project
    Given Cura has been started with preset configurations
    And I clear the buildplate
    When I load project POS.3mf in performance mode
	Then the file load time is retrieved from the log
    And the file load time is printed

  Scenario: Saving file as project
    Given Cura has been started with preset configurations
    And I clear the buildplate
    When I load file 'Robot.stl'
    And I save the file as a project in performance mode
    Then the writing time is retrieved from the log
    And the writing time is printed