# -*- coding: utf-8 -*-
from model.groupe import Groupe
import  pytest


def test_test_ad_group(app, db, json_groups,check_ui):
    group = json_groups
    with pytest.allure.step('Given a groupe list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('when i add groupe %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new groupe list is equal to the list with the added groupe'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Groupe.id_or_max) == sorted(app.group.get_group_list(), key=Groupe.id_or_max)





