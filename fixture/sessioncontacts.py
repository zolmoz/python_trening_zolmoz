class Sessioncotacts:
    def __init__(self,app):
        self.app = app

    def login(self,  username, password):
        wd = self.app.wd
        self.app.open_homepage()
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
        # logout
        wd.find_element_by_link_text("Logout").click()