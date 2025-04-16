import numpy as np

# Creating two arrays of the same shape
arr1 = np.array([[2, 4, 6], [8, 10, 12]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("Array 1:\n", arr1)
print("\nArray 2:\n", arr2)

# Element-wise operations
addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

print("\nElement-wise Addition:\n", addition)
print("\nElement-wise Subtraction:\n", subtraction)
print("\nElement-wise Multiplication:\n", multiplication)
print("\nElement-wise Division:\n", division)

# Dot Product of Two Vectors
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])

dot_product = np.dot(vec1, vec2)
print("\nDot Product of vec1 and vec2:", dot_product)

# Cross Product of Two Vectors
cross_product = np.cross(vec1, vec2)
print("Cross Product of vec1 and vec2:", cross_product)
