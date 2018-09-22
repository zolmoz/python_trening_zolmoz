
class SessionHelper:
    def __init__(self,app):
        self.app = app

    def login(self, user_name, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
        # logout
        wd.find_element_by_link_text("Logout").click()

    def is_logget_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logget_in_as(self, user_name):
        wd = self.app.wd
        return  self.get_logged_user() == user_name

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logget_in():
            self.logout()

    def ensure_login(self, user_name, password):
        wd = self.app.wd
        if self.is_logget_in():
            if self.is_logget_in_as(user_name):
                return
            else:
                self.logout()
        self.login(user_name, password)