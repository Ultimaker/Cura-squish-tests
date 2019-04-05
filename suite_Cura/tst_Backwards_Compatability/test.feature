Feature: Verify if configurations of older versions still work

  The latest version of Cura should still be able to handle older configurations
  This feature checks the same scenarios with different configs

  Scenario Outline: Regression scenario's for older configs
    Given Cura has been started with <version> configuration
	# TODO: Implement checks for each version (CURA-6298)

    Examples:
      | version |
      | 2.7     |
      | 3.0     |
      | 3.1     |
      | 3.2     |
      | 3.3     |
      | 3.4     |
      | 3.5     |