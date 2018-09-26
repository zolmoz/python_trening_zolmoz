from model.contactfilld import Contactfilld
import random



def test_edit_first_contact(app,db,check_ui):
    success = True
    contact = Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                           company="Rose", address="ertyui", homephone="1234", mobilephone="5678", workphone="90123",
                           fax="4567",
                           email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry",
                           selectbday="3",
                           selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000",
                           address2="dferesdfe", secondaryphone="rererr", notes="fgwewerewrw")
    if db.get_contact_list() == 0:
        app.contacts.newcontact(contact)
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact.id = old_contact.id
    app.contacts.edit_contact_by_id(old_contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(old_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contactfilld.id_or_max) == sorted(new_contacts, key=Contactfilld.id_or_max)
    if check_ui:
       assert sorted(new_contacts, key=Contactfilld.id_or_max()) == sorted(app.contacts.get_contact_list(), key=Contactfilld.id_or_max())




