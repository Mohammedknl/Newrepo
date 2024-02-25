#Prog on for loop
# Loops is used to iterate or repeate over each and every element in list
obj = [2, 3, 5, 7, 9] # Declaring a vriable obj to iterate a list element
for i in obj :  # Here for and in are keywords to iterate the list elements
    print(i)
print("second loop starts here to print list elements multiply by 2")
for x in obj:
    print(x*2)
# prog to print sum of first 5 natural no's like 1+2+3+4+5=15
print("Below is to print first 5 natural no's")
for y in range(1,6): # It will iterate from 1 to till 6-1=5
    print(y) # Here it will print only natural no's till 5 without adding
#prog to take sum of 4 natural no's by iterating j values from 1 to 4
print("Below is to add the value by 1 or increment by 1")
addition = 0
for j in range(1,5): # It will increment the value of j by 1
    addition = addition +j
print(addition)

# To print the values with 2 indexes diferent like i+2
print("Below is to print the values with 2 indexes different")
for k in range(1,10,2): # Here we have passed index for increamenting its value by 2
    print(k) # It will print the k value incremented by 2 from 1 til 9
# prog by passing only one index ie 4
for l in range(4): # It will print all values starting from 0 to 4-1 ie 3
    print(l)
w= [7,8,9] # creating list object to call in for loop
for m in w : # giving list object for iteration
    print(m)