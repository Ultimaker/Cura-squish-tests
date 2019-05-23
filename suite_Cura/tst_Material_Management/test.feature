Feature: Material manager

    Scenario: Create material
   		Given Cura has been started with preset configurations
    	When I navigate to menu Preferences and Configure Cura
    	And I navigate to Materials in preferences
    	And I select Create material
    	Then the material 'Custom Custom Material' has been added
    	And I close the preferences
    	Then Extruder one makes use of material 'Custom Custom Material'


    #Scenario: Customise a material
    	#And I create a new material with the following properties
    	 #|Display Name |Brand|
    	 #|customAndreea | ABC|
    	#And I give the new material 'andreea' name
    	#Then the material overview contains the name: 'andreea'
		#And I close the preferences
