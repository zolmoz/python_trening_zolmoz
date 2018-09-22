from sys import maxsize

class Contactfilld:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickename=None, title=None, company=None, address=None,
                 homephone=None, mobilephone=None, workphone=None,
                   fax=None, email1=None, email2=None, email3=None, homepage=None, selectbday=None, selectbmonthe=None, byear=None, selectaday=None,
                 selectamothe=None, ayear=None, address2=None, secondaryphone=None, notes=None, id=None,all_phones_from_home_page=None):
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
        self.all_phones_from_home_page = all_phones_from_home_page


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,self.all_phones_from_home_page)



    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)\
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.all_phones_from_home_page is None or other.all_phones_from_home_page is None or self.all_phones_from_home_page == other.all_phones_from_home_page)



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize