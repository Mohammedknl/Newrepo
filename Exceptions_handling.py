'''In this we will learn about exceptions and how to handle the exceptions in python'''
'''Explicityly throughing an error is called Exception
There are two ways to through an error explicitly  if the condition is not met
1) Raise and 2)Assertion'''
# exception means telling python to stop the current execution and throughing an error explicitly
# condition and fails if it don't meet the condition
# Prog1 to raise the exception error message
itemcart = 0
# Here there is no code written to stop the exceptional error message so it will through an error.Here 2 items can be added
if itemcart != 2:
#    raise Exception("Product cart count not matching") # raise and exception are the keywords will understand that something is wrong and it will display the message
# Assertion is also one way to have some condition or expect a true condition and fails if it don't meet the condition
# whenever assert receives a false condition then it fails the test case
# prog on assertion with a true condition
     pass # if condition will do nothing
#assert (itemcart==0) # Here consdition matches and test is not failing as itemcart matches so it pass the o/p
assert (itemcart == 2) # condition should be always true if condition false then test will fail and it will show assertion error in o/p
#whenever assert receives a false condition then it will break your test



