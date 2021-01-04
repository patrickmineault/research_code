import matplotlib.pyplot as plt
import numpy as np
import os
import pickle


"""Run a linear centered-kernel alignment (CKA) to find how close two 
latent representations of 

Kornblith et al. (2019) https://arxiv.org/abs/1905.00414

Load data from ../data and compare them. All the matrices in 
../data/matrices.pkl have the same height (number of examplars) but 
potentially different numbers of columns.
"""
f = open('../data/matrices.pkl', 'rb')
data = pickle.load(f)['reps']

cka = np.zeros((5, 5))
for i in range(5):
    for j in range(i+1, 5):
        X, Y = data[i], data[j]
        X = (X - X.mean(0).reshape((1, -1)))
        Y = (Y - Y.mean(0).reshape((1, -1)))
        
        XTX = X.T.dot(X)
        YTY = Y.T.dot(Y)
        YTX = Y.T.dot(X)

        # Equation (4)
        cka[i, j] = (YTX ** 2).sum() / np.sqrt((XTX * XTX).sum() * (YTY * YTY).sum())

cka = cka + cka.T
cka = cka + np.eye(cka.shape[0])

plt.figure()
plt.imshow(cka)
plt.colorbar()
plt.xticks([0, 1, 2, 3, 4], ['baseline', 'rescaled', 'nuisance', 'truncated1', 'truncated2'])
plt.yticks([0, 1, 2, 3, 4], ['baseline', 'rescaled', 'nuisance', 'truncated1', 'truncated2'])
plt.title('Similarity of different representations (CKA)')

# os.makedirs('../results')
plt.savefig('../results/closeness.png')

