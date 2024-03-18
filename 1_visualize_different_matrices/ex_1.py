'''
This script shows how a plane can get affected by a matrix.
'''
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
    
    # Plot raw plane:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_1__raw_plane.png'
    )
    plot_plane(
        object_2D=flattened_plane,
        output_path=plane_path
    )
    
    # Create new plane:
    new_plane = conf['matrix_to_use'] @ flattened_plane
    
    # Plot new plane:
    plane_path = os.path.join(
        conf['output_data_path'],
        'ex_1__new_plane.png'
    )
    plot_plane(
        object_2D=new_plane,
        output_path=plane_path
    )


if __name__ == '__main__':
    
    conf = {
        'output_data_path': '1_visualize_different_matrices/output_data/ex_1',
        'matrix_to_use': np.array([
                            [1, 2],
                            [2, 0]
                        ])
    }
    main(conf=conf)