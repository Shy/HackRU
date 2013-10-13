import urllib2
import json

for x in range(1, 11):
    path = 'data/week' + str(x) + '.json'
    f = open(path,'w')
    zipcodes = [0]*11436
    urban = 'https://demo.urbancompass.com/api/public/neighborhoods/popular?json={%22aggregateBy%22:%22zipcode%22,%22weeksBack%22:%22'
    response = urllib2.urlopen(urban + str(x) + '%22}')
    data = response.read()
    hyperdata = json.loads(data)

    for k, v in hyperdata['response'].items():
        zip = int(k)
        val = int(v)
        zipcodes[zip] = val

    output = '{"specification": [{"id":"count","text":"Count","per-capita":false}],"data":{'
    for s in range(len(zipcodes)):
        if zipcodes[s] != 0:

            output += '"' + str(s) + '":{"count":' + str(zipcodes[s]) + "},"
    tout = output [:len(output)-1] + '}}'
    f.write(tout)
    f.close()
    print str(x) + " complete"
