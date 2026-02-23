import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here

    x_samples, x_features = X.shape
    weights = np.zeros(x_features)
    bias = 0

    for _ in range(steps):
        linear_model = np.dot(X, weights) + bias
        y_predict = _sigmoid(linear_model)

        dw = (1/x_samples) * np.dot(X.T, y_predict - y)
        db = (1/x_samples) * np.sum(y_predict - y)

        weights -= lr * dw
        bias -= lr * db
    
    return weights, bias