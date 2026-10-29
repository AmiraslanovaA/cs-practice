import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values)%width!= 0:
        return []
    arr = np.asarray(values, dtype = float)
    rarr = arr.reshape(-1,width)
    return np.round(rarr, 6).tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype = float)
    blocks = arr[np.ix_(rows,columns)]
    return np.round(blocks, 6).tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype = float)
    means = np.mean(arr, axis = 0)
    return np.round(means,6).tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    arr = np.asarray(matrix, dtype = float)
    colmean = arr[:,column]
    maxwithoutmin = np.max(colmean) - np.min(colmean)
    return float(np.round(maxwithoutmin,6))
