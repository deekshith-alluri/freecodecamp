import numpy as np

def calculate(list_with_nine_numbers):
    if len(list_with_nine_numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list_with_nine_numbers).reshape((3,3))
    calculations = {
        # beginning of the returning dictionary
        'mean': [matrix.mean(axis=0).tolist(),matrix.mean(axis=1).tolist(), float(matrix.mean())],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(),float( matrix.var())],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix,axis=1).tolist(), float(matrix.std())],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), float(matrix.max())],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), float(matrix.min())],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), float(matrix.sum())]
    }

    return calculations