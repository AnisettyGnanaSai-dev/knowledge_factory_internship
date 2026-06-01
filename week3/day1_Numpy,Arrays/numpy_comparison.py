import timeit
import numpy as np
import statistics

python_time = timeit.timeit(
  "sum(data)",
  setup = """data = list(range(1000000))""",
  number = 10

 )
print(python_time)


numpy_time = timeit.timeit(
    "np.sum(data)",
    setup="""
import numpy as np
data = np.arange(1000000)
""",
    number=10
)

print(numpy_time)


python_time = timeit.timeit(
    "[x*2 for x in data]",
    setup="""
data = list(range(1000000))
""",
    number=10
)

numpy_time = timeit.timeit(
    "arr * 2",
    setup="""
import numpy as np
arr = np.arange(1000000)
""",
    number=10
)

print(python_time)
print(numpy_time)


python_time = timeit.timeit(
    "statistics.mean(data)",
    setup="""
import statistics
data = list(range(1000000))
""",
    number=10
)

numpy_time = timeit.timeit(
    "np.mean(data)",
    setup="""
import numpy as np
data = np.arange(1000000)
""",
    number=10
)

print(python_time)
print(numpy_time)



results = []

# ------------------
# Test 1
# ------------------

py_sum = timeit.timeit(
    "sum(data)",
    setup="""
data = list(range(1000000))
""",
    number=10
)

np_sum = timeit.timeit(
    "np.sum(data)",
    setup="""
import numpy as np
data = np.arange(1000000)
""",
    number=10
)

results.append(
    (
        "sum",
        py_sum,
        np_sum,
        py_sum/np_sum
    )
)

# ------------------
# Test 2
# ------------------

py_mult = timeit.timeit(
    "[x*2 for x in data]",
    setup="""
data = list(range(1000000))
""",
    number=10
)

np_mult = timeit.timeit(
    "arr * 2",
    setup="""
import numpy as np
arr = np.arange(1000000)
""",
    number=10
)

results.append(
    (
        "multiply",
        py_mult,
        np_mult,
        py_mult/np_mult
    )
)

# ------------------
# Print Table
# ------------------

print(
    f"{'Test':15}"
    f"{'Python':15}"
    f"{'NumPy':15}"
    f"{'Speedup':15}"
)

for row in results:

    print(
        f"{row[0]:15}"
        f"{row[1]:15.4f}"
        f"{row[2]:15.4f}"
        f"{row[3]:15.2f}x"
    )
