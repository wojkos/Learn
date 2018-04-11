import time
from datetime import datetime as dt
host_path = '/etc/hosts'
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "gazeta.pl","www.gazeta.pl"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
		print("Working hours...keep working")
		with open(host_path, 'r+') as file:
		 	content = file.read()
		 	for website in website_list:
		 		if website in content:
		 			pass
		 		else:
		 			file.write(redirect+" "+website+"\n")
	else:
		with open(host_path,'r+') as file:
			content = file.readline()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()		
	print(content)
	time.sleep(5)
