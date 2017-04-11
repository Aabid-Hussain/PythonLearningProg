import re

Device_Log = "adfd sdf 12 25.25 5.255.255 55.5 192.169.1.2 1.1.1.1 adf 2.0 999.999.999.999"

RegEx = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"

match = re.findall(RegEx,Device_Log)

for line in match:
    print line

