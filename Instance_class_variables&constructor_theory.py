'''The variables declared inside class are class variables and
the variables which are declared inside constructor are caled instance variabes
Class varibles are constant irrespective of no of objects created for that class ie we can create n no of objects for class'''
# Class variables are independent of objects we have to call by its class name(class.variable or self.variable name) where as instance variables should always call with self. keyword
# Instance variables differs from each and every object ie for each and every object created variables will differ
# To send parameters from object to class  to perform sum of two no's at run time by passing parameters
# while passing parameters or arguments from object to class it will first reach to constructor and constructor should have
# while sending parameters from object it should be catch in constructor by giving paramer
#**If N no of arguments sending in class from object those many n parameters should be present in constructor decleration excluding self keyword
# self keyword is by default in constructor once the constructor catchs the arguments pass by the object will be stored in instance variables by self.
# Initially when object is created for the class that object is attached with self so self is an object and the parameters will be stored in instance variables using self object
# For instance variables we can load values at runtime in object decleration using self keyword inside constructor
#**Instance variables values are keep on changing for every new object creation but class variables values are constant for every new objects
# In python we can't call instance/class variables simply with its name always we have to always attach with self. because self is object referrence ie which object is calling the variable
#self is object referrence who is calling you
# when we create object (obj) with parameters at first it  will first pass parmaters  to constructor self object and it will store in memory so we have to always declare as self.variables
#** class variables can be called using classname.variable name or self.variable name as it is class variable
# self. is used for calling instance variables and classname./self. can be used for calling class variables
# Summary:self keyword is mandatory for calling variable names into methods
#instance and class variables have different purpose ie instance variable is attach with the object and class variables are not attach to the object
#Constructor name should be init
#like other programing languages new keyword is not used to create object

