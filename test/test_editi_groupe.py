from model.groupe import Groupe

def test_modefi_first_emty_groupe(app):
    success = True
    try:
        app.group.modefi_first_empty_groupe(Groupe(name="test222"))
        return True
    except:
        app.group.return_to_groups_page()
        return False



def test_modefi_first_groupe(app):
    success = True
    if app.group.count() == 0:
        app.group.create(Groupe(name="efsef", header="sfd", footer="adwd"))
    app.group.modefi_first_groupe(Groupe(header="test"))


