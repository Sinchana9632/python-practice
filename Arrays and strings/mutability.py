"""a=[10,2,34,45]  
b= a
b[0]=99
print(a)
print(b)"""   # Syntax: range(start_index, stop_index, step_size)

nums = [10, 20, 30, 40]
n = len(nums)

for i in range(n - 1, -1, -1):
    print(i, nums[i])
    