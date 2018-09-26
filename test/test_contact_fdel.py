from model.contactfilld import Contactfilld
import random

def test_delete_some_contact_01(app,db,check_ui):
    contacts = Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                         company="Rose", address="ertyui", homephone="1234", mobilephone="5678", workphone="90123", fax="4567",
                         email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry",
                         selectbday="3",
                         selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000",
                         address2="dferesdfe", secondaryphone="rererr", notes="fgwewerewrw")
    success = True
    if db.get_contact_list() == 0:
        app.contacts.newcontact(contacts)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(db.get_contact_list())
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contactfilld.id_or_max()) == sorted(app.contacts.get_contact_list(),
                                                                            key=Contactfilld.id_or_max())


def test_delete_rose_contact_02(app,db,check_ui):
    success = True
    old_groups_contact = db.get_contact_list()
    try:
        app.contacts.delete_Rose_contact()
        return True
    except:
        app.contacts.open_home_page()
        return False
    assert len(old_groups_contact) - 1 == app.contacts.count()
    new_groups_contacts = db.get_contact_list()
    old_groups_contact[0:1] = []
    assert old_groups_contact == new_groups_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contactfilld.id_or_max()) == sorted(app.contacts.get_contact_list(),
                                                                            key=Contactfilld.id_or_max())


def test_delete_all_contact_03(app,db,check_ui):
    success = True
    old_groups_contact = db.get_contact_list()
    if not db.get_contact_list() == 0:
        app.contacts.delete_all_contact()
    else:
        app.contacts.open_home_page()
    assert len(old_groups_contact) - len(old_groups_contact) == app.contacts.count()
    new_contacts = db.get_group_list()
    if check_ui:
        assert sorted(new_contacts, key=Contactfilld.id_or_max()) == sorted(app.contacts.get_contact_list(),
                                                                            key=Contactfilld.id_or_max())
