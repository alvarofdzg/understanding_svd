'''
This script shows two differents applications of Singular Value Decomposition.
- 1. Apply SVD to calculate the Pseudoinverse and solve Least Squares.
- 2. Apply SVD to show how the different eigen vectors contribute in an image.
'''
import os
import sys
import cv2 as cv
import numpy as np
# Adding parent folder:
sys.path.append(os.getcwd())
from utils import (
    plot_image_decomposition
)

def main(conf:dict) -> None:
    
    # Creating output folder:
    if not os.path.exists(conf['output_data_path']):
        os.mkdir(conf['output_data_path'])
        
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
    U, s, Vt = np.linalg.svd(A, full_matrices=True)
    
    # Prepare S inverse:
    n_rows, n_cols = A.shape
    S_inv = np.zeros((n_cols, n_rows))
    len_diag = min(n_rows, n_cols)
    S_inv[:len_diag, :len_diag] = np.diag(1 / s)
    
    # Calculate x:
    x = (Vt.T @ S_inv @ U.T) @ b
    print('x:\n', x)
    print('Done!')


    ########
    # SVD Decomposition of an image:
    print('\n\nSVD decomposition of an image:')
    # Read skyline image:
    skyline_path = os.path.join(
        conf['input_data_path'],
        'skyline_NY.jpg'
    )
    skyline_bgr = cv.imread(skyline_path)

    # Convert to grayscale:
    skyline_grayscale = cv.cvtColor(skyline_bgr, cv.COLOR_BGR2GRAY)
    
    # Calculate the SVD of the image:
    U, s, Vt = np.linalg.svd(skyline_grayscale, full_matrices=True)
    
    # Building S:
    S = np.zeros((skyline_grayscale.shape[0], skyline_grayscale.shape[1]))
    S[:len(s), :len(s)] = np.diag(s)

    # Plotting Skyline decomposition:
    skyline_decomposition_path = os.path.join(
        conf['output_data_path'],
        'skyline_decomposition.png'
    )
    plot_image_decomposition(
        original_image=skyline_grayscale,
        U=U, 
        S=S, 
        Vt=Vt, 
        output_path=skyline_decomposition_path)
    print('Done!')


if __name__ == '__main__':
    
    conf = {
        'output_data_path': '3_singular_value_decomposition/output_data/svd_applications',
        'input_data_path': 'data'
    }
    main(conf=conf)