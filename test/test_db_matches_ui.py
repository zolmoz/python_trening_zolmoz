from model.groupe import Groupe


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Groupe(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Groupe.id_or_max) == sorted(db_list, key=Groupe.id_or_max)




