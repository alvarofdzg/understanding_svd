import time
import scipy
import numpy as np
from build import svd_module


def main() -> None:
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    start_time = time.time()
    python_results = scipy.linalg.svd(a=matrix)
    end_time = time.time()
    print(f'Python SVD: {end_time - start_time} seconds')
    
    start_time = time.time()
    cpp_results = svd_module.compute_svd(matrix)
    end_time = time.time()
    print(f'C++ SVD: {end_time - start_time} seconds')
    
    print("Comparing the results...")
    print("\nU:")
    print("Python:")
    print(python_results[0])
    print("C++:")
    print(cpp_results[0])
    print("\nS:")
    print("Python:")
    print(python_results[1])
    print("C++:")
    print(cpp_results[1])
    print("\nV:")
    print("Python:")
    print(python_results[2])
    print("C++:")
    print(cpp_results[2])
    
    
if __name__ == '__main__':
    main()