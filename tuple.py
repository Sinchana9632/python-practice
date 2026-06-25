a = ("Python")
b = ("Python",)
c = ["Python"]
print(type(a),type(b),type(c))




#The One-Element Tuple Trap
my_name=("python")
print(type(my_name))

my_name=("python",)                          #output  
                                                       # <class 'str'>
                                                        #<class 'tuple'>
                                                        #<class 'int'>
                                                        #<class 'tuple'>
                                                        # print(type(my_name))

num=(6)
print(type(num))


num=(6,)
print(type(num))


import sys
empty_list=[]
empty_tuple=()
print(sys.getsizeof(empty_list))   # size is 56 bytes  bcz it gives the extra backup memory for the list to add more elements in future
print(sys.getsizeof(empty_tuple))   # size is 40 bytes  bcz it alrady has fixed size and it will not change in future

names=("sinchan","shiro","bobby","hima")   #unpacking
girl,boys,transgender,gender=names
print(girl,boys,transgender,gender)  #instad of the names[0],names[1],names[2],names[3] we can use this unpacking method to get the values of the tuple

a=10
b=23
a,b=b,a      # in c++ and java we use the temp variable to swap the values of a and b but in python we can do it in one line
print(a,b)



# tuple methods

name=("sinchan","shiro","bobby","hima","hima")
print(name.count("hima"))
print(name.count("sinchan"))   # it will count the number of times the element is present in the tuple
print(name.index("shiro"))   # it will return the index of the element in the tuple

print(name.index("hima"))   # it will return the index of the first occurrence of the element in the tuple