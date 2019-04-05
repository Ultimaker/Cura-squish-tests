Feature: A complete walkthrough of the onboarding flow


  Scenario: Start onboarding flow
    Given Cura has been started with no configurations
    When I start the onboarding flow
    Then the user agreement page is shown with title 'User Agreement'

  Scenario: Accept user agreement
    Given I'm on the user agreement page of the onboarding flow
    When I accept the user agreement
    Then the changelog page is shown with title 'What's new in Ultimaker Cura'

  Scenario: Confirm changelog changes
    Given I'm on the changelog page of the onboarding flow
    When I confirm the changelog changes
    Then the data collection page is shown with title 'Help us to improve Ultimaker Cura'

  Scenario: Accept anonymous data collection
    Given I'm on the data collection page of the onboarding flow
    When I agree to my data being collected
    Then the printer page is shown with title 'Add a printer'

  Scenario: Add non-networked printer
    Given I'm on the printer screen of the onboarding flow
    When I add a non-networked Ultimaker S5 printer
    Then the cloud page is shown with title 'Ultimaker Cloud'

  Scenario: Finish onboarding flow and verify non-networked printer has been added
    Given I'm on the home page of Cura
    When I finish the onboarding flow
    Then I can see that a Ultimaker S5 printer has been selected