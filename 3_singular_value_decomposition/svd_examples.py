'''
This script shows how to work with the Singular Value Decomposition.
It applies the different sections of the decomposition (U, S & Vt) one by one to
different shapes in 2D and 3D, so we can understand more clearly what each 
operation is doing.
'''
import os
import sys
import numpy as np
# Adding parent folder:
sys.path.append(os.getcwd())
from utils import (
    plot_cube,
    plot_plane,
    plot_cube_2D,
    plot_plane_3D,
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
        'raw_plane.png'
    )
    plot_plane(
        object_2D=flattened_plane,
        output_path=plane_path
    )
    
    ##########
    # Matrix 1:
    matrix_1 = np.array([
        [2,   1],
        [3,   1],
        [0, 1.8]
    ])
    # Calculating plane 1:
    plane_1 = matrix_1 @ flattened_plane
    
    # Plotting plane 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'matrix_1.png'
    )
    plot_plane_3D(
        object_3D=plane_1,
        output_path=plane_path
    )
    
    # Calculate te matrix decomposition of our matrix:
    U, s, Vt = np.linalg.svd(matrix_1, full_matrices=True)
    
    # Building S:
    S = np.zeros((matrix_1.shape[0], matrix_1.shape[1]))
    S[:len(s), :len(s)] = np.diag(s)
    
    # Computing axis to represent the eigen values:
    axis_eigen_vectors_2D = Vt * 10
    axis_eigen_vectors_3D = U * 30
    
    # Applying rotation with Vt:
    plane_2 = Vt @ flattened_plane
    
    # Plotting plane 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'first_part_matrix_1.png'
    )
    plot_plane(
        object_2D=plane_2,
        eigen_vectors=axis_eigen_vectors_2D,
        output_path=plane_path
    )
    
    # Applying scaling with S:
    plane_3 = S @ plane_2
    
    # Plotting plane 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'second_part_matrix_1.png'
    )
    plot_plane_3D(
        object_3D=plane_3,
        eigen_vectors=axis_eigen_vectors_3D,
        output_path=plane_path
    )

    # Applying rotation with U:
    plane_4 = U @ plane_3
    
    # Plotting plane 4:
    plane_path = os.path.join(
        conf['output_data_path'],
        'third_part_matrix_1.png'
    )
    plot_plane_3D(
        object_3D=plane_4,
        eigen_vectors=axis_eigen_vectors_3D,
        output_path=plane_path
    )
    
    
    ##########
    # Matrix 2:
    matrix_2 = np.array([
        [-1,   -2],
        [ 2,    3],
        [-2, -1.8]
    ])
    # Calculating plane 1:
    plane_1 = matrix_2 @ flattened_plane
    
    # Plotting plane 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'matrix_2.png'
    )
    plot_plane_3D(
        object_3D=plane_1,
        output_path=plane_path
    )
    
    # Calculate te matrix decomposition of our matrix:
    U, s, Vt = np.linalg.svd(matrix_2, full_matrices=True)
    
    # Building S:
    S = np.zeros((matrix_2.shape[0], matrix_2.shape[1]))
    S[:len(s), :len(s)] = np.diag(s)
    
    # Computing axis to represent the eigen values:
    axis_eigen_vectors_2D = Vt * 10
    axis_eigen_vectors_3D = U * 30
    
    # Applying rotation with Vt:
    plane_2 = Vt @ flattened_plane
    
    # Plotting plane 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'first_part_matrix_2.png'
    )
    plot_plane(
        object_2D=plane_2,
        eigen_vectors=axis_eigen_vectors_2D,
        output_path=plane_path
    )
    
    # Applying scaling with S:
    plane_3 = S @ plane_2
    
    # Plotting plane 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'second_part_matrix_2.png'
    )
    plot_plane_3D(
        object_3D=plane_3,
        eigen_vectors=axis_eigen_vectors_3D,
        output_path=plane_path
    )

    # Applying rotation with U:
    plane_4 = U @ plane_3
    
    # Plotting plane 4:
    plane_path = os.path.join(
        conf['output_data_path'],
        'third_part_matrix_2.png'
    )
    plot_plane_3D(
        object_3D=plane_4,
        eigen_vectors=axis_eigen_vectors_3D,
        output_path=plane_path
    )
    

    ##########
    ##########
    # Create flattened_box:
    flattened_box = prepare_flattened_3D_plane()
    
    # Plotting raw box:
    plane_path = os.path.join(
        conf['output_data_path'],
        'raw_box.png'
    )
    plot_cube(
        object_3D=flattened_box,
        output_path=plane_path)

    ##########
    # Matrix 3:
    matrix_3 = np.array([
        [3, 2,  2],
        [2, 3, -2]
    ])
    # Calculating box 1:
    box_1 = matrix_3 @ flattened_box

    # Plotting box 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'matrix_3.png'
    )
    plot_cube_2D(
        object_2D=box_1,
        output_path=plane_path,
        min_axis=-70,
        max_axis=70)
    
    # Calculate te matrix decomposition of our symmetric matrix:
    U, s, Vt = np.linalg.svd(matrix_3, full_matrices=True)
    
    # Building S:
    S = np.zeros((matrix_3.shape[0], matrix_3.shape[1]))
    S[:len(s), :len(s)] = np.diag(s)
    
    # Computing axis to represent the eigen values:
    axis_eigen_vectors_3D = Vt * 30
    axis_eigen_vectors_2D = U * 10
    
    # Applying rotation with Vt:
    box_2 = Vt @ flattened_box
    
    # Plotting box 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'first_part_matrix_3.png'
    )
    plot_cube(
        object_3D=box_2,
        eigen_vectors=axis_eigen_vectors_3D,
        output_path=plane_path
    )
    
    # Applying scaling with S:
    box_3 = S @ box_2
    
    # Plotting box 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'second_part_matrix_3.png'
    )
    plot_cube_2D(
        object_2D=box_3,
        eigen_vectors=axis_eigen_vectors_2D,
        output_path=plane_path,
        min_axis=-70,
        max_axis=70)
    
    # Applying rotation with U:
    box_4 = U @ box_3
    
    # Plotting box 4:
    plane_path = os.path.join(
        conf['output_data_path'],
        'third_part_matrix_3.png'
    )
    plot_cube_2D(
        object_2D=box_4,
        eigen_vectors=axis_eigen_vectors_2D,
        output_path=plane_path,
        min_axis=-70,
        max_axis=70)


    ##########
    # Matrix 4:
    matrix_4 = np.array([
        [3,  2,  2],
        [2,  3, -2],
        [1, -1,  2]
    ])
    # Calculating box 1:
    box_1 = matrix_4 @ flattened_box

    # Plotting box 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'matrix_4.png'
    )
    plot_cube(
        object_3D=box_1,
        output_path=plane_path)
    
    # Calculate te matrix decomposition of our symmetric matrix:
    U, s, Vt = np.linalg.svd(matrix_4, full_matrices=True)
    
    # Building S:
    S = np.zeros((matrix_4.shape[0], matrix_4.shape[1]))
    S[:len(s), :len(s)] = np.diag(s)
    
    # Computing axis to represent the eigen values:
    axis_eigen_vectors_3D = Vt * 30
    
    # Applying rotation with Vt:
    box_2 = Vt @ flattened_box
    
    # Plotting box 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'first_part_matrix_4.png'
    )
    plot_cube(
        object_3D=box_2,
        eigen_vectors=axis_eigen_vectors_3D,
        output_path=plane_path
    )
    
    # Applying scaling with S:
    box_3 = S @ box_2
    
    # Plotting box 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'second_part_matrix_4.png'
    )
    plot_cube(
        object_3D=box_3,
        eigen_vectors=axis_eigen_vectors_3D,
        output_path=plane_path)
    
    # Applying rotation with U:
    box_4 = U @ box_3
    
    # Plotting box 4:
    plane_path = os.path.join(
        conf['output_data_path'],
        'third_part_matrix_4.png'
    )
    plot_cube(
        object_3D=box_4,
        eigen_vectors=axis_eigen_vectors_3D,
        output_path=plane_path)


if __name__ == '__main__':
    
    conf = {
        'output_data_path': '3_singular_value_decomposition/output_data/svd_examples'
    }
    main(conf=conf)