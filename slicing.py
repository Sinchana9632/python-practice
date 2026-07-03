"""code="sinchana"
list=[23,45,67,"sinchana"]
name=input("enter your name:")
reversed=name[::1]  # positive slincing 

if reversed==name:
    print("given string id palindrome")
else:
    print("given string is not a palindrome")   # sicing are used to chacek the if the input is palindraome or not 
    
# space complexity=o(n)  #  its require the copy and compare 
#time complextity =o(n)  bcz if statement trvanser evry item on the lost 
"""
list=[23,67,4,6,6,"sincaha"]
print(list[3:1:-1])