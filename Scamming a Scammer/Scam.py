import requests
import os
import random
import string
import json
from lxml.html import fromstring
from itertools import cycle
import traceback



chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
names = json.loads(open('names.json').read())
url = 'http://www.taiwansa.com/sw.php'
urlwebsite = 'http://www.taiwansa.com/86193//zj7xoK9f3WZb2H5/fcbg/?cat=3&i=2076499'

for name in names:
	# r = requests.get(urlwebsite)
	# print(r.content)
	# a = r.content.find(b'="',r.content.find(b'user_id_victim'))
	# b = r.content.find(b'"',a+2)
	# print(r.content[a+2:b+1])

	user_id = "BsPdLnVFdwQk0wNXFVVFZQVVQwOQ=="

	# a = r.content.find(b'="',r.content.find(b'user_ip'))
	# b = r.content.find(b'"',a+2)
	user_ip = "2401:4900:40ac:d4f6:d020:638b:fd8b:85a4"
	

	name_extra = ''.join(random.choice(string.digits))
	username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'email': username,
		'pass': password,
    	'user_id_victim': user_id,
    	'user_ip': user_ip,
    	'type': 'instagram'
	})

	print ('sending username %s and password %s' % (username, password))