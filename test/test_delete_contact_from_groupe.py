import random
from model.contactfilld import Contactfilld
from model.groupe import Groupe


def test_delete_contact_from_group(app, db, orm):

    groups = orm.get_groups_with_contacts()

    if len(groups) == 0:
        if len(db.get_group_list())==0:
            app.group.create(Groupe(name="n1", header="h1", footer="f1"))
        if (len(db.get_contact_list())==0):
            app.contacts.newcontact(
                Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                             company="Rose", address="ertyui", homephone="1234", mobilephone="5678", workphone="90123",
                             fax="4567",
                             email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry",
                             selectbday="3",
                             selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000",
                             address2="dferesdfe", secondaryphone="rererr", notes="fgwewerewrw"))

        groups = db.get_group_list()
        group = random.choice(groups)
        contacts = orm.get_contacts_not_in_group(group)
        contact = random.choice(contacts)
        app.contact.add_contact_to_group(contact, group)
        groups = orm.get_groups_with_contacts()

    group = random.choice(groups)
    contacts = orm.get_contacts_in_group(group)
    contact=random.choice(contacts)
    app.contact.remove_contact_from_group(contact, group)

    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact not in contacts_in_group, "Contact id=%s не удален из id=%s" % (contact.id, group.id)