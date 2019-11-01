Feature: Login
    To test if the user can login through the IPPhone
    #Scenario: Sanity_Check
    #    Given Ellie is assigned a device

    Scenario: Signin_Personal_Account
        ## TBD given Ellie is assigned a <partner_name>/<model_name> device ##
        Given Shadab is assigned a device
		When Shadab tries to sign in
		Then Shadab sees that sign in was successful
        When Shadab signs out from the device
        Then Shadab sees that sign out was successful

    Scenario: Signin_Shared_Account
        Given Shadab is assigned a device
		When Shadab tries to login using shared account
		Then Shadab sees that sign in was successful
        When Shadab signs out from the device
        Then Shadab sees that sign out was successful

