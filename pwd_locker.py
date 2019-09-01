#!/usr/bin/env python3.6
import pyperclip
from user_credentials import User, Credentials


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

