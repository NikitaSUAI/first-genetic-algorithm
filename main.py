from typing import Tuple
import numpy as np
import convert
import operators
import matplotlib.pyplot as plt
import model

def image(arr, gen=0):
    x = np.linspace(-20, -2.3, 2*15)
    y = model.fitnes(x)
    z = np.around(convert.B2D(arr),decimals=5)
    y2 = model.fitnes(z)
    fig, ax = plt.subplots()
    ax.plot(x, y, color="blue", label="cos(2x)/x^2")
    ax.scatter(z, y2, c="red")
    ax.set_facecolor("white")
    ax.set_title(f"geniration : {gen}\n {arr.shape} - matrix shape")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    return fig


def draw(fig, _):
    fig.tight_layout()
    plt.show()

def make_image(fig, i):
    fig.savefig(f"./generations/gen{i}.png")


def reduc(arr, max):
    # сокращаем число хромосом до изначального (max)
    # сокращаем путем удаления максильных по значению хромосом
    # для поиска минимума
    for _ in range(len(arr) - max):
        tmp = model.fitnes(convert.B2D(arr))
        arr = np.delete(arr, tmp.argmax(), axis=0)
        tmp = np.delete(tmp, tmp.argmax())
    return arr

def main(pop_len:int, gens:int, func):
    # создаем случайный массив хромосом
    genotype = np.random.uniform(low=0, high=2, size=(pop_len,15)).astype(np.uint8)
    for i in range(gens):
        print(f"generation : {i}")
        # получаем новый массив родителей методом рулетки
        genotype = operators.Reproductions(genotype)
        # скрещиваем родителей и получаем еще одну популяцию
        child = operators.Crosses(genotype)
        # часть новой популяции мутирует с вероятностью 1/1000
        child = operators.Mutations(child)
        # сокращаем популяцию до исходного значения
        genotype = reduc(np.append(genotype, child, axis=0), len(genotype))
        # выводим на экран результат
        print(genotype)
        print(convert.B2D(genotype))
        print("="*100)
        print(f"Экстреммум в точке : ({convert.B2D(genotype)[np.argmin(model.fitnes(convert.B2D(genotype)))]},{(model.fitnes(convert.B2D(genotype))).min()})")
        func(image(genotype, i), i)

if __name__ == "__main__":
    func = make_image
    # запускаем генетический алгоритм с 50 хромосомами и 20 поколениями
    main(50, 20, func)



