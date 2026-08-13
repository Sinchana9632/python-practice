
# 📝 Python Concepts: Modules, Packages, and Libraries

## 📌 Summary & Definitions

- **Module (`.py` file):** A single Python code file containing functions, classes, or variables.
    
- **Package (Folder):** A directory containing one or more modules grouped together, usually identified by an `__init__.py` file.
    
- **Library (Tool Set):** An umbrella term for a collection of packages and modules designed to accomplish specific tasks (e.g., Data Science, Web Development).
    

## 🧰 Real-World Analogy

| **Term**     | **Technical Meaning**    | **Analogy**     | **NumPy Example**           |
| ------------ | ------------------------ | --------------- | --------------------------- |
| **Module**   | A single `.py` file      | Single Tool     | `numpy.random`              |
| **Package**  | Folder of modules        | Toolbox         | `numpy`                     |
| **Library**  | Collection of packages   | Hardware Store  | The whole NumPy ecosystem   |
| **Function** | Actionable block of code | Built-in action | `np.array()` or `np.mean()` |

## 💻 Structure Overview

Plaintext

```
project_folder/
│
├── my_package/          <-- PACKAGE (Directory)
│   ├── __init__.py      <-- Marks directory as a package
│   ├── module_a.py      <-- MODULE (Single Python File)
│   └── module_b.py      <-- MODULE
│
└── main.py
```

Python

```
# Importing a module from a package
from my_package import module_a

# Calling a function inside a module
module_a.my_function()
```

"""grid=[

    [1,2,3,4],

    [4,6,7,8]

]

print(grid[0][1])   # it will print the value of the first row and second column  means 2

print(len(grid))   # it will print the number of rows in the grid  means 2

print(len(grid[0]))   # it will print the number of columns in the grid  means 4

print(grid)"""

  

grid=[

    [1,2,3,4],    # 4 columns

    [4,6,7,8]         # 2 rows

]

r=len(grid)

c=len(grid[0])

blanl_matrix= [[0]*c   for _ in range(r)]

blank_matrix= [[0]*r  for _ in range(c)]

print(blanl_matrix)

print(blank_matrix)