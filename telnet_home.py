import re
import os
import telnetlib


host = "192.168.0.50"
telnet = telnetlib.Telnet(host)

telnet.read_until("Password:",2)
telnet.write("cisco \n")

telnet.read_until("R1>",2)
telnet.write("cisco \n")




telnet.read_until("R1#",2)
telnet.write("show ip interface brief \r\n")

output=telnet.read_until("R1#",timeout=0)

print (output)

telnet.close()



