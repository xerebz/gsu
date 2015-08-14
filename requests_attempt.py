import requests

#r = requests.get("https://www.gosolar.gsu.edu/bprod/twbkwbis.P_WWWLogin", verify=False)
params = { 'PIN': 'PASS' , 'sid':'USER' }
cookie = { 'TESTID': 'SET' , 'WDB_GATEWAY_LOGOUT':'YES' }
login = requests.post("https://www.gosolar.gsu.edu/bprod/twbkwbis.P_ValLogin", data=params, cookies=cookie, verify=False)
register = requests.post("https://www.gosolar.gsu.edu/bprod/bwckcoms.P_Regs",cookies=login.cookies, verify=False)
print login.cookies
print register.cookies
print register.text
