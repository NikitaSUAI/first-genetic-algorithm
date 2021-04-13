import numpy as np


class Mutation:
    def __init__(self, prob=0.01):
        self.prob = prob * 1000

    def do(self, arr:np.array):
        # С вероятностью 0.001 в каждой хромосоме,
        # происходит инверсия случайного бита
        for i in arr:
            if np.random.randint(1000) > self.prob:
                continue
            rand_pos = np.random.randint(len(i) - 1)
            i[rand_pos] = 1 - i[rand_pos]
        return arr


if __name__ == "__main__":
    """Tests"""
    genotype = np.random.uniform(low=0, high=2, size=(10, 15)).astype(
        np.uint8)
    m = Mutation()
    for _ in range(100):
        m.do(genotype)