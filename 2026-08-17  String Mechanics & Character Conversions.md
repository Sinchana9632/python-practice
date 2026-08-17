

  

# 📝 Day 8 Notes: String Mechanics & Character Conversions

## 1. ASCII Values in Python (`ord()` and `chr()`)

Computers do not store letters directly—they store them as numbers using **ASCII (American Standard Code for Information Interchange)** values.

  

- Standard ASCII values range from **0 to 127**.
    
      
    
- **`ord(char)`**: Converts a single character $\rightarrow$ its integer ASCII code.
    
      
    
- **`chr(code)`**: Converts an ASCII integer code $\rightarrow$ its character.
    
      
    

### ASCII Ranges to Remember

- **Uppercase (`'A'` to `'Z'`):** `65` to `90`
    
      
    
- **Lowercase (`'a'` to `'z'`):** `97` to `122`
    
      
    
- **Digits (`'0'` to `'9'`):** `48` to `57`
    
      
    
- **Space (`' '`):** `32`
    
      
    

### Key Code Operations

Python

```
# Character to ASCII Number
print(ord('a'))  # Output: 97
print(ord('b'))  # Output: 98

# ASCII Number to Character
print(chr(97))   # Output: 'a'
print(chr(100))  # Output: 'd'

# Finding character distance/difference
distance = abs(ord('a') - ord('d'))  # abs(97 - 100) = 3
```

## 2. String Immutability

In Python, **strings are immutable**. Once created in memory, individual characters inside a string **cannot be erased or modified in-place**.

  

### Important Rules

1. **Direct assignment fails:**
    
      
    
    Python
    
    ```
    s = "hello"
    s[0] = 'j'  # ❌ TypeError: 'str' object does not support item assignment
    ```
    
2. **Creating new strings:**
    
    To change a string, you must build a **brand-new string** using concatenation (`+`) or slicing:
    
      
    
    Python
    
    ```
    s = "hello"
    s = 'j' + s[1:]  # Creates a brand-new string "jello"
    ```
    

## 3. Efficient String Building (`''.join()`)

Because strings are immutable, repeatedly appending characters using `+` inside a loop creates a new string during every iteration, leading to **$\mathcal{O}(N^2)$ time complexity** (slow).

  

### Best Practice for Building Strings:

1. Append characters into a **list** ($\mathcal{O}(1)$ per append).
    
      
    
2. Use `''.join(list)` at the end to convert it back into a string ($\mathcal{O}(N)$ overall).
    
      
    

Python

```
# Slow Way - O(N^2)
s = ""
for char in ["h", "e", "l", "l", "o"]:
    s += char

# Fast/Optimal Way - O(N)
char_list = []
for char in ["h", "e", "l", "l", "o"]:
    char_list.append(char)
s = "".join(char_list)  # "hello"
```

