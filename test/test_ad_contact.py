# -*- coding: utf-8 -*-
from model.contactfilld import Contactfilld

def test_ad_contact_01(app):
    success = True
    old_groups_contact = app.contacts.get_contact_list()
    contact = Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                        company="Rose", address="ertyui", homephone="1234", mobilephone="5678", workphone="90123", fax="4567",
                        email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry", selectbday="3",
                        selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000", address2="dferesdfe", secondaryphone="878787", notes="fgwewerewrw")
    app.contacts.newcontact(contact)
    assert len(old_groups_contact) + 1 == app.contacts.count()
    new_groups_contacts = app.contacts.get_contact_list()
    old_groups_contact.append(contact)
    assert sorted(old_groups_contact, key=Contactfilld.id_or_max) == sorted(new_groups_contacts, key=Contactfilld.id_or_max)




def test_ad_contact_02_empty(app):
    success = True
    old_groups_contact = app.contacts.get_contact_list()
    contact = Contactfilld(firstname="", middlename="", lastname="", nickename="",
                                             title="",
                                             company="", address="", homephone="", mobilephone="", workphone="",
                                             fax="",
                                             email1="", email2="", email3="",
                                             homepage="", selectbday="0",
                                             selectbmonthe="0", byear="", selectaday="0", selectamothe="0",
                                             ayear="", address2="", secondaryphone="", notes="")
    app.contacts.newcontact(contact)
    assert len(old_groups_contact) + 1 == app.contacts.count()
    new_groups_contacts = app.contacts.get_contact_list()
    old_groups_contact.append(contact)
    assert sorted(old_groups_contact, key=Contactfilld.id_or_max) == sorted(new_groups_contacts,key=Contactfilld.id_or_max)


def test_ad_contact_03_notall(app):
    old_groups_contact = app.contacts.get_contact_list()
    contact = Contactfilld(firstname="Kira", middlename="", lastname="", nickename="zzzz",
                                             title="",
                                             company="", address="dfsfdsfsdf", homephone="", mobilephone="", workphone="",
                                             fax="7854784",
                                             email1="", email2="a@z.ty", email3="",
                                             homepage="", selectbday="0",
                                             selectbmonthe="8", byear="", selectaday="18", selectamothe="0",
                                             ayear="", address2="", secondaryphone="788858", notes="")
    app.contacts.newcontact(contact)
    assert len(old_groups_contact) + 1 == app.contacts.count()
    new_groups_contacts = app.contacts.get_contact_list()
    old_groups_contact.append(contact)
    assert sorted(old_groups_contact, key=Contactfilld.id_or_max) == sorted(new_groups_contacts,
    key = Contactfilld.id_or_max)
