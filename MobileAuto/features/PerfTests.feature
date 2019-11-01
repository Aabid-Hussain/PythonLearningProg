Feature: PerfTests
    Below are the most commonly used scenario, we want to get performance metrics for each of them.
    Firmware boot time test only works in kiosk mode
    Scenario: Perf-001-Firmware-boot-time
        Given Ellie is assigned a device
	    When Ellie reboots the device
        And Performance Data is collected for Ellie
        And reboot is repeated for 1 times for Ellie

    Scenario: Perf-002-1-Sign-in
        Given Ellie is assigned a device
        And No action is taken for 30 seconds
		When Ellie tries to sign in
		Then Ellie sees that sign in was successful
        And No action is taken for 2 minutes
        When Ellie signs out from the device
        Then Ellie sees that sign out was successful
        And Performance Data is collected for Ellie
        And Signin is repeated for 5 times for Ellie

    Scenario: Perf-002-2-SharedAcct-Sign-in
        Given Ellie is assigned a device
        And No action is taken for 30 seconds
		When Ellie tries to login using shared account
		Then Ellie sees that sign in was successful
        And No action is taken for 2 minutes
        When Ellie signs out from the device
        Then Ellie sees that sign out was successful
        And Performance Data is collected for Ellie
        And Shared account Signin is repeated for 5 times for Ellie

    Scenario: Perf-003-1-P2P-Outgoing-Call
        Given Ellie,Leo signs in to their respective devices
        And Reset Performance Data
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie mutes the call
        Then Ellie sees that the call is muted
        When Leo mutes the call
        Then Leo sees that the call is muted
        And No action is taken for 2 minutes
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo
        And Performance Data is collected for Ellie
        When P2P Call is repeated for 5 times for Ellie to Leo using displayname

    Scenario: Perf-003-2-P2P-PhoneNumber-Outgoing-Call
        Given Ellie,Leo signs in to their respective devices
        And Reset Performance Data
		When Ellie places an outgoing call to Leo using phonenumber
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie mutes the call
        Then Ellie sees that the call is muted
        When Leo mutes the call
        Then Leo sees that the call is muted
        And No action is taken for 2 minutes
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo
        And Performance Data is collected for Ellie
        When P2P Call is repeated for 5 times for Ellie to Leo using phonenumber

    Scenario: Perf-003-3-P2P-Incoming-Call
        Given Ellie,Leo signs in to their respective devices
        And Reset Performance Data
		When Leo places an outgoing call to Ellie using displayname
        And Ellie receives the call from Leo
        And No action is taken for 10 seconds
        Then call is connected between Leo and Ellie
        When Leo mutes the call
        Then Leo sees that the call is muted
        When Ellie mutes the call
        Then Ellie sees that the call is muted
        And No action is taken for 2 minutes
        When Leo hangs up on Ellie
        Then call is ended between Leo and Ellie
        And Performance Data is collected for Leo
        When P2P Call is repeated for 5 times for Leo to Ellie using displayname

    Scenario: Perf-003-4-P2P-PhoneNumber-Incoming-Call
        Given Ellie,Leo signs in to their respective devices
        And Reset Performance Data
		When Leo places an outgoing call to Ellie using phonenumber
        And Ellie receives the call from Leo
        And No action is taken for 10 seconds
        Then call is connected between Leo and Ellie
        When Leo mutes the call
        Then Leo sees that the call is muted
        When Ellie mutes the call
        Then Ellie sees that the call is muted
        And No action is taken for 2 minutes
        When Leo hangs up on Ellie
        When Leo hangs up on Ellie
        Then call is ended between Leo and Ellie
        And Performance Data is collected for Leo
      
	  #PSTN user Peter is Federated tenant
    Scenario: Perf-003-5-P2P-Call-PSTN-Outgoing
        Given Ellie,Peter signs in to their respective devices
        And Reset Performance Data
		When Ellie places an outgoing call to Peter using phonenumber
        And Peter receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Peter
        When Ellie mutes the call
        Then Ellie sees that the call is muted
        When Peter mutes the call
        Then Peter sees that the call is muted
        And No action is taken for 2 minutes
        When Ellie hangs up on Peter
        Then call is ended between Ellie and Peter
        And Performance Data is collected for Ellie
        When P2P Call is repeated for 5 times for Ellie to Peter using phonenumber

    Scenario: Perf-003-6-P2P-Call-PSTN-Incoming
        Given Ellie,Peter signs in to their respective devices
        And Reset Performance Data
		When Peter places an outgoing call to Ellie using phonenumber
        And Ellie receives the call from Peter
        And No action is taken for 10 seconds
        Then call is connected between Peter and Ellie
        When Peter mutes the call
        Then Peter sees that the call is muted
        When Ellie mutes the call
        Then Ellie sees that the call is muted
        And No action is taken for 2 minutes
        When Peter hangs up on Ellie
        Then call is ended between Peter and Ellie  
        And Performance Data is collected for Peter 
        When P2P Call is repeated for 5 times for Peter to Ellie using phonenumber

	  
    Scenario: Perf-004-1-Meeting-Join
        Given Ellie signs in to a device
        And Reset Performance Data
        When Ellie joins meeting named single_person_meeting
        And No action is taken for 30 seconds
        Then Ellie sees that join was successful
        And No action is taken for 2 minutes
        When Ellie hangs up
        And No action is taken for 30 seconds
        Then Ellie sees that call is ended
        And Performance Data is collected for Ellie
        When single_person_meeting Join is repeated for 5 times for Ellie
		
	Scenario: Perf-005-Meetings-To-Calls-Tab
        Given Ellie signs in to a device
        And Reset Performance Data
        When Ellie navigates to Meetings tab
        And No action is taken for 2 minutes
        When Ellie navigates to Calls tab
        And No action is taken for 2 minutes
        Then Performance Data is collected for Ellie
        When Meetings to calls action is repeated for 5 times for Ellie

    Scenario: Perf-006-Calls-To-Meetings-Tab
        Given Ellie signs in to a device
        And Reset Performance Data
        When Ellie navigates to Calls tab
        And No action is taken for 2 minutes
        When Ellie navigates to Meetings tab
        And No action is taken for 2 minutes
        Then Performance Data is collected for Ellie
        When calls to meetings action is repeated for 5 times for Ellie

    Scenario: Perf-007-Calls-To-VM-Tab
        Given Ellie signs in to a device
        And Reset Performance Data
        When Ellie navigates to Calls tab
        And No action is taken for 2 minutes
        When Ellie navigates to Voicemails tab
        And No action is taken for 2 minutes
        Then Performance Data is collected for Ellie
        When calls to vm action is repeated for 5 times for Ellie

    Scenario: Perf-008-VM-To-Meetings-Tab
        Given Ellie signs in to a device
        And Reset Performance Data
        When Ellie navigates to Voicemails tab
        And No action is taken for 2 minutes
        When Ellie navigates to Meetings tab
        And No action is taken for 2 minutes
        Then Performance Data is collected for Ellie
        When vm to meetings action is repeated for 5 times for Ellie
		
	 ## Assumption : User has good number of populated meetings ##
    Scenario: Perf-010-Scroll-Meetings
        Given Ellie signs in to a device
        And Reset Performance Data
        When Ellie scrolls through meetings for 5 times
        And No action is taken for 2 minutes
        And Performance Data is collected for Ellie
        When meeting items scroll is repeated for 5 times for Ellie
		
    ## Assumption : User has good number of populated call logs ##
    Scenario: Perf-011-Scroll-CallLogIem
        Given Ellie signs in to a device
        And Reset Performance Data
        When Ellie scrolls through calls for 5 times
        And No action is taken for 2 minutes
        And Performance Data is collected for Ellie
        When Call logs scroll is repeated for 5 times for Ellie

    # Assumption : User has good number of populated voicemails ##
    Scenario: Perf-012-Scroll-VMItems
        Given Ellie signs in to a device
        And Reset Performance Data
        When Ellie scrolls through voicemails for 5 times
        And No action is taken for 2 minutes
        And Performance Data is collected for Ellie
        When VM items scroll is repeated for 5 times for Ellie
    
	Scenario: Perf-013-Open-Partner-Settings
        Given Ellie is assigned a device
        Then Ellie opens partner settings page
        And No action is taken for 10 seconds
        And Ellie comes out of partner settings page
        Then Performance Data is collected for Ellie
        When Open Partner Settings is repeated for 5 times for Ellie
		
    Scenario: Perf-014-Add-Participant-In-Meeting
        Given Ellie,Leo signs in to their respective devices
		When Ellie joins meeting named single_person_meeting
        And No action is taken for 30 seconds
        Then Ellie sees that join was successful
        When Ellie adds Leo to the conversation using displayname
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Leo mutes the call
        Then Leo sees that the call is muted
        When Leo hangs up
        And No action is taken for 10 seconds
        Then Leo sees that call is ended
        When Add Participant is repeated for 5 times for Ellie with Leo

    Scenario: Perf-015-P2P-Call-Add-PSTN
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
        When Add User is repeated for 5 times for Ellie to Leo with Peter using phonenumber

    Scenario: Perf-016-P2P-Call-Escalate-Conference
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
        When Add User is repeated for 5 times for Ellie to Leo with Elizabeth using displayname
        

    