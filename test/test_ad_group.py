# -*- coding: utf-8 -*-
from model.groupe import Groupe

def test_test_ad_group(app):
    success = True
    app.group.create(Groupe(name="group2", header="group2", footer="group2"))


def test_test_ad_notall_group(app):
    success = True
    app.group.create(Groupe(name="group", header="", footer=""))


def test_test_ad_kirilic_group(app):
    success = True
    app.group.create(Groupe(name="группа3", header="группа3", footer="группа3"))


def test_test_ad_empty_group(app):
    success = True
    app.group.create(Groupe (name=" ", header=" ", footer=" "))


