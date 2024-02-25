'''Continue keyword is used when you want to skip current iteration and proceed to next iteration'''
# prog on continue with while loop
a=10
while a > 1:
    if a == 9:
        a =a-1 # If this code is not written before continue then it will print only 10 and executes infinitely
        continue # If it satisfies it will stop the below iteration for 9 and will start the next iteration ie for 8
    if a ==3:
        break
    print(a) # This is w.r.t while loop not if
    a = a-1
