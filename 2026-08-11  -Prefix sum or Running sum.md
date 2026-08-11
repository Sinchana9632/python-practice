# Prefix Sum Pattern & In-Place Accumulation

## 📌 1. What is a Prefix Sum?

A **Prefix Sum** (or Running Sum) transforms an array so that the element at index `i` becomes the total sum of all elements from index `0` through `i`.

- **Formula:** $\text{PrefixSum}[i] = \text{PrefixSum}[i - 1] + \text{arr}[i]$
    
- **Time Complexity:** $\mathcal{O}(N)$ (Single pass).
    
- **Space Complexity:** $\mathcal{O}(1)$ if done in-place, or $\mathcal{O}(N)$ if creating a new array.
    

## 📌 2. Python Concepts

1. **Forward Range with Custom Start:**
    
    - `range(1, len(nums))` starts at index `1` and stops at `len(nums) - 1`.
        
    - Index `0` is skipped because it has no preceding elements.
        
2. **In-Place Accumulation (`+=`):**
    
    - `nums[i] += nums[i - 1]` adds the accumulated total of everything before `i` directly into `nums[i]`.