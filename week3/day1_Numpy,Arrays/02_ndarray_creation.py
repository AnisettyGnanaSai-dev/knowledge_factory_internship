"""
02_ndarray_creation.py

Topics Covered:
1. np.array()
2. np.zeros()
3. np.ones()
4. np.full()
5. np.arange()
6. np.linspace()
7. np.eye()
8. np.empty()
9. np.random.rand()
10. np.random.randn()

Also prints:
shape
ndim
dtype
size
itemsize
"""

import numpy as np

arrays = {
    "zeros": np.zeros((2,2)),
    "ones": np.ones((2,2)),
    "full": np.full((2,2), 7),
    "arange": np.arange(4),
    "linspace": np.linspace(0,1,5),
    "eye": np.eye(2)
}

for name, arr in arrays.items():
    print(f"\n{name}")
    print(arr)
    print("shape:", arr.shape)
    print("dtype:", arr.dtype)