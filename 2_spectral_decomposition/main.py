'''
This script shows how to work with the Spectral Decomposition.
It applies the different sections of the decomposition (Q, V & Qt) one by one to
different shapes in 2D and 3D, so we can understand more clearly what each 
operation is doing.
We have to remember that this decomposition is only possible when we are working
with symmetric matrices, that's why we only use them in this section.
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
        'raw_plane.png'
    )
    plot_plane(
        object_2D=flattened_plane,
        output_path=plane_path
    )
    
    ##########
    # Symmetric matrix 1:
    symmetric_matrix_1 = np.array([
        [  3, 1.5],
        [1.5,   3]
    ])
    # Calculating plane 1:
    plane_1 = symmetric_matrix_1 @ flattened_plane
    
    # Plotting plane 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'symmetric_matrix_1.png'
    )
    plot_plane(
        object_2D=plane_1,
        output_path=plane_path
    )
    
    # Calculate te matrix decomposition of our symmetric matrix:
    eigenvalues, eigenvectors = np.linalg.eig(symmetric_matrix_1)
    
    # Computing axis to represent the eigen values:
    axis_eigen_vectors = eigenvectors.T * 10
    
    # Applying rotation with Qt:
    plane_2 = eigenvectors.T @ flattened_plane
    
    # Plotting plane 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'first_part_matrix_1.png'
    )
    plot_plane(
        object_2D=plane_2,
        eigen_vectors=axis_eigen_vectors,
        output_path=plane_path
    )
    
    # Applying scaling with V:
    plane_3 = np.diag(eigenvalues) @ plane_2
    
    # Plotting plane 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'second_part_matrix_1.png'
    )
    plot_plane(
        object_2D=plane_3,
        eigen_vectors=axis_eigen_vectors,
        output_path=plane_path
    )

    # Applying rotation with Q:
    plane_4 = eigenvectors @ plane_3
    
    # Plotting plane 4:
    plane_path = os.path.join(
        conf['output_data_path'],
        'third_part_matrix_1.png'
    )
    plot_plane(
        object_2D=plane_4,
        eigen_vectors=axis_eigen_vectors,
        output_path=plane_path
    )
    
    
    ##########
    # Symmetric matrix 2:
    symmetric_matrix_2 = np.array([
        [-1,   -2],
        [-2, -1.8]
    ])
    # Calculating plane 1:
    plane_1 = symmetric_matrix_2 @ flattened_plane
    
    # Plotting plane 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'symmetric_matrix_2.png'
    )
    plot_plane(
        object_2D=plane_1,
        output_path=plane_path
    )
    
    # Calculate te matrix decomposition of our symmetric matrix:
    eigenvalues, eigenvectors = np.linalg.eig(symmetric_matrix_2)
    
    # Computing axis to represent the eigen values:
    axis_eigen_vectors = eigenvectors.T * 10

    # Applying rotation with Qt:
    plane_2 = eigenvectors.T @ flattened_plane
    
    # Plotting plane 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'first_part_matrix_2.png'
    )
    plot_plane(
        object_2D=plane_2,
        eigen_vectors=axis_eigen_vectors,
        output_path=plane_path
    )
    
    # Applying scaling with V:
    plane_3 = np.diag(eigenvalues) @ plane_2
    
    # Plotting plane 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'second_part_matrix_2.png'
    )
    plot_plane(
        object_2D=plane_3,
        eigen_vectors=axis_eigen_vectors,
        output_path=plane_path
    )

    # Applying rotation with Q:
    plane_4 = eigenvectors @ plane_3
    
    # Plotting plane 4:
    plane_path = os.path.join(
        conf['output_data_path'],
        'third_part_matrix_2.png'
    )
    plot_plane(
        object_2D=plane_4,
        eigen_vectors=axis_eigen_vectors,
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
    # Symmetric matrix 3:
    symmetric_matrix_3 = np.array([
        [3,   1,   2],
        [1, 0.4,  -1],
        [2,  -1, 0.5]
    ])
    # Calculating box 1:
    box_1 = symmetric_matrix_3 @ flattened_box

    # Plotting box 1:
    plane_path = os.path.join(
        conf['output_data_path'],
        'symmetric_matrix_3.png'
    )
    plot_cube(
        object_3D=box_1,
        output_path=plane_path)
    
    # Calculate te matrix decomposition of our symmetric matrix:
    eigenvalues, eigenvectors = np.linalg.eig(symmetric_matrix_3)
    
    # Computing axis to represent the eigen values:
    axis_eigen_vectors = eigenvectors.T * 30
    
    # Applying rotation with Qt:
    box_2 = eigenvectors.T @ flattened_box
    
    # Plotting box 2:
    plane_path = os.path.join(
        conf['output_data_path'],
        'first_part_matrix_3.png'
    )
    plot_cube(
        object_3D=box_2,
        eigen_vectors=axis_eigen_vectors,
        output_path=plane_path
    )
    
    # Applying scaling with V:
    box_3 = np.diag(eigenvalues) @ box_2
    
    # Plotting box 3:
    plane_path = os.path.join(
        conf['output_data_path'],
        'second_part_matrix_3.png'
    )
    plot_cube(
        object_3D=box_3,
        eigen_vectors=axis_eigen_vectors,
        output_path=plane_path
    )

    # Applying rotation with Q:
    box_4 = eigenvectors @ box_3
    
    # Plotting box 4:
    plane_path = os.path.join(
        conf['output_data_path'],
        'third_part_matrix_3.png'
    )
    plot_cube(
        object_3D=box_4,
        eigen_vectors=axis_eigen_vectors,
        output_path=plane_path
    )


if __name__ == '__main__':
    
    conf = {
        'output_data_path': '2_spectral_decomposition/output_data'
    }
    main(conf=conf)