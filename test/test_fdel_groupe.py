
def test_delete_first_groupe_01(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.group.delete_first_groupe()
    app.session.logout()

def test_delete_cirilic_groupe_02(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.group.delete_cirilic_groupe()
    app.session.logout()


def test_delete_all_groupe_03(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.group.delete_all_groupe()
    app.session.logout()