from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.contacts import ContactHelper
from fixture.sessioncontacts import Sessioncotacts

class App_for_contants:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.sessioncontacts = Sessioncotacts(self)
        self.contacts = ContactHelper(self)


    def open_homepage(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()