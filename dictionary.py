'''Dictionary is also a datatype
It is an unordered sequence of data of key-value pair form. It is similar to the hash table type.
Dictionaries are written within curly braces in the form key:value.
It is very useful to retrieve data in an optimized way among a large amount of data.'''
dic = {"a":10, 2:"Hello", "3":'My Name'}
print(dic["a"]) # by using key it will show the corresponding value
print("This is id of key a :",id("a")) # it will prin the id where value of a is present in memory
print(dic[2])
print("This is id of key 2:", id(2))
# prog to pass/ add values in the empty dictionary
edic = {}
print(edic) # print empty dictionary
edic[1] = "Mohammed" # adding key value pair to empty dictionary
print(edic)
edic["2"] = 123
print(edic)
edic[3] = "Muzammil"
print(edic)
print(edic[3])
