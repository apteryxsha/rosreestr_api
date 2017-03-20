import requests

url = ('https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn')
page = requests.get(url)
html = page.text
print(html)