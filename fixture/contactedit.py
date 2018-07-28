from fixture.contacts import ContactHelper

class ContactEdit:
    def __init__(self,app):
        self.app = app


    def edit_first_contact(self, Contactfilld):
        wd = self.app.wd
        ContactHelper.open_home_page(self)
        # selest first contact
        wd.find_element_by_css_selector("[title^='Edit']").click()
        # fill contact firm
        ContactHelper.fild_contact(self,Contactfilld)
        # submit update
        wd.find_element_by_name("update").click()
        ContactHelper.open_home_page(self)

