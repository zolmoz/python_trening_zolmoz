# -*- coding: utf-8 -*-
from model.contactfilld import Contactfilld



def test_ad_contact_01(app,json_contsct):
    success = True
    old_groups_contact = app.contacts.get_contact_list()
    app.contacts.newcontact(json_contsct)
    assert len(old_groups_contact) + 1 == app.contacts.count()
    new_groups_contacts = app.contacts.get_contact_list()
    old_groups_contact.append(json_contsct)
    assert sorted(old_groups_contact, key=Contactfilld.id_or_max) == sorted(new_groups_contacts, key=Contactfilld.id_or_max)



