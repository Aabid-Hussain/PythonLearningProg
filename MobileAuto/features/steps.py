
import sys

sys.path.append("../")

from shutil import copytree
from Driver import Driver
from lettuce import *
from multiprocessing import Process
from threading import Thread
from Logger import Logger
from collections import namedtuple
from collections import OrderedDict
from pprint import pprint
from numpy import mean
from scipy import stats
from threading import Thread
from Logger import Logger
from random import randint
from enums import NavigationWindows
from TeamsMessaging import TeamsMessaging
from mail import MailClient
from WindowsCmdHelper import WindowsCmdHelper

import collections
import time
import thread

import shutil
import os
import datetime
import operator
import time

import scipy.signal
import numpy as np

import matplotlib.pyplot as plt,mpld3
import matplotlib

import dateutil.parser as dateParser
import enums

teamsAppLogger = None
mystring = None

import xlsxwriter
import pickle
import json
import subprocess



devices = {}
users = {}
test_device = ""
available_appium_port = 4723
teams_messaging = None
scenarios = {}
current_scenario = ""
apk_download_path = ""
common_log_share =""
sendgrid_api_key = ""
mail_to_users = ""
windows_helper = WindowsCmdHelper()
#with open(os.getcwd()+"\config.json") as json_file:
with open("D:\\SakuraiAutomation\\config.json") as json_file:
    json_data = json.load(json_file)
    devices = json_data["devices"]
    users = json_data["users"]
    #primary test device
    global test_device
    test_device = json_data["primary_test_device_model"]
    if "appium_starting_port" in json_data.keys():
        global available_appium_port
        available_appium_port = json_data["appium_starting_port"]
    if "teams_webhooks" in json_data.keys():
        global teams_messaging
        teams_messaging = TeamsMessaging(json_data["teams_webhooks"])
    if "apk_download_path" in json_data.keys():
        global apk_download_path
        apk_download_path = json_data["apk_download_path"]
    if "common_log_share" in json_data.keys():
        global common_log_share
        common_log_share = json_data["common_log_share"]
    if "sendgrid_api_key" in json_data.keys():
        global sendgrid_api_key
        sendgrid_api_key = json_data["sendgrid_api_key"]
    if "mail_to_users" in json_data.keys():
        global mail_to_users
        mail_to_users = json_data["mail_to_users"]

user_device_mapping = {}
## List of available devices ##
available_devices = list(devices.keys())

overall_perf_data = {}

crash_data = list()

graph_counter = {'CPU_Plot': 1, 'MEM_Plot' : 2}

critical_memory = False

def reset_global_settings():
    global user_device_mapping
    user_device_mapping = {}
    global available_devices
    available_devices = list(devices.keys())
    global overall_perf_data
    overall_perf_data = {}
    global crash_data
    crash_data = list()
    global critical_memory
    critical_memory = False

## Pick up an available device, initialize device driver and assign it to user ##

@step(' (.*) signs in to a device')
def i_have_a_device_and_i_sign_in (step, user_name):
    
    windows_helper.sleep_with_timeout(2)
    try :
        step.behave_as("""
            Given {user} is assigned a device
            And {user} tries to sign in
            And {user} sees that sign in was successful
        """.format(user=user_name))
    except AssertionError as e:
        Logger.error("ASSERTION ERROR : "+ str(e))
        raise AssertionError(e)
    

@step(' (.*) is assigned a device')
def i_have_a_device (step, user_name):
    windows_helper.sleep_with_timeout(2)
    Logger.info("Available devices : " + str(len(available_devices)))
    assert available_devices is not None and (len(available_devices)>0)
    ## First time when assigning device, check if it is the test device if we need, if we dont have any, we throw an error ##
    if len(available_devices) == len(devices) :
        Logger.info("First device")
        matching = [device for device in available_devices if test_device in devices[device]["model"]]
        assert matching is not None and len(matching) > 0
        selected = matching[0]
        Logger.info( "First device selected" +selected)
        available_devices.remove(selected)
    else:
        ## we have already assinged test device to primary user, so now select any available device ##
        selected = available_devices.pop(0)
    global available_appium_port
    local_appium_port = available_appium_port    
    available_appium_port = available_appium_port + 2

    device_serial = str(devices[selected]["serial"])
    Logger.info("Checking if device " +device_serial  +" is connected via adb")
    adb_output = subprocess.check_output("adb devices",stderr=subprocess.STDOUT, shell=True)
    if device_serial not in adb_output :
        Logger.error("Device NOT CONNECTED via adb. Please connect manually.")
        assert False
    assert device_serial in adb_output
    Logger.info("Device " +device_serial  +" is connected via adb")
    driver = Driver(device_serial, str(local_appium_port))
    # Increment port by 2, as bootstrap and appium uses 2 ports on every call    
    assert driver is not None
    user_device_mapping[user_name] = driver
    
    if apk_download_path != "" :
        driver.install_apk(apk_download_path)
    windows_helper.sleep_with_timeout(30)


@step(' (.*) tries to sign in')
def i_sign_in (step, user_name):
    driver = user_device_mapping[user_name]
    assert driver is not None
    driver.login(users[user_name]["username"],users[user_name]["password"])
    #windows_helper.sleep_with_timeout(60)

@step(' (.*) tries to login using shared account')
def i_sign_in_as_shared_acct (step, user_name):
    driver = user_device_mapping[user_name]
    assert driver is not None
    driver.login(users[user_name]["username"],users[user_name]["password"],True)
    #windows_helper.sleep_with_timeout(60)

@step(' (.*) sees that sign in was successful')
def i_verify_signin (step, user_name):
    driver = user_device_mapping[user_name]
    assert driver is not None
    assert driver.is_signed_in() == True
    windows_helper.sleep_with_timeout(2)


@step(' (.*) signs in to their respective devices')
def parallel_signin (step, users):
    # try :
    #     user_list = users.split(",")
    #     methods= []
    #     for each_user in user_list :
    #         Logger.info( "current_user = " + each_user)
    #         structure = {
    #                 "name" : step.behave_as,
    #                 "args" : """Given {user} signs in to a device""".format(user=each_user)
    #         }
    #         methods.append(structure)
    #     run_in_parallel(methods)
    # except Exception as e:
    #     Logger.error("Exception thrown in parallel signin "+ str(e))
    #     raise Exception(str(e))

    try :
        user_list = users.split(",")
        for each_user in user_list :
            step.behave_as("""
                Given {user} is assigned a device
                And {user} tries to sign in
                And {user} sees that sign in was successful
            """.format(user=each_user))
    except Exception as e:
        Logger.error("Exception thrown in parallel signin "+ str(e))
        raise Exception(str(e))

@step(' (.*) signs out from the device')
def i_sign_out (step, user_name):
    driver = user_device_mapping[user_name]
    assert driver is not None
    driver.signout()
    windows_helper.sleep_with_timeout(30)


@step(' (.*) sees that sign out was successful')
def i_verify_signout (step, user_name):
    driver = user_device_mapping[user_name]
    assert driver is not None
    assert driver.is_signed_in() == False
    windows_helper.sleep_with_timeout(2)

@step(' (.*) places an outgoing call to (.*) using (.*)')
def i_make_a_call (step, user_name, callee_user_tag, call_using):
    if call_using.lower() == "displayname".lower():
        driver = user_device_mapping[user_name]
        assert driver is not None
        driver.search_and_start_a_audio_call(users[callee_user_tag][call_using])
    if call_using.lower() == "phonenumber".lower():
        driver = user_device_mapping[user_name]
        assert driver is not None
        driver.search_and_start_a_pstn_call(users[callee_user_tag][call_using])

@step(' (.*) makes an outgoing call from shared mode to (.*) using (.*)')
def i_make_a_call_from_shared_mode (step, user_name, callee_user_tag, call_using):
    if call_using.lower() == "phonenumber".lower():
        driver = user_device_mapping[user_name]
        assert driver is not None
        driver.start_pstn_call_from_shared_mode(users[callee_user_tag][call_using])

@step(' (.*) receives the call from (.*)')
def i_receive_call (step,callee_user_tag, caller_user_tag):
    callee_driver = user_device_mapping[callee_user_tag]
    assert callee_driver is not None
    callee_driver.accept_call()
    
@step('call is connected between (.*) and (.*)')
def i_see_call_connected (step, caller_user_tag, callee_user_tag):
    caller_driver = user_device_mapping[caller_user_tag]
    callee_driver = user_device_mapping[callee_user_tag]
    assert callee_driver is not None and  caller_driver is not None
    assert caller_driver.is_on_call() and callee_driver.is_on_call()

@step('call is ended between (.*) and (.*)')
def we_dont_see_call (step, caller_user_tag, callee_user_tag):
    caller_driver = user_device_mapping[caller_user_tag]
    callee_driver = user_device_mapping[callee_user_tag]
    assert callee_driver is not None and  caller_driver is not None
    assert not caller_driver.is_on_call() and not callee_driver.is_on_call()

@step(' (.*) sees that call is ended')
def i_dont_see_call(step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None 
    assert not driver.is_on_call()

@step(' (.*) hangs up on (.*)')
def i_hangup_call_on (step, caller_user_tag, callee_user_tag):
    caller_driver = user_device_mapping[caller_user_tag]
    assert caller_driver is not None
    caller_driver.end_call()

@step(' (.*) hangs up')
def i_hangup_call (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.end_call()

@step(' (.*) blind transfers the call with (.*) to (.*) using (.*)')
def i_blind_transfer_call(step, transferor_tag, transferee_tag, transfertarget_tag,call_using):
    driver = user_device_mapping[transferor_tag]
    target_driver = user_device_mapping[transfertarget_tag]
    assert driver is not None and target_driver is not None
    Logger.info("Trying to transfer to : "+ str(users[transfertarget_tag][call_using]))
    driver.blind_transfer_call(users[transfertarget_tag][call_using])
    windows_helper.sleep_with_timeout(5)
    target_driver.accept_call()

@step(' (.*) consults with (.*) to transfer call with (.*) using (.*)')
def i_start_consult_transfer(step, transferor_tag, transfertarget_tag, transfere_tag,call_using):
    driver = user_device_mapping[transferor_tag]
    target_driver = user_device_mapping[transfertarget_tag]
    assert driver is not None and target_driver is not None
    Logger.info("Trying to transfer to : "+ str(users[transfertarget_tag][call_using]))
    driver.start_consultation(users[transfertarget_tag][call_using])
    windows_helper.sleep_with_timeout(5)
    target_driver.accept_call()

@step(' (.*) completes consultation with (.*) to accept call from (.*) using (.*)')
def i_complete_consult_transfer(step, transferor_tag, transfertarget_tag, transfere_tag,call_using):
    driver = user_device_mapping[transferor_tag]
    assert driver is not None
    Logger.info("Trying to transfer to : "+ str(users[transfertarget_tag][call_using]))
    driver.complete_consulation(users[transfertarget_tag][call_using])
    windows_helper.sleep_with_timeout(5)

@step(' (.*) holds the call')
def i_hold_call (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.hold_call()

@step(' (.*) resumes the call')
def i_resume_call (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.resume_call()

@step(' (.*) sees that the call is on hold')
def i_verify_my_hold_status (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    hold_status = driver.is_on_hold()
    assert hold_status == True

@step(' (.*) sees that the call is resumed')
def i_verify_my_resume_status (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    hold_status = driver.is_on_hold()
    assert hold_status == False

@step(' (.*) sees that the the call is held by (.*)')
def i_verify_my_held_status (step, user_tag,holder_user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    hold_status = driver.is_held_by(holder_user_tag)
    assert hold_status == True       

@step(' (.*) sees that the (.*) has resumed the call')
def i_verify_my_unheld_status (step, user_tag,holder_user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    hold_status = driver.is_held_by(holder_user_tag)
    assert hold_status == False  

@step(' (.*) mutes the call')
def i_mute_call (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.mute_call()

@step(' (.*) unmutes the call')
def i_unmute_call (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.unmute_call()

@step(' (.*) sees that the call is muted')
def i_verify_mute (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    mute_status = driver.is_muted()
    assert mute_status == True

@step(' (.*) sees that the call is not muted')
def i_verify_un_mute (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    mute_status = driver.is_muted()
    assert mute_status == False


@step('Performance Data is collected for (.*)')
def i_collect_and_reset_perf_data (step, user_tag):
    try :
        collect_perf_data_helper(user_tag)
    except AssertionError as e:
        Logger.error("ASSERTION ERROR : "+ str(e))
        raise AssertionError(e)
    except Exception as e :
        Logger.error("Error collecting perf data :" + str(e))

def collect_perf_data_helper (user_tag):
    try :
        driver = user_device_mapping[user_tag]
        assert driver is not None
        global overall_perf_data
        
        perf_data = driver.get_perf_data()
        analyzed_data = WorkWithPerfData(user_tag, perf_data)

        if (user_tag not in overall_perf_data):
            overall_perf_data[user_tag] = analyzed_data
        else :
            ## append computed perf data to the existing list ##
            for key,value in analyzed_data.iteritems():
                if key == "latency":
                    for action,delay in value.iteritems():
                        if (action not in overall_perf_data[user_tag][key].keys()):
                            overall_perf_data[user_tag][key][action]=[]
                        try :
                            overall_perf_data[user_tag][key][action].extend(analyzed_data[key][action])
                        except TypeError:
                            overall_perf_data[user_tag][key][action].append(analyzed_data[key][action])

                elif key == "device_info":
                    overall_perf_data[user_tag][key] = analyzed_data[key]

                elif key == "firmware_launch_time":
                    try :
                        overall_perf_data[user_tag][key].extend(analyzed_data[key])
                    except TypeError:
                        overall_perf_data[user_tag][key].append(analyzed_data[key])
                else:
                    try :
                        overall_perf_data[user_tag][key].extend(analyzed_data[key])
                    except TypeError:
                        overall_perf_data[user_tag][key].append(analyzed_data[key])

        Logger.info ("Overall perf data for user : " + user_tag+" :" + str(overall_perf_data[user_tag]))
        driver.reset_perf_data()
        if (len(crash_data) > 0):
            Logger.error("Crash has occured!!")            
            for data in crash_data:
                Logger.error(str(data))
        assert (len(crash_data) == 0)
        critical = driver.is_memory_critical()
        if critical is True:
            Logger.error("MEMORY IS IN CRITICAL STATE ")
            global critical_memory
            critical_memory = True
        #assert not critical_memory

    except AssertionError as e:
        Logger.error("ASSERTION ERROR : "+ str(e))
        raise AssertionError(e)
        
    except Exception as e :
        Logger.error("Error getting perf data :" + str(e))

@step(' (.*) scrolls through (.*) for (.*) times')
def i_scroll_up_and_down (step, user_tag, tab_item, iterations):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    if tab_item.lower() == "calls":
        target = NavigationWindows.CallsWindow
    elif tab_item.lower() == "meetings":
        target = NavigationWindows.MeetingsWindow
    elif tab_item.lower() == "voicemails":
        target = NavigationWindows.VoicemailsWindow
    else:
        raise AssertionError("Specified window is not supported")
    
    driver.navigate_to_page(target)
    print "Scrolling down"
    for i in range(int(iterations)):
        driver.scroll_down()
        windows_helper.sleep_with_timeout(10)
    driver.take_screenshot("after_scroll_down")

    print "Scrolling up"
    for i in range(int(iterations)):
        driver.scroll_up()
        windows_helper.sleep_with_timeout(10)

    driver.take_screenshot("after_scroll_up")

@step(' (.*) navigates to (.*) tab')
def i_navigate_to_tab (step, user_tag, tab_item):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.take_screenshot("before_"+str(tab_item)+"_navigation")
    if tab_item.lower() == "calls":
        target = NavigationWindows.CallsWindow
    elif tab_item.lower() == "meetings":
        target = NavigationWindows.MeetingsWindow
    elif tab_item.lower() == "voicemails":
        target = NavigationWindows.VoicemailsWindow
    else:
        raise AssertionError("Specified window is not supported")
    
    driver.navigate_to_page(target)
    driver.take_screenshot("after_"+str(tab_item)+"_navigation")
 
@step(' (.*) opens partner settings page')
def i_open_partner_settings (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.open_fre_partner_settings()

@step(' (.*) resets the app')
def i_reset_app (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.reset_app()

@step(' (.*) comes out of partner settings page')
def i_exit_partner_settings (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.exit_partner_settings()

@step(' (.*) joins meeting named (.*)')
def i_join_meeting (step, user_tag, meeting_name):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.join_meeting(meeting_name)

@step(' (.*) sees that join was successful')
def i_see_join_successful (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    assert driver.is_on_call()


@step(' (.*) adds (.*) to the conversation using (.*)')
def i_add_to_conversation (step, user_tag, participant_tag, call_using):
    driver = user_device_mapping[user_tag]
    participant_driver = user_device_mapping[participant_tag]
    assert driver is not None and  participant_driver is not None
    if call_using.lower() == "phonenumber".lower():
        driver.add_participant_to_meeting(users[participant_tag][call_using], users[participant_tag]["pstndisplay"])
    elif call_using.lower() == "displayname".lower():
        driver.add_participant_to_meeting(users[participant_tag][call_using], users[participant_tag][call_using])
    participant_driver.accept_call()

@step('No action is taken for (.*) minutes*')
def i_go_to_sleep (step, idle_time):
    idle_time = int(idle_time)
    windows_helper.sleep_with_timeout(idle_time*60)

@step('No action is taken for (.*) seconds*')
def i_go_to_sleep_in_seconds (step, idle_time_seconds):
    idle_time = int(idle_time_seconds)
    windows_helper.sleep_with_timeout(idle_time)

@step('call is connected between (.*),(.*) and (.*)')
def i_see_call_connected_conference (step, caller_user_tag, callee1_user_tag, callee2_user_tag):
    caller_driver = user_device_mapping[caller_user_tag]
    callee1_driver = user_device_mapping[callee1_user_tag]
    callee2_driver = user_device_mapping[callee2_user_tag]
    assert callee1_driver is not None and caller_driver is not None and callee2_driver is not None
    assert caller_driver.is_on_call() and callee1_driver.is_on_call() and callee2_driver.is_on_call()

        
@step(' (.*) joins a meeting named (.*) for (.*) times with random sleep after every (.*) iterations')
def i_join_long_haul_meeting (step, user_tag, meeting_name, times, sleep_after_iterations):
    driver = user_device_mapping[user_tag]
    for i in range(int(times)):        
        Logger.info("Joining meeting " + str(i) + " / " + str(times))
        driver.join_meeting(meeting_name)
        windows_helper.sleep_with_timeout(30)
        driver.take_screenshot("Join_meeting")
        sleep_time_in_minutes = 5
        Logger.info("Sleeping for "+ str(sleep_time_in_minutes)+" minutes..")
        windows_helper.sleep_with_timeout(sleep_time_in_minutes*60)
        driver.wakeup_device()
        assert driver.is_on_call()
        driver.end_call()
        windows_helper.sleep_with_timeout(10)
        if (i%int(sleep_after_iterations) == 0):
            ## Sleep for a random time between 10 to 20 minutes ##
            sleep_time_in_minutes = randint(10,20)
            Logger.info("Sleeping for "+ str(sleep_time_in_minutes)+" minutes..")
            windows_helper.sleep_with_timeout(sleep_time_in_minutes*60)
            driver.wakeup_device()

@step(' (.*) makes an outgoing call to the first item in call logs')
def i_make_a_call_to_first_call_log_item (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.call_first_call_log_item()
    # assert driver.is_on_call()
    windows_helper.sleep_with_timeout(60)
    driver.end_call()
    windows_helper.sleep_with_timeout(10)


@step(' (.*) reboots the device')
def i_reboot_device (step, user_tag):
    driver = user_device_mapping[user_tag]
    assert driver is not None
    driver.reboot()

@step('reboot is repeated for (.*) times for (.*)')  
def i_repeat_reboot(step,iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Signin : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} reboots the device
                And Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('above long haul conference steps are repeated for (.*) times for (.*)')
def i_run_conf_longhaul(step, iterations, user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Long haul conference : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} joins a meeting named single_person_meeting for 50 times with random sleep after every 5 iterations
                And {user} makes an outgoing call to the first item in call logs
                And Performance Data is collected for {user}
                And Analyze Performance Data
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('Signin is repeated for (.*) times for (.*)')
def i_repeat_signin(step, iterations, user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Signin : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} tries to sign in
                Then {user} sees that sign in was successful
                And No action is taken for 2 minutes
                When {user} signs out from the device
                Then {user} sees that sign out was successful
                And Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('Shared account Signin is repeated for (.*) times for (.*)')
def i_repeat_shared_signin(step, iterations, user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Signin : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} tries to login using shared account
                Then {user} sees that sign in was successful
                And No action is taken for 2 minutes
                When {user} signs out from the device
                Then {user} sees that sign out was successful
                And Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('P2P Call is repeated for (.*) times for (.*) to (.*) using (.*)')
def i_repeat_outgoing_call(step, iterations, user_tag,callee_user_tag,call_using):
    for i in range(int(iterations)):
        Logger.info("Repeat P2P call : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} places an outgoing call to {callee} using {using} 
                And {callee} receives the call from {user}
                And No action is taken for 10 seconds
                Then call is connected between {user} and {callee}
                When {user} mutes the call
                Then {user} sees that the call is muted
                When {callee} mutes the call
                Then {callee} sees that the call is muted
                And No action is taken for 2 minutes
                When {user} hangs up on {callee}
                Then call is ended between {user} and {callee}
                And Performance Data is collected for {user}
            """.format(user=user_tag, callee=callee_user_tag, using=call_using))
        windows_helper.sleep_with_timeout(60)

@step('P2P Call is repeated for (.*) times for (.*) from (.*) using (.*)')
def i_repeat_incoming_call(step, iterations, user_tag,caller_user_tag,call_using):
    for i in range(int(iterations)):
        Logger.info("Repeat Incoming P2P call : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {caller} places an outgoing call to {user} using {using}
                And {user} receives the call from {caller}
                And No action is taken for 10 seconds
                Then call is connected between {user} and {caller}
                When {user} mutes the call
                Then {user} sees that the call is muted
                When {caller} mutes the call
                Then {caller} sees that the call is muted
                And No action is taken for 2 minutes
                When {caller} hangs up on {user}
                Then call is ended between {user} and {caller}
                And Performance Data is collected for {user}
            """.format(user=user_tag, caller=caller_user_tag, using=call_using))
        windows_helper.sleep_with_timeout(60)

@step(' (.*) Join is repeated for (.*) times for (.*)')
def i_repeat_meeting(step, meeting_name, iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Meeting Join : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} joins meeting named {meeting}
                And No action is taken for 30 seconds
                Then {user} sees that join was successful                
                And No action is taken for 2 minutes
                When {user} hangs up
                And No action is taken for 30 seconds
                Then {user} sees that call is ended
                And Performance Data is collected for {user}
            """.format(user=user_tag,meeting=meeting_name))
        windows_helper.sleep_with_timeout(60)

@step('Call logs scroll is repeated for (.*) times for (.*)')
def i_repeat_call_scroll(step, iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Call Logs Scroll : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} scrolls through calls for 10 times
                And No action is taken for 2 minutes
                And Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('VM items scroll is repeated for (.*) times for (.*)')
def i_repeat_vm_scroll(step, iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat VM Logs Scroll : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} scrolls through voicemails for 10 times
                And No action is taken for 2 minutes
                And Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('meeting items scroll is repeated for (.*) times for (.*)')
def i_repeat_mtg_scroll(step, iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Meeting Logs Scroll : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} scrolls through meetings for 10 times
                And No action is taken for 2 minutes
                And Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('Meetings to calls action is repeated for (.*) times for (.*)')
def i_repeat_mtg_to_call(step, iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Meetings to calls tab : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} navigates to Meetings tab
                And No action is taken for 2 minutes
                When {user} navigates to Calls tab
                And No action is taken for 2 minutes
                Then Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('calls to meetings action is repeated for (.*) times for (.*)')
def i_repeat_call_to_mtg(step, iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat calls to mtgs tab : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} navigates to Calls tab
                And No action is taken for 2 minutes
                When {user} navigates to Meetings tab
                And No action is taken for 2 minutes
                Then Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('calls to vm action is repeated for (.*) times for (.*)')
def i_repeat_call_to_vm(step, iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat calls to vm tab : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} navigates to Calls tab
                And No action is taken for 2 minutes
                When {user} navigates to Voicemails tab
                And No action is taken for 2 minutes
                Then Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('vm to meetings action is repeated for (.*) times for (.*)')
def i_repeat_vm_to_mtg(step, iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat vm to meetings tab : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} navigates to Voicemails tab
                And No action is taken for 2 minutes
                When {user} navigates to Meetings tab
                And No action is taken for 2 minutes
                Then Performance Data is collected for {user}
            """.format(user=user_tag))
        windows_helper.sleep_with_timeout(60)

@step('Open Partner Settings is repeated for (.*) times for (.*)')
def i_repeat_partner_settings(step, iterations,user_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Partner Settings : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} opens partner settings page
                And No action is taken for 10 seconds
                And {user} comes out of partner settings page
                Then Performance Data is collected for {user}
            """.format(user=user_tag))

@step('Add Participant is repeated for (.*) times for (.*) with (.*)')
def i_repeat_add_participant(step, iterations,user_tag, participant_tag):
    for i in range(int(iterations)):
        Logger.info("Repeat Add Participant : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} adds {participant} to the conversation using displayname
                And No action is taken for 10 seconds
                Then call is connected between {user} and {participant}
                When {participant} mutes the call
                Then {participant} sees that the call is muted
                When {participant} hangs up
                And No action is taken for 10 seconds
                Then {participant} sees that call is ended
            """.format(user=user_tag, participant=participant_tag))

@step('Add User is repeated for (.*) times for (.*) to (.*) with (.*) using (.*)')
def i_repeat_add_pstn(step, iterations,user_tag,callee_user_tag, participant_tag,call_using):
    for i in range(int(iterations)):
        Logger.info("Repeat Add User : "+ str(i) + " / "+ str(iterations))
        step.behave_as("""
                When {user} places an outgoing call to {callee} using {using}
                And {callee} receives the call from {user}
                Then call is connected between {user} and {callee}               
                When {user} adds {participant} to the conversation using {using}
                Then call is connected between {user},{callee} and {participant}
                And No action is taken for 10 seconds
                When {user} hangs up
                And {callee} hangs up
                And {participant} hangs up
                And No action is taken for 10 seconds
                Then {participant} sees that call is ended
                And Performance Data is collected for {user} 
            """.format(user=user_tag,callee=callee_user_tag,  participant=participant_tag, using=call_using))
                

@before.each_feature
def startup_feature(feature):
    print "The feature %r just has just started" % feature.name    
    currentTime = time.strftime("%Y%m%d-%H%M%S")
    Logger.LoggingDir = feature.name+"_Logs_"+currentTime+"/"
    if teams_messaging is not None :
        teams_messaging.send_schedule_message(feature.name + " scheduled on device " + test_device)
    
@after.each_feature
def teardown_feature(feature):
    print "The feature %r just has just ran" % feature.name
    if teams_messaging is not None :
        message = "<b>Feature <i>" + feature.name+"</i> has just ran on "+ test_device +"</b><br/>"
        passed_scenarios = [ key for key,value in scenarios.iteritems() if 'status' in value.keys() and value['status'] =="Passed"]
        passed_count = len(passed_scenarios)
        failed_scenarios = [ key for key,value in scenarios.iteritems() if 'status' in value.keys() and value['status'] =="Failed"]
        failed_count = len(failed_scenarios)
        status = "Passed"
        if (passed_count > 0) :
            message += "<div style=\"color:green\"> Total passed : " + str(passed_count)+" </div><br/>"
            for f in passed_scenarios :
                message += "Passed scenario : " + str(f) +"<br/>"
        if (failed_count > 0) :
            status = "Failed"
            message += "<div style=\"color:red\"> Total failed : " + str(failed_count)+" </div><br/>"
            for f in failed_scenarios :
                message += "Failed scenario : " + str(f) +"<br/>"
        current_feature = {}
        current_feature["name"] = feature.name
        current_feature["status"] = status
        current_feature["scenarios"] = scenarios

        teams_messaging.send_info_message(message)
        try :
            mail_client = MailClient(test_device,sendgrid_api_key, mail_to_users)
            print (str(current_feature))
            mail_client.send_email(current_feature)
        except Exception as e:
            print("Exception sending email : " + str(e))

@before.each_scenario
def startup_scenario(scenario):
    reset_global_settings()
    Logger.LoggingDir = Logger.LoggingDir +"/"+scenario.name+"/"
    Logger.Start()
    scenarios[scenario.name] = {}
    global current_scenario
    current_scenario = scenario.name

def build_data_report(scenario_name):
    user_data = scenarios[scenario_name]["users"]
    message = ""
    for user in user_data :
        if (user == "Ellie"):
            device_info = scenarios[scenario_name]["users"][user]['device_info']
            if (len(device_info) > 0 ) :
                message += "<b> Device Info </b><br/><br/>"
                message += "<table width='20%' style='font-family : Trebuchet MS'>"
                for key,value in device_info.iteritems():
                    message += "<tr>"
                    message += "<td style=' text-align:left ; color: black;  background :#D3D3D3' >"+ key+"</td>"
                    message += "<td style=' text-align:left ; color: black;  background :#D3D3D3' >"+ str("{0:.2f}".format(np.mean(value)) if isinstance(value,list) else value) + "</td>"
                    message += "</tr>"
                message += "</table><br/><br/><br/>"

            latency = None
            if ("latency" in scenarios[scenario_name]["users"][user].keys()) :
                latency = scenarios[scenario_name]["users"][user]['latency']
            firmware_launch_time = 0
            if ("firmware_launch_time" in scenarios[scenario_name]["users"][user].keys()):
                firmware_launch_time = scenarios[scenario_name]["users"][user]['firmware_launch_time']
            
            message += "<b> Latency (seconds) </b><br/><br/>"
            message += "<table width='40%' cellspacing='5px' cellpadding='5px' style='font-family : Trebuchet MS'>"
            if (latency is not None and len(latency) > 0):
                for key,value in latency.iteritems():
                    message += "<tr>"
                    message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ key+"</td>"
                    message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ str("{0:.2f}".format(np.mean(value))  if isinstance(value,list) else value)+"</td>"
                    message += "</tr>"
            if (firmware_launch_time > 0):
                value = scenarios[scenario_name]["users"][user]["firmware_launch_time"]
                message += "<tr>"
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ "Firmware Launch Time"+"</td>"
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ str("{0:.2f}".format(np.mean(value))  if isinstance(value,list) else value)+"</td>"
                message += "</tr>"
            message += "</table><br/><br/><br/>"

            message += "<b> CPU/MEM </b>"
            message += "<table width='40%' cellspacing='5px' cellpadding='5px' style='font-family : Trebuchet MS'>"
            if ("cpu_max" in scenarios[scenario_name]["users"][user].keys()) :
                message += "<tr>"
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ "CPU MAX "+"</td>"
                value = scenarios[scenario_name]["users"][user]["cpu_max"]
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ str("{0:.2f}".format(np.mean(value))  if isinstance(value,list) else value) +"&#37;</td>"
                message += "</tr>"
            if ("cpu_avg" in scenarios[scenario_name]["users"][user].keys()) :
                message += "<tr>"
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ "CPU AVG "+"</td>"
                value = scenarios[scenario_name]["users"][user]["cpu_avg"]
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ str("{0:.2f}".format(np.mean(value))  if isinstance(value,list) else value) +"&#37;</td>"
                message += "</tr>"
            if ("cpu_trimmed_avg" in scenarios[scenario_name]["users"][user].keys()) :
                message += "<tr>"
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ "CPU TRIMMED AVG "+"</td>"
                value = scenarios[scenario_name]["users"][user]["cpu_trimmed_avg"]
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ str("{0:.2f}".format(np.mean(value))  if isinstance(value,list) else value) +"&#37;</td>"
                message += "</tr>"
            if ("mem_max" in scenarios[scenario_name]["users"][user].keys()) :
                message += "<tr>"
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ "MEM MAX "+"</td>"
                value = scenarios[scenario_name]["users"][user]["mem_max"]
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ str("{0:.2f}".format(np.mean(value)) if isinstance(value,list) else value) +"MB</td>"
                message += "</tr>"
            if ("mem_avg" in scenarios[scenario_name]["users"][user].keys()) :
                message += "<tr>"
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ "MEM TRIMMED AVG "+"</td>"
                value = scenarios[scenario_name]["users"][user]["mem_avg"]
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ str("{0:.2f}".format(np.mean(value))  if isinstance(value,list) else value) +"MB</td>"
                message += "</tr>"
            if ("mem_trimmed_avg" in scenarios[scenario_name]["users"][user].keys()) :
                message += "<tr>"
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ "MEM AVG "+"</td>"
                value = scenarios[scenario_name]["users"][user]["mem_trimmed_avg"]
                message += "<td style=' text-align:left ; color:white; text-color: white; background :black' >"+ str("{0:.2f}".format(np.mean(value))  if isinstance(value,list) else value) +"MB</td>"
                message += "</tr>"
            message += "</table><br/><br/><br/>"
    return message

@after.each_scenario
def end_scenario(scenario):
    Logger.info ("End of scenario")
    
    total = len(scenario.steps)
    passed = 0
    failed = 0 
    for step in scenario.steps:
        if (step.passed):
            passed = passed + 1
        if (step.failed):
            failed = failed + 1
    source = Logger.LoggingDir
    Logger.info ("Scenario : " + str(scenario))
    Logger.info ("Total :"+ str(total))
    Logger.info ("Passed :"+ str(passed))
    Logger.info ("Failed :"+ str(failed))
    for user_name,driver in user_device_mapping.iteritems() :
        if driver is not None:
            try :
                collect_perf_data_helper(user_name)            
            except Exception as e:
                Logger.error("Error collecting perf data. "+ str(e))
            driver.cleanup()
            driver = None
    analyze_perf_data()
    Logger.Stop()
    ## Move folder ##
    # source = Logger.LoggingDir
    # destination = Logger.LoggingDir.replace(scenario.name,scenario.)
    try :
        data_report = build_data_report(scenario.name)
        if (total == passed):            
            scenarios[scenario.name]["status"] = "Passed"
            destination = Logger.LoggingDir.replace(scenario.name,"PASSED_"+scenario.name)
            network_path = common_log_share
            network_path = os.path.join(network_path,time.strftime("%Y%m%d-%H%M%S")+"-"+test_device+"-PASSED-"+scenario.name.replace("_","-"))
            network_path = network_path.replace("_","-")
            try :
                copytree(source, network_path)
            except Exception as e:
                print "Exception caught " + str(e)

            try :
                os.rename(source, destination)
            except Exception as e:
                print "Exception renaming folder"
            
            if teams_messaging is not None :
                network_path = str(network_path)
                print "Network path : " + network_path
                message = scenario.name + " passed on device " + test_device + "<br/> Logs at "+ """ <style> a.tooltips
                    {position: relative; display: inline;} a.tooltips span { position: absolute; 
                    width:240px;  color: #FFFFFF;  background: #000000;  height: 30px;  line-height: 30px;  text-align: center; 
                    visibility: hidden;  border-radius: 6px; } a.tooltips span:after {  content: '';  position: absolute;  top: 100%;  left: 50%;
                    margin-left: -8px;  width: 0; height: 0;  border-top: 8px solid #000000;  border-right: 8px solid transparent; 
                    border-left: 8px solid transparent; } a:hover.tooltips span {  visibility: visible;  opacity: 0.8;  bottom: 30px;
                    left: 50%;  margin-left: -76px;  z-index: 999; } </style>
                    <a class="tooltips" href="#">""" + "\\"+ network_path + " .</a><br/><br/>"
                
                message += data_report
                teams_messaging.send_success_message(message)
            
        else:            
            scenarios[scenario.name]["status"] = "Failed"
            scenarios[scenario.name]["failure_reason"] = list()
            if crash_data is not None and len(crash_data) > 0:
                scenarios[scenario.name]["failure_reason"].append("Crash")
            if critical_memory is True :
                scenarios[scenario.name]["failure_reason"].append("Critical Memory")
        
            network_path = common_log_share
            network_path = os.path.join(network_path,time.strftime("%Y%m%d-%H%M%S")+"_"+test_device+"_FAILED_"+scenario.name.replace("_","-"))
            network_path = network_path.replace("_","-")
            try :
                copytree(source, network_path)
            except Exception as e:
                print "Exception caught " + str(e)

            
            destination = Logger.LoggingDir.replace(scenario.name,"FAILED_"+scenario.name)
            try :
                os.rename(source, destination)
            except Exception as e:
                print "Exception renaming folder"

            if teams_messaging is not None :
                network_path = str(network_path)
                print "Network path : " + network_path
                failure_reason_string = "Failure Reason : Test Failure <br/>"
                for reason in scenarios[scenario.name]["failure_reason"]:
                    failure_reason_string += "Failure Reason : " + reason +"<br/>"
                message = scenario.name + " failed on device " + test_device + "<br/> "+failure_reason_string+ " Logs at "+ """ <style> a.tooltips
                    {position: relative; display: inline;} a.tooltips span { position: absolute; 
                    width:240px;  color: #FFFFFF;  background: #000000;  height: 30px;  line-height: 30px;  text-align: center; 
                    visibility: hidden;  border-radius: 6px; } a.tooltips span:after {  content: '';  position: absolute;  top: 100%;  left: 50%;
                    margin-left: -8px;  width: 0; height: 0;  border-top: 8px solid #000000;  border-right: 8px solid transparent; 
                    border-left: 8px solid transparent; } a:hover.tooltips span {  visibility: visible;  opacity: 0.8;  bottom: 30px;
                    left: 50%;  margin-left: -76px;  z-index: 999; } </style>
                    <a class="tooltips" href="#">""" + "\\"+ network_path + " .</a><br/><br/>"

                message += data_report
                teams_messaging.send_failure_message(message)

    except Exception as e:
        print("Exception caught when renaming folder" + str(e))
    Logger.LoggingDir = Logger.LoggingDir.replace(scenario.name+"/","")
    
def sanitize_unc_html(network_path):
    network_path = network_path.replace("\\","/")
    network_path = "file:///" + network_path
    print "After sanitizing" + str(network_path)
    return network_path

@before.each_step
def before_each_step(step):
	print "logger started? " , Logger.IsStarted()
	if Logger.IsStarted() == True:
		Logger.info("Running step --- "+ step.sentence)

@after.each_step
def after_each_step(step):
    if Logger.IsStarted() == True:
        pprint(vars(step))
        Logger.info("Finished step --- "+ step.sentence)
        if step.passed is not None:
            Logger.info("Status : "+ str(step.passed))
        else:
            Logger.error("FAILED STEP")

    
def run_in_parallel(methods):
    try :
        threads = []
        for method in methods :
            
            t = Thread(target=method["name"], args=(method["args"],))
            t.start()
            Logger.info ("Starting thread : "+ str(method["name"]) + " args :"+ str(method["args"]))
            threads.append(t)
            windows_helper.sleep_with_timeout(5)
        
        ## wait for threads to complete
        for t in threads :          
            t.join()

    except Exception as e:
        Logger.error("Exception running parallel threads :"+ str(e))
        raise Exception(str(e))

def analyze_perf_data():
    for user_tag in overall_perf_data.keys() :
        ## Get (max,avg) of data for individual users ##
        perf_data = overall_perf_data[user_tag]        
        if "users" not in scenarios[current_scenario].keys() :
            scenarios[current_scenario]["users"] = {}
        scenarios[current_scenario]["users"][user_tag] = perf_data
        GetTPMetricsWithAnalyzedData(user_tag, perf_data, 100)
        GetTPMetricsWithAnalyzedData(user_tag, perf_data, 50)

    ## Reset overall data after analysis
    overall_perf_data.clear()

@step('Reset Performance Data')
def i_reset_perf_data(step):
    for user_name,driver in user_device_mapping.iteritems() :
        if driver is not None:
            collect_perf_data_helper(user_name)

    global overall_perf_data
    overall_perf_data.clear()

@step('Analyze Performance Data')
def i_analyze_perf_data (step):
    try :
        analyze_perf_data()
    
    except AssertionError as e:
        Logger.error("ASSERTION ERROR : "+ str(e))
        raise AssertionError(e)
    except Exception as e:
        Logger.error("Exception in analyzing performance data : " + str(e))

def GetTPMetricsWithAnalyzedData (user_data,analyzed_data, metric):
    try :
        Logger.info("############## BEGIN ANALYZED DATA . FOR :"+ user_data+" TP "+ str(metric)+" ###################")
        cpu_mem_info = ""
        for key in analyzed_data.keys():
            if (key == "device_info"):
                Logger.info("Device Info : ")
                Logger.info("**************")
                for k,v in analyzed_data[key].iteritems():
                    Logger.info( k + " :: " + str(v).strip())
            elif (key == "firmware_launch_time"):
                Logger.info("Firmware Launch Time : ")
                Logger.info("***********************")
                percentile = np.percentile(analyzed_data[key], metric)
                Logger.info(str(key) + " :: TP " + str(metric) + " :: " + str(percentile))

            elif (key == "latency"):
                Logger.info("LATENCY : ")
                Logger.info("**********")
                for event in analyzed_data[key] :
                    if (len(analyzed_data[key][event]) > 0):              
                        percentile = np.percentile(analyzed_data[key][event], metric)
                        Logger.info(event + " :: TP " + str(metric) + " :: " + str(percentile))
                    Logger.info("")
            else :                
                percentile = np.percentile(analyzed_data[key], metric)
                cpu_mem_info = cpu_mem_info + (str(key) + " :: TP " + str(metric) + " :: " + str(percentile)) + "\n"
        Logger.info("CPU/MEM info : ")
        Logger.info("***************")
        Logger.info(cpu_mem_info)
        Logger.info("############## END ANALYZED DATA . TP "+ str(metric)+" ###################")

    except Exception as e :
        Logger.error("Error getting TP metrics : " + str(e))

def Generate2DPlot(name,xData,yData,xLabel,yLabel,eventsData):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xticks(rotation=45)
    plt.plot(xData,yData, linestyle='-', marker='o', color='r')
    dates = eventsData.keys()
    xfmt = matplotlib.dates.DateFormatter('%H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    ymax = max(100,max(yData))
    ax.set_ylim(0,ymax+20)
    for x in dates:
        y = randint(0,ymax-20)
        ax.annotate(eventsData[x],xy=(x,0),xytext=(x,y),arrowprops=dict(arrowstyle="->"))
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.tight_layout()
    plt.title(name)
    plt.grid()
    figure_name = Logger.LoggingDir + name + time.strftime("%Y%m%d-%H%M%S")+".png"
    plt.savefig(figure_name)
    plt.close('all')

#Extract Perf averages
def WorkWithPerfData(user_tag , perf_data):
    try :
        analyzed_data = {}        
        cpuAvg = 0
        cpuMax = 0
        memAvg = 0
        CommemMax = 0

        cpuDict = perf_data["cpu"]
        if (len(cpuDict) > 0) :
            cpuTimeData = cpuDict.keys()
            cpuData = cpuDict.values()              
            max_index, max_value = max(enumerate(cpuData), key=operator.itemgetter(1))
            Logger.info( 'MAX CPU at time' + str(list(cpuTimeData)[max_index]) + 'is ' + str(max_value))
            if ("cpu_max" not in analyzed_data):
                analyzed_data["cpu_max"] = list()
            analyzed_data["cpu_max"].append(max_value)
            avgCPU = TrimmedAvg(cpuData)
            Generate2DPlot('CPU_Plot_' + user_tag+'_',cpuTimeData,cpuData,'Time','CPU %',perf_data["events"])
            if ("cpu_trimmed_avg" not in analyzed_data):
                analyzed_data["cpu_trimmed_avg"] = list()
            analyzed_data["cpu_trimmed_avg"].append(avgCPU)

            avgCPU = Avg(cpuData)
            if ("cpu_avg" not in analyzed_data):
                analyzed_data["cpu_avg"] = list()
            analyzed_data["cpu_avg"].append(avgCPU)


        memDict = perf_data["mem"]
        if (len(memDict) > 0) :
            timeData = memDict.keys()
            memData = memDict.values()
            max_index, max_value = max(enumerate(memData), key=operator.itemgetter(1))
            if ("mem_max" not in analyzed_data):
                analyzed_data["mem_max"] = list()
            analyzed_data["mem_max"].append(max_value)
            Logger.info( 'MAX Memory at time' + str(list(timeData)[max_index]) + 'is ' + str(max_value) + "MB")
            avgMem = TrimmedAvg(memData)
            if ("mem_trimmed_avg" not in analyzed_data):
                analyzed_data["mem_trimmed_avg"] = list()
            analyzed_data["mem_trimmed_avg"].append(avgMem)
            Generate2DPlot('MEM_Plot_' + user_tag+'_',timeData,memData,'Time','Heap (MB)',perf_data["events"])

            avgMem = Avg(memData)
            if ("mem_avg" not in analyzed_data):
                analyzed_data["mem_avg"] = list()
            analyzed_data["mem_avg"].append(avgMem)

        latencyDict = perf_data["latency"]
        if (len(latencyDict) > 0):
            if ("latency" in latencyDict ):
                for key,value in latencyDict.iteritems():
                    if key not in analyzed_data["latency"]:
                        analyzed_data["latency"][key] = list()
                    analyzed_data["latency"][key].append(value)
            else:
                analyzed_data["latency"]=latencyDict

        deviceInfoDict = perf_data["device_info"]
        if (len(deviceInfoDict) > 0):
            analyzed_data["device_info"]=deviceInfoDict

        if ("firmware_launch_time" in perf_data.keys()):
            launch_time = perf_data["firmware_launch_time"]
            if (launch_time is not None and launch_time > 0.0 ):
                if "firmware_launch_time" not in analyzed_data:
                    analyzed_data["firmware_launch_time"] = list()
                analyzed_data["firmware_launch_time"].append(launch_time)

        ## Check for crash ##
        if (len(perf_data["events"]) > 0):
            for key,value  in perf_data["events"].iteritems():
                Logger.info("Value : " + str(value) + " key : " + str(key))
                if '!Crash!' in value:
                    global crash_data
                    crash_data.append(key)
                    Logger.info("Added to crash data")

        Logger.info("Analyzed data : " + str(analyzed_data))

        return analyzed_data
    except Exception as e :
        Logger.error("Invalid perf data" + str(e))
        return None

def DetectPeaks(data,time):
    indexes = scipy.signal.find_peaks_cwt(data, np.arange(1, 20),
        max_distances=np.arange(1, 20)*2)
    indexes = np.array(indexes) - 1
    prevIndex = 1
    Logger.info('Peaks are: %s' % (indexes))
    for index in indexes:
        frame = enumerate(data[prevIndex-1:index])
        Logger.info ("Length of frame " + str(len(list(frame))))
        if (len(list(frame)) >= 1):
            max_index, max_value = max(frame, key=operator.itemgetter(1))
            Logger.info ('Peak at time' + str(time[max_index])+ 'is '+str(max_value))
        prevIndex = index

def TrimmedAvg(data, m=2):
    return float("{0:.2f}".format(stats.trim_mean(data, 0.4)))

def Avg(data):
    return float("{0:.2f}".format(np.mean(data)))
