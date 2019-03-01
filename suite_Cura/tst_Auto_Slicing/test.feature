Feature: Auto slicing

    Scenario: Enable auto slicing
        Given Cura has been started with a pre-loaded model
        When I navigate to general preferences
        And I enable "Slice automatically"
        And I exit general preferences
        Then the model has been sliced automatically