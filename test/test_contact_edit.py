from model.contactfilld import Contactfilld
from random import randrange


def test_edit_first_contact(app):
    success = True
    if app.contacts.count() == 0:
        app.contacts.newcontact(
            Contactfilld(firstname="", middlename="", lastname="", nickename="", title="",
                         company="", address="", home="", mobile="", work="", fax="",
                         email1="", email2="", email3="", homepage="",
                         selectbday="0",
                         selectbmonthe="0", byear="", selectaday="0", selectamothe="0", ayear="",
                         address2="", phone2="", notes=""))
    old_groups_contact = app.contacts.get_contact_list()
    index = randrange(len(old_groups_contact))
    contact = Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                         company="Rose", address="ertyui", home="1234", mobile="5678", work="90123", fax="4567",
                         email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry",
                         selectbday="3",
                         selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000",
                         address2="dferesdfe", phone2="rererr", notes="fgwewerewrw")
    contact.id = old_groups_contact[index].id
    app.contacts.edit_contact_by_index(index,contact)
    assert len(old_groups_contact) == app.contacts.count()
    new_groups_contacts = app.contacts.get_contact_list()
    old_groups_contact[index] =contact
    assert sorted(old_groups_contact, key=Contactfilld.id_or_max) == sorted(new_groups_contacts, key=Contactfilld.id_or_max)


