from model.contactfilld import Contactfilld
import re



def clear(s):
    return re.sub("[() -]", "", s)

def test_contact_on_home_page(app, db):
    contact = Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                           company="Rose", address="ertyui", homephone="1234", mobilephone="5678", workphone="90123",
                           fax="4567",
                           email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry",
                           selectbday="3",
                           selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000",
                           address2="dferesdfe", secondaryphone="rererr", notes="fgwewerewrw")

    if db.get_contact_list2() == 0:
        app.contacts.newcontact(contact)
    contacts_from_home_page = app.contacts.get_contact_list()[0]
    contacts_from_db = db.get_contact_list2()[0]
    assert contacts_from_home_page.firstname == contacts_from_db.firstname
    assert contacts_from_home_page.lastname == contacts_from_db.lastname
    assert contacts_from_home_page.address == contacts_from_db.address
    assert contacts_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db )
    assert contacts_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contacts_from_db )
    assert sorted(contacts_from_home_page,key=Contactfilld.id_or_max) == sorted(contacts_from_db, key=Contactfilld.id_or_max)



def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda  x: x is not  None,
                                                          [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))

def clean(contact):
    contact = re.sub("\s{2,}", " ", contact)  # заменяем множественные пробелы (от 2х) на 1 пробел
    contact = contact.strip()  # убираем пробел в начале и в конце
    return contact

