Feature: Calls
    To test if the user can place/receive calls
    Scenario: P2P-Call
        Given Ellie,Leo signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo

    Scenario: Conference-Join
        Given Ellie signs in to a device
        When Ellie joins meeting named single_person_meeting
        And No action is taken for 30 seconds
        Then Ellie sees that join was successful
        When Ellie hangs up
        And No action is taken for 30 seconds
        Then Ellie sees that call is ended

    Scenario: Conference-Join-Add-Participant
        Given Ellie,Leo signs in to their respective devices
		When Ellie joins meeting named single_person_meeting
        And No action is taken for 30 seconds
        Then Ellie sees that join was successful
        When Ellie adds Leo to the conversation using displayname
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie hangs up
        And Leo hangs up
        And No action is taken for 10 seconds
        Then call is ended between Ellie and Leo

    Scenario: Call-From-Shared-Mode
        Given Ellie is assigned a device
        And Leo is assigned a device
		When Ellie tries to login using shared account
        And Leo tries to sign in
        Then Ellie sees that sign in was successful
        And Leo sees that sign in was successful
        When Ellie makes an outgoing call from shared mode to Leo using phonenumber
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo

    #PSTN user Peter is Federated tenant
    Scenario: P2P-Call-PSTN-Outgoing
        Given Ellie,Peter signs in to their respective devices
		When Ellie places an outgoing call to Peter using phonenumber
        And Peter receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Peter
        When Ellie hangs up on Peter
        Then call is ended between Ellie and Peter

    Scenario: P2P-Call-PSTN-Incoming
        Given Ellie,Peter signs in to their respective devices
		When Peter places an outgoing call to Ellie using phonenumber
        And Ellie receives the call from Peter
        And No action is taken for 10 seconds
        Then call is connected between Peter and Ellie
        When Peter hangs up on Ellie
        Then call is ended between Peter and Ellie    

    Scenario: P2P-Call-Add-PSTN
        Given Ellie,Leo,Peter signs in to their respective devices
	    When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
	    When Ellie adds Peter to the conversation using phonenumber
	    No action is taken for 30 seconds.
        Then call is connected between Ellie,Leo and Peter
        When Ellie hangs up
	    And Leo hangs up
	    And Peter hangs up
	
	Scenario: P2P-Call-Escalate-Conference
        Given Ellie,Leo,Elizabeth signs in to their respective devices
	    When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
	    When Ellie adds Elizabeth to the conversation using displayname
	    No action is taken for 30 seconds.
        Then call is connected between Ellie,Leo and Elizabeth
        When Ellie hangs up
	    And Leo hangs up
	    And Elizabeth hangs up
