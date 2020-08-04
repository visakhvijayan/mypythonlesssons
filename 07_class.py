# A class is like a blueprint for creating objects. An object has properties and methods associted with ut. Almost everything in python is an object

# Create Class
class User: 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting (self):
        return (f'My name is {self.name} and my age is {self.age} ') 
    
    def has_birthday(self):
        self.age += 1

# Init user object
visakh = User ('Visakh','viv@gmail.com',29)


#Extend class
class Customer(User):
    
    def __init__(self):
        self.balance = 0
        
    def set_balance(self, balance):
        self.balance = balance

print (type(visakh))
print (visakh.name)
print (visakh.email)
print (visakh.age)
print (visakh.greeting())
print (visakh.has_birthday())
print (visakh.greeting())

obj2  = Customer ()
obj2.set_balance(1000)
print (obj2.balance)



