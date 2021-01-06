from typing import List
import os
import seaborn as sns

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

def cka(X, Y):
    """
    Calculate CKA for two matrices

    Use a non-naive algorithm involving the SVD. This is faster when X or Y 
    (or both) are much wider than tall.
    """
    X = X - X.mean(0, keepdims=True)
    Y = Y - Y.mean(0, keepdims=True)

    Ux, Sx, _ = np.linalg.svd(X, full_matrices=False)
    Uy, Sy, _ = np.linalg.svd(Y, full_matrices=False)

    # Equation 14
    bottom = np.sqrt((Sy ** 4).sum() * (Sx ** 4).sum())
    top = np.sum((Sy ** 2) @ (Uy.T  @ Ux) ** 2 @ (Sx ** 2))

    c = top / bottom

    return c


def multi_cka(reps: List[np.array]) -> np.array:
    """
    Calculate CKA matrix for a list of matrices.

    Kornblith et al. (2019) https://arxiv.org/abs/1905.00414

    Args:
        reps: a list of representations of the same data from different 
              networks. All have the same height (number of examplars) but 
              potentially different numbers of columns.

    Returns:
        the CKA matrix (larger values mean more similar).
    """
    C = np.zeros((len(reps), len(reps)))
    for i in range(len(reps)):
        C[i, i] = 1.0 # by definition
        for j in range(i+1, len(reps)):
            c = cka(reps[i], reps[j])

            C[i, j] = c
            C[j, i] = c

    return C

def main():
    with open ('../data/matrices.pkl', 'rb') as f:
        data = pickle.load(f)

    C = multi_cka(data['reps'])

    df = pd.DataFrame(C)
    df.index = data['models']
    df.columns = data['models']

    ax = sns.heatmap(df, annot=True, fmt='.2f')
    try:
        os.makedirs('../results')
    except FileExistsError:
        pass

    plt.title('Similarity of different representations (CKA)')
    plt.savefig('../results/closeness_sns.png')

if __name__ == "__main__":
    main()

        

