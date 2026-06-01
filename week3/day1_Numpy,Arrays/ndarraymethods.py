import numpy as np

arr = np.array([1,2,3,4])

print(arr * 2)

weights = np.zeros((3,4))

print(weights)

arr = np.full((3,3), 7)

print(arr)

arr = np.arange(10)

print(arr)

arr = np.arange(0,20,2)

print(arr)

arr = np.linspace(0,10,5)
print(arr)

arr = np.arange(0,1,0.2)
print(arr)

I = np.eye(4)

print(I)

arr = np.empty((3,3))

print(arr)

arr = np.random.rand(3,3)

print(arr)

weights = np.random.rand(64,3,3,3)
print(weights)