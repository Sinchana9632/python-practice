
# 🏃 Array Marathon — Today's Revision Notes

## 1. Iteration

**Iteration** means visiting the elements of an array/list one by one.

### `for` loop — iterate over values

```python
arr = [10, 20, 30, 40]

for x in arr:
    print(x)
```

Here:

- `x` → directly gets the **value**
    
- It does NOT represent the index.
    

Execution:

```text
x = 10
x = 20
x = 30
x = 40
```

### `for` loop — iterate using indexes

```python
for i in range(len(arr)):
    print(arr[i])
```

Here:

- `i` → index
    
- `arr[i]` → value at that index
    

### `enumerate()` — index + value

```python
for i, x in enumerate(arr):
    print(i, x)
```

Example:

```text
0 10
1 20
2 30
3 40
```

### Important distinction

```text
for x in arr
→ x = value

for i in range(len(arr))
→ i = index

for i, x in enumerate(arr)
→ i = index
→ x = value
```

---

# 2. Running Maximum Pattern

A common DSA pattern is to maintain the best answer while traversing.

```python
arr = [4, 9, 2, 15, 7]

maximum = arr[0]

for x in arr:
    if x > maximum:
        maximum = x
```

Execution:

```text
maximum = 4
4  → no change
9  → maximum = 9
2  → no change
15 → maximum = 15
7  → no change
```

Final:

```text
15
```

### DSA pattern

```text
Initialize
    ↓
Traverse
    ↓
Check
    ↓
Update
```

This pattern is useful for:

- Maximum element
    
- Minimum element
    
- Best profit
    
- Largest/smallest value
    
- One-pass array problems
    

**Time:** O(N)  
**Extra Space:** O(1)

---

# 3. Counting Pattern

Example:

```python
arr = [5, 2, 8, 2, 9, 2]

count = 0

for x in arr:
    if x == 2:
        count += 1
```

Final:

```text
count = 3
```

General pattern:

```python
count = 0

for x in arr:
    if condition:
        count += 1
```

### DSA pattern

```text
Initialize count
      ↓
Traverse every element
      ↓
Check condition
      ↓
Increase count if true
```

**Time:** O(N)  
**Extra Space:** O(1)

---

# 4. `while` Loop

A `while` loop repeatedly executes while its condition is `True`.

Basic structure:

```python
i = 0

while condition:
    # work
    i += 1
```

Think:

```text
Initialize
    ↓
Check condition
    ↓
Work
    ↓
Update
    ↓
Check again
```

### Array traversal using `while`

```python
arr = [10, 20, 30, 40, 50]

i = 0

while i < len(arr):
    print(arr[i])
    i += 1
```

Output:

```text
10
20
30
40
50
```

Here:

```text
i       → index
arr[i]  → value
```

### Important DSA understanding

Don't think only:

> Known iterations = `for`, unknown iterations = `while`.

A better DSA understanding is:

```text
for
→ naturally traverse a collection/range

while
→ continue while a condition remains true
```

`while` is especially important for:

- Two pointers
    
- Binary search
    
- Sliding window
    
- Linked lists
    
- Condition-based searching
    

---

# 5. `break`

`break` immediately stops the entire loop.

Example:

```python
arr = [4, 7, 2, 9, 5]

i = 0

while i < len(arr):
    if arr[i] == 9:
        break

    print(arr[i])
    i += 1
```

Output:

```text
4
7
2
```

When `arr[i] == 9` becomes true:

```python
break
```

→ loop stops immediately.

### Remember

```text
i += 1
→ move to the next iteration

break
→ stop the entire loop
```

---

# 6. `len()`

`len()` gives the **number of elements**.

```python
arr = [10, 20, 30, 40, 50]

print(len(arr))
```

Output:

```text
5
```

### Important distinction

```text
Length      → number of elements
Index       → position of an element
```

For:

```python
arr = [10, 20, 30, 40, 50]
```

Indexes:

```text
0  1  2  3  4
```

Length:

```text
5
```

### Golden rule

```text
Last index = len(arr) - 1
```

Therefore:

```text
len(arr) = 5
last index = 4
```

This is why array traversal commonly uses:

```python
i < len(arr)
```

and not:

```python
i <= len(arr)
```

---

# 7. `in` and `not in`

Used to check whether an element exists.

```python
arr = [10, 25, 30, 45, 50]

30 in arr
```

→ `True`

```python
35 in arr
```

→ `False`

```python
35 not in arr
```

→ `True`

### DSA connection

```python
if target in arr:
    print("Found")
```

For a normal Python list, membership checking is generally **O(N)** in the worst case.

Python may need to inspect elements one by one.

This becomes important later when learning why **sets and dictionaries provide faster average-case lookup**.

---

# 8. `min()`, `max()`, `sum()`

Given:

```python
arr = [10, 40, 20, 70, 30]
```

### `min()`

```python
min(arr)
```

→ `10`

Finds the smallest value.

### `max()`

```python
max(arr)
```

→ `70`

Finds the largest value.

### `sum()`

```python
sum(arr)
```

→ `170`

Adds all values:

```text
10 + 40 + 20 + 70 + 30 = 170
```

### Quick memory table

|Function|Meaning|
|---|---|
|`len(arr)`|Number of elements|
|`min(arr)`|Smallest value|
|`max(arr)`|Largest value|
|`sum(arr)`|Total of all values|
|`x in arr`|Check whether `x` exists|

---

# 🧠 Most Important DSA Takeaways From Today

## Pattern 1 — Traverse

```python
for x in arr:
    ...
```

## Pattern 2 — Traverse with index

```python
for i in range(len(arr)):
    ...
```

## Pattern 3 — Index + value

```python
for i, x in enumerate(arr):
    ...
```

## Pattern 4 — Track maximum

```python
maximum = arr[0]

for x in arr:
    if x > maximum:
        maximum = x
```

## Pattern 5 — Count

```python
count = 0

for x in arr:
    if condition:
        count += 1
```

## Pattern 6 — Condition-based traversal

```python
i = 0

while i < len(arr):
    ...
    i += 1
```

## Pattern 7 — Stop early

```python
if condition:
    break
```

---

# ⭐ Mental Model

When you see an array problem, start asking:

```text
1. Do I need to visit every element?
        ↓
      Traverse

2. Do I need the index?
        ↓
      Use i / enumerate()

3. Am I finding the biggest/smallest?
        ↓
      Track maximum/minimum

4. Am I counting something?
        ↓
      count += 1

5. Do I need to stop early?
        ↓
      break

6. Does movement depend on a condition?
        ↓
      Consider while
```

This is the foundation we will use when we start the **actual Array DSA Patterns**.