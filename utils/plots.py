import numpy as np
import matplotlib.pyplot as plt


def plot_plane(object_2D:np.array, output_path:str, eigen_vectors:np.array=None, min_axis:int=-30, max_axis:int=30) -> None:
    
    plt.figure()
    plt.xlim([min_axis, max_axis])
    plt.ylim([min_axis, max_axis])
    plt.scatter(object_2D[0, :100], object_2D[1, :100], c='black')
    plt.scatter(object_2D[0, 100:200], object_2D[1, 100:200], c='r')
    plt.scatter(object_2D[0, 200:300], object_2D[1, 200:300], c='b')
    plt.scatter(object_2D[0, 300:], object_2D[1, 300:], c='g')
    
    # Plotting eigen vectors:
    if eigen_vectors is not None:
        plot_2D_eigen_vectors(eigen_vectors=eigen_vectors)
        
    # Save figure:
    plt.savefig(output_path)
    plt.close()


def plot_2D_eigen_vectors(eigen_vectors:np.array) -> None:

    # Colors for eigen vectors arrows:
    color_axis = ['orange', 'yellow']

    # Loop for each eigen vector:
    for idx in range(eigen_vectors.shape[0]):
        # Draw arrow:
        plt.quiver(
            0, 
            0, 
            eigen_vectors[idx, 0], 
            eigen_vectors[idx, 1], 
            color=color_axis[idx],
            scale=1,
            angles='xy',
            scale_units='xy')
        
        # Draw axis name:
        plt.text(
            eigen_vectors[idx, 0], 
            eigen_vectors[idx, 1], 
            f'e_{idx + 1}')


def plot_plane_3D(object_3D:np.array, output_path:str, eigen_vectors:np.array=None, min_axis:int=-30, max_axis:int=30) -> None:
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    ax.set_xlim(min_axis, max_axis)
    ax.set_ylim(min_axis, max_axis)
    ax.set_zlim(min_axis, max_axis)
    
    # Plotting reference frame:
    ax = plot_reference_frame(ax=ax)
    
    ax.scatter(object_3D[0, :100], object_3D[1, :100], object_3D[2, :100], c='black')
    ax.scatter(object_3D[0, 100:200], object_3D[1, 100:200], object_3D[2, 100:200], c='r')
    ax.scatter(object_3D[0, 200:300], object_3D[1, 200:300], object_3D[2, 200:300], c='b')
    ax.scatter(object_3D[0, 300:], object_3D[1, 300:], object_3D[2, 300:], c='g')
    
    # Plotting eigen vectors:
    if eigen_vectors is not None:
        plot_3D_eigen_vectors(ax=ax, eigen_vectors=eigen_vectors)
        
    # Save figure:
    plt.savefig(output_path)
    plt.close()
    
     
def plot_cube(object_3D:np.array, output_path:str, eigen_vectors:np.array=None, min_axis:int=-40, max_axis:int=40, alpha:float=1) -> None:
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    ax.set_xlim(min_axis, max_axis)
    ax.set_ylim(min_axis, max_axis)
    ax.set_zlim(min_axis, max_axis)
    
    # Plotting reference frame:
    ax = plot_reference_frame(ax=ax)
    
    # Plotting cube:
    ax.scatter(object_3D[0, :1000], object_3D[1, :1000], object_3D[2, :1000], c='black', alpha=alpha)
    ax.scatter(object_3D[0, 1000:2000], object_3D[1, 1000:2000], object_3D[2, 1000:2000], c='red', alpha=alpha)
    ax.scatter(object_3D[0, 2000:3000], object_3D[1, 2000:3000], object_3D[2, 2000:3000], c='blue', alpha=alpha)
    ax.scatter(object_3D[0, 3000:4000], object_3D[1, 3000:4000], object_3D[2, 3000:4000], c='green', alpha=alpha)
    ax.scatter(object_3D[0, 4000:5000], object_3D[1, 4000:5000], object_3D[2, 4000:5000], c='brown', alpha=alpha)
    ax.scatter(object_3D[0, 5000:6000], object_3D[1, 5000:6000], object_3D[2, 5000:6000], c='purple', alpha=alpha)
    ax.scatter(object_3D[0, 6000:7000], object_3D[1, 6000:7000], object_3D[2, 6000:7000], c='orange', alpha=alpha)
    ax.scatter(object_3D[0, 7000:], object_3D[1, 7000:], object_3D[2, 7000:], c='gray', alpha=alpha)

    # Plotting eigen vectors:
    if eigen_vectors is not None:
        plot_3D_eigen_vectors(ax=ax, eigen_vectors=eigen_vectors)

    # Save figure:
    plt.savefig(output_path)
    plt.close()


def plot_cube_2D(object_2D:np.array, output_path:str, eigen_vectors:np.array=None, min_axis:int=-30, max_axis:int=30, alpha:float=1) -> None:
    
    plt.figure()
    plt.xlim([min_axis, max_axis])
    plt.ylim([min_axis, max_axis])
    
    # Plotting cube:
    plt.scatter(object_2D[0, :1000], object_2D[1, :1000], c='black', alpha=alpha)
    plt.scatter(object_2D[0, 1000:2000], object_2D[1, 1000:2000], c='red', alpha=alpha)
    plt.scatter(object_2D[0, 2000:3000], object_2D[1, 2000:3000], c='blue', alpha=alpha)
    plt.scatter(object_2D[0, 3000:4000], object_2D[1, 3000:4000], c='green', alpha=alpha)
    plt.scatter(object_2D[0, 4000:5000], object_2D[1, 4000:5000], c='brown', alpha=alpha)
    plt.scatter(object_2D[0, 5000:6000], object_2D[1, 5000:6000], c='purple', alpha=alpha)
    plt.scatter(object_2D[0, 6000:7000], object_2D[1, 6000:7000], c='orange', alpha=alpha)
    plt.scatter(object_2D[0, 7000:], object_2D[1, 7000:], c='gray', alpha=alpha)

    # Plotting eigen vectors:
    if eigen_vectors is not None:
        plot_2D_eigen_vectors(eigen_vectors=eigen_vectors)
        
    # Save figure:
    plt.savefig(output_path)
    plt.close()
    
    
# Plot the results with the Eigen Vectors
def plot_3D_eigen_vectors(ax, eigen_vectors:np.array) -> None:

    # Colors for eigen vectors arrows:
    color_axis = ['orange', 'yellow', 'brown']

    # Loop for each eigen vector:
    for idx in range(eigen_vectors.shape[0]):
        # Draw arrow:
        ax.quiver(
            0, 
            0,
            0, 
            eigen_vectors[idx, 0], 
            eigen_vectors[idx, 1], 
            eigen_vectors[idx, 2], 
            color=color_axis[idx])
        
        # Draw axis name:
        ax.text(
            eigen_vectors[idx, 0], 
            eigen_vectors[idx, 1], 
            eigen_vectors[idx, 2], 
            f'e_{idx + 1}')
    

def plot_reference_frame(ax) -> plt.axes:
    
    color_axis = ['red', 'blue', 'green']

    axis = np.array([
        [40,  0,  0],
        [ 0, 40,  0],
        [ 0,  0, 40]
    ])
    
    names = ['X', 'Y', 'Z']
    
    for idx in range(axis.shape[1]):
        
        # Draw arrow:
        ax.quiver(
            0, 
            0, 
            0,
            axis[idx, 0], 
            axis[idx, 1], 
            axis[idx, 2],
            color=color_axis[idx])
        
        # Draw axis name:
        ax.text(axis[idx, 0], 
                axis[idx, 1], 
                axis[idx, 2], 
                names[idx])


    return ax