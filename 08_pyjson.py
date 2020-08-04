import json

userJSON = '{"name":"Visakh", "lastname":"viajayan","age":29}'

# parse to dict
userDict = json.loads(userJSON)

print (userDict['name'])

car = {'mkae':'Ford', 'Model':'Mustang','Year':1970}

carJSON = json.dumps(car)

print (carJSON)