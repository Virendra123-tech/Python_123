import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
])
top = arr[0]
bottom = arr[-1]
left = arr[1:-1, 0]
right = arr[1:-1, -1]
print(right,left)