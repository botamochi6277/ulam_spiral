import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
from typing import List, Tuple
import argparse


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
         figsize: Tuple[int, int] = (800, 600),
         no_color: str = '#cccccc',
         prime_no_color: str = '#4A00E0',
         marker_color: str = '#ffffff',
         prime_marker_color: str = '#8E2DE2',
         marker: str = 'o',
         markersize: float = 32,
         fontsize: float = 16,
         bg_color: str = '#f7f7f7',
         no_window: bool = False,
         output_name: str = ''):
    rot = np.matrix([[np.cos(np.pi/2), -np.sin(np.pi/2)],
                     [np.sin(np.pi/2), np.cos(np.pi/2)]]
                    )
    edge_lengths = [sq_edge_length(i) for i in range(num_edges)]

    fig, ax = plt.subplots(figsize=(figsize[0]/72, figsize[1]/72))
    fig.patch.set_facecolor(bg_color)
    fig.patch.set_alpha(1.0)

    n = 1
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
                    m_c = prime_marker_color
            ax.plot(xy[0], xy[1], marker=marker, color=m_c,
                    markersize=markersize)  # background
            ax.text(xy[0], xy[1], f'{n}', color=no_c,
                    va='center', ha='center', fontsize=fontsize)
            xy += np.ravel(v).astype(np.int32)
            n += 1
            if i == (edge_length-1):
                v = rot*v

    ax.set_aspect('equal')
    ax.axis('off')

    if len(output_name) > 0:
        plt.savefig(output_name)

    if not no_window:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num_edges', type=int, default=20)
    parser.add_argument('-s', '--figsize', type=int,
                        nargs=2, default=(800, 600))
    parser.add_argument('--no_color', default='#cccccc')
    parser.add_argument('--prime_no_color', default='#4A00E0')
    parser.add_argument('--marker', default='o')
    parser.add_argument('--marker_color', default='#ffffff')
    parser.add_argument('--prime_marker_color', default='#8E2DE2')
    parser.add_argument('--markersize', type=int, default=32)
    parser.add_argument('--fontsize', type=int, default=16)
    parser.add_argument('--bg_color', default='#f7f7f7')
    parser.add_argument('--no_window', action='store_true')
    parser.add_argument('-o', '--output_name', default='')

    args = parser.parse_args()
    params = vars(args).copy()
    draw(**params)
