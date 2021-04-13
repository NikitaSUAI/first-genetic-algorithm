import numpy as np

# матрицу следует транспонировать а то хуй
def _B2D(array):
    if array.size:
        return 2 ** (len(array)-1) * array[0] + _B2D(array[1:]) 
    else:
        return 0

def D2B(array):
    ...

def B2D(array):
    a = np.array(_B2D(array[:,:8].T), dtype=np.float)
    b = np.array(_B2D(array[:,8:].T), dtype=np.float)
    a = np.array((a * (2 / 2 ** 8)) + 2, dtype=np.float)
    b = np.array((b * (1 / 2 ** 8)) + 1, dtype=np.float)
    return a, b

def B2D_one(array):
    a = np.array(_B2D(array[:8]), dtype=np.float)
    b = np.array(_B2D(array[8:]), dtype=np.float)
    a = np.array((a * (2 / 2**8)) + 2, dtype=np.float)
    b = np.array((b * (1 / 2**8)) + 1, dtype=np.float)
    return a, b


if __name__ == "__main__":
    arr = np.random.uniform(low=0, high=2, size=(3,3)).astype(np.uint8)
    print(arr)
    print(arr.T)
    print(B2D(arr))
