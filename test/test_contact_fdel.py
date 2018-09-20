from model.contactfilld import Contactfilld

def test_delete_first_contact_01(app):
    success = True
    if app.contacts.count() == 0:
        app.contacts.newcontact(
            Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                         company="Rose", address="ertyui", home="1234", mobile="5678", work="90123", fax="4567",
                         email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry",
                         selectbday="3",
                         selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000",
                         address2="dferesdfe", phone2="rererr", notes="fgwewerewrw"))
    old_groups_contact = app.contacts.get_contact_list()
    app.contacts.delete_first_contact()
    assert len(old_groups_contact) - 1 == app.contacts.count()
    new_groups_contacts = app.contacts.get_contact_list()
    old_groups_contact[0:1] = []
    assert old_groups_contact == new_groups_contacts


def test_delete_rose_contact_02(app):
    success = True
    old_groups_contact = app.contacts.get_contact_list()
    try:
        app.contacts.delete_Rose_contact()
        return True
    except:
        app.contacts.open_home_page()
        return False
    assert len(old_groups_contact) - 1 == app.contacts.count()
    new_groups_contacts = app.contacts.get_contact_list()
    old_groups_contact[0:1] = []
    assert old_groups_contact == new_groups_contacts


def test_delete_all_contact_03(app):
    success = True
    old_groups_contact = app.contacts.get_contact_list()
    if not app.contacts.count() == 0:
        app.contacts.delete_all_contact()
    else:
        app.contacts.open_home_page()
   # new_groups_contacts = app.contacts.get_contact_list()
    assert len(old_groups_contact) - len(old_groups_contact) == app.contacts.count()
