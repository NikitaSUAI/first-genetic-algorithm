import numpy as np

#
def get_chromosome(arr):
    # ищет 2 случайные хромосомы
    how = len(arr)
    if how == 1:
        res = arr[0], arr[0]
        arr.clear()
        return res
    elif how == 2:
        res = arr[0], arr[1]
        arr.clear()
        return res
    first = np.random.randint(how)
    sec = np.random.randint(how)
    while sec == first:
        sec = np.random.randint(how)
    res = arr[first], arr[sec]
    arr.remove(arr[first])

    if first > sec:
        arr.remove(arr[sec])
    else:
        arr.remove(arr[sec-1])
    return res



class Crossingover:
    def __init__(self, prob=0.5):
        self.prob = (1 - prob) * 100

    def do(self, arr: np.array):
        """Одноточечный оператор крссенговера
        :param arr: двумерный массив значений, где каждый подмассив это
        двоичное число
        :type arr: np.array
        :return массив с хромасомами подвергимися кроссенговеру
        :rtype: np.array
        """
        arr = arr.tolist()

        crosses = lambda k, a, b: [[a[i], b[i]] if i < k else
                                   [b[i], a[i]] for i in range(len(a))]

        res = lambda array: [] if not array else \
            np.array(crosses(np.random.randint(len(array[0])),
                     *get_chromosome(array))).T.tolist() + res(array) \
                if np.random.randint(100) > self.prob else res(array[1:])

        return np.array(res(arr), dtype=np.uint8)


if __name__ == "__main__":
    """Tests"""
    c = Crossingover(0.1)
    genotype = np.random.uniform(low=0, high=2, size=(9, 15)).astype(
        np.uint8)
    print(len(genotype))
    mean = 0
    n = 1000
    for _ in range(n):
        mean += len(c.do(genotype))
    mean /= n
    print(mean)
