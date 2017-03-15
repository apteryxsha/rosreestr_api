import requests
r = requests.get('http://rosreestr.ru/api/online/regions/107000000000')

print (r.text)