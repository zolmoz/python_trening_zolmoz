from model.groupe import Groupe
import random


def test_modefi_some_groupe(app,db,check_ui):
    success = True
    group = Groupe(name="efsef", header="sfd", footer="adwd")
    if db.get_group_list() == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    group.id = old_group.id
    app.group.modefi_groupe_by_id(old_group.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(old_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Groupe.id_or_max) == sorted(app.group.get_group_list(), key=Groupe.id_or_max)








