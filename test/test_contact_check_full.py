import re
from model.contactfilld import Contactfilld


def test_contact_on_home_page(app,orm):
    if len(orm.get_contact_list()) == 0:
        app.contacts.newcontact(
             Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                         company="Rose", address="ertyui", homephone="1234", mobilephone="5678", workphone="90123",
                         fax="4567",
                         email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry",
                         selectbday="3",
                         selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000",
                         address2="dferesdfe", secondaryphone="rererr", notes="fgwewerewrw"))
    contact_from_home_page = app.contacts.get_contact_list()
    contact_db = orm.get_contact_list()
    assert sorted(contact_from_home_page, key = Contactfilld.id_or_max) == sorted(contact_db, key = Contactfilld.id_or_max)
    for contact_from_home_page in contact_from_home_page:
        contact_db = list(filter(lambda x: x.id == contact_from_home_page.id, clean(contact_db)))[0]
        assert contact_from_home_page.address == clean(contact_db.address)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)
        assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_db)


def clear(s):
   return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
   return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x),
                               filter(lambda  x: x is not  None,
                                                    [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_home_page(contact):
   return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                    [contact.email1, contact.email2, contact.email3]))))


def clean(contact):
    contact = re.sub("\s{2,}", " ", contact)
    contact = contact.strip()
    return contact
