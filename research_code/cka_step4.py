from typing import List
import os
import seaborn as sns

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle


def cka_wide(X, Y):
    """
    Calculate CKA for two matrices. This algorithm uses a Gram matrix 
    implementation, which is fast when the data is wider than it is 
    tall.

    This implementation is inspired by the one in this colab:
    https://colab.research.google.com/github/google-research/google-research/blob/master/representation_similarity/Demo.ipynb#scrollTo=MkucRi3yn7UJ

    Note that we use center the features rather than the Gram matrix
    because we think the latter is tricky and mysterious. It only works for 
    linear CKA though (we only implement linear CKA throughout).
    """     
    X = X - X.mean(0, keepdims=True)
    Y = Y - Y.mean(0, keepdims=True)

    XXT = X @ X.T
    YYT = Y @ Y.T

    top = (XXT.ravel() * YYT.ravel()).sum()
    bottom = np.sqrt((XXT ** 2).sum() * (YYT ** 2).sum())
    c = top / bottom

    return c


def cka_tall(X, Y):
    """
    Calculate CKA for two matrices.
    """
    X = X - X.mean(0, keepdims=True)
    Y = Y - Y.mean(0, keepdims=True)
            
    XTX = X.T @ X
    YTY = Y.T @ Y
    YTX = Y.T @ X

    # Equation (4)
    top = (YTX ** 2).sum()
    bottom = np.sqrt((XTX ** 2).sum() * (YTY ** 2).sum())
    c = top / bottom

    return c

def cka(X, Y):
    """
    Calculate CKA for two matrices.

    CKA has several potential implementations. The naive implementation is 
    appropriate for tall matrices (more examples than features), but this 
    implementation uses lots of memory and it slow when there are many more 
    features than examples. In that case, which often happens with DNNs, we 
    prefer the Gram matrix variant.
    """
    
    if X.shape[0] < X.shape[1]:
        return cka_wide(X, Y)
    else:
        return cka_tall(X, Y)


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

        

