import sqlite3, time

# login function checks if any given username and password exists within database
def login():
	while True:
		username = input("Please enter your username: ")
		password = input("Please enter your password: ")
		with sqlite3.connect("Quiz.db") as db:
			cursor = db.cursor()
		find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
		cursor.execute(find_user,[(username), (password)])
		results = cursor.fetchall()

		if results:
			for i in results:
				print("Welcome " + i[2])
			#return("exit")
			break

		else:
			print("Username and password not recognize")
			again = input("Do you want to try again?(y/n): ")
			if again.lower() == "n":
				print("Goodbye")
				time.sleep(1)
				#return ("exit")
				break

#function to create a new account
def newUser():
	found = 0
	while found == 0:
		username = input("Please enter a username: ")
		with sqlite3.connect("Quiz.db") as db:
			cursor = db.cursor()
		findUser = ("SELECT * FROM user WHERE username = ?")
		cursor.execute(findUser, [(username)])

		if cursor.fetchall():
			print("Username Taken, please try again")
		else:
			found = 1

	firstname = input("Enter your first name: ")
	surname = input("Enter you sur name: ")
	password = input("Please enter your password: ")
	password1 = input("Please reenter your password: ")
	while password != password1:
		print("Your password didn't match, please try again")
		password = input("Please enter your password: ")
		password1 = input("Please reenter your password: ")
	insertData = '''INSERT INTO user(username, firstname, surname, password)
	VALUES(?,?,?,?)'''
	cursor.execute(insertData, [(username), (firstname), (surname), (password)])
	db.commit()

def menu():
	while True:
		print("Welcome to my system")
		menu = ('''
		1 - Create New User
		2 - Login to system
		3 - Exit system\n 
		''')
		userChoice = input(menu)

		if userChoice == '1':
			newUser()
		elif userChoice == '2':
			login()
		elif userChoice == '3':
			print("Goodbye")
			break
		else:
			print("Input not valid: ")

menu()