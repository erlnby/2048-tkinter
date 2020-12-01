import numpy as np

import random

from utils import compose


class State:
    def __init__(self, data=np.zeros([4, 4], dtype=int), start=False):
        self.data = data
        self.scores = 0

        if start:
            self._random()
            self._random()

    def down(self):
        self._move(np.fliplr, np.transpose)

    def up(self):
        self._move(np.transpose)

    def right(self):
        self._move(np.fliplr)

    def left(self):
        self._move(lambda x: x)

    def _move(self, *fs):
        data = self.data
        forward = compose(*fs)
        backward = compose(*reversed(fs))

        data = forward(data)
        data, scores = State._left(data)
        data = backward(data)

        if (data != self.data).any():
            self.scores += scores
            self.data = data
            self._random()

    @staticmethod
    def _left(data):
        result = []
        scores = 0
        for row in data:
            clear = np.delete(row, row == 0)
            merge = clear
            i = 0
            while i < len(merge) - 1:
                if merge[i] == merge[i + 1]:
                    merge = np.delete(merge, i + 1)
                    merge[i] *= 2
                    scores += merge[i]
                i += 1
            result.append(np.append(merge, np.zeros(4 - len(merge))))
        return np.array(result), scores

    def _random(self):
        result = np.array(np.where(self.data == 0)).T
        if len(result):
            row = np.random.choice(result.shape[0], 1)[0]
            index = result[row]
            value = 4
            if random.random() < 0.9:
                value = 2
            self.data[index[0]][index[1]] = value

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    s1 = State(np.eye(4))
    s2 = State(np.array([
        [2, 2, 0, 0],
        [0, 2, 2, 0],
        [2, 4, 2, 2],
        [2, 0, 0, 2]
    ]))
    print(s1._left())
    print(s2._left())
