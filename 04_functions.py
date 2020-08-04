# function

# Create function

def sayHello(name ='default name'):
    print (f'hello {name}')

# Return values
def getSum (num1, num2):
    return num1+num2


# Function call
sayHello('Visakh')
print (getSum(4,10))

# lambda function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow function.

getSum = lambda num1,num2 : num1+ num2

print (getSum(1,2))