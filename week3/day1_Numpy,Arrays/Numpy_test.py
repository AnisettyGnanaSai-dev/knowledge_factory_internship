import time
import numpy as np

n = 1000000
m = []

t1 = time.time()
for i in range(n):
    m.append(i * 2)

t2 = time.time()
t3 = time.time()
arr =  np.arange(n) * 2
t4 = time.time()

print("List time: ", (t2 - t1)*10000, "ms")
print("Numpy time: ", (t4 - t3)*10000, "ms")

arr1 = np.arange(10)
print(arr1.dtype)
print(arr1.itemsize)
print(arr1.nbytes)
print(arr1.shape)
print(arr1.size)

"""
01_why_numpy.py

Purpose:
Demonstrates why NumPy exists.

Topics:
1. Python list vs NumPy performance
2. Contiguous memory
3. Fixed dtypes
4. Vectorized multiplication
5. Timing comparison
"""