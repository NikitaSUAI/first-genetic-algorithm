import numpy as np
import convert
import json
L, Ef = [], []
test_L, test_Ef = [], []

def load():
    global L, Ef, test_L, test_Ef
    with open("data.json") as f:
        tmp = json.load(f)
        for i in range(int(len(tmp["L"])/3)):
            r = np.random.randint(len(tmp["L"]) - i)
            L.append(tmp["L"][r])
            Ef.append(tmp["Ef"][r])
            del tmp["L"][r]
            del tmp["Ef"][r]
        test_L = tmp["L"]
        test_Ef = tmp["Ef"]
        L = np.array(L)
        Ef = np.array(Ef)


def fitnes(x:np.array):
    A, B = convert.B2D(x)
    res = []
    for a, b in zip(A, B):
        Em = a * L ** b
        diff = np.absolute(Ef - Em).sum()
        # diff = np.absolute((Ef - Em)/Ef).sum()/len(Em)
        res.append(diff)
    return np.array(res)


def fitnes_test(x:np.array):
    b, a = convert.B2D_one(x)
    Em = a * test_L ** b
    return Em