import os
import sys
import numpy as np
# Adding parent folder:
sys.path.append(os.getcwd())
from utils import (
    plot_plane,
    prepare_flattened_2D_plane
)

def main(conf:dict) -> None:
    
    # Creating output folder:
    if not os.path.exists(conf['output_data_path']):
        os.mkdir(conf['output_data_path'])
        
    # Create flattened_plane:
    flattened_plane = prepare_flattened_2D_plane()
    
    # Plotting raw plane:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__raw_plane.png'
    )
    plot_plane(
        object_2D=flattened_plane,
        output_path=plane_path
    )
    
    ##########
    # Identity matrix:
    matrix_1 = np.array([
        [1, 0],
        [0, 1]
    ])
    # Calculating plane 1:
    plane_1 = matrix_1 @ flattened_plane

    # Plot plane 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__identity_matrix.png'
    )
    plot_plane(
        object_2D=plane_1,
        output_path=plane_path
    )

    ##########
    # Scalar matrix 1:
    matrix_2 = np.array([
        [2, 0],
        [0, 2]
    ])
    # Calculating plane 2:
    plane_2 = matrix_2 @ flattened_plane

    # Plot plane 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__scalar_matrix_1.png'
    )
    plot_plane(
        object_2D=plane_2,
        output_path=plane_path
    )

    ##########
    # Scalar matrix 2:
    matrix_3 = np.array([
        [0.5,   0],
        [  0, 0.5]
    ])
    # Calculating plane 3:
    plane_3 = matrix_3 @ flattened_plane

    # Plot plane 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__scalar_matrix_2.png'
    )
    plot_plane(
        object_2D=plane_3,
        output_path=plane_path
    )

    #########
    # Off-one matrix 1:
    matrix_4 = np.array([
        [2, 0],
        [0, 1]
    ])
    # Calculating plane 4:
    plane_4 = matrix_4 @ flattened_plane
    
    # Plot plane 4:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__off-one_matrix_1.png'
    )
    plot_plane(
        object_2D=plane_4,
        output_path=plane_path
    )

    #########
    # Off-one matrix 2:
    matrix_5 = np.array([
        [1, 0],
        [0, 2]
    ])
    # Calculating plane 5:
    plane_5 = matrix_5 @ flattened_plane
    # Plot plane 5:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__off-one_matrix_2.png'
    )
    plot_plane(
        object_2D=plane_5,
        output_path=plane_path
    )

    #########
    # Reflection matrix 1:
    matrix_6 = np.array([
        [-1, 0],
        [ 0, 1]
    ])
    # Calculating plane 6:
    plane_6 = matrix_6 @ flattened_plane
    
    # Plot plane 6:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__reflexion_matrix_1.png'
    )
    plot_plane(
        object_2D=plane_6,
        output_path=plane_path
    )
    
    #########
    # Reflection matrix 2:
    matrix_7 = np.array([
        [1,  0],
        [0, -1]
    ])
    # Calculating plane 7:
    plane_7 = matrix_7 @ flattened_plane
    
    # Plot plane 7:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__reflexion_matrix_2.png'
    )
    plot_plane(
        object_2D=plane_7,
        output_path=plane_path
    )

    #########
    # Reflection matrix 3:
    matrix_8 = np.array([
        [-1,  0],
        [ 0, -1]
    ])
    # Calculating plane 8:
    plane_8 = matrix_8 @ flattened_plane

    # Plot plane 8:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__reflexion_matrix_3.png'
    )
    plot_plane(
        object_2D=plane_8,
        output_path=plane_path
    )

    #########
    # Diagonal matrix:
    matrix_9 = np.array([
        [-2.5,  0],
        [ 0, 0.6]
    ])
    # Calculating plane 9:
    plane_9 = matrix_9 @ flattened_plane
    
    # Plot plane 9:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_2__diagonal.png'
    )
    plot_plane(
        object_2D=plane_9,
        output_path=plane_path
    )


if __name__ == '__main__':
    
    conf = {
        'output_data_path': '1_visualize_different_matrices/output_data/ex_2'
    }
    main(conf=conf)