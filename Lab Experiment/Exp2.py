import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Multiplication:\n", np.dot(A, B))
print("Transpose of A:\n", A.T)
