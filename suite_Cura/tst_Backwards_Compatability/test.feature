Feature: Verify if configurations of older versions still work

  The latest version of Cura should still be able to handle older configurations
  This feature checks the same scenarios with different configs

  Scenario Outline: Regression scenario's for older configs
    Given Cura has been started with <version> configuration
    And The following custom profiles are available
      | profiles  |
      | UM3E_Fast |
      | UM3E_Fine |
      | UM3_Fast  |
      | Um3_Fine  |
    When I Activate profile 'UM3_Fast'
          #TODO: Finish this step!!
    Then The print settings display profile 'UM3_Fast'
    And 14 Printers are present
    And It is possible to switch to single extruder printer Ultimaker 2+
    When I activate material 'Custom PLA Custom'
    Then Extruder one makes use of material 'Custom PLA Custom'
    And I close Cura


    Examples:
      | version |
      | 2.7     |
#      | 3.0     |
#      | 3.1     |
#      | 3.2     |
#      | 3.3     |
#      | 3.4     |
#      | 3.5     |
#      | 3.6     |
#      | 4.0     |