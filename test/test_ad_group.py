# -*- coding: utf-8 -*-
from model.groupe import Groupe





def test_test_ad_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups,key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)





