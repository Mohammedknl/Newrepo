'''Tuple is same as list datatype but it is immutable
 List is  mutable means we can update, delete and append  the values
 Tuple is immutable means we can't change the existing values by updating the values ie we can't modify the tuple values'''
c=(1,5.6,"Good")
print(c)
print(c[1])
print(c[0])
print(c[-1])
print(c[:])
# example prog on tuple
#tuple having only integer type of data.
a = (1, 2, 3, 4)
print(a) #prints the whole tuple

#tuple having multiple type of data.
b = ("hello", 1, 2, 3,"go")
print(b) #prints the whole tuple

#index of tuples are also 0 based.

print(b[4]) #this prints a single element in a tuple, in this case "go"
