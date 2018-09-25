# -*- coding: utf-8 -*-
from model.contactfilld import Contactfilld



def test_ad_contact_01(app, db, json_contact,check_ui):
    success = True
    contact = json_contact
    old_contacts = db.get_contact_list()
    app.contacts.newcontact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contactfilld.id_or_max) == sorted(new_contacts, key=Contactfilld.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contactfilld.id_or_max()) == sorted(app.contacts.get_contact_list(), key=Contactfilld.id_or_max())







