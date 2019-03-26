Feature: Downloading plugin from marketplace

    Scenario: Open Marketplace, Download and install plugin
        Given Cura has been started with preset configuration
        When I navigate to stage menu Marketplace
        And I select plugin 'Custom Supports' and install it
        Then I close Cura from Marketplace

    Scenario: Checking installation
        Given Cura has been started
        When I navigate to stage menu Marketplace
        And I select plugin 'Custom Supports'
        Then I can verify that the plugin is installed