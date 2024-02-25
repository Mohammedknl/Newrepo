'''Instead of creating an object to open the text file we can also open the text file using "with and as" keywords'''
# Method 1 of opening the file
# like fopen = open(test.txt)
#fopen.close()
#Method 2 of opening and closing the file automatically without fopen.close() method
#with open(test.txt) as fopen: # for this type of syntax there is no need to write fopen.close() method for closing automatically once the file is executed it will close
# In writing data in to text file we use above syntax to open the file here r indicate flag mode to read the file and w for writing the file
#Prog to 1) read the file and store all the lines in list
#2)Reverse the list
#3)write the list back to the file
with open('test.txt','r') as reader: # opening the file in read mode with its object name a reader, if we don't write r automatically it assumes as read mode
    lcontent = reader.readlines() # to store all the lines of a file as list elements and storing in a cariable called lcontent
    reversed(lcontent) # this method will reverse the lcontent elements present in list
    with open('test.txt', 'w') as writer: # open the file test.txt in write mode
        for x in reversed(lcontent):# It will extract the elements of reversed of lcontent and store in x for iteration
            writer.write(x) # to write the list in to file in reverse order

# Check the O/P in test.txt file if successfully executed
