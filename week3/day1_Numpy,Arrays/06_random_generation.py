"""
06_random_generation.py

NumPy Random Module Complete Practice

Topics Covered:
1. np.random.seed()
2. np.random.rand()
3. np.random.randn()
4. np.random.randint()
5. np.random.choice()
6. np.random.shuffle()
7. np.random.normal()
8. np.bincount()
9. Synthetic ML Dataset Generation

Run:
python 06_random_generation.py
"""

import numpy as np

# =====================================================
# 1. RANDOM SEED
# =====================================================

print("\n" + "="*50)
print("1. RANDOM SEED")
print("="*50)

np.random.seed(42)

print(np.random.rand(5))

# Expected:
# [0.37454012 0.95071431 0.73199394 0.59865848 0.15601864]


# =====================================================
# 2. RANDOM FLOATS (UNIFORM DISTRIBUTION)
# =====================================================

print("\n" + "="*50)
print("2. np.random.rand()")
print("="*50)

random_floats = np.random.rand(3, 4)

print(random_floats)
print("Shape:", random_floats.shape)

# Values between:
# 0 <= x < 1


# =====================================================
# 3. RANDOM NORMAL DISTRIBUTION
# =====================================================

print("\n" + "="*50)
print("3. np.random.randn()")
print("="*50)

normal_values = np.random.randn(3, 4)

print(normal_values)

print("Mean:", np.mean(normal_values))
print("Std :", np.std(normal_values))

# Mean approximately 0
# Std approximately 1


# =====================================================
# 4. RANDOM INTEGERS
# =====================================================

print("\n" + "="*50)
print("4. np.random.randint()")
print("="*50)

dice_rolls = np.random.randint(
    1,
    7,
    size=20
)

print("Dice Rolls:")
print(dice_rolls)

# Integers from 1 to 6


# =====================================================
# 5. RANDOM CHOICE
# =====================================================

print("\n" + "="*50)
print("5. np.random.choice()")
print("="*50)

fruits = np.array([
    "Apple",
    "Banana",
    "Orange",
    "Mango"
])

selected = np.random.choice(
    fruits,
    size=10
)

print(selected)


# =====================================================
# 6. CHOICE WITH PROBABILITY
# =====================================================

print("\n" + "="*50)
print("6. WEIGHTED CHOICE")
print("="*50)

fraud_labels = np.random.choice(
    [0, 1],
    size=50,
    p=[0.95, 0.05]
)

print(fraud_labels)

print("Fraud Count:", np.sum(fraud_labels))


# =====================================================
# 7. SHUFFLE
# =====================================================

print("\n" + "="*50)
print("7. np.random.shuffle()")
print("="*50)

students = np.arange(1, 11)

print("Before Shuffle:")
print(students)

np.random.shuffle(students)

print("After Shuffle:")
print(students)


# =====================================================
# 8. CUSTOM NORMAL DISTRIBUTION
# =====================================================

print("\n" + "="*50)
print("8. np.random.normal()")
print("="*50)

heights = np.random.normal(
    loc=170,     # mean
    scale=10,    # std deviation
    size=20
)

print("Sample Heights:")
print(heights)

print("Average Height:", np.mean(heights))
print("Std Deviation :", np.std(heights))


# =====================================================
# 9. SIMULATE 10,000 DICE ROLLS
# =====================================================

print("\n" + "="*50)
print("9. DICE SIMULATION")
print("="*50)

rolls = np.random.randint(
    1,
    7,
    size=10000
)

counts = np.bincount(rolls)

print("Face Counts:")

for face in range(1, 7):
    print(
        f"Face {face}: {counts[face]}"
    )

# Approximately:
# 10000 / 6 = 1667 each


# =====================================================
# 10. np.bincount()
# =====================================================

print("\n" + "="*50)
print("10. np.bincount()")
print("="*50)

numbers = np.array([
    1, 1, 1,
    2, 2,
    3,
    4, 4, 4, 4
])

frequency = np.bincount(numbers)

print(frequency)

# Meaning:
# Index 0 -> count of 0
# Index 1 -> count of 1
# Index 2 -> count of 2
# Index 3 -> count of 3
# Index 4 -> count of 4


# =====================================================
# 11. SYNTHETIC ML DATASET
# =====================================================

print("\n" + "="*50)
print("11. SYNTHETIC DATASET")
print("="*50)

np.random.seed(42)

students = 100

study_hours = np.random.normal(
    5,
    2,
    students
)

attendance = np.random.randint(
    60,
    101,
    students
)

marks = (
    study_hours * 10
    + attendance * 0.5
    + np.random.normal(
        0,
        5,
        students
    )
)

dataset = np.column_stack(
    (
        study_hours,
        attendance,
        marks
    )
)

print("Dataset Shape:")
print(dataset.shape)

print("\nFirst 5 Rows:")
print(dataset[:5])

# Columns:
# Study Hours
# Attendance
# Marks


# =====================================================
# 12. TRAIN-TEST SPLIT STYLE SHUFFLE
# =====================================================

print("\n" + "="*50)
print("12. TRAIN TEST SHUFFLE")
print("="*50)

indices = np.arange(100)

np.random.shuffle(indices)

train_idx = indices[:80]
test_idx = indices[80:]

print("Train Size:", len(train_idx))
print("Test Size :", len(test_idx))

# Train: 80
# Test : 20


# =====================================================
# 13. MODERN RANDOM GENERATOR
# =====================================================

print("\n" + "="*50)
print("13. default_rng()")
print("="*50)

rng = np.random.default_rng(42)

print(rng.random(5))

print(
    rng.integers(
        1,
        10,
        size=5
    )
)

# Modern NumPy approach


# =====================================================
# END
# =====================================================

print("\n" + "="*50)
print("STEP 6 COMPLETE")
print("="*50)