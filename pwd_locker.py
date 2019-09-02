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

if __name__ == '__main__':
	main()
