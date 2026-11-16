import numpy as np

A = np.array([5, 2, 0, 1])
B = np.array([4, 1, 1, 0])

dot = np.dot(A, B)

cosine = dot / (
    np.linalg.norm(A) * np.linalg.norm(B)
)

print("Dot Product:", dot)
print("Cosine Similarity:", cosine)
