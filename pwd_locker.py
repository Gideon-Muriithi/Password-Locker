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
		print("-"*60)
		print("Use these codes to navigate: \n CA-Create Account \n LI-Log In \n Ex-Exit")
		short_code = input("Enter a choice: ").lower().strip()
		if short_code == "Ex":
			break	
				

if __name__ == '__main__':
	main()
