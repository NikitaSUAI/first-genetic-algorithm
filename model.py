import numpy as np  

def fitnes(x):
    # функция для которой необходимо найти мин/макс
    return np.cos(2 * x) / (x * x)