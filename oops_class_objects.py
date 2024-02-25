'''OOPS Concept
Classes are userdefined blueprint or prototype
For example if calculator is class then sum, add,mul,div are methods ie prototypes/operations
classes will have methods, class variables, instance variables,constructor etc
classes can be created by class keyword and class name
functions when used in class are called methods
So Methods and functions are same method is inside class and func is individual code'''
class calculator: # creating a class by name calcu and declaring variables and methods inside it
    num = 100 # creating class variable by name num and its value is 100
    def getdata(self): # creating a method called getdata where self is a keyword
        print("I am executing a getdata method of class calculator")
# To call any method of a class we have to call from outside of method and class with proper indentation by creating its object
obj=calculator() # creating object obj for the class calculator and assign to one variable with this object we can call any methods of that class
obj.getdata() # calling getdata method of class calculator using obj.
# We can also call variables of a class by its object
#obj.num
print("This is the value of a variable of class calculator ie",obj.num)


