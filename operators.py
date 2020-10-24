from copy import copy
import numpy as np
import convert
import model


def Crosses(arr):
    if np.random.randint(10) < 5:
        return arr
    # поиск 2 рандомных хромосом
    first, second = get_chromosomy(len(arr))
    rnd_bit = np.random.randint(len(arr[0]))
    arr[first][rnd_bit], arr[second][rnd_bit] = arr[second][rnd_bit], arr[first][rnd_bit]
    return arr

plus = "+"

def Reproductions(arr):
    #перевернутая модель
    dec = -model.fitnes(convert.B2D(arr))
    # опускаем в 3 четверть
    dec = dec - dec.max() - 1
    print(f"{plus*10}\ndec : {dec}\n{plus*10}")
    # ищем вероятности от суммы, то есть если значение больше то вероятность больше
    prob = dec / np.sum(dec)
    print(f"{plus*10}\nprob : {prob}\n{plus*10}")
    cumulata = find_cumulatu(prob)
    print(f"{plus*10}\ncumulata : {cumulata}\n{plus*10}")
    res = []
    for _ in arr:
        rand = np.random.random()
        for i in range(len(cumulata)):
            if rand <= cumulata[i]:
                res.append(arr[i])
                break
    return np.array(res, dtype=np.uint8)

def Mutations(arr):
    for i in arr:
        if np.random.randint(1000) > 1:
            continue
        rand_pos = np.random.randint(len(i) - 1)
        i[rand_pos] = 1 - i[rand_pos]
    return arr


def get_chromosomy(how):
    first = np.random.randint(how)
    sec = np.random.randint(how)
    while sec == first:
        sec = np.random.randint(how)
    return first, sec


def find_cumulatu(prob):
    cumulata = [prob[0], ]
    for i in range(1, len(prob)):
        cumulata.append(prob[i] + cumulata[-1])
    return np.array(cumulata, dtype=np.float)
