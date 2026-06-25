number=[1,3,4]
num=[]
for i in number:
    a=i*2
    num.append(a)         
print(num)                  #output [2, 6, 8]



number=[1,3,4]
num=[i*2 for i in number ]   # this is the list comprehension method to do the same thing as above
print(num)                 #output [2, 6, 8] 


number=[1,3,4]
num=[i*2 for i in number if i>2]   # this is the list comprehension method to do the same thing as above
print(num)           #output [6, 8]   # it will only take the values which are greater than 2 and multiply them by 2 and store them in the list num


numbers = [1, 2, 2, 3, 4, 4, 5]

# Set comprehension automatically filters out duplicates
unique_squares = {x * x for x in numbers}

print(unique_squares)  # Output: {1, 4, 9, 16, 25}

words = ["apple", "banana", "cherry"]

# Key is the word, Value is the length of the word
word_lengths = {w: len(w) for w in words}

print(word_lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}

# Create a list comprehension first, then cast it to a tuple
tuple_squares = tuple([x * x for x in range(1, 4)])

print(tuple_squares)  # Output: (1, 4, 9)