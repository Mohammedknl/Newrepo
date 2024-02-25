''' Here we will see how to read multiple lines of content present in text file without using readline method multiple times'''
#prog to print the content of file line by line using readline method
fopen =open('test.txt') # fopen is an object where we store the test.txt file data
#print(fopen.read()) # To read the complete data of the file using read method
# Method 1 prog to read the content of file line by line using readline method
#line = fopen.readline()
#while line!="":  # It check if any line is not equalt to blank means if the content is present in the line then
#    print(line) #It will execute the readline method and iterate multiple times until it gets blank line
#    line = fopen.readline()  # This loop continues untill the condition is false
# Mthod 2 prog to read the content of file line by line using readlines method
#readlines method will read all the content of file and each and every line will print in the form of list with index starts from 0 for line1 to last line
#print(fopen.readlines()) # It prints all the line in the form of list including spaces in betwen 2 lines
for x in fopen.readlines(): # once we get the file in the form of list we can iterate and print the list elements using for loop
    print(x)

fopen.close() # without close method also it works but it is better to close the file once read
