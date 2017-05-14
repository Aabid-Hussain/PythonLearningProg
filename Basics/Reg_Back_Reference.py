import re

randStr = "https://www.youtube.com http://www.google.com"

'''output:
<a href = 'https://www.youtube.com'>www.youtube.com</a>
<a href = 'http://www.youtube.com'>www.youtube.com</a>
'''

regex = re.compile(r"(https?://([\w.]+))")

randStr = re.sub(regex,r"<a href='\1'>'\2'</a>\n",randStr)

print randStr