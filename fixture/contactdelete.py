from fixture.contacts import ContactHelper

class ContactDelete:
    def __init__(self,app):
        self.app = app

    def delete_first_contact(self):
        wd = self.app.wd
        ContactHelper.open_home_page (self)
        # selest first groupe
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        ContactHelper.open_home_page(self)

    def delete_all_contact(self):
        wd = self.app.wd
        ContactHelper.open_home_page(self)
        # selest first groupe
        wd.find_element_by_id("MassCB").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        ContactHelper.open_home_page(self)

    def delete_Rose_contact(self):
        wd = self.app.wd
        ContactHelper.open_home_page(self)
        # selest first groupe
        wd.find_element_by_css_selector("[title^='Select (Mia Rose)']").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        ContactHelper.open_home_page(self)

