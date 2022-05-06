import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
from typing import List


def prime_factorize(n: int) -> List[int]:
    """
    Notes:
        https://en.wikipedia.org/wiki/Trial_division
        https://note.nkmk.me/python-prime-factorization/
    """
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    if len(a) == 0:
        a = [n]
    return a


def sq_edge_length(i: int) -> int:
    if i % 2 == 0:
        edge = 0.5*i+1
    else:
        edge = 0.5*(i-1)+1
    return int(edge)


def draw():
    rot = np.matrix([[np.cos(np.pi/2), -np.sin(np.pi/2)],
                     [np.sin(np.pi/2), np.cos(np.pi/2)]]
                    )
    edge_lengths = [sq_edge_length(i) for i in range(20)]

    fig, ax = plt.subplots()

    n = 0
    xy = np.array([0, 0])
    v = np.matrix([[1], [0]])
    for edge_length in edge_lengths:
        for i in range(edge_length):
            # print(n)
            c = '#cccccc'
            if n >= 2:
                p = prime_factorize(n)
                if len(p) == 1:
                    # print(n)
                    c = '#cc0000'
            ax.plot(xy[0], xy[1], 'o', color='white')
            ax.text(xy[0], xy[1], f'{n}', color=c, va='center', ha='center')
            xy += np.ravel(v).astype(np.int32)
            n += 1
            if i == (edge_length-1):
                v = rot*v

    ax.set_aspect('equal')

    plt.show()


if __name__ == '__main__':
    draw()
