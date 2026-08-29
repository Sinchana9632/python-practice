
# 🐍 Python Array Foundation — Revision Notes

## B. List Operations

Python lists provide several built-in methods for modifying and working with elements.

### 1. `append()`

Adds **one element at the end** of the list.

```python
arr = [10, 20, 30]
arr.append(40)

print(arr)
# [10, 20, 30, 40]
```

**Typical complexity:** Amortized `O(1)`

---

### 2. `pop()`

Removes and returns an element.

Without an index, it removes the **last element**.

```python
arr = [10, 20, 30, 40]

arr.pop()

# [10, 20, 30]
```

`pop()` from the end → **O(1)**

---

### 3. `pop(index)`

Removes the element at a specified index.

```python
arr = [10, 20, 30, 40]

arr.pop(0)

# [20, 30, 40]
```

Removing from the beginning requires shifting the remaining elements.

**Typical complexity:** `O(N)`

> Important: `pop(index)` is not always O(N). Removing the last element by its index is O(1); removing near the beginning generally costs O(N).

---

### 4. `insert(index, value)`

Adds an element at a specific position.

```python
arr = [10, 20, 30, 40]

arr.insert(0, 5)

# [5, 10, 20, 30, 40]
```

The existing elements must shift to make space.

**Typical complexity:** `O(N)`

---

### 5. `remove(value)`

Removes the **first occurrence** of the given value.

```python
arr = [10, 20, 30, 20]

arr.remove(20)

# [10, 30, 20]
```

Python searches for the value first.

**Typical complexity:** `O(N)`

---

### 6. `extend()`

Adds elements from another iterable to the existing list.

```python
arr = [10, 20, 30]

arr.extend([40, 50, 60])

# [10, 20, 30, 40, 50, 60]
```

It can work with iterables such as lists and tuples.

If `K` elements are added:

**Typical complexity:** `O(K)`  
(or more generally proportional to the number of elements processed)

---

### 7. `reverse()`

Reverses the existing list **in-place**.

```python
arr = [10, 20, 30, 40, 50]

arr.reverse()

# [50, 40, 30, 20, 10]
```

It does **not** create a separate reversed list.

**Time:** `O(N)`  
**Extra space:** `O(1)`

### Important distinction

```python
arr.reverse()
```

→ modifies the existing list.

```python
arr[::-1]
```

→ creates a new reversed list.

---

### 8. `sort()`

Sorts the existing list **in-place**.

```python
arr = [40, 10, 30, 20]

arr.sort()

# [10, 20, 30, 40]
```

**Typical time complexity:** `O(N log N)`

### Important distinction

```python
arr.sort()
```

→ modifies the original list.

```python
sorted(arr)
```

→ returns a new sorted list.

---

# ⭐ Important DSA Observation

Remember the reason behind the complexity:

> Operations at the end of a Python list are usually cheap, while operations near the beginning or middle may require shifting elements.

For example:

```text
append()     → amortized O(1)
pop()        → O(1)
pop(0)       → O(N)
insert(0,x)  → O(N)
remove(x)    → O(N)
reverse()    → O(N)
sort()       → O(N log N)
```

---

# C. Python List vs Traditional Array

A Python `list` is **not exactly the same** as a traditional C array.

### Python List

```python
arr = [10, 20, 30]
```

- Built-in Python type/data structure.
    
- Dynamic in size.
    
- Can contain objects of different types.
    
- Internally implemented using a dynamic-array-like structure.
    
- `append()` is amortized `O(1)`.
    

Example:

```python
data = [10, "hello", 3.14, True]
```

Python lists can therefore be heterogeneous.

### Traditional C Array

```c
int arr[4] = {10, 20, 30, 40};
```

- Normally stores elements of the same type.
    
- Size is fixed after declaration.
    
- Provides contiguous array storage.
    

### Interview Answer

> A Python list is not exactly the same as a traditional C array. A C array normally stores elements of the same type and has a fixed size, whereas a Python list is dynamic and can contain objects of different types. Python lists are implemented using a dynamic-array-like structure, which makes appending at the end amortized O(1).

---

# D. Memory and References

## `b = a`

```python
a = [1, 2, 3]
b = a

b.append(4)
```

Both `a` and `b` refer to the **same list object**.

Therefore:

```python
print(a)
# [1, 2, 3, 4]

print(b)
# [1, 2, 3, 4]
```

### Mental Model

```text
a ─────┐
       ↓
    [1, 2, 3, 4]
       ↑
b ─────┘
```

`b = a` does not create a new list.

---

# `copy()`

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)
```

Now `a` and `b` refer to different list objects.

```python
print(a)
# [1, 2, 3]

print(b)
# [1, 2, 3, 4]
```

### Remember

```text
b = a
→ same list object

b = a.copy()
→ separate list object
```

---

# E. Nested Lists / 2D Arrays

A list can contain other lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

Think of it as:

```text
        Column
        0  1  2
Row 0   1  2  3
Row 1   4  5  6
```

Python uses:

```python
matrix[row][column]
```

Example:

```python
matrix[0][1]
```

Output:

```text
2
```

Because:

```text
row 0 → [1, 2, 3]
             ↑
          column 1
```

---

## Matrix Traversal

```python
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j])
```

Here:

- `i` → row index
    
- `j` → column index
    

---

## Correct Matrix Initialization

For a matrix with `rows` rows and `cols` columns:

```python
matrix = [[0] * cols for _ in range(rows)]
```

Example:

```python
rows = 3
cols = 4

matrix = [[0] * cols for _ in range(rows)]
```

Result:

```text
[
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]
]
```

### ⚠️ Avoid blindly using:

```python
[[0] * cols] * rows
```

This can make multiple rows refer to the **same inner list**, causing unexpected changes.

The safer pattern is:

```python
[[0] * cols for _ in range(rows)]
```

because a new inner list is created for each iteration.

---

# F. List Comprehension

List comprehension is a compact way to create a new list.

### Normal approach

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for x in numbers:
    squares.append(x * x)
```

Result:

```text
[1, 4, 9, 16, 25]
```

### List comprehension

```python
squares = [x * x for x in numbers]
```

Same result:

```text
[1, 4, 9, 16, 25]
```

### Basic Structure

```python
[expression for item in iterable]
```

Example:

```python
[x * 2 for x in numbers]
```

For:

```python
numbers = [1, 2, 3, 4, 5]
```

Result:

```text
[2, 4, 6, 8, 10]
```

---

## List Comprehension with `if`

```python
numbers = [1, 2, 3, 4, 5, 6]

result = [x for x in numbers if x > 3]
```

Result:

```text
[4, 5, 6]
```

Meaning:

> Traverse the list and include `x` only when `x > 3`.

### General Pattern

```python
[expression for item in iterable if condition]
```

---

# G. Why Python Doesn't Have Traditional `do-while`

Languages such as C, C++, and Java have a `do-while` loop.

Its important property is:

> The loop body executes at least once before the condition is checked.

Python does not have a dedicated `do-while` keyword.

The same behavior can be achieved using:

```python
while True:
    # code

    if condition:
        break
```

### Example

```python
i = 1

while True:
    print(i)
    i += 1

    if i > 5:
        break
```

Output:

```text
1
2
3
4
5
```

### Remember

```text
C/C++/Java
→ do-while

Python
→ no traditional do-while

Python equivalent
→ while True + break
```

Python keeps the language relatively simple because the same behavior can be expressed using existing constructs.

---

# 🧠 FINAL REVISION CHECKLIST

Before starting actual DSA Array Patterns, I should be able to explain:

-  `append()`
    
-  `pop()`
    
-  `pop(0)`
    
-  `insert()`
    
-  `remove()`
    
-  `extend()`
    
-  `reverse()`
    
-  `sort()`
    
-  Why some list operations are `O(1)` and others `O(N)`
    
-  Amortized `O(1)`
    
-  Python list vs C array
    
-  References: `b = a`
    
-  Copy: `b = a.copy()`
    
-  Nested lists / 2D arrays
    
-  Matrix indexing
    
-  Matrix initialization
    
-  List comprehension
    
-  List comprehension with `if`
    
-  Python's `while` + `break` alternative to `do-while`
    

## 🚀 Next Stage

**Python Array Foundation → COMPLETE ✅**

Next:

# 🔥 DSA ARRAY PATTERNS

The focus now changes from:

> "What does this Python feature do?"

to:

> **"How do I recognize an array problem and choose the correct algorithm/pattern?"**

That is the next major step in the placement journey.