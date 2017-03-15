import csv, requests
arr = []
with open('adr_lst.csv') as cs:
    rdr = csv.DictReader(cs)
    for row in rdr:
        st = row['street']
        hs = row['house']
        sear = {'macroRegionId': 107000000000, 'regionId': 107401000000, 'street': st, 'house':hs}
        r = requests.get('http://rosreestr.ru/api/online/address/fir_objects', params=sear)
        output = open("result.txt", "a")
        output.write(r.text)
        output.close()
        print('Seek for ' + st,hs)
