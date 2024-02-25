'''Functions is a group/set of related statements that perform a specific task by declaring a function name
To call that function we can call by function name
In python to create a function we have to use def keyword/identifier
As there are no flower brackets/paranthesis unlike other codes we have to follow code indentation'''
#prog1 Defining a simple function with function name as greet
def greet(): # Here greet is function name and def is keyword/identifier to create a function with colon
    print("Good morning")# This line is a part of function
greet() # Calling function greet so that it will print the code inside the function and its indentation should be outside the function
# prog2 defining function and passing parameters inside function an calling that function
def hello(name):
    print("Hello" +name)
hello("Mohammed")
# prog3 to take sum of two integers
def addint(a,b):
    c=b/a
    print("sum of two integers is:",a+b)
    print("product of two integers is:",a*b)
    print("Division of two integers is:",c)
addint(2,4)
# prog to return the values in a function by using return keyword
def mul(d,e):
    return d*e
print("Multiplication of 2 no's is:",mul(3,5))



