'''Here we will see how to read the text file and write the data in to the text file using python
Step1: creating text file with name test.txt with some data'''
#prog to read the test.txt file data
fopen = open('test.txt') # creating one object fopen to open the file for reading or writing the data using open method and the file path
print("Printing all the content of the file",fopen.read())# this .read method is used to read all the content of the file and to print we have to write in print code
#print function will retrieve all the content from .read method and it will print the o/p
# To read n no of characters by passing parameters
#print("Prints first 2 characters of the file:",fopen.read(2)) # To print first 2 characters from the file and print

#print("To print up to 5 characters from text file:",fopen.read(6)) # Here in between onle line to another line it counts one character of space
# To read the first two lines of file content line by line then we can't execute both read and readline method at a time
#print("This is the first line of tst file:",fopen.readline())
#print("This is the second line of tst file:",fopen.readline())
fopen.close() # always close the file whenever it opens using its object and close method

