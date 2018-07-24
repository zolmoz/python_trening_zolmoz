# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from selenium.webdriver.support.ui import Select

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class ad_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def newcontact(self, wd, firstname, middlename, lastname, nickename, title, company, address, home, mobile, work,
                   fax, email1, email2, email3, homepage, byear, ayear, address2, phone2, notes, selectbday,
                   selectbmonthe, selectaday, selectamothe):
        # open add contact form
        wd.find_element_by_link_text("add new").click()
        # fill contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickename)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)
        bday = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
        bday.select_by_index(selectbday)
        bmonthe = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[2]"))
        bmonthe.select_by_index(selectbmonthe)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(byear)
        aday = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[3]"))
        aday.select_by_index(selectaday)
        amonthe = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[4]"))
        amonthe.select_by_index(selectamothe)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        # submit contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # open contact form
        wd.find_element_by_link_text("home").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_homepage(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def test_ad_contact(self):
        success = True
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.newcontact(wd, firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                        company="Rose", address="ertyui", home="1234", mobile="5678", work="90123", fax="4567",
                        email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry", selectbday="3",
                        selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000", address2="dferesdfe", phone2="rererr", notes="fgwewerewrw")

        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
