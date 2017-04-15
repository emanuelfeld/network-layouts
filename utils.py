import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def display_plot(G, pos, size=50):
    nx.draw_networkx(G, pos, node_size=size, with_labels=False)
    plt.draw()
    plt.show()

def normalize(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    dist = l2
    l2[l2==0] = 1
    return dist, a / np.expand_dims(l2, axis)

def div0(a, b):
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide(a, b)
        c[~np.isfinite(c)] = 0
    return c