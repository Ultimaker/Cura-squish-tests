Feature: Command Line Execution Tests - EXPERIMENTAL

  Scenario: TestCase - run cura from CMD
    Given Cura has been started with a project file as argument
    And I check the Remember my choice checkbox
    And I select open as project
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Printers in preferences
    And I close the preferences
    And I restart Cura with a project file as argument
    Then the open as project window does not appear
