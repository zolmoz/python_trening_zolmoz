from model.groupe import Groupe

#def test_modefi_first_emty_groupe(app):
 #   success = True
  #  old_groups = app.group.get_group_list()
  #  try:
  #      app.group.modefi_first_empty_groupe(Groupe(name="test222"))
  #      return True
  # except:
  #      app.group.return_to_groups_page()
   #     return False
   # new_groups = app.group.get_group_list()
  #  assert len(old_groups) == len(new_groups)



def test_modefi_first_groupe(app):
    success = True
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Groupe(name="efsef", header="sfd", footer="adwd"))
    group = Groupe(header="test")
    group.id=old_groups[0].id
    app.group.modefi_first_groupe(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] =group
    assert sorted(old_groups, key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)


