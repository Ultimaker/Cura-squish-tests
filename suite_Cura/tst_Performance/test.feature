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
#
#    Scenario: Slicing single object
#		Given Cura is running
#		When I clear the buildplate
#		And I load file "Cat.STL"
#		And I slice the object with the "fine" profile
#		Then the slice time is retrieved from the log
#		And the slice time is printed



