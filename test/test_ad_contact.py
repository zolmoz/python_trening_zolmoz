# -*- coding: utf-8 -*-
from model.contactfilld import Contactfilld

def test_ad_contact_01(app):
    success = True
    app.contacts.newcontact(Contactfilld( firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                        company="Rose", address="ertyui", home="1234", mobile="5678", work="90123", fax="4567",
                        email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry", selectbday="3",
                        selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000", address2="dferesdfe", phone2="rererr", notes="fgwewerewrw"))


def test_ad_contact_02_empty(app):
    success = True
    app.contacts.newcontact(Contactfilld(firstname=" ", middlename=" ", lastname=" ", nickename=" ",
                                             title=" ",
                                             company=" ", address=" ", home=" ", mobile=" ", work=" ",
                                             fax=" ",
                                             email1=" ", email2=" ", email3=" ",
                                             homepage=" ", selectbday="0",
                                             selectbmonthe="0", byear=" ", selectaday="0", selectamothe="0",
                                             ayear=" ", address2=" ", phone2=" ", notes=" "))


def test_ad_contact_03_notall(app):
    success = True
    app.contacts.newcontact(Contactfilld(firstname="Kira", middlename=" ", lastname=" ", nickename="zzzz",
                                             title=" ",
                                             company=" ", address="dfsfdsfsdf", home=" ", mobile=" ", work=" ",
                                             fax="7854784",
                                             email1=" ", email2="a@z.ty", email3=" ",
                                             homepage=" ", selectbday="0",
                                             selectbmonthe="8", byear=" ", selectaday="18", selectamothe="0",
                                             ayear=" ", address2=" ", phone2="788858", notes=" "))
