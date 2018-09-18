from sys import maxsize

class Contactfilld:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickename=None, title=None, company=None, address=None, home=None, mobile=None, work=None,
                   fax=None, email1=None, email2=None, email3=None, homepage=None, selectbday=None, selectbmonthe=None, byear=None, selectaday=None,
                 selectamothe=None, ayear=None, address2=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickename = nickename
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.selectbday = selectbday
        self.selectbmonthe = selectbmonthe
        self.byear = byear
        self.selectaday = selectaday
        self.selectamothe = selectamothe
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id


    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)



    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize