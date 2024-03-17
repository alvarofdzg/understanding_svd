'''
In this script we show how some rectangular matrices work.
'''
import numpy as np


def main() -> None:
    
    # Dimension Eraser:
    print('\nDimension Eraser Matrix:')
    matrix_1 = np.array([
        [ 1, 0, 0],
        [ 0, 1, 0]
    ])
    print(matrix_1)
    
    matrix_2 = np.array([
        [1],
        [2],
        [7]
    ])
    result_1 = matrix_1 @ matrix_2
    print('The first matrix is:')
    print(matrix_2)
    print('And the result after using Dimension Eraser is:')
    print(result_1)

    matrix_3 = np.array([
        [1],
        [2],
        [1]
    ])
    result_2 = matrix_1 @ matrix_3
    print('The second matrix is:')
    print(matrix_3)
    print('And the result after using Dimension Eraser is:')
    print(result_2)

    matrix_4 = np.array([
        [ 1],
        [ 2],
        [11]
    ])
    result_3 = matrix_1 @ matrix_4
    print('The third matrix is:')
    print(matrix_4)
    print('And the result after using Dimension Eraser is:')
    print(result_3)
    
    # Dimension Adder:
    print('\n\nDimension Adder Matrix:')
    matrix_1 = np.array([
        [ 1, 0],
        [ 0, 1],
        [ 0, 0]
    ])
    print(matrix_1)
    
    matrix_2 = np.array([
        [1],
        [2]
    ])
    result_1 = matrix_1 @ matrix_2
    print('The first matrix is:')
    print(matrix_2)
    print('And the result after using Dimension Adder is:')
    print(result_1)

    matrix_3 = np.array([
        [3],
        [6]
    ])
    result_2 = matrix_1 @ matrix_3
    print('The second matrix is:')
    print(matrix_3)
    print('And the result after using Dimension Adder is:')
    print(result_2)

    matrix_4 = np.array([
        [ 4],
        [ 8]
    ])
    result_3 = matrix_1 @ matrix_4
    print('The third matrix is:')
    print(matrix_4)
    print('And the result after using Dimension Adder is:')
    print(result_3)



if __name__ == '__main__':
    main()