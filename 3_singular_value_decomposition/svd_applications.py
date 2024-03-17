'''
In this script we show how some rectangular matrices work.
'''
import numpy as np


def main() -> None:
    
    # Pseudoinverse:
    print('\nPseudoinverse:')
    print('Ax=b')
    A = np.array([
        [1, 0],
        [0, 1],
        [1, 1]
    ])
    print('A:\n', A)
    
    b = np.array([
        [1],
        [1],
        [0]
    ])
    print('b:\n', b)
    
    # Calculate SVD:
    U, S, Vt = np.linalg.svd(A, full_matrices=True)
    
    # Prepare S inverse:
    n_rows, n_cols = A.shape
    S_inv = np.zeros((n_cols, n_rows))
    S_inv[:min(n_rows, n_cols), :min(n_rows, n_cols)] = np.diag(1 / S)
    
    # Calculate x:
    x = (Vt.T @ S_inv @ U.T) @ b
    print('x:\n', x)


if __name__ == '__main__':
    main()