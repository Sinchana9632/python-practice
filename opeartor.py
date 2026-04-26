a=10
b=10
z=a
y=12
print(a is b)
print(b is b)   # is and  isnot are the identity function 
print(z is a)  #True 
print(z is b)
print(z is y)
print(z is not y)  #True
print(id(a))
print(id(b),id(z),id(y))  # all momery are same expect y address are differnt 
s="Hii"   # it also same as number 
y="Hii"
print(s is y)## id functio  is used to get the address of the variable 
list=[10,20,30]
list1=[10,20,30]
print(list is list1)  #False
print(list is not list1)  #True
print(id(list))  #2616649439360
print(id(list1))  # memory address of the list have same value is differnt bcz  the list have colection of  values so that 
#2616649437440

num = None
num2=None  
print(num is num2) #True   becuse None is the keyword 