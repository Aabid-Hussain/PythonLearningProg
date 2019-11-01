Feature: LongHaul
    Simulate typical application workload and expect system to remain operational for hours to days
    ## Typical conference room scenarios, 
    Scenario: Long-Haul-Conference
        Given Ellie signs in to a device
        And No action is taken for 1 minute
        And Performance Data is collected for Ellie
        When Ellie joins a meeting named single_person_meeting for 50 times with random sleep after every 5 iterations
        And Ellie makes an outgoing call to the first item in call logs
        And Performance Data is collected for Ellie
        And Analyze Performance Data
        When above long haul conference steps are repeated for 2 times for Ellie