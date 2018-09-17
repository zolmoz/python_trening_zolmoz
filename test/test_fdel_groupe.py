
def test_delete_first_groupe_01(app):
    success = True
    app.group.delete_first_groupe()


def test_delete_cirilic_groupe_02(app):
    success = True
    app.group.delete_cirilic_groupe()



def test_delete_all_groupe_03(app):
    success = True
    app.group.delete_all_groupe()
