class User:
    users_list = []
    def __init__(self, fname, lname, password):
        self.fname = fname
        self.lname = lname
        self.password = password

    def user_saving:
        user.users_list.append(self)    

class Credentials:
    crededentials_list = []
    user_credentials = []

    @classmethod
    def user_check(cls, fname, password):
        current_user = ''
        for user in User.users_list:
            if (user.fname == fname and password == password):
                current_user = user.fname
        return current_user        