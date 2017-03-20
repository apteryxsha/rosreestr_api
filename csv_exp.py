import csv, requests, json
arr = []
rw = 0
with open('adr_tst.csv') as cs:
    rdr = csv.DictReader(cs)
    for row in rdr:
        st = row['street']
        hs = row['house']
        sear = {'macroRegionId': 107000000000, 'regionId': 107401000000, 'street': st, 'house':hs}
        r = requests.get('http://rosreestr.ru/api/online/address/fir_objects', params=sear)
        output = open("result.txt", "a")
        output.write(r.text)
        output.close()
        rw = rw + 1
        print('Seek for ' + st,hs)
        print(r.text)
        js_pars = json.loads(r.text)
        rjs = js_pars['objectId']
        js_out = open('js_out.csv','w')
        csvwriter = csv.write(js_out)
        for jsd in rjs:
            if count == 0:
                header = jsd.keys()
                csvwriter.writerow(header)
                count+=1
            csvwriter.writerow(jsd.values())
        js_out.close()
print(rw)