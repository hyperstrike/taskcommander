users = {} #migrate this to database 
status = ""
while status != "q":
	status = raw_input("Are you a registered user y/n? Press q to quit: ")

	if status == "n":
		username = raw_input("Create user name: ") #add input validation

		if username in users:
                                                print "Hi"
		else:
                                                password = raw_input("Create password: ") #add input validation
		        users[username] = password
                                                 print "\nUser created!\n"
	elif status == 'y':
		exusername = raw_input("Enter user name: ")
		if exusername in users:
		      expassword = raw_input("Enter password: ")
			if expassword = users[exusername]:  
				print "login successful!"
		else:
		       print "User doesn't exist!\n"
