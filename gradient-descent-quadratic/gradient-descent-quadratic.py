def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    res = x0
    f = 2 * a * x0 + b
    for _ in range(steps):
        res -= lr * f
        f = 2 * a * res + b

    return float(res)