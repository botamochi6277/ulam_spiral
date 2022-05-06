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


def draw(num_edges: int = 20,
         no_color: str = '#cccccc',
         prime_no_color: str = '#4A00E0',
         marker_color: str = '#ffffff',
         marker_prime_color: str = '#8E2DE2',
         bg_color: str = '#f7f7f7'):
    rot = np.matrix([[np.cos(np.pi/2), -np.sin(np.pi/2)],
                     [np.sin(np.pi/2), np.cos(np.pi/2)]]
                    )
    edge_lengths = [sq_edge_length(i) for i in range(num_edges)]

    fig, ax = plt.subplots()
    fig.patch.set_facecolor(bg_color)
    fig.patch.set_alpha(1.0)

    n = 0
    xy = np.array([0, 0])
    v = np.matrix([[1], [0]])
    for edge_length in edge_lengths:
        for i in range(edge_length):
            no_c = no_color
            m_c = marker_color
            if n >= 2:
                p = prime_factorize(n)
                if len(p) == 1:
                    no_c = prime_no_color
                    m_c = marker_prime_color
            ax.plot(xy[0], xy[1], 'o', color=m_c, markersize=16)  # background
            ax.text(xy[0], xy[1], f'{n}', color=no_c,
                    va='center', ha='center')
            xy += np.ravel(v).astype(np.int32)
            n += 1
            if i == (edge_length-1):
                v = rot*v

    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()


if __name__ == '__main__':
    draw()
