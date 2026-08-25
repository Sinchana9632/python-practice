

# 🏃 Array Marathon — Python List Revision Notes

### Part 1: List Fundamentals + Indexing + Slicing

---

## 1. What is a List?

A **list** is an ordered collection of elements in Python.

```python
marks = [80, 90, 75]
```

Here:

```text
marks              → variable
[80, 90, 75]       → list
80, 90, 75         → elements/items
```

A list can contain different types of data:

```python
data = [10, "Hello", 3.14, True]
```

### DSA perspective

We commonly use Python lists as a **dynamic-array-like structure** for array problems.

---

# 2. Why is a Python List Dynamic?

A list can **grow and shrink during program execution**.

```python
numbers = [10, 20, 30]

numbers.append(40)
```

Result:

```python
[10, 20, 30, 40]
```

And:

```python
numbers.pop()
```

Result:

```python
[10, 20, 30]
```

### Remember

> **Dynamic = size can change during execution.**

### Important operations

```python
arr.append(x)     # add x at the end
arr.pop()         # remove last element
arr.pop(i)        # remove element at index i
```

---

# 3. List Indexing

Indexing means **accessing an element using its position**.

```python
arr = [10, 20, 30, 40, 50]
```

```text
Index:    0    1    2    3    4
Value:   10   20   30   40   50
```

Python uses **zero-based indexing**.

```python
arr[0]     # 10
arr[2]     # 30
arr[4]     # 50
```

### Important

```text
Index → position
Value → actual data stored at that position
```

Trying to access an index that doesn't exist:

```python
arr[5]
```

produces:

```text
IndexError: list index out of range
```

---

# 4. Positive Indexing

Positive indexing starts from the **left**.

```text
Index:    0    1    2    3    4
Value:   10   20   30   40   50
```

So:

```python
arr[0]     # 10
arr[3]     # 40
```

---

# 5. Negative Indexing

Negative indexing starts from the **right**.

The rightmost element is always `-1`.

```text
Positive:  0    1    2    3    4
Value:    10   20   30   40   50
Negative: -5   -4   -3   -2   -1
```

Examples:

```python
arr[-1]    # 50
arr[-2]    # 40
arr[-3]    # 30
arr[-5]    # 10
```

### Important distinction

**Negative index ≠ moving backward.**

The **step** determines direction during slicing.

---

# 6. Slicing

Slicing extracts a portion of a list.

Basic syntax:

```python
arr[start:stop]
```

### Golden rule

> **Start is included, stop is excluded.**

Example:

```python
arr = [10, 20, 30, 40, 50]

arr[1:4]
```

Result:

```python
[20, 30, 40]
```

Because indexes `1, 2, 3` are included, but `4` is excluded.

---

# 7. Three-Part Slicing

Syntax:

```python
arr[start:stop:step]
```

Example:

```python
arr[0:7:2]
```

means:

```text
start → 0
stop  → 7 (excluded)
step  → 2
```

Result:

```python
[10, 30, 50, 70]
```

---

# 8. Common Slicing Patterns

Given:

```python
arr = [10, 20, 30, 40, 50]
```

### First 3 elements

```python
arr[:3]
```

→ `[10, 20, 30]`

### From index 2 to the end

```python
arr[2:]
```

→ `[30, 40, 50]`

### Copy the whole list

```python
arr[:]
```

→ `[10, 20, 30, 40, 50]`

### Reverse

```python
arr[::-1]
```

→ `[50, 40, 30, 20, 10]`

### Reverse with step 2

```python
arr[::-2]
```

→ `[50, 30, 10]`

---

# 9. Negative Step

A **negative step means move from right to left.**

Example:

```python
arr[5:1:-1]
```

Think:

```text
5 → 4 → 3 → 2
```

Stop before `1`.

So:

```python
[60, 50, 40, 30]
```

---

# 10. Negative Index + Negative Step

Example:

```python
arr[-2:-7:-2]
```

Indexes:

```text
-7   -6   -5   -4   -3   -2   -1
 ↓    ↓    ↓    ↓    ↓    ↓    ↓
10   20   30   40   50   60   70
```

Start at `-2`:

```text
-2 → -4 → -6
 ↓    ↓    ↓
60   40   20
```

Therefore:

```python
arr[-2:-7:-2]
```

→ `[60, 40, 20]`

### Golden rule

> **The step determines the direction.**

```text
+ step → left → right
- step → right → left
```

---

# 🧠 DSA Point: What is O(K)?

When slicing:

```python
arr[1:4]
```

Python creates a **new list** containing the selected elements.

If it copies `K` elements, the work is approximately:

```text
O(K)
```

Where:

```text
N = total elements in the original list
K = number of elements being copied/processed
```

Example:

```text
N = 1,000,000
K = 5
```

If you slice only 5 elements, you're dealing with those 5 copied elements, so we describe the slicing cost as **O(K)**.

### Important for DSA

Slicing is **not free**.

For example:

```python
arr[1:]
```

creates a new list, so it takes time proportional to the number of elements copied.

---

# ⭐ What You Should Be Able to Explain Now

If an interviewer asks:

### "What is a Python list?"

You should be able to say:

> **A Python list is an ordered, mutable, dynamically resizable collection of elements. It supports indexing, negative indexing, slicing, and iteration. In DSA, we commonly use Python lists as dynamic-array-like structures.**



---

