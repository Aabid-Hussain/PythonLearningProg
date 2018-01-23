#spawn network gear using pexpect

import pexpect

devices = {'iosv-1':{
    'prompt':'iosv-1#',
    'ip':'192.168.182.101',
    'status':'True'
},
    'iosv-2':{
        'prompt':'iosv-2#',
        'ip':'192.168.182.102',
        'status':'True'

    }

}

username = 'cisco'
password = 'cisco'

for device in devices.keys():
    device_prompt = devices[device]['prompt']

    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    child.expect('Username')
    child.sendline(username)
    child.expect('Password')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline('show version | include V')
    child.expect(device_prompt)
    print(child.before())
    child.sendline(exit)
