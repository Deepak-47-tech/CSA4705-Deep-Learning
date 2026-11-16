import numpy as np

A = np.array([[3, 3], [2, 5]])

print("Matrix:\n", A)
print("Determinant:", np.linalg.det(A))
print("Rank:", np.linalg.matrix_rank(A))

if np.linalg.det(A) != 0:
    print("Inverse:\n", np.linalg.inv(A))
    print("Matrix is suitable for invertible matrix encryption.")
else:
    print("Inverse does not exist.")
