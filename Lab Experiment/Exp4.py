import numpy as np

P = np.array([
    [0, 0.5, 0.5],
    [0.5, 0, 0.5],
    [0.5, 0.5, 0]
])

values, vectors = np.linalg.eig(P)

print("Transition Matrix:\n", P)
print("Eigenvalues:\n", values)
print("Eigenvectors:\n", vectors)

index = np.argmin(abs(values - 1))
rank = abs(vectors[:, index])
rank = rank / sum(rank)

print("Page Ranking:", rank)
print("Important Page:", np.argmax(rank) + 1)
