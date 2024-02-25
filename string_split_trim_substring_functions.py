''' string is also a data type'''
str = "Rahulshettyacademy.com"  # Declaring a string variable
str1 = "No 1 academy"
str2 = "Rahulshetty"
str3 = "10"
print(str[1]) # To print any characters of string
print(str[0:5]) # To extract sub string from string ie only rahul it will print 0 to n-1 ie 4
'''To concatinate two strings str and str1 values using concatination operator + if both are same return types
If there are two different datatypes then we have to type {}{}.format()'''
print(str + str1) # To concatinate two strings str and str1 values using concatination operator + if both are same return types
# To check or validate if str2 value is present in str or not
if str2 in str:
    print("Yes Rahulshetty is present in str")
else:
    print("No")
if str3 in str:
    print("No 10 found")
else:
    print("No 10 not  found")
# split and trim the string are operations performed on string
#prog on split
print(str.split(".")) #To split the string in to two indexes based on the value here based on . breaks in to two strings left and right
# split will result in the form of list with indexes
splitvar=str1.split("1") # here we are spliting the string and placing in a variable called splitvar
print("This is split of string2 based on 1:", splitvar)
print("This is printed value of str2 after splitting with index 0:", splitvar[0])
# Trim is basically an operation to remove white spaces at the begining or end of your test
#trim in python can be done using method called strip() it will trim both starting and ending spaces
str4 = " great " # Declaring variable str3 with value great and one space at the begining and end
print("This is to trim the str4 by removing white spaces in the begining:", str4.strip())
# OR
#print(str4.strip())
# To trim or remove begining white spaces of any string use method called lstrip()
print(str4.lstrip()) # To verify put the cursor in o/p it will show the space at right after triming left side
print(str4.rstrip()) # To verify put the cursor in o/p it will show the space at left after triming right side



