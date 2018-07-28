# -*- coding: utf-8 -*-
from model.groupe import Groupe

def test_test_ad_group(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.group.create(Groupe(name="group2", header="group2", footer="group2"))
    app.session.logout()

def test_test_ad_empty_group(app):
    success = True
    app.session.login( user_name="admin", password="secret")
    app.group.create(Groupe (name=" ", header=" ", footer=" "))
    app.session.logout()

