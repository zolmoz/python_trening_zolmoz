# -*- coding: utf-8 -*-
import pytest
from model.groupe import Groupe
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_ad_group(app):
    success = True
    app.session.login(user_name="admin", password="secret")
    app.create_groupe( Groupe(name="group2", header="group2", footer="group2"))
    app.session.logout()

def test_test_ad_empty_group(app):
    success = True
    app.session.login( user_name="admin", password="secret")
    app.create_groupe(Groupe (name=" ", header=" ", footer=" "))
    app.session.logout()

