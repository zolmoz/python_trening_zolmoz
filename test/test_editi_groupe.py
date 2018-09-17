from model.groupe import Groupe

def test_modefi_first_emty_groupe(app):
    success = True
    app.group.modefi_first_empty_groupe(Groupe(name="test222"))


def test_modefi_first_groupe(app):
    success = True
    app.group.modefi_first_groupe(Groupe(header="test"))


