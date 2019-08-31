import pyperclip
import unittest
from user_credentials import User, Credentials

class TestUser(unittest.TestCase):
    def createAcc(self):
        self.new_user = User("Gideon", "Chef", "Been2000")

    def test__init__(self):
        self.assertEqual(self.new_user.fname, "Gideon")
        self.assertEqual(self.new_user.lname, "Chef")    
        self.assertEqual(self.new_user.password, "Been2000")    
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1) 

class TestCredentials(unittest.TestCase):
    def test_user_check(self):
        self.new_user = User("Gideon", "Chef", "Been2000")
        self.new_user.save_user()
        addUser = User("Peter", "Chamgei", "Double10")
        addUser.save_user()
        for user in User.users_list:
            if user.fname == addUser.fname and user.password == addUser.password:
                current_user = user.fname
        return current_user
        self.assertEqual(current_user, Credentials.user_check(addUser.password, addUser.fname))

    def setUp(self):
		self.new_credential = Credentials("Gideon","Twitter","@gideonm","Been2000")
    
    def test__init__(self):
        self.assertEqual(self.new_credential.username,"Gideon")
		self.assertEqual(self.new_credential.site_name, "Twitter")
		self.assertEqual(self.new_credential.account_name, "@gideonm")
		self.assertEqual(self.new_credential.password, "Been2000")    
    
    def test_save_credentials(self):
		self.new_credential.save_credentials()
		Facebook = Credential("Grace", "Facebook", "@graceg",'Been2000')
		Facebook.save_credentials()
		self.assertEqual(len(Credentials.credentials_list),2)

    def tearDown(self):
		Credentials.credentials_list = []
		User.users_list = []    
    
    def test_display_credentials(self):
		self.new_credential.save_credentials()
		Facebook = Credential("Grace", "Facebook", "@graceg",'Been2000')
		Facebook.save_credentials()
		gmail = Credentials("Grace",'Gmail', "graceg", "Been2000")
		gmail.save_credentials()
		self.assertEqual(len(Credentials.display_credentials(Facebook.username)),2)

    def test_get_by_site_name(self):
		self.new_credential.save_credentials()
		Facebook = Credential("Grace", "Facebook", "@graceg",'Been2000')
		Facebook.save_credentials()
		credential_exists = Credentials.get_by_site_name("Facebook")
		self.assertEqual(credential_exists, Facebook) 

    def test_copy_credential(self):
		self.new_credential.save_credentials()
		Facebook = Credential("Grace", "Facebook", "@graceg",'Been2000')
		Facebook.save_credentials()
		get_credential = None
		for credential in Credentials.user_credentials_list:
				get_credential = Credentials.get_by_site_name(credential.site_name)
				return pyperclip.copy(get_credential.password)
		Credentials.copy_credential(self.new_credential.site_name)
		self.assertEqual("Been200", pyperclip.paste())
		print(pyperclip.paste())   
            
if __name__ == '__main__':
	unittest.main(verbosity=2)



               
    