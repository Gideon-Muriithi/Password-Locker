import pyperclip
from user_credentials import User, Credentials

def main():
	def create_user(fname, lname, password):
		'''
		Function to create a new user account
		'''
		new_user = User(fname, lname, password)
		return new_user


	def save_user(user):
		'''
		Function to save a new user account
		'''
		User.save_user(user)


	def verify_user(fname, password):
		'''
		Function to verify user exist before creating the user credentials
		'''
		user_verification = Credentials.user_check(fname, password)
		return user_verification


	def pwd_generation():
		'''
		pwd_generation function to generate a password automatically
		'''
		pwd_gen = Credentials.pwd_generation()
		return pwd_gen

	def create_credentials(username,site_name,account_name,password):
		'''
		Function that create new credential
		'''
		new_credential = Credentials(username,site_name,account_name,password)
		return new_credential

	def save_credentials(credential):
		'''
		Function to save a newly created credential
		'''
		Credentials.save_credentials(credential)

	def display_credentials(username):
		'''
		Function to display user credentials
		'''
		return Credentials.display_credentials(username)

	def copy_credential(site_name):
		'''
		Function to copy credential details to the clipboard
		'''
		return Credentials.copy_credential(site_name)

	print(" ")
	print("Hi there! Welcome to Password Locker App!")
	while True:
		print(" ")
		print("-"*40)
		print("Use these codes to navigate: \n ca-Create Account \n li-Log In \n ex-Exit")
		short_code = input("Enter a choice: ").lower().strip()
		
		if short_code == "ex":
			break	

		elif short_code == "ca":
			print("-"*40)
			print(" ")
			print("To create an account:")
			fname = input("Enter your first name - ").strip()
			lname = input("Enter your last name - ").strip()
			password = input("Enter your password - ").strip()
			save_user(create_user(fname, lname,password))
			print(" ")
			print(f"New Account Created for: {fname} {lname} using password: {password}")	

		elif short_code == 'li':
			print("-"*40)
			print(" ")
			print("Please enter your account details to log in:")
			username = input("Enter your first name - ").strip()
			password = str(input("Enter your password - "))
			user_exists = verify_user(username,password)
			if user_exists == username:
				print(" ")
				print(f"Welcome {username}. Please pick an option to continue.")
				print(" ")	
				while True:
					print("-"*40)
					print("Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n cp-Copy Password \n ex-Exit")
					short_code = input("Enter an option: ").lower().strip()
					print("-"*40)
					if short_code == "ex":
						print(" ")
						print(f"Goodbye {username}")
						break
					elif short_code == "cc":
						print(" ")
						print("Enter your credential details:")
						site_name = input("Enter the site\'s name- ").strip()
						account_name = input("Enter your account\'s name - ").strip()	


if __name__ == '__main__':
	main()
