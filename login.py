
import hashlib
import uuid
import string 
users = {}
status = ""

def hash_password(passwordpar):
	salt = uuid.uuid4().hex
	return hashlib.sha256(salt.encode() + passwordpar.encode()).hexdigest() + ':'+ salt


def check_password(hashed_passwordpar, user_passwordpar):
	password, salt = hashed_passwordpar.split(':')
	return password == hashlib.sha256(salt.encode() + user_passwordpar.encode()).hexdigest()

while (status != "q"):
	status = raw_input("Are you a registered user y/n? Press q to quit.")
	if (status == "n"):
		username = raw_input("Create user name: ")
		if username in users:
			print("This username already exists.")
		else:
			password = raw_input("Create password: ")
			hashed_password = hash_password(password)
			users[username]= hashed_password
			print("\n User created! \n")
	elif (status == "y"):
		exusername = raw_input("Enter user name: ")
		if exusername in users:
			expassword = raw_input("Enter password: ")
			if (check_password(hashed_password, expassword)):
				print ("login successful")
			else:
				count = 3
				while (expassword != users[exusername] and count > 0):
					print("password is not correct\n you have %s more tries") % count
					count-= 1
					expassword = raw_input("Enter password: ")
				
		else:
			print("user does not exist")




