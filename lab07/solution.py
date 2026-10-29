import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values)%width!= 0:
        return []
    arr = np.asarray(values, dtype = float)
    rarr = arr.reshape(-1,width)
    return list(np.round(rarr, 6))
