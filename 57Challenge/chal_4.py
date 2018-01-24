import paramiko
from time import sleep
from getpass import getpass


devices = {
            'SVR-1': {'ip': '192.168.182.101'}
}

max_buffer = 65535

commands = ['ls -ltr', 'ps -aux | grep network', 'compgen -u']

username = raw_input("Username: ")
password = getpass('Password: ')

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


for dev in devices.keys():
    output_file = 'dev' + '_output.txt'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(devices[dev]['ip'], username=username, password=password,
                look_for_keys=False, allow_agent=False)

    new_connection = ssh.invoke_shell()
    output = clear_buffer(new_connection)
    sleep(2)

    new_connection.send("ps -aux \n")

    output += clear_buffer(new_connection)


    with open(output_file, 'wb') as fob:
        for command in commands:
            new_connection.send(command + "\n")
            sleep(2)
            output = clear_buffer(new_connection)
            print(output)
            fob.write(output)

    new_connection.close()



