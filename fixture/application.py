from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sesion import SessionHelper
from fixture.group import GroupHelper
from fixture.contacts import ContactHelper
from fixture.groupdelete import GroupDelete
from fixture.groupeedit import GroupEdit



class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contacts = ContactHelper(self)
        self.groupdelete = GroupDelete(self)
        self.groupeedit = GroupEdit(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy (self):
        self.wd.quit()