'''To understand self keyword of class we have to know about constructor
Constructor is also one method which is automatically called when we create an object for a class'''
# Here we learnt how to call methods variables and constructors
#if we don't define any object then default constructor will be called outside of the class by creating an object
# Even if we don't create constructor in claass at runtime automatically it will create and wil attach to the class
#init is a keyword to declare constructors in python but in other programmings constructor is declared using class
# In other programming languages constructor name should be same as class name but in python constructor name should always be init
# Prog to call default constructor once a class object is created
class calc:
    y = "This is class variable" # Declaring class variable y with value as string
    #Declaring default constructor
    def __init__(self): # This constructor is not called anywhere outside of class it is automatically called when object is created
        print("I am called first automatically when object is created") # This message is displaye dfirst before other methods
    def getdata(self): # Declaring getdata method inside class
        print("I am executing second from getdata method of class calc")
obj =calc() # Creating object for class calc
obj.getdata() # calling getdata method of class calc
print(obj.y) # Calling class variable y of class calc
''' Variables which are declared inside class are called class variables
Variables which are declared inside constructor are called instance variables'''
