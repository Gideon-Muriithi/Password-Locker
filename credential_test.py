import pyperclip
import unittest
from user_credentials import User, Credentials


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before each test cases is executed
        '''
        self.new_user = User("Gideon", "Chef", "Been2000")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.fname, "Gideon")
        self.assertEqual(self.new_user.lname, "Chef")
        self.assertEqual(self.new_user.password, "Been2000")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Crededentials class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def test_check_credentials(self):
        '''
		test_check_credentials to test whether user_check method executes as intended
		'''
        self.new_user = User("Gideon", "Chef", "Been2000")
        self.new_user.save_user()
        addUser = User("Peter", "Chamgei", "Double10")
        addUser.save_user()

        for user in User.user_list:
            if user.fname == addUser.fname and user.password == addUser.password:
                current_user = user.fname
        return current_user

        self.assertEqual(current_user, Credentials.user_check(
            addUser.password, addUser.fname))

    def setUp(self):
        '''
		setUp method to create an account's credentials before each test
		'''
        self.new_credential = Credentials(
            "Gideon", "Twitter", "@gideonm", "Been2000")

    def test_init(self):
        '''
		test_init to test if the initialization of credential instances is properly done
		'''
        self.assertEqual(self.new_credential.username, "Gideon")
        self.assertEqual(self.new_credential.site_name, "Twitter")
        self.assertEqual(self.new_credential.account_name, "@gideonm")
        self.assertEqual(self.new_credential.password, "Been2000")

    def test_save_credentials(self):
        '''
		test_save_credentials to test if the new credentials are saved into the credentials list
		'''
        self.new_credential.save_credentials()
        Facebook = Credentials("Grace", "Facebook", "@graceg", 'Been2000')
        Facebook.save_credentials()
        self.assertEqual(len(Credentials.user_credentials_list), 2)

    def tearDown(self):
        Credentials.user_credentials_list = []
        User.user_list = []

    def test_display_credentials(self):
        self.new_credential.save_credentials()
        Facebook = Credentials("Grace", "Facebook", "@graceg", 'Been2000')
        Facebook.save_credentials()
        gmail = Credentials("Grace", 'Gmail', "graceg", "Been2000")
        gmail.save_credentials()
        self.assertEqual(
            len(Credentials.display_credentials(Facebook.username)), 2)

    def test_get_by_site_name(self):
        self.new_credential.save_credentials()
        Facebook = Credentials("Grace", "Facebook", "@graceg", 'Been2000')
        Facebook.save_credentials()
        credential_exists = Credentials.get_by_site_name("Facebook")
        self.assertEqual(credential_exists, Facebook)

    def test_copy_credential(self):
        self.new_credential.save_credentials()
        Facebook = Credentials("Grace", "Facebook", "@graceg", 'Been2000')
        Facebook.save_credentials()
        get_credential = None
        for credential in Credentials.user_credentials_list:
            get_credential = Credentials.get_by_site_name(credential.site_name)
            return pyperclip.copy(get_credential.password)
        Credentials.copy_credential(self.new_credential.site_name)
        self.assertEqual("Been200", pyperclip.paste())
        print(pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
