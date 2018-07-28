from fixture.group import GroupHelper

class GroupDelete:
    def __init__(self,app):
        self.app = app


    def delete_first_groupe (self):
        wd = self.app.wd
        GroupHelper.open_group_page(self)
        #selest first groupe
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        GroupHelper.return_to_groups_page(self)


    def delete_all_groupe(self):
        wd = self.app.wd
        GroupHelper.open_group_page(self)
        # selest first groupe
        elements = wd.find_elements_by_name("selected[]")
        for e in elements:
            e.click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        GroupHelper.return_to_groups_page(self)