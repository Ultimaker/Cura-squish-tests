from PageObjects.MarketplacePage import Marketplace

marketplace = Marketplace()

@Then("I can verify that the plugin is installed")
def step(context):
    marketplace.verifyPluginInstalled()
    

@When(r"I select plugin 'Custom Supports'?(.*)", regexp=True)
def step(context, action):
    marketplace.selectPlugin('Custom Supports')
    if "and install it" in action:     
        marketplace.selectPluginInstall()