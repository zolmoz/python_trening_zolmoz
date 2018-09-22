from model.contactfilld import Contactfilld
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f ="data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix,maxlen):
    symbol = string.ascii_letters+string.digits + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

def random_numbers(prefix,maxlen):
    symbol = string.digits + " "*2
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

testdata = [Contactfilld(firstname="Mia",
                          middlename="Rk",
                          lastname="Rose",
                          nickename="Rose",
                          title="Rosw comp",
                          company="Rose",
                          address="ertyui",
                          homephone="1234",
                          mobilephone="5678",
                          workphone="90123",
                          fax="4567",
                          email1="1admin@z.ru",
                          email2="2admin@z.ru",
                          email3="3admin@z.ru",
                          homepage="ya.ry",
                          secondaryphone="878787",
                          notes="fgwewere")] + [
              Contactfilld(firstname=random_string("firstname", 10),
                         middlename=random_string("middlename", 12),
                         lastname=random_string("lastname", 14),
                         nickename=random_string("nickename", 15),
                         title=random_string("title", 10),
                         address = random_string("address", 10),
                         company=random_string("company", 20),
                         homephone=random_numbers("+",9),
                         mobilephone=random_numbers("+",9),
                         workphone=random_numbers("+",9),
                         fax=random_numbers("+",9),
                         email1=random_string("email1", 10),
                         email2=random_string("email2", 10),
                         email3=random_string("email3", 10),
                         homepage=random_string("homepage", 10),
                         secondaryphone=random_numbers("+",9),
                         notes=random_string("notese", 14)

                 )
    for i in range(n)
   ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))