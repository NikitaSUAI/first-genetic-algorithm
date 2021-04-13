import numpy as np

from BinaryGA.model.model import fitnes as f


def find_cumulates(prob):
    # строит кумуляту в виде списка предельных значений
    # [0, 0.1, 0.5, 0.7, 1]
    cumulates = [prob[0], ]
    for i in range(1, len(prob)):
        cumulates.append(prob[i] + cumulates[-1])
    return np.array(cumulates)


class Reproduction:
    def __init__(self, fitness=f):
        self.fitness = fitness

    def do(self, arr):
        """ оператор "рулетка"
        ищем вероятности как частное от фенотипа хромосомы к сумме
        фенотипов хромосом и методом "рулетка" генерируем новую популяцию """
        dec = self.fitness(arr)
        # # для удобства поднимим график во 2 четверть
        # dec += dec.min() + 1
        # ищем вероятности от суммы, то есть если значение больше то
        # вероятность больше
        prob = dec / np.sum(dec)
        prob -= 1
        prob *= -1
        cumulates = find_cumulates(prob)
        # print(cumulates)
        res = []
        for _ in arr:
            rand = np.random.random() * prob.sum()
            for i in range(len(cumulates)):
                if rand <= cumulates[i]:
                    res.append(arr[i])
                    break
        return np.array(res, dtype=np.uint8)


if __name__ == "__main__":
    """Tests"""
    genotype = np.random.uniform(low=0, high=2, size=(5, 15)).astype(
        np.uint8)
    print(genotype)
    r = Reproduction()
    print(r.do(genotype))
