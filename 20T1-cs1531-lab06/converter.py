import json
import yaml
#json to yml
data = open('data_1.json', 'r')
jdata = json.load(data)
data.close()

yml = open('data_1.yml', 'w+')
ymlData = {'channels' : ''}
ymlData['channels'] = jdata['channels']
yaml.dump(ymlData, yml)
#yml to json
data2 = open('data_2.yml', 'r')
ydata = yaml.load(data2)
data2.close()

with open('data_2.json', 'w') as FILE:
    json.dump(ydata, FILE)

