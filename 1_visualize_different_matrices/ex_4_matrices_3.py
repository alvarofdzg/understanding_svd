'''
In this script we work with the Orthogonal matrix.
'''
import os
import sys
import numpy as np
# Adding parent folder:
sys.path.append(os.getcwd())
from utils import (
    plot_plane,
    prepare_flattened_2D_plane,
    prepare_flattened_3D_plane,
    plot_cube
)


def main(conf:dict) -> None:

    # Creating output folder:
    if not os.path.exists(conf['output_data_path']):
        os.mkdir(conf['output_data_path'])
        
    # Create flattened_box:
    flattened_plane = prepare_flattened_2D_plane()

    # Plotting raw plane:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_4__raw_plane.png'
    )
    plot_plane(
        object_2D=flattened_plane,
        output_path=plane_path
    )
    
    ##########
    # Orthogonal matrix 1:
    matrix_1 = np.array([
        [np.sqrt(2) / 2, np.sqrt(2) / 2],
        [-np.sqrt(2) / 2, np.sqrt(2) / 2]
    ])
    # Calculating plane 1:
    plane_1 = matrix_1 @ flattened_plane
    
    # Plotting plane 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_4__plane_orthogonal_matrix_1.png'
    )
    plot_plane(
        object_2D=plane_1,
        output_path=plane_path
    )
    
    ##########
    # Orthogonal matrix 2:
    matrix_2 = np.array([
        [0,  1],
        [-1, 0]
    ])
    # Calculating plane 2:
    plane_2 = matrix_2 @ flattened_plane
    
    # Plotting plane 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_4__plane_orthogonal_matrix_2.png'
    )
    plot_plane(
        object_2D=plane_2,
        output_path=plane_path
    )
    
    ##########
    # Orthogonal matrix 3:
    matrix_3 = np.array([
        [1, 0],
        [1, 1]
    ])
    # Calculating plane 3:
    plane_3 = matrix_3 @ flattened_plane
    
    # Plotting plane 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_4__plane_orthogonal_matrix_3.png'
    )
    plot_plane(
        object_2D=plane_3,
        output_path=plane_path
    )

    ##########
    ##########
    # Create flattened_box:
    flattened_box = prepare_flattened_3D_plane()
    
    # Plotting raw box:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_4__raw_box.png'
    )
    plot_cube(
        object_3D=flattened_box,
        output_path=plane_path)

    ##########
    # Orthogonal matrix 4:
    matrix_4 = np.array([
        [1,              0,               0],
        [0,          1 / 2, -np.sqrt(3) / 2],
        [0, np.sqrt(3) / 2,           1 / 2]
    ])
    # Calculating box 1:
    box_1 = matrix_4 @ flattened_box

    # Plotting box 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_4__box_orthogonal_matrix_4.png'
    )
    plot_cube(
        object_3D=box_1,
        output_path=plane_path)

    ##########
    # Orthogonal matrix 5:
    matrix_5 = np.array([
        [ np.sqrt(2) / 2, 0, np.sqrt(2) / 2],
        [              0, 1,              0],
        [-np.sqrt(2) / 2, 0, np.sqrt(2) / 2]
    ])
    # Calculating box 2:
    box_2 = matrix_5 @ flattened_box
    
    # Plotting box 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_4__box_orthogonal_matrix_5.png'
    )
    plot_cube(
        object_3D=box_2,
        output_path=plane_path)

    ##########
    # Shear matrix 7:
    matrix_6 = np.array([
        [np.sqrt(2) / 2, -np.sqrt(2) / 2, 0],
        [np.sqrt(2) / 2,  np.sqrt(2) / 2, 0],
        [             0,               0, 1]
    ])
    matrix_7 = np.array([
        [1,              0,               0],
        [0,          1 / 2, -np.sqrt(3) / 2],
        [0, np.sqrt(3) / 2,           1 / 2]
    ])
    # Calculating box 3:
    box_3 = matrix_6 @ matrix_7 @ flattened_box

    # Plotting box 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_4__box_orthogonal_matrix_6_7.png'
    )
    plot_cube(
        object_3D=box_3,
        output_path=plane_path)
    
    # Calculating box 4:
    box_4 = matrix_7 @ matrix_6 @ flattened_box

    # Plotting box 4:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_4__box_orthogonal_matrix_7_6.png'
    )
    plot_cube(
        object_3D=box_4,
        output_path=plane_path)


if __name__ == '__main__':
    
    conf = {
        'output_data_path': '1_visualize_different_matrices/output_data/ex_4'
    }
    main(conf=conf)