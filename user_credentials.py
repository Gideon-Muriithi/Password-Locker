import pyperclip
import random
import string


class User:
    """
    Class that generates new instances of users
    """

    user_list = []

    def __init__(self, fname, lname, password):
        '''
		__init__ method that define the properties each user object will have
		'''

        self.fname = fname
        self.lname = lname
        self.password = password

    def save_user(self):
        '''
        save_contact method that saves contact objects into contact_list
        '''
        User.user_list.append(self)


class Credentials:
    credentials_list = []
    user_credentials_list = []

    @classmethod
    def user_check(cls, fname, password):
        '''
		user_check method that checks if the name and password entered match entries in the users_list
		'''
        current_user = ''
        for user in User.user_list:
            if user.fname == fname and password == password:
                current_user = user.fname
        return current_user

    def __init__(self, username, site_name, account_name, password):
        '''
		__init__ method that define the properties each credentials object will have
		'''
        self.username = username
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
		save_credentials method to save a newly created credentials instances
		'''
        Credentials.user_credentials_list.append(self)

    def pwd_generation(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
		pwd_generation method to generate password for credentials instances
		'''
        pwd_gen = " ".join(random.choice(char) for _ in range(size))
        return pwd_gen

    @classmethod
    def display_credentials(cls, username):
        '''
		Class method to display the list of credentials saved
		'''
        user_credentials_list = []
        for credential in user_credentials_list:
            if credential.username == username:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def get_by_site_name(cls, site_name):
        '''
		Method that takes in a site_name and returns a credential that matches that site_name
		'''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
        return credential

    @classmethod
    def copy_credential(cls, site_name):
        '''
	    method that copies a credential's info after the credential's site name is entered
	    '''
        get_credential = Credentials.get_by_site_name(site_name)
        return pyperclip.copy(get_credential.password)
