from copy import copy
import numpy as np
import convert
import model


def Crosses(arr):
    # скрещиванее популяций путем перестановки подстрок
    res = []
    for i in arr:
        if np.random.randint(10) < 5:
            continue
        # поиск 2 рандомных хромосом
        first, second = get_chromosomy(len(arr))
        #замена подстрок
        for i in range(np.random.randint(len(arr[0])), len(arr[0])):
            arr[first][i], arr[second][i] = arr[second][i], arr[first][i]
        res.append(arr[first])
        res.append(arr[second])
    res = np.array(res, dtype=np.uint8)
    return res

plus = "+"

def Reproductions(arr):
    """Модифицируем оператор репродукции,
    путем переворачивания целевой функции
    ищем вероятности как частное от фенотипа хромосомы к сумме фенотипов хромосом
    и методом "рулетка" генерируем новую популяцию"""
    dec = -1 * model.fitnes(convert.B2D(arr))
    # для удобства поднимим график во 2 четверть
    dec = dec + dec.min() + 1
    # ищем вероятности от суммы, то есть если значение больше то вероятность больше
    prob = dec / np.sum(dec)
    cumulata = find_cumulatu(prob)
    res = []
    for _ in arr:
        rand = np.random.random()
        for i in range(len(cumulata)):
            if rand <= cumulata[i]:
                res.append(arr[i])
                break
    return np.array(res, dtype=np.uint8)

def Mutations(arr):
    # С вероятностью 0.001 в каждой хромосоме, 
    # происходит инверсия случайного бита
    for i in arr:
        if np.random.randint(1000) > 1:
            continue
        rand_pos = np.random.randint(len(i) - 1)
        i[rand_pos] = 1 - i[rand_pos]
    return arr


def get_chromosomy(how):
    # ищет 2 случайные хромосомы
    first = np.random.randint(how)
    sec = np.random.randint(how)
    while sec == first:
        sec = np.random.randint(how)
    return first, sec


def find_cumulatu(prob):
    # строит кумуляту в виде списка предельных значений
    # [0, 0.1, 0.5, 0.7, 1]
    cumulata = [prob[0], ]
    for i in range(1, len(prob)):
        cumulata.append(prob[i] + cumulata[-1])
    return np.array(cumulata, dtype=np.float)
