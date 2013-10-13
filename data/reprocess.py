import sys
import json

zipcodes = [0]*11436
f = open('dataset.json', 'r')
data = f.read()
hyperdata = json.loads(data)

for x in hyperdata['response']:
    temp =  x['zipCode']
    zipcodes[int(temp)] += 1
output = '{"specification": [{"id":"google","text":"Google","per-capita":false}],"data":{'
for x in range(len(zipcodes)):
    if zipcodes[x] != 0:

        output += '"' + str(x) + '":{"google":' + str(zipcodes[x]) + "},"
tout = output [:len(output)-1] + '}}'
print tout
