from app import config

class Login(object):

    def __init__(self, arg):
        self.rb = arg

        try:
            self.rb.open("https://stackoverflow.com/users/login")
            form = self.rb.get_form(id="login-form")
            form['email'].value = config.stackemail
            form['password'].value = config.stackpassword
            self.rb.submit_form(form)
        except Exception:
            return None