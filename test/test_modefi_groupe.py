def test_delete_first_groupe(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.group.modefi_groupe()
    app.session.logout()