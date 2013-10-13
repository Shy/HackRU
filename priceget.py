import urllib2
import json

f = open("data/price.json",'w')
zipcodes = [0]*11436
urban = 'https://gist.github.com/sjlu/032694a860ca1e07653f/raw/abc095d66bbfad61031253fc4638709fa7e53d10/average_prices_per_zipcode.json'
response = urllib2.urlopen(urban)
data = response.read()
hyperdata = json.loads(data)
output = '{"specification": [{"id": "0.5","text": "Studio","per-capita": false},{"id": "1.0","text": "One Bedroom","per-capita": false},{"id": "2.0","text": "Two Bedroom","per-capita": false},{"id": "3.0","text": "Three Bedroom","per-capita": false},{"id": "4.0","text": "Four Bedroom","per-capita": false},{"id": "5.0","text": "Five Bedroom","per-capita": false},{"id": "6.0","text": "Six Bedroom","per-capita": false},{"id": "7.0","text": "Seven Bedroom","per-capita": false},{"id": "8.0","text": "Eight Bedroom","per-capita": false},{"id": "10.0","text": "Ten Bedroom","per-capita": false} ],"data": {'

for k,v in hyperdata['response'].iteritems():
    temp = ""
    temp += '"' + str(k) + '": {'
    for s,r in v.iteritems():
        temp += '"'  + str(s) + '": ' + str(r) + ', '
    temp = temp[:len(temp)-2] + '},'
    output += temp

    # zip = int(k['zipcode'])
    # val = int(k['uniqueViews'])
    # zipcodes[zip] = val
output = output[:len(output)-1] + '}}'
print output



f.write(output)
f.close()
