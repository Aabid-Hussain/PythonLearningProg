Feature: Sanity
    Below is the list of sanity tests

    Scenario: Signin-Personal-Account
        Given Ellie is assigned a device
		When Ellie tries to sign in
		Then Ellie sees that sign in was successful
        When Ellie signs out from the device
        Then Ellie sees that sign out was successful

    Scenario: Signin-Shared-Account
        Given Ellie is assigned a device
		When Ellie tries to login using shared account
		Then Ellie sees that sign in was successful
        When Ellie signs out from the device
        Then Ellie sees that sign out was successful

    Scenario: P2P-Call-Outgoing
        Given Ellie,Leo signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo

    Scenario: P2P-Call-PhoneNumber-Outgoing
        Given Ellie,Leo signs in to their respective devices
		When Ellie places an outgoing call to Leo using phonenumber
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo

    Scenario: P2P-Call-Incoming
        Given Ellie,Leo signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo

    Scenario: P2P-Call-PhoneNumber-Incoming
        Given Ellie,Leo signs in to their respective devices
		When Leo places an outgoing call to Ellie using phonenumber
        And Ellie receives the call from Leo
        And No action is taken for 10 seconds
        Then call is connected between Leo and Ellie
        When Leo hangs up on Ellie
        Then call is ended between Leo and Ellie    

    Scenario: P2P-Call-Outgoing-Caller-Hold
        Given Ellie,Leo signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie holds the call
        Then Ellie sees that the call is on hold
        And Leo sees that the the call is held by Ellie
        When Ellie resumes the call
        Then Ellie sees that the call is resumed
        And Leo sees that the Ellie has resumed the call
        And call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo
    
    Scenario: P2P-Call-Outgoing-Callee-Hold
        Given Ellie,Leo signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Leo holds the call
        Then Leo sees that the call is on hold
        And Ellie sees that the the call is held by Leo
        When Leo resumes the call
        Then Leo sees that the call is resumed
        And Ellie sees that the Leo has resumed the call
        And call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo

    Scenario: P2P-Call-Incoming-Caller-Hold
        Given Ellie,Leo signs in to their respective devices
		When Leo places an outgoing call to Ellie using displayname
        And Ellie receives the call from Leo
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Leo holds the call
        Then Leo sees that the call is on hold
        And Ellie sees that the the call is held by Leo
        When Leo resumes the call
        Then Leo sees that the call is resumed
        And Ellie sees that the Leo has resumed the call
        And call is connected between Ellie and Leo
        When Leo hangs up on Ellie
        Then call is ended between Ellie and Leo
    
    Scenario: P2P-Call-Incoming-Callee-Hold
        Given Ellie,Leo signs in to their respective devices
		When Leo places an outgoing call to Ellie using displayname
        And Ellie receives the call from Leo
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie holds the call
        Then Ellie sees that the call is on hold
        And Leo sees that the the call is held by Ellie
        When Ellie resumes the call
        Then Ellie sees that the call is resumed
        And Leo sees that the Ellie has resumed the call
        And call is connected between Ellie and Leo
        When Leo hangs up on Ellie
        Then call is ended between Ellie and Leo

    Scenario: P2P-Call-BlindTransfer-Transferor
        Given Ellie,Leo,Elizabeth signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie blind transfers the call with Leo to Elizabeth using displayname
        And No action is taken for 10 seconds
        Then call is connected between Leo and Elizabeth
        When Leo hangs up on Elizabeth
        Then call is ended between Leo and Elizabeth

    Scenario: P2P-Call-ConsultativeTransfer-Transferor
        Given Ellie,Leo,Elizabeth signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie consults with Elizabeth to transfer call with Leo using displayname
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Elizabeth
        When Ellie completes consultation with Elizabeth to accept call from Leo using displayname
        And Elizabeth receives the call from Leo
        And No action is taken for 10 seconds
        Then call is connected between Leo and Elizabeth
        And Ellie sees that call is ended
        When Leo hangs up on Elizabeth
        Then call is ended between Leo and Elizabeth

    Scenario: P2P-Call-BlindTransfer-Transferee
        Given Ellie,Leo,Elizabeth signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Leo blind transfers the call with Ellie to Elizabeth using displayname
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Elizabeth
        When Ellie hangs up on Elizabeth
        Then call is ended between Ellie and Elizabeth
        
    Scenario: P2P-Call-ConsultativeTransfer-Transferee
        Given Ellie,Leo,Elizabeth signs in to their respective devices
        When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Leo consults with Elizabeth to transfer call with Ellie using displayname
        And No action is taken for 10 seconds
        Then call is connected between Leo and Elizabeth
        When Leo completes consultation with Elizabeth to accept call from Ellie using displayname
        And Elizabeth receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Elizabeth
        And Leo sees that call is ended
        When Ellie hangs up on Elizabeth
        Then call is ended between Ellie and Elizabeth

    Scenario: P2P-Call-BlindTransfer-TransferTarget
        Given Ellie,Leo,Elizabeth signs in to their respective devices
		When Elizabeth places an outgoing call to Leo using displayname
        And Leo receives the call from Elizabeth
        And No action is taken for 10 seconds
        Then call is connected between Elizabeth and Leo
        When Elizabeth blind transfers the call with Leo to Ellie using displayname
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo

    Scenario: P2P-Call-ConsultativeTransfer-TransferTarget
        Given Ellie,Leo,Elizabeth signs in to their respective devices
        When Elizabeth places an outgoing call to Leo using displayname
        And Leo receives the call from Elizabeth
        And No action is taken for 10 seconds
        Then call is connected between Elizabeth and Leo
        When Elizabeth consults with Ellie to transfer call with Leo using displayname
        And No action is taken for 10 seconds
        Then call is connected between Elizabeth and Ellie
        When Elizabeth completes consultation with Ellie to accept call from Leo using displayname
        And Ellie receives the call from Leo
        And No action is taken for 10 seconds
        Then call is connected between Leo and Ellie
        And Elizabeth sees that call is ended
        When Leo hangs up on Ellie
        Then call is ended between Leo and Ellie

    Scenario: P2P-Call-Outgoing-Caller-Mute
        Given Ellie,Leo signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Ellie mutes the call
        Then Ellie sees that the call is muted
        When Ellie unmutes the call
        Then Ellie sees that the call is not muted
        When Ellie holds the call
        And call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo
        
    Scenario: P2P-Call-Outgoing-Callee-Mute
        Given Ellie,Leo signs in to their respective devices
		When Ellie places an outgoing call to Leo using displayname
        And Leo receives the call from Ellie
        And No action is taken for 10 seconds
        Then call is connected between Ellie and Leo
        When Leo mutes the call
        Then Leo sees that the call is muted
        When Leo unmutes the call
        Then Leo sees that the call is not muted
        When Ellie holds the call
        And call is connected between Ellie and Leo
        When Ellie hangs up on Leo
        Then call is ended between Ellie and Leo

    Scenario: Join-Scheduled-Meeting
        Given Ellie signs in to a device
        When Ellie joins meeting named single_person_meeting
        And No action is taken for 30 seconds
        Then Ellie sees that join was successful
        When Ellie hangs up
        And No action is taken for 30 seconds
        Then Ellie sees that call is ended

    Scenario: Join-Scheduled-Meeting-Mute-and-Hold
        Given Ellie signs in to their respective devices
        When Ellie joins meeting named single_person_meeting
        And No action is taken for 30 seconds
        Then Ellie sees that join was successful
        When Ellie mutes the call
        Then Ellie sees that the call is muted
        When Ellie unmutes the call
        Then Ellie sees that the call is not muted
        When Ellie holds the call
        Then Ellie sees that the call is on hold
        When Ellie resumes the call
        Then Ellie sees that the call is resumed
        When Ellie hangs up
        And No action is taken for 30 seconds
        Then Ellie sees that call is ended

