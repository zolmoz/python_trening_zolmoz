import random
from model.contactfilld import Contactfilld
from model.groupe import Groupe


def test_add_contact_to_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Groupe(name="n1", header="h1", footer="f1"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(group)
    if len(contacts) == 0:
        app.contacts.newcontact(
            Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                         company="Rose", address="ertyui", homephone="1234", mobilephone="5678", workphone="90123",
                         fax="4567",
                         email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry",
                         selectbday="3",
                         selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000",
                         address2="dferesdfe", secondaryphone="rererr", notes="fgwewerewrw"))
        contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contacts.add_contact_to_group(contact, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group, "Contact id=%s не добавлен id=%s" % (contact.id, group.id)

