from typing import Tuple
import numpy as np
import convert
import operators
import matplotlib.pyplot as plt
import model

def image(arr, gen=0):
    # plt.annotation()
    x = np.linspace(-20, -2.3, 2*15)
    y = model.fitnes(x)
    z = np.around(convert.B2D(arr),decimals=5)
    y2 = model.fitnes(z)
    fig, ax = plt.subplots()
    ax.plot(x, y/x, color="blue", label="cos(2x)/x^2")
    ax.scatter(z, y2/z, c="red")
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
    print("arrrrrr")
    print(arr.shape)
    for _ in range(len(arr) - max):
        tmp = model.fitnes(convert.B2D(arr))
        print(tmp.argmin())
        arr = np.delete(arr, tmp.argmin(), axis=0)
        print(arr.shape)
        tmp = np.delete(tmp, tmp.argmin())
    return arr

def main(pop_len:int, gens:int, func):
    genotype = np.random.uniform(low=0, high=2, size=(pop_len,15)).astype(np.uint8)
    for i in range(gens):
        print(f"generation : {i}")
        genotype = operators.Reproductions(genotype)
        child = operators.Crosses(genotype)
        child = operators.Mutations(child)
        genotype = reduc(np.append(genotype, child, axis=0), len(genotype))
        print(genotype)
        print(convert.B2D(genotype))
        print("="*100)
        func(image(genotype, i), i)

if __name__ == "__main__":
    func = make_image
    main(50, 20, func)



