'''Break is a keyword used to break the entire while loop based on the condition
break is generally used to halt/stop the loop abruptly'''
# example prog with break keyword
x = 5
while x>1:
    if x==2:
        print("2 is found so it will break the while loop")# this print is w.r.t if not while
        break
    print(x) #This is w.r.t while loop not if if it breaks then it will not execute these 2 while loop lines
    x = x-1
print("This completes while loop with break keyword")