#prog To print integer and string together like to concatinate string and variable value
#Like example print("the value is:"+b)
b, c, d, e =5, 10.5, "great", (2+3j)
print("Value of b is:", b) #Method 1
#or method2
print("{} {}".format("Value of c is:", c))
print("{} {}".format("Value of d is:", d))
print("The return type of b is:",type(b))
print("The return type of c is:",c, type(c))
print("The datatype of e is:",e, type(e))
#Concatination of two same datatypes is possible in python but with 2 different datatypes is not
f="This is"
g='Mohammed'
print(f,"concatinate with",g)
print(f + "concatinate again with" + g)
