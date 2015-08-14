#
# register.py
# alain leon - 1/14/14
#
# signs up for a Georgia State University course by navigating
# through its registration website at GoSOLAR.gsu.edu
#
# input - username, password, registration numbers (CRNs)
# output - webpage containing new schedule or any errors
#

from __future__ import print_function
from mechanize import Browser

user='USER'
password='PASS'
crns=['12345','12346']

#start at login page
br = Browser()
br.open("https://www.gosolar.gsu.edu/bprod/twbkwbis.P_WWWLogin")
#login
br.select_form(name="loginform")
br['sid']=user
br['PIN']=password
br.submit()
#enter registration menu
br.follow_link(text="Registration")
#go to add classes page
br.follow_link(text="Add/Drop/Withdraw Classes")
#select default semester (e.g. Fall, Spring)
br.select_form(nr=1)
br.submit()
#enter CRNs and attempt to register
br.select_form(nr=1)
for index, crn in enumerate(crns,start=1):
	br.form.set_value(crn,id="crn_id"+str(index))
br.submit()
#write resulting page to file
response = open("response.html","w")
print (br.response().read(),file=response)
