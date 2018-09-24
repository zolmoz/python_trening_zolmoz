from model.groupe import Groupe
import random


def test_delete_some_groupe_01(app,db):
    success = True
    if  db.get_group_list() == 0:
        app.group.create(Groupe(name="group2", header="group2", footer="group2"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_groupe_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups


def test_delete_cirilic_groupe_02(app):
    success = True
    old_groups = app.group.get_group_list()
    try:
        app.group.delete_cirilic_groupe()
        return True
    except:
        app.group.return_to_groups_page()
        return False
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups




def test_delete_all_groupe_03(app):
    success = True
    old_groups = app.group.get_group_list()
    if not app.group.count() == 0:
        app.group.delete_all_groupe()
    else:
        app.group.return_to_groups_page()
    #new_groups = app.group.get_group_list()
    assert len(old_groups)-len(old_groups) == app.group.count()
