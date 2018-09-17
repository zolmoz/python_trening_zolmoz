from model.groupe import Groupe


def test_delete_first_groupe_01(app):
    success = True
    if app.group.count() == 0:
        app.group.create(Groupe(name="group2", header="group2", footer="group2"))
    app.group.delete_first_groupe()


def test_delete_cirilic_groupe_02(app):
    success = True
    try:
        app.group.delete_cirilic_groupe()
        return True
    except:
        app.group.return_to_groups_page()
        return False



def test_delete_all_groupe_03(app):
    success = True
    if not app.group.count() == 0:
        app.group.delete_all_groupe()
    else:
        app.group.return_to_groups_page()