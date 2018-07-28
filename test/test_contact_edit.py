from model.contactfilld import Contactfilld

def test_edit_first_emty_contact(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.contactedit.edit_first_contact(Contactfilld( firstname="Ray", middlename="Ray", lastname="Ray", nickename="Ray", title="Rosw Ray",
                        company="Ray", address="Ray", home="1234", mobile="5678", work="90123", fax="4567",
                        email1="1admin@z.ru", email2="2admin@z.ru", email3="3admin@z.ru", homepage="ya.ry", selectbday="3",
                        selectbmonthe="4", byear="1989", selectaday="8", selectamothe="12", ayear="2000", address2="Ray", phone2="Ray", notes="Ray"))
    app.session.logout()

