import numpy as np
import cv2
import matplotlib.pyplot as plt

def my_svd(A):
    # compute A^T * A
    AtA = np.dot(A.T, A)

    # eigenvalues & eigenvectors of A^T * A
    eigvals, eigvecs = np.linalg.eig(AtA)

    # sort eigenvalues & eigenvectors in decreasing order
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    # singular values
    singular_values = np.sqrt(eigvals)

    # U = A * V * S.T
    U = np.zeros((A.shape[0], A.shape[0]), dtype=float)
    for i in range(len(singular_values)):
        U[:, i] = np.dot(A, eigvecs[:, i]) / singular_values[i]

    # fill singular values diagonally
    S = np.zeros((U.shape[0], eigvecs.shape[1]), dtype=float)
    for i in range(len(singular_values)):
        S[i, i] = singular_values[i]

    return U, S, eigvecs.T

img = cv2.imread('lenna.tiff', cv2.IMREAD_GRAYSCALE).astype(float)
img /= 255.0    # normalize in range [0, 1]

plt.figure(figsize=(3,3))
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()

U, S, Vt = my_svd(img)    # decompose using SVD

# re construct image with different level of compression
for k in [5, 25, 50, 100]:
    img2 = np.dot(U[:, :k], np.dot(S[:k, :k], Vt[:k, :]))    # A = U * S * V.T
    # rescale to range [0, 255]
    img2 *= 255.0
    img2 = np.clip(img2, 0, 255).astype(np.uint8)

    plt.figure(figsize=(3,3))
    plt.imshow(img2, cmap='gray')
    plt.title(f'k = {k}')
    plt.axis('off')
    plt.show()

total_variance = np.sum(S**2) #Total sum of squared singular values
variance_ratios = []

for i in range(5, 512, 20):
    # Calculate the variance captured by the first i singular values
    captured_variance = np.sum(S[:i]**2)  # Sum of squared singular values
    variance_ratio = captured_variance / total_variance  # Proportion of total variance
    variance_ratios.append(variance_ratio)

plt.plot(range(5, 512, 20), variance_ratios, marker='o')
plt.xlabel('Number of Singular Values')
plt.ylabel('Variance Captured')
plt.title('Variance Captured by Each Number of Singular Values')
plt.grid(True)
plt.show()
