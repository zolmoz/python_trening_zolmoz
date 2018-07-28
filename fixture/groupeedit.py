from fixture.group import GroupHelper

class GroupEdit:
    def __init__(self,app):
        self.app = app

    def modefi_first_groupe(self, groupe):
        wd = self.app.wd
        GroupHelper.open_group_page(self)
        # selest first groupe
        wd.find_element_by_name("selected[]").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        # fill groupe firm
        GroupHelper.fild_contact(self,groupe)
        # submit update
        wd.find_element_by_name("update").click()
        GroupHelper.return_to_groups_page(self)

    def modefi_first_empty_groupe(self, groupe):
        wd = self.app.wd
        GroupHelper.open_group_page(self)
        # selest first groupe
        wd.find_element_by_css_selector("[title^='Select ( )']").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        # fill groupe firm
        GroupHelper.fild_contact(self,groupe)
        # submit update
        wd.find_element_by_name("update").click()
        GroupHelper.return_to_groups_page(self)