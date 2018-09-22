# -*- coding: utf-8 -*-
from model.groupe import Groupe
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbol = string.ascii_letters+string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])



testdata = [Groupe(name="", header="", footer="")] + [Groupe(name="группа3", header="группа3", footer="группа3")]+ [
    Groupe(name=random_string("name", 10),
          header=random_string("header", 20),
          footer=random_string("footer", 20))
    for i in range(5)
   ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_test_ad_group(app, group):
    success = True
    pass
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups,key=Groupe.id_or_max) == sorted(new_groups, key=Groupe.id_or_max)





