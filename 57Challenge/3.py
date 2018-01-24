import getpass

from pexpect import pxssh


devices = {

    'server-1':{'prompt':'[stack@localhost ~]$', 'ip':'192.168.182.101'},
    'server-2':{'prompt':'iosv-2#', 'ip':'192.168.195.182'},

    }

commands = ['ls -ltr', 'ps -aux | grep network', 'compgen -u']

username = raw_input('Username: ')
password = getpass.getpass('Password: ')

for device in devices.keys():
    prompt_detail = devices[device]['prompt']
    output_filename = device + '_output.txt'
    child = pxssh.pxssh()
    child.login(devices[device]['ip'], username.strip(), password.strip(),
                auto_prompt_reset=False)

    with open(output_filename, 'wb') as fob:
        for command in commands:
            child.sendline(command)
            child.expect(prompt_detail)
            fob.write(child.before)

    child.logout()
