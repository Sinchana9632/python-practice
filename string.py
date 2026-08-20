"""
av="a"
print(ord(av))
print(chr(100))

s1="sinchaan\n"
s2="good Girls\n"
s3=s1+s2  
print(s3) 

   

char_list=[]
for i in ['h','l','o']:
    char_list.append(i)
    print(char_list)
    print("".join(char_list))
    """
list=[1,3,4,5]
for i in list:
    if i==4:
       continue
    print([i])
list=[1,3,4,5]
for i in list:
    if i==4:
       break
    print([i])
    
list=[1,3,4,5]
for i in list:
    if i==4:
       pass   
    print([i])