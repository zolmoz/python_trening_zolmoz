from model.groupe import Groupe
from model.contactfilld import Contactfilld






def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Groupe(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Groupe.id_or_max) == sorted(db_list, key=Groupe.id_or_max)




 def test_contact_list(app, db):
    ui_list = app.contact.get_contacts_list() # список, загруженный через UI
    db_list = db.get_contact_list()  # список, загруженный через БД
    print("\nui_list", ui_list)
    print("\ndb_list", db_list)
    assert sorted(ui_list, key=Contactfilld.id_or_max) == sorted(db_list, key=Contactfilld.id_or_max)