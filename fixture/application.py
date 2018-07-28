from selenium.webdriver.firefox.webdriver import WebDriver

class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)


    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        # return to groupse page
        wd.find_element_by_link_text("groups").click()

    def create_groupe(self,  groupe):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill groupe firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(groupe.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(groupe.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(groupe.footer)
        # submin groupe creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self,  user_name, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy (self):
        self.wd.quit()