from selenium.webdriver.support.ui import Select

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
        wd.find_element_by_name("home").send_keys(Contactfilld.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contactfilld.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contactfilld.work)
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
        bday = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
        bday.select_by_index(Contactfilld.selectbday)
        bmonthe = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[2]"))
        bmonthe.select_by_index(Contactfilld.selectbmonthe)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contactfilld.byear)
        aday = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[3]"))
        aday.select_by_index(Contactfilld.selectaday)
        amonthe = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[4]"))
        amonthe.select_by_index(Contactfilld.selectamothe)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Contactfilld.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contactfilld.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contactfilld.phone2)
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


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page ()
        # selest first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def delete_all_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # selest first contact
        wd.find_element_by_id("MassCB").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def delete_Rose_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # selest first contact
        wd.find_element_by_css_selector("[title^='Select (Mia Rose)']").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def edit_first_contact(self, Contactfilld):
        wd = self.app.wd
        self.open_home_page()
        # selest first contact
        wd.find_element_by_css_selector("[title^='Edit']").click()
        # fill contact firm
        self.fild_contact(Contactfilld)
        # submit update
        wd.find_element_by_name("update").click()
        self.open_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))