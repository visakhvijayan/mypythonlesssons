# A module is a basically a file containing a set of funcitons to include in your application. There are core pythn modules, modules you can install using the pip package manager (including Django ) as well as custom modules.

# Core modules
from datetime import date
from time import time

#Pip modules
from camelcase import CamelCase

from validator import validate_email


today = date.today();
case = CamelCase()
print (case.hump('hello there world'))
print (today)
print (time())
print (validate_email('visakh@gmail.com'))
print (validate_email('visakh_gmail.com'))