'''
This script shows how the inverse of a matrix can return different shapes to their
initial shape after being modified by the original matrix.
'''
import os
import sys
import numpy as np
# Adding parent folder:
sys.path.append(os.getcwd())
from utils import (
    plot_cube,
    plot_plane,
    prepare_flattened_2D_plane,
    prepare_flattened_3D_plane
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
        'ex_5__raw_plane.png'
    )
    plot_plane(
        object_2D=flattened_plane,
        output_path=plane_path
    )
    
    ##########
    # Matrix 1:
    matrix_1 = np.array([
        [ 1, 3],
        [-2, 4]
    ])
    # Calculating plane 1:
    plane_1 = matrix_1 @ flattened_plane
    
    # Plotting plane 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_5__plane_1.png'
    )
    plot_plane(
        object_2D=plane_1,
        output_path=plane_path
    )
    
    # Calculating original raw plane applying inverse of matrix 1:
    new_original_plane = np.linalg.inv(matrix_1) @ plane_1
    
    # Plotting new original plane:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_5__plane_1_inversed.png'
    )
    plot_plane(
        object_2D=new_original_plane,
        output_path=plane_path
    )

    ##########
    ##########
    # Create flattened_box:
    flattened_box = prepare_flattened_3D_plane()
    
    # Plotting raw box:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_5__raw_box.png'
    )
    plot_cube(
        object_3D=flattened_box,
        output_path=plane_path)

    ##########
    # Matrix 2:
    matrix_2 = np.array([
        [1,              0,               0],
        [0,          1 / 2, -np.sqrt(3) / 2],
        [0, np.sqrt(3) / 2,           1 / 2]
    ])
    # Calculating box 1:
    box_1 = matrix_2 @ flattened_box

    # Plotting box 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_5__box_1.png'
    )
    plot_cube(
        object_3D=box_1,
        output_path=plane_path)
    
    # Calculating original box  applying inverse of matrix 2:
    new_original_box = np.linalg.inv(matrix_2) @ box_1
    
    # Plotting new original box:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_5__box_1_inversed.png'
    )
    plot_cube(
        object_3D=new_original_box,
        output_path=plane_path)


if __name__ == '__main__':
    
    conf = {
        'output_data_path': '1_visualize_different_matrices/output_data/ex_5'
    }
    main(conf=conf)