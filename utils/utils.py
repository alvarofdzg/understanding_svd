import numpy as np


def prepare_flattened_2D_plane() -> np.array:
        # Black plane:
    x_values = np.arange(-10, 0)
    y_values = np.arange(-10, 0)
    xx, yy = np.meshgrid(x_values, y_values)
    black_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    # Red plane:
    x_values = np.arange(  0, 10)
    y_values = np.arange(-10,  0)
    xx, yy = np.meshgrid(x_values, y_values)
    red_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    # Blue plane:
    x_values = np.arange(-10,  0)
    y_values = np.arange(  0, 10)
    xx, yy = np.meshgrid(x_values, y_values)
    blue_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    # Green plane:
    x_values = np.arange( 0, 10)
    y_values = np.arange( 0, 10)
    xx, yy = np.meshgrid(x_values, y_values)
    green_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    flattened_plane = np.concatenate(
        (black_values, red_values, blue_values, green_values),
        axis=1)
    return flattened_plane


def prepare_flattened_3D_plane() -> np.array:
    
    # Black box:
    x_values = np.arange(-10, 0)
    y_values = np.arange(-10, 0)
    z_values = np.arange(-10, 0)
    xx, yy, zz = np.meshgrid(x_values, y_values, z_values)
    black_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :], 
            zz.flatten()[np.newaxis, :]
            
        ], 
        axis=0)
    
    # Red box:
    x_values = np.arange(  0, 10)
    y_values = np.arange(-10,  0)
    xx, yy, zz = np.meshgrid(x_values, y_values, z_values)
    red_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :],
            zz.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    # Blue box:
    x_values = np.arange(-10,  0)
    y_values = np.arange(  0, 10)
    xx, yy, zz = np.meshgrid(x_values, y_values, z_values)
    blue_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :],
            zz.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    # Green box:
    x_values = np.arange( 0, 10)
    y_values = np.arange( 0, 10)
    xx, yy, zz = np.meshgrid(x_values, y_values, z_values)
    green_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :],
            zz.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    # Brown box:
    x_values = np.arange(-10,  0)
    y_values = np.arange(-10,  0)
    z_values = np.arange(  0, 10)
    xx, yy, zz = np.meshgrid(x_values, y_values, z_values)
    brown_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :], 
            zz.flatten()[np.newaxis, :]
            
        ], 
        axis=0)
    
    # Purple box:
    x_values = np.arange(  0, 10)
    y_values = np.arange(-10,  0)
    xx, yy, zz = np.meshgrid(x_values, y_values, z_values)
    purple_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :],
            zz.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    # Orange box:
    x_values = np.arange(-10,  0)
    y_values = np.arange(  0, 10)
    xx, yy, zz = np.meshgrid(x_values, y_values, z_values)
    orange_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :],
            zz.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    # Gray box:
    x_values = np.arange( 0, 10)
    y_values = np.arange( 0, 10)
    xx, yy, zz = np.meshgrid(x_values, y_values, z_values)
    gray_values = np.concatenate(
        [   
            xx.flatten()[np.newaxis, :], 
            yy.flatten()[np.newaxis, :],
            zz.flatten()[np.newaxis, :]
        ], 
        axis=0)
    
    flattened_plane = np.concatenate(
        (
            black_values, 
            red_values, 
            blue_values, 
            green_values, 
            brown_values,
            purple_values,
            orange_values,
            gray_values
            ),
        axis=1)
    return flattened_plane