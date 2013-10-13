import urllib2
import json

f = open("data/trending.json",'w')
zipcodes = [0]*11436
urban = 'https://gist.github.com/sjlu/ceb958db3e09081fb9bc/raw/7c708c95fcc1966858bb07405b93338584de1728/trending_neighborhoods.json'
response = urllib2.urlopen(urban)
data = response.read()
hyperdata = json.loads(data)

for k in hyperdata['response']:
    zip = int(k['zipcode'])
    val = int(k['uniqueViews'])
    zipcodes[zip] = val

output = '{"specification": [{"id":"count","text":"Count","per-capita":false}],"data":{'
for s in range(len(zipcodes)):
    if zipcodes[s] != 0:

        output += '"' + str(s) + '":{"count":' + str(zipcodes[s]) + "},"
tout = output [:len(output)-1] + '}}'
print tout
f.write(tout)
f.close()
