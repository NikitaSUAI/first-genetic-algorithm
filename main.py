import numpy as np
import convert
from BinaryGA import BinaryGA
import matplotlib.pyplot as plt
from BinaryGA.model import model

def image(arr, gen=0, convert=convert.B2D):
    # x = np.linspace(-20, -2.3, 2*15)
    # y = model_d(x)
    # z = np.around(convert(arr), decimals=5)
    # y2 = model_d(z)
    # fig, ax = plt.subplots()
    # ax.plot(x, y, color="blue", label="cos(2x)/x^2")
    # ax.scatter(z, y2, c="red")
    # ax.set_facecolor("white")
    # ax.set_title(f"geniration : {gen}\n {arr.shape} - matrix shape")
    # ax.set_xlabel("x")
    # ax.set_ylabel("y")
    # ax.legend()
    # return fig
    ...

def draw(fig, _):
    fig.tight_layout()
    plt.show()


def make_image(fig, i=0):
    fig.savefig(f"./generations/gen{i}.png")


def main(func):
    model.load()
    GA = BinaryGA.BinaryGA(pop_len=20, ch_len=16)
    res = GA.train(100)
        # print(genotype)
        # print(convert.B2D(genotype))
        # print("="*100)
    GA.plot()
    point_a = convert.B2D_one(GA.result)
    point_b = (model.fitnes(res)).min()
    print(f"Экстреммум в точке : ({point_a},{point_b})")
    result = GA.predict()
    for i, j in zip(result, model.test_Ef):
        print(f"Результат ГА : {i}, истенный результат: {j}")

if __name__ == "__main__":
    func = make_image
    # запускаем генетический алгоритм с 50 хромосомами и 20 поколениями
    main(func)



