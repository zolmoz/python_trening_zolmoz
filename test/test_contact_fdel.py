def test_delete_first_contact_01(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.contacts.delete_first_contact()
    app.session.logout()

def test_delete_rose_contact_02(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.contacts.delete_Rose_contact()
    app.session.logout()


def test_delete_all_contact_03(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.contacts.delete_all_contact()
    app.session.logout()