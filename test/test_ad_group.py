# -*- coding: utf-8 -*-
from model.groupe import Groupe


def test_test_ad_group(app):
    success = True
    old_groups = app.group.get_group_list()
    group = Groupe(name="group2", header="group2", footer="group2")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups,key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)



def test_test_ad_notall_group(app):
    success = True
    old_groups = app.group.get_group_list()
    group =Groupe(name="group", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)


def test_test_ad_kirilic_group(app):
    success = True
    old_groups = app.group.get_group_list()
    group = Groupe(name="группа3", header="группа3", footer="группа3")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)


def test_test_ad_empty_group(app):
    success = True
    old_groups = app.group.get_group_list()
    group = Groupe(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)


