# Dictionary : It is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name' : 'Visakh',
    'last_name': 'Vijayan',
    'age':29,
    'phone':123456789
}

# Use Constructor
person2 = dict(first_name='Kavya',last_name='vinod')

#Get Value
print (person['first_name'])
print (person.get('last_name'))

# Add Key/Value
person['place'] = 'Trivandrum'

# Get Keys
print ('Keys : ',person.keys())
    
# Get Values/Items
print ('Values : ', person.items())

#Copyt dict
person3= person.copy();
person3['working_city']='Bangalore'

#Remove items
del(person3['age'])
person3.pop('phone')

person4 = person3.copy()
#Clear dictionary
person4.clear();

#Get length
print (len(person))
print (len(person2))
print (len(person3))
print (len(person4))

print (person)
print (person2)
print ('person 3',person3)
print ('person 4',person4)