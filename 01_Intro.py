# Run python3  using command
#  python3 <filename>
# Variabl declarartion
name = 1
age= 2.5

house,place,salary = 1,'trivandrum',1.52

# Different variable printing
print ('Hello World',name,age);
print ('Test 2')
print (house,place,salary)
print (type(house))
print (f'Hello {house} {place} {salary}')

# List
fruits = ['Apple','Orange','Pineapple']

#Add new element
fruits.append('Jackfruit')


# Remove particular element
fruits.remove('Orange');


# Insert at particular positiom
fruits.insert(0,'Orange')
fruits.insert(-1,'Red Apple')
fruits.insert(-8,'Green Apple')
fruits.insert(10,'Kashmir Apple')

# Remove with Pop
fruits.pop()

# Pop with particular position
fruits.pop(2)

# Sorting and reverse sorting
fruits.sort()
fruits.sort(reverse= True)

print (fruits) 