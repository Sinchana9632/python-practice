"""grid=[
    [1,2,3,4],
    [4,6,7,8]
]
print(grid[0][1])   # it will print the value of the first row and second column  means 2
print(len(grid))   # it will print the number of rows in the grid  means 2
print(len(grid[0]))   # it will print the number of columns in the grid  means 4
print(grid)"""
 

grid=[
    [1,2,3,4],    # 4 columns 
    [4,6,7,8]         # 2 rows 
]
r=len(grid)
c=len(grid[0])
blanl_matrix= [[0]*c   for _ in range(r)]
blank_matrix= [[0]*r  for _ in range(c)]
print(blanl_matrix)
print(blank_matrix)