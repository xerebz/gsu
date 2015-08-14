import mechanize
from bs4 import BeautifulSoup

#for link in br.links(): print link
#for form in br.formss(): print form
#for control in br.form.controls: print control
br = mechanize.Browser()
br.open("")
#select form by name= or index(nr=)
br.select_form(name="loginform")
#select item(form) by name
br['sid']='PASS'
#submit selected form
br.submit()
#follow a link based on text= or url=
br.follow_link(text="Registration")
#set value of item by name, id, etc
br.form.set_value("12345",id="crn_id1")
#convert final response to soup
soup = BeautifulSoup(br.response().read())
#find, find_all, prettify
print soup.find('table', summary="This layout table is used to present Registration Errors.").prettify()
