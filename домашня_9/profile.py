user_login_in = False

def check_login(func):

    def login():
        if not user_login_in:
            print("User is not login in ")
            return
        return func()
    return login

@check_login
def show_profile():
    print("Welcome to your profile !")

show_profile()