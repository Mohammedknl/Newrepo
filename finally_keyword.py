'''Finally is a keyword and it is connected or written only whe we write try and except block of codes in exception mechanism
this finally keyword will run irrespective of pass or failure of try and except blocks means it runs even if there is any exceptional error or not
So finally block of code will be executed even if there is an eror in try block or not or not catching the except block'''
#prog1 on finally by failing the test in try block and accepting except code and running finally block of code
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("This is from finally of prog1 to clean up all resources/cookies")

#prog2 on finally keyword by passing the test in try block , without accepting except block and still executing the finally block of code
try:
    with open('test.txt','r') as reader:
        reader.read()
except Exception as f:
    print(f)
finally:
    print("This is from finally of prog2 to clean up the resources")
# Finally keyword block of code is used to delete the records/data created for test/cleaning the data/deleting your cookies