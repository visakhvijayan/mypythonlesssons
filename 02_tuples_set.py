# Tuple :Tuple is a collection whihch is ordered and unchangable. Allows duplicate members

# Tuple creation
fruits_tuple = ('Banana','grapes','grapes')
fruits2 = tuple(('Apple','Ornages','grapes'))

# For Single element it is treated as string
fruits3 = ('Apple'), 

# For single elements the  trialing comma will make it as tuple format
fruits4 = ('Apple',) 

# List can change the values but th tuple can't change the values
# fruits_tuple[1]='Anar'

# Delete tuple, will completely delet the tuple
del fruits2
del fruits3
del fruits4


# Gettinglength
print (len(fruits_tuple))


# Set : It is a collection which is unordered and unindexed. No duplicate members.

# Create Set , It will automatically elimates duplicates
fruits_set ={'Apple','Grapes','Grapes'}
fruits_set1 ={'Apple','Grapes','Grapes'}

# Add to set
fruits_set.add('Anar')
fruits_set.add('Water melon')

# Add duplicates
fruits_set.add('Apple')

# Remove from set
fruits_set.remove('Grapes')

# Clear the content from the set
fruits_set.clear();

#Delete fruit
del fruits_set1

print (fruits_set) 
print (len (fruits_set)) 
