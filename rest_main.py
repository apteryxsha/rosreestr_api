import requests, json
ins = open("intext.txt","r")
for line in ins:
    sear = {'macroRegionId':107000000000,'regionId':107401000000, 'street':line}
    r = requests.get('http://rosreestr.ru/api/online/address/fir_objects', params=sear)
    output = open("result.txt","a")
    output.write(r.text)
    output.close()


