# Summary:self keyword is mandatory for calling variable names into methods
#self is the first parameter of any method
#instance and class variables have different purpose ie instance variable is attach with the object and class variables are not attach to the object
#Constructor name should be init
#like other programing languages new keyword is not used to create object
''' prog on Instance variables by creating parameterised constructor by passing no's from object creation to
take sum of two no's of instance variable and adding with class variable by creating two different objects'''
class addition: # class by name addition is created
    x = 100 # class variable by name x is declared with it's value 100
    def __init__(self,a,b): # Constructor method is created using init keyword and arguments a,b excluding self to catch values at runtime
        self.firstnumber = a # declaring instance variable firstnumber with self. object keyword with value a ie initialising the values
        self.secondnumber = b # declaring instance variable secondnumber with self. object keyword with value b
        print("I am called automatically from constructor when objecct is created ")
    def getdata(self): # creating getdata method of class addition
        print("I am executing as a getdata method from class addition") # printing the message from getdata method
    def summation(self): # creating summation method of class addition and returning the sum of two no's
        return self.firstnumber + self.secondnumber + addition.x  # here we called instance variables with self keyword and class variables with class name.
        #or
        #return self.firstnumber + self.secondnumber +self.x  # here we can call class variable with self. keyword also
obj1 = addition(2,3) # creating first objectie obj1 for the class addition and passing arguements/parameters to constructor with self object
obj1.getdata() # calling getdata method of class addition using obj1.
print(obj1.summation())# printing and calling the summation method and return value using obj1.
print("This is from object1 of class addition:",obj1.summation())
obj2 = addition(4,5) # creating another object by name obj2 for the class addition and passing the parameters from there to constructor and instance variables
obj2.getdata() # calling getdata method of class addition using obj2.
print(obj2.summation()) # printing and calling the summation method and return value using obj2.
print("This is from object2 of class addition:",obj2.summation())