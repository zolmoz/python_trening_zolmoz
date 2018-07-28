
def test_delete_first_groupe(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.group.delete_first_groupe()
    app.session.logout()


def test_delete_all_groupe(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.group.delete_all_groupe()
    app.session.logout()