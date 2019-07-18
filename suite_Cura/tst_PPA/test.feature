Feature: Print Profile Assistant
	Tests an auxillary plug-in for creating printing profiles.
	To run this feature test, you must first download the plug-in, and put it
	in the folder next to the Cura-squish-tests folder.

	Scenario: Run all experiments once
	    Given Cura has been started with preset configurations
	    And the PPA plug-in is installed
	    When I navigate to stage menu CuraPrintProfileCreator