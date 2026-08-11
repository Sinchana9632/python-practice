# Python Concepts: Array Memory & In-Place Performance

## 📌 1. Python List Memory Structure & Object References

In Python, lists do not store the raw data values directly inside the list structure. Instead, they store **pointers (memory references)** to objects stored elsewhere in memory.

- **Fast Index Access:** Accessing `nums[i]` or updating `nums[k]` takes $\mathcal{O}(1)$ constant time because the pointer block is stored sequentially in memory.
    
- **In-Place Mutation:** Executing `nums[k] = nums[i]` simply updates the pointer at position `k` to point to the same object as position `i`. This modifies the original list directly without creating a new list object ($\mathcal{O}(1)$ space).
    

## 📌 2. The Trap of `.remove()` and `.pop()`

Python has built-in list methods like `nums.remove(val)` or `nums.pop(i)`. While easy to read, they are inefficient for Data Structures & Algorithms (DSA):

Python

```
# ❌ SLOW APPROACH: O(N²) Time Complexity
while val in nums:
    nums.remove(val)  # Scans array + shifts all remaining elements left
```

### Why it is slow:

1. `nums.remove(val)` must scan the array to locate `val` $\rightarrow \mathcal{O}(N)$ time.
    
2. Once found, it **shifts all elements to the right of `val` one position to the left** to close the gap $\rightarrow \mathcal{O}(N)$ time.
    
3. Repeating this inside a loop leads to **$\mathcal{O}(N^2)$ time complexity**.
    

## 📌 3. Optimal Pattern: Index Overwriting ($\mathcal{O}(N)$)

Instead of deleting and shifting elements, use **direct index overwriting** (`nums[k] = nums[i]`):

| **Approach**                   | **Time Complexity** | **Space Complexity** | **Why?**                                          |
| ------------------------------ | ------------------- | -------------------- | ------------------------------------------------- |
| **`nums.remove(val)` in loop** | $\mathcal{O}(N^2)$  | $\mathcal{O}(1)$     | Repeated element searching and shifting           |
| **Two-Pointer Overwrite**      | $\mathcal{O}(N)$    | $\mathcal{O}(1)$     | Single pass traversal; overwrites values directly |