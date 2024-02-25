'''Inheritance is nothing but aquring properties of parent class in child class
It means a child class can have access to call the properties like variables and methods of parent/base class without creating an object in child class
This concept is useful while creating automation scripts '''
# Prog to inherit the parent class methods like getdata and summation from parent class addition of (Instance_class_variables_constructor.py) in to this file.
from Instance_class_variables_constructor import addition  # as there are two files of same class name addition we have to import from particular parent class
# The above is how to import other classes or files in python so that we can use those methods without creating objects again for the class
class child(addition): # this is syntax for inheriting parent class (addition) properties in to child class (childaddition)
    y = 200 # creating a class variable with value 200
    def __init__(self): # Defining/invoking  a constructor of child class if it is not default means if there is code present
        addition.__init__(self, 2, 10) # invoking child constructor by connecting parent class constructor in child class with parameters

    def getcompletedata(self): # Here in below code sum is (200+100+2+10+100=412)
        return self.y + self.x +self.summation() # returning to the value of class variable y with self.y/classname.y and adding with parent class variable x value  and method summation result which is inherited here

# Here summation() of parent class is the addition of a+b+x value of addition class ie 2+10+100
childobj=child() # creating object for childclass to call the method present in that ie getcomplete data
print(childobj.getcompletedata()) # Here calling the getcompleteddata method with the object. and printing
# To run the program error free we have to invoke the parent class constructor in to child class so that it will accept the values of a and for sumation method.
#In inheritance concept If the constructor of parent class is not default means if there is any code present in the constructor then it is complusory to define that parent constructor in child class
# while inheriting parent class in child class check for the parent constructor if the parent constructor is not default (ie it has some code written in parent constructor)
# if there is any code written then we have to inherit the constructor in child class also by connecting with parent class name
'''Note:For constructors there will be no object cereations it will automatically executed once object for class is created
There are 3 points to keep in mind while working with inheritance concept
 1)importing the parent class name from file where the parent class is created
 2)placing the parent class name inside child class name
 3) If the parent constructor is not default means if there is any code inside parent constructor then in child constructor first we have to call the parent constructor'''






