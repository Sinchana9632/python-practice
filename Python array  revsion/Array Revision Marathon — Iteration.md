# Array Revision Marathon — Iteration

You already know the basic idea, so let's do a **quick but DSA-focused revision**.

## 1. What is Iteration?

**Iteration means visiting elements one by one.**

```
arr = [10, 20, 30, 40]
```

```
for x in arr:
    print(x)
```

Output:

```
10
20
30
40
```

Here, `x` takes each value one by one:

```
x = 10
x = 20
x = 30
x = 40
```

---

## 2. Three Ways to Iterate

### A. Directly over values

```
for x in arr:
    print(x)
```

Use this when you need the **values**.

Example:

```
total = 0

for x in arr:
    total += x
```

---

### B. Using indexes

```
for i in range(len(arr)):
    print(arr[i])
```

Here:

```
i → index
arr[i] → value
```

This is useful when you need to **modify elements**.

```
for i in range(len(arr)):
    arr[i] *= 2
```

---

### C. Using `enumerate()`

When you need **both index and value**:

```
for i, x in enumerate(arr):
    print(i, x)
```

Example:

```
arr = [10, 20, 30]
```

Output:

```
0 10
1 20
2 30
```

---

# ⭐ DSA Important Difference

Suppose:

```
arr = [10, 20, 30, 40]
```

### Just need values?

```
for x in arr:
```

### Need index + value?

```
for i, x in enumerate(arr):
```

### Need to modify using the index?

```
for i in range(len(arr)):
    arr[i] = ...
```

This distinction will help you write cleaner DSA solutions.

---

# 🧠 One Important Concept: Iteration Complexity

If the array has `N` elements and you visit every element once:

```
for x in arr:
    ...
```

the time complexity is:

**O(N)**

Why?

If:

```
N = 5      → 5 elements visited
N = 100    → 100 elements visited
N = 1,000  → 1,000 elements visited
```

The work grows with the size of the array