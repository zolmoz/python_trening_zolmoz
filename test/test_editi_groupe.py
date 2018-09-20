from model.groupe import Groupe
from random import randrange


def test_modefi_some_groupe(app):
    success = True

    if app.group.count() == 0:
        app.group.create(Groupe(name="efsef", header="sfd", footer="adwd"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Groupe(header="test")
    group.id=old_groups[index].id
    app.group.modefi_groupe_by_index(index,group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] =group
    assert sorted(old_groups, key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)


