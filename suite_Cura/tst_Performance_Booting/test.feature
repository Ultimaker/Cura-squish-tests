Feature: Performance of booting Cura

	@performance
    Scenario: Booting Cura
        Given Cura is being started in performance mode
        Then the boot time is retrieved from the log
        And the boot time is printed