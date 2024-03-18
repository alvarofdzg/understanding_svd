import os


def main(paths:list) -> None:

    # Creating output folders:
    for path in paths:
        cur_path = os.path.join(
            path,
            'output_data'
        )
        if not os.path.exists(cur_path):
            os.mkdir(cur_path)
        

if __name__ == '__main__':
    
    paths = [
        '1_different_matrices',
        '2_spectral_decomposition',
        '3_singular_value_decomposition'
    ]
    main(paths=paths)