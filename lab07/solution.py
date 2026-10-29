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
    blocks = arr[np.ix(rows,columns)]
    return np.round(blocks, 6).tolist()

##def column_means(matrix: list[list[float]]) -> list[float]:
