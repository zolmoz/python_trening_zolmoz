#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

from model.contactfilld import Contactfilld
import re

class ContactHelper:
    def __init__(self,app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Sende - Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def fild_contact(self, Contactfilld):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contactfilld.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contactfilld.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contactfilld.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contactfilld.nickename)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contactfilld.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contactfilld.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contactfilld.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contactfilld.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contactfilld.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contactfilld.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contactfilld.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contactfilld.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contactfilld.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Contactfilld.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contactfilld.homepage)
      #  bday = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
      #  bday.select_by_index(Contactfilld.selectbday)
       # bmonthe = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[2]"))
       # bmonthe.select_by_index(Contactfilld.selectbmonthe)
       # wd.find_element_by_name("byear").click()
       # wd.find_element_by_name("byear").clear()
       # wd.find_element_by_name("byear").send_keys(Contactfilld.byear)
       # aday = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[3]"))
      #  aday.select_by_index(Contactfilld.selectaday)
      #  amonthe = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[4]"))
      #  amonthe.select_by_index(Contactfilld.selectamothe)
      #  wd.find_element_by_name("ayear").click()
      #  wd.find_element_by_name("ayear").clear()
      #  wd.find_element_by_name("ayear").send_keys(Contactfilld.ayear)
      #  wd.find_element_by_name("address2").click()
      #  wd.find_element_by_name("address2").clear()
       # wd.find_element_by_name("address2").send_keys(Contactfilld.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contactfilld.secondaryphone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contactfilld.notes)

    def newcontact(self, Contactfilld):
        wd = self.app.wd
        # open add contact form
        wd.find_element_by_link_text("add new").click()
        # fill contact
        self.fild_contact(Contactfilld)
        # submit contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # open contact form
        self.open_home_page ()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_by_index(0)

    def delete_by_index(self,index):
        wd = self.app.wd
        self.open_home_page ()
        # selest first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        driver.switch_to.alert.accept()
        self.open_home_page()
        self.contact_cache = None


    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contactfilld(firstname=firstname,lastname=lastname,id=id,homephone=homephone,mobilephone=mobilephone,
                       workphone=workphone,secondaryphone=secondaryphone, email1=email1, email2=email2, email3=email3,
                            address=address)

    def get_contact_info_from_viwe_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contactfilld(homephone=homephone, mobilephone=mobilephone,workphone=workphone, secondaryphone=secondaryphone)



    def delete_all_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # selest first contact
        wd.find_element_by_id("MassCB").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.open_home_page()
        self.contact_cache = None

    def delete_Rose_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # selest first contact
        wd.find_element_by_css_selector("[title^='Select (Mia Rose)']").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.open_home_page()
        self.contact_cache = None

    def select_contact_by_index_modify(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("[title^='Edit']")[index].click()


    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd

        wd.find_element_by_xpath("//table[@id='maintable']//a[@href='edit.php?id=%s']" % id).click()

    def select_contact_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # selest first contact
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.open_home_page()
        self.contact_cache = None



    def edit_first_contact(self):
        self.edit_contact_by_index(0)


    def edit_contact_by_index(self, index, Contactfilld):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        self.open_contact_to_edit_by_id(id)
        self.fild_contact(Contactfilld)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cash = None


    def edit_contact_by_id(self, id, Contactfilld):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fild_contact(Contactfilld)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cash = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_email = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contactfilld(firstname=firstname, lastname=lastname, id=id,
                                                       all_phones_from_home_page=all_phones,
                                                       all_email_from_home_page=all_email, address=address))
        return  list(self.contact_cache)

    def select_by_xpath(self, xpath, text):
        if text is not None:
            wd = self.app.wd
            select_element = Select(wd.find_element_by_xpath(xpath))
            select_element.select_by_value(text)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(contact.id)
        self.select_by_xpath("//select[@name='to_group']", group.id)
        wd.find_element_by_xpath("//input[@name='add']").click()

    def remove_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.open_home_page()
        self.select_by_xpath("//select[@name='group']", group.id)
        self.select_contact_by_id(contact.id)
        wd.find_element_by_xpath("//input[@name='remove']").click()


