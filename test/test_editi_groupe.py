from model.groupe import Groupe

def test_modefi_first_emty_groupe(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.groupeedit.modefi_first_empty_groupe(Groupe(name="test222", header="test222", footer="test222"))
    app.session.logout()

def test_modefi_first_groupe(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.groupeedit.modefi_first_groupe(Groupe(name="test", header="test", footer="test"))
    app.session.logout()

