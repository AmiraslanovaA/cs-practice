import numpy as np

def make_hours() -> list[int]:
    arr = np.arange(0,22,3)
    return arr.tolist()

def vector_report(values: list[float]) -> dict:
    arr = np.asarray(values, dtype = float)
    return dict(third = float(arr[2]),
                lasr = float(arr[-1]),
                middlesl = arr[2:6].tolist(),
                everysecond = arr[::2].tolist(),
                reverse = arr[::-1].tolist())

def change_vector(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype = float).copy()
    arr[2:5] = 99
    arr[::2] = -1
    return arr.tolist()

def cap_above(values: list[float], limit: float) -> list[float]:
    arr = np.asarray(values, dtype = float).copy()
    mask = arr > limit
    arr[mask] = limit
    return arr.tolist()

def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    arr = np.asarray(values)
    farenh = arr*9/5 + 32
    return farenh.tolist() 