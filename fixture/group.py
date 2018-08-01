class GroupHelper:
    def __init__(self,app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groupse page
        wd.find_element_by_link_text("groups").click()

    def fild_contact (self, groupe):
        # fill groupe firm
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(groupe.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(groupe.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(groupe.footer)

    def create(self, groupe):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fild_contact(groupe)
        # submin groupe creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()


    def delete_first_groupe (self):
        wd = self.app.wd
        self.open_group_page()
        #selest first groupe
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def delete_cirilic_groupe (self):
        wd = self.app.wd
        self.open_group_page()
        #selest first groupe
        wd.find_element_by_css_selector("[title^='Select (группа3)']").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def delete_all_groupe(self):
        wd = self.app.wd
        self.open_group_page()
        # selest first groupe
        elements = wd.find_elements_by_name("selected[]")
        for e in elements:
            e.click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modefi_first_groupe(self, groupe):
        wd = self.app.wd
        self.open_group_page()
        # selest first groupe
        wd.find_element_by_name("selected[]").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        # fill groupe firm
        self.fild_contact(groupe)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def modefi_first_empty_groupe(self, groupe):
        wd = self.app.wd
        self.open_group_page()
        # selest first groupe
        wd.find_element_by_css_selector("[title^='Select ( )']").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        # fill groupe firm
        self.fild_contact(groupe)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
