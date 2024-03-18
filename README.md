# Understanding SVD

The idea of this repository is to provide some examples to better understand what is the Singular Value Decomposition (SVD) and how to work with it.


## Explanation Section
In this journey, until we totally understand this topic, we distinguish three steps:

### 1.- Different Matrices
In the first section, we just want to show how some matrices work and their effects to different 2D and 3D shapes. It would work the same for images.

The matrices that we work with are:
- Identity matrix.
- Scalar matrix.
- Off-one matrix.
- Reflection matrix.
- Diagonal matrix.
- Shear matrix.
- Orthogonal matrix.

### 2.- Spectral Decomposition
In the second section, we show what the Spectral Decomposition is and the effect that the different parts of the decomposition apply to different 2D and 3D shapes. 

Showing these effects help to understand what we are doing with each matrix.

### 3.- Singular Value Decomposition
Finally, in last section is where we work with the SVD.

We show the effects of the different parts of the decomposition, as we did for the Spectral Decomposition, which helps to show what is going on.

Also, we provide a couple of examples of how the SVD can be used to solve other problems:
- Least Squares.
- Decomposition of an image in its eigen vectors.


## Notebook
In the PDF called "Understanding SVD" we added some explanations for the different parts of this repository and where we dig deeper into the theory behind the different concepts that have been used here.

## Getting Started
Clone the repo:
  ```bash
  git clone https://github.com/alvarofdzg/understanding_svd.git
  cd understanding_svd
  ```  

Create environment:
  ```bash
conda env create -f environment.yml
  ```  

## Set up
  ```bash
python setup.py
  ```

## Usage
Run all the scripts from the main directory.

Example:
  ```bash
python 1_visualize_different_matrices/ex_1.py
  ```  

## Credits
- [Visual Kernel Youtube Channel](https://youtube.com/@visualkernel?si=rzzy5FTS6ZnYTxEB)
- [Geeks for geeks](https://www.geeksforgeeks.org/singular-value-decomposition-svd/)
- [Wiki - Solving homogeneous equations](https://en.wikipedia.org/wiki/Singular_value_decomposition#Solving_homogeneous_linear_equations)
- [Wiki - Linear Least Squares](https://en.wikipedia.org/wiki/Linear_least_squares)