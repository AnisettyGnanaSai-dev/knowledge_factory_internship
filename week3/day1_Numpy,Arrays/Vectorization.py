"""
| Function      | Purpose        |
| ------------- | -------------- |
| np.add()      | Addition       |
| np.subtract() | Subtraction    |
| np.multiply() | Multiplication |
| np.divide()   | Division       |
| np.sqrt()     | Square root    |
| np.exp()      | e^x            |
| np.log()      | Natural log    |
| np.sin()      | Sine           |
| np.cos()      | Cosine         |
| np.abs()      | Absolute value |

"""

"""
05_vectorized_math.py

Topics:
1. Ufuncs
2. Element-wise operations
3. Aggregations
4. Axis understanding
5. np.where()
6. np.any()
7. np.all()
8. np.dot()
9. Matrix multiplication
10. Euclidean distance

Goal:
Replace loops with vectorized operations.
"""
import numpy as np

a = np.array([1, 2, 3])

print(a + 10)

# [11 12 13]
a = np.array([10, 20, 30])

print(a - 5)

# [ 5 15 25]
a = np.array([1, 2, 3])

print(a * 4)

# [ 4  8 12]
a = np.array([10, 20, 30])

print(a / 10)

# [1. 2. 3.]
a = np.array([1, 2, 3, 4])

print(a ** 2)

# [ 1  4  9 16]

a = np.array([1, 4, 9, 16])

print(np.sqrt(a))

# [1. 2. 3. 4.]

a = np.array([1, 2, 3])

print(np.exp(a))

# [ 2.71828183  7.3890561  20.08553692]

a = np.array([1, np.e, np.e**2])

print(np.log(a))

# [0. 1. 2.]

a = np.array([-10, -5, 3])

print(np.abs(a))

# [10  5  3]

a = np.array([0, np.pi/2, np.pi])

print(np.sin(a))

# [0. 1. 0.]

a = np.array([0, np.pi])

print(np.cos(a))

# [ 1. -1.]

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(np.sum(arr))

# 45
print(np.mean(arr))

# 5.0
print(np.std(arr))

# 2.581988897471611
print(np.min(arr))

# 1
print(np.max(arr))

# 9
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(np.sum(arr, axis=0))

# [12 15 18]
print(np.sum(arr, axis=1))

# [ 6 15 24]
a = np.array([1,5,10,15])
print(a > 5)

# [False False True True]
print(a < 10)

# [ True True False False]
print(a == 10)

# [False False True False]
a = np.array([False, False, True])

print(np.any(a))

# True
a = np.array([True, True, True])

print(np.all(a))

# True
marks = np.array([35, 60, 80, 25])

result = np.where(marks >= 40,
                  "PASS",
                  "FAIL")

print(result)

# ['FAIL' 'PASS' 'PASS' 'FAIL']

a = np.array([1,2,3])

b = np.array([4,5,6])

print(np.dot(a,b))

# 32
A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(A @ B)

# [[19 22]
#  [43 50]]

a = np.array([1,2,3])

b = np.array([4,6,8])

dist = np.sqrt(
    np.sum((a-b)**2)
)

print(dist)

# 7.0710678118654755