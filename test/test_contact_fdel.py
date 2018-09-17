def test_delete_first_contact_01(app):
    success = True
    app.contacts.delete_first_contact()


def test_delete_rose_contact_02(app):
    success = True
    app.contacts.delete_Rose_contact()



def test_delete_all_contact_03(app):
    success = True
    app.contacts.delete_all_contact()
