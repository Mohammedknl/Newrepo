'''List work as an array elements with different datatypes
List is mutable means we can update dlete and add list elements
Basically List is a datatype which allows multiple values and can be different datatypes  '''
x = [1,2,"Great",50.23]# Here x is the variable/object for the list containing elements with index no's starting from 0 to n
# To print the values of the list with the index no's starting from 0 to n from left and -1 from right
print(x[0])
print(x[3])
print(x[-1])
print(x[-4])
print(x[1:2])# including 1st index and excluding 2nd index
print(x[0:]) #starts from 0th index to last index including
print(x[:-1])#Excluding -1 indes till starting including 0
print(x[:])# print all the index elements
print(x[1:-1]) #including 1st index and till excluding -1st index
x.insert(3,"Mohammed")# To add new list element using insert method
print(x[:])# To print all values or
print(x)
# To add the new value at last index using append
x.append(10)
print(x)
# Insert and append are two different methods of list to manipulate
# To update any values of list
x[3]="MOHAMMED"
print(x)
# To delete any value of list
del x[5]
print(x)
# we can perform delete, update, insert, append and retrieve on list elements