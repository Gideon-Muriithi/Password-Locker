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

# class TestCredentials(unittest.TestCase):
#     def test_user_credentials(self):
#     self.new_user = User("Gideon", "Chef", "Been2000")

               