from model.contactfilld import Contactfilld


def test_edit_first_emty_contact(app):
    success = True
    try:
        app.contacts.edit_first_contact(Contactfilld( firstname="Ray", middlename="Ray", lastname="Ray", nickename="Ray", title="Rosw Ray",ompany="Ray", address="Ray", home="1234", mobile="5678", work="90123", fax="4567",email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry", selectbday="3",selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000", address2="Ray", phone2="Ray", notes="Ray"))
        return True
    except:
        app.contacts.open_home_page()
        return False

