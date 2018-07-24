# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from groupe import Groupe

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_ad_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        # return to groupse page
        wd.find_element_by_link_text("groups").click()

    def create_groupe(self, wd, groupe):
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

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, user_name, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def test_test_ad_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_group_page(wd)
        self.create_groupe(wd, Groupe(name="group2", header="group2", footer="group2"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_test_ad_empty_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_group_page(wd)
        self.create_groupe(wd, Groupe (name=" ", header=" ", footer=" "))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
