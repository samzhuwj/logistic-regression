import numpy as np
from sigmoid import *


def predict(theta, X):
    """
    logistic regression prediction function
    """
    m = X.shape[0]

    # Return the following variable correctly
    p = np.zeros(m)

    # ===================== Your Code Here =====================
    # Instructions : Complete the following code to make predictions using
    #                your learned logistic regression parameters.
    #                You should set p to a 1D-array of 0's and 1's
    #

    p = sigmoid(np.dot(X, theta))
    pos = np.where(p >= 0.5)
    neg = np.where(p < 0.5)

    p[pos] = 1
    p[neg] = 0

    # ===========================================================

    return p
