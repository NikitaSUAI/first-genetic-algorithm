from BinaryGA.operators.Crossingover import  Crossingover
from BinaryGA.operators.Mutation import Mutation
from BinaryGA.operators.Reproduction import Reproduction
from BinaryGA.model.model import fitnes as f
from BinaryGA.model.model import fitnes_test as test

import numpy as np
import matplotlib.pyplot as plt

def reduc(arr, max, model):
    # сокращаем число хромосом до изначального (max)
    # сокращаем путем удаления максильных по значению хромосом
    # для поиска минимума
    tmp = model(arr)
    for _ in range(len(arr) - max):
        arr = np.delete(arr, tmp.argmax(), axis=0)
        tmp = np.delete(tmp, tmp.argmax())
    return arr


class BinaryGA:
    def __init__(self, pop_len=20, ch_len=8, model=f):
        self.pop_len = pop_len
        self.ch_len = ch_len
        self.model = model
        self.cross = Crossingover(0.5)
        self.mut = Mutation(0.01)
        self.rep = Reproduction()
        self.min = []

    def train(self, gens=10):
        genotype = np.random.uniform(low=0, high=2, size=(self.pop_len,
                                                self.ch_len)).astype(np.uint8)

        for i in range(gens):
            print(f"generation : {i+1}")
            # получаем новый массив родителей методом рулетки
            genotype = self.rep.do(genotype)
            # скрещиваем родителей и получаем еще одну популяцию
            child = self.cross.do(genotype)
            # часть новой популяции мутирует с вероятностью 1/1000
            child = self.mut.do(child)
            # сокращаем популяцию до исходного значения
            if len(child) != 0:
                genotype = reduc(np.append(genotype, child, axis=0),
                             len(genotype), self.model)
            # выводим на экран результат
            self.min.append(self.model(genotype).min())
        self.result = genotype[np.argmin(self.model(genotype))]
        return genotype

    def plot(self):
        plt.plot(range(len(self.min)), self.min)
        plt.show()


    def predict(self):
        return test(self.result)
