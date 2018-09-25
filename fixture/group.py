from model.groupe import Groupe

class GroupHelper:
    def __init__(self,app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groupse page
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def change_fild_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fild_contact (self, groupe):
        # fill groupe firm
        wd = self.app.wd
        self.change_fild_value("group_name", groupe.name)
        self.change_fild_value("group_header", groupe.header)
        self.change_fild_value("group_footer", groupe.footer)




    def create(self, groupe):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fild_contact(groupe)
        # submin groupe creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_groupe(self):
        self.delete_groupe_by_index(0)

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_groupe_by_id(self,id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_groupe_by_index(self,index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_grupe(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_cirilic_groupe (self):
        wd = self.app.wd
        self.open_group_page()
        #selest first groupe
        wd.find_element_by_css_selector("[title^='Select (группа3)']").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


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
        self.group_cache = None

    def modefi_groupe_by_index(self, index, groupe):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        #open modification form
        wd.find_element_by_name("edit").click()
        #fill groupe
        self.fild_contact(groupe)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def modefi_groupe_by_id(self, id, groupe):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        #open modification form
        wd.find_element_by_name("edit").click()
        #fill groupe
        self.fild_contact(groupe)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def modefi_first_groupe(self):
        self.modefi_groupe_by_index(0)




    def modefi_first_empty_groupe(self, groupe):
        wd = self.app.wd
        self.open_group_page()
        # selest first empty groupe
        wd.find_element_by_css_selector("[title^='Select ( )']").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        # fill groupe firm
        self.fild_contact(groupe)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache= []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Groupe(name=text, id=id))
        return list(self.group_cache)
