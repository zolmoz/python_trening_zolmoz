from sys import maxsize

class Contactfilld:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickename=None, title=None, company=None, address=None,
                 homephone=None, mobilephone=None, workphone=None,
                   fax=None, email1=None, email2=None, email3=None, homepage=None, selectbday=None, selectbmonthe=None, byear=None, selectaday=None,
                 selectamothe=None, ayear=None, address2=None, secondaryphone=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickename = nickename
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
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
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.homephone,self.mobilephone, self.workphone,self.secondaryphone)



    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)\
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.homephone is None or other.homephone is None or self.homephone == other.homephone) \
               and (self.mobilephone is None or other.mobilephone is None or self.mobilephone == other.mobilephone) \
               and (self.workphone is None or other.workphone is None or self.workphone == other.workphone) \
               and (self.secondaryphone is None or other.secondaryphone is None or self.secondaryphone == other.secondaryphone) \








    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize