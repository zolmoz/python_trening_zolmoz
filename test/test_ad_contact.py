# -*- coding: utf-8 -*-
from model.contactfilld import Contactfilld
import  pytest



def test_ad_contact_01(app, db, json_contact,check_ui):
    success = True
    contact = json_contact
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('when i add contact %s to the list' % contact):
        app.contacts.newcontact(contact)
    with pytest.allure.step('Then the new contact list is equal to the list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contactfilld.id_or_max) == sorted(new_contacts, key=Contactfilld.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contactfilld.id_or_max()) == sorted(app.contacts.get_contact_list(), key=Contactfilld.id_or_max())







