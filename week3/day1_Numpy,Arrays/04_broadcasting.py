import numpy as np

matrix = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

vector = np.array([10,20,30,40])

print(matrix + vector)

a = np.array([1,2,3])

b = np.array([
    [10],
    [20],
    [30]
])

print(a.shape)
# (3,)

print(b.shape)
# (3,1)

print(a + b)

x = np.array([1,2,3])
expanded = np.broadcast_to(x, (4,3))
print(expanded)
#in reality the expanded array is not actually created in memory, but rather a view that behaves as if it were expanded. 
# This is one of the reasons why broadcasting is efficient in NumPy.

"""
04_broadcasting.py

Topics:
1. Scalar broadcasting
2. Matrix + vector
3. Shape compatibility rules
4. Broadcasting failures
5. Mean normalization
6. np.broadcast_to()
7. Memory-efficient expansion

Goal:
Understand how NumPy performs loop-free calculations.
"""