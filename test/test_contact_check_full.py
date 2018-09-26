from model.contactfilld import Contactfilld
import re
from random import randrange


def test_check_contact_between_home_page_edit_page(app,db,check_ui):
    contact = Contactfilld(firstname="Mia", middlename="Rk", lastname="Rose", nickename="Rose", title="Rosw comp",
                         company="Rose", address="ertyui", homephone="1234", mobilephone="5678", workphone="90123", fax="4567",
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
    index = randrange(app.contacts.count())
    print(str(index))
    contact_from_home_page = app.contacts.get_contact_list()[index] # информация о контакте с гл.страницы
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)#информация о контакте с edit page
    assert contact_from_home_page.lastname == clean(contact_from_edit_page.lastname)
    assert contact_from_home_page.firstname == clean(contact_from_edit_page.firstname)
    assert contact_from_home_page.address.strip() == merge_address_like_from_home_page(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_from_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_emails_like_from_home_page(contact_from_edit_page)
    if check_ui:
        assert sorted(new_groups, key=Groupe.id_or_max) == sorted(app.group.get_group_list(), key=Groupe.id_or_max)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # Сравнение телефонов объединенным куском с view page и объединенным куском с edit page
    assert merge_phones_like_from_home_page(contact_from_view_page) == merge_phones_like_from_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,[contact.email1, contact.email2, contact.email3])))


def merge_address_like_from_home_page(contact):
    contact = re.sub("\s{2,}", " ", contact)  # заменяем множественные пробелы (от 2х) на 1 пробел
    contact = contact.strip()  # убираем пробел в начале и в конце
    return contact

def clean(contact):
    contact = re.sub("\s{2,}", " ", contact)  # заменяем множественные пробелы (от 2х) на 1 пробел
    contact = contact.strip()  # убираем пробел в начале и в конце
    return contact

