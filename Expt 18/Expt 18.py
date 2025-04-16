import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5, 6])  # Fixed: Removed extra []
print("1D Array:\n", arr_1d)

# Creating a 2D array (3x3 matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Fixed: Added missing ]
print("\n2D Array:\n", arr_2d)

# Creating a 3D array (2x3x3)
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
])
print("\n3D Array:\n", arr_3d)

# Reshaping 1D to 2D
reshaped_arr = arr_1d.reshape(2, 3)
print("\nReshaped 1D to 2D (2x3):\n", reshaped_arr)

# Slicing 2D array
slice_2d = arr_2d[0:2, 1:3]  # Rows 0-1, Columns 1-2
print("\nSliced 2D Array (Rows 0-1, Columns 1-2):\n", slice_2d)

# Indexing
element_2d = arr_2d[1, 2]  # Row 1, Column 2
print("\nElement at Row 1, Column 2 in 2D Array:", element_2d)

element_3d = arr_3d[1, 2, 1]  # Second matrix, Row 2, Column 1
print("Element at [1,2,1] in 3D Array:", element_3d)
