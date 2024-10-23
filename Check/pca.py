import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()

X = iris['data']
y = iris['target']

# standarize data
mean = np.mean(X, axis=0)
stdev = np.std(X, axis=0)
X = (X - mean) / stdev

# covarience matrix
cov_mat = np.cov(X.T)

# eigenvalues & eigenvectors of covarience matrix
eigval, eigvec = np.linalg.eig(cov_mat)
eigvec = eigvec.T

# sort eigenvalues & eigenvectors in decreasing order
idx = np.argsort(eigval)[::-1]
eigval = eigval[idx]
eigvec = eigvec[idx]

# choose principal components
k = 2
comp = eigvec[:k]

# transform into k-dimensions
X_new = X.dot(comp.T)

plt.scatter(X_new[:, 0], X_new[:, 1], c = y)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()

eigval_total = sum(eigval)
explained_variance = [(i / eigval_total)*100 for i in eigval]
explained_variance = np.round(explained_variance, 2)
cum_explained_variance = np.cumsum(explained_variance)

print('Explained variance: {}'.format(explained_variance))
print('Cumulative explained variance: {}'.format(cum_explained_variance))

plt.plot(np.arange(1,X.shape[1]+1), cum_explained_variance, '-o')
plt.xticks(np.arange(1,X.shape[1]+1))
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance');
plt.show()