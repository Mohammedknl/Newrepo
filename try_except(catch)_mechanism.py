'''Try and catch in other programming language is used to pass the code of try block
even if there is an error/exception in runtime by providing proper catch block code with customized message'''
'''In python same try and except blocks are used to handle with exceptional errors at runtime '''
# In python instead of catch we call here as expect which work same as catch of other programming languages
#In other programming when any exception is raised in try block then the control will switch to catch block same here it will go to expect block so that test will not fail
# except/ catch block will be executed only if the try block code fails or any exceptional error in try block during runtime
# prog1 without try and expect blocks

#with open('filelog.txt','r') as reader: # here we are trying to open the filelog.txt which is not present if we run without try block it will show an error
#    reader.read() # reading the content of the file with a variable reader
#O/P of prog1 with out try block:FileNotFoundError: [Errno 2] No such file or directory: 'filelog.txt'
#prog2 using try and except blocks of code (If you don't want to fail your test and execute at runtime by catching it's exception then use except block same as catch)
try:
    with open('filelog.txt', 'r') as reader: # Here we are failing the test by giving wrong file name but still it will execute in runtime with the help of try and except block by giving control to the except block
        reader.read()
except:  # In python except keyword is same as catch block where if there is any exception raised in try block control goes to except block at runtime
    print("This is from except block of prog2 as there is an exception error during runtime in try block") # This is the customized exceptional error message not from python

# O/P of prog2 with try and except blocks: This is from except block of prog2 as there is an exception error during runtime in try block
# in prog2 if we give the correct file name in try block code then there will be no exception and control will not go to except block
#Except block of code will be executed only if there is an exceptional error in try block
#prog3 using try and except blocks with exact error message by the python interpreter not from the user
try:
    with open('filelog.txt','r') as reader:
        reader.read()
except Exception as e: # Here we are providing the exact error message from exception of python and stroing in e variable
    print(e) # It will pass thr try block and print the e value which is the exact error message of an exception from python interpreter
#O/P of prog3 with exception variable :Here the exact error message from python interpreter will be shown by passing the try block even if there is an error in try block using except

