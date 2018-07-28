from model.groupe import Groupe

def test_modefi_first_groupe(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.group.modefi_first_groupe(Groupe(name="test", header="test", footer="test"))
    app.session.logout()