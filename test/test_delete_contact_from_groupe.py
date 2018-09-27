import random
from test import test_ad_contact_to_groupe


def test_delete_contact_from_group(app, db, orm):
    groups = orm.get_groups_with_contacts()
    if len(groups) == 0:
        test_ad_contact_to_groupe.test_add_contact_to_group(app, db, orm)
    group = random.choice(groups)
    contacts = orm.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contacts.remove_contact_from_group(contact, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact not in contacts_in_group, "Contact id=%s не удален из id=%s" % (contact.id, group.id)