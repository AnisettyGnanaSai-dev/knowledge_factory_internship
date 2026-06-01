"""
03_indexing_slicing.py

Topics:
1. 1D indexing
2. Negative indexing
3. Slicing
4. Step slicing
5. 2D indexing
6. Column selection
7. Submatrices
8. 3D indexing
9. Fancy indexing
10. Boolean masking
11. Views vs Copies

Goal:
Learn how to extract data without loops.
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

part = arr[1:4]

part[0] = 999

print("part:", part)
print("arr :", arr)

# Output:
# part: [999  30  40]
# arr : [ 10 999  30  40  50]


arr = np.array([10,20,30,40,50])

print(arr[1:4])

print(arr[[1,4]])#fancy indexing creates a copy, not a view
# [20 50]