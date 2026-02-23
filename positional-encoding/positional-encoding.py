import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    matrix = np.zeros((seq_len, d_model))
    for pos in range(seq_len):
        for dim in range(d_model):
            temp = pos / np.power(base, 2 * (dim // 2) / d_model)
            if dim % 2 == 0:
                matrix[pos, dim] = np.sin(temp)
            else:
                matrix[pos, dim] = np.cos(temp)

    return matrix