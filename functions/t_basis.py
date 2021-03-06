import numpy as np


def inverse_tensor(t):
    delta = 2 * (t[0] * t[5] - t[2] * t[3])
    i_t = np.zeros(6)
    i_t[0] = 0.5 * t[5] / delta
    i_t[1] = 1 / t[1]
    i_t[2] = -t[2] / delta
    i_t[3] = -t[3] / delta
    i_t[4] = 4 / t[4]
    i_t[5] = 2 * t[0] / delta
    i_t = np.around(i_t, decimals=15)
    return i_t


def t_multiply(t1, t2):
    t_n = np.zeros(6)
    t_n[0] = 2 * t1[0] * t2[0] + t1[2] * t2[3]
    t_n[1] = t1[1] * t2[1]
    t_n[2] = 2 * t1[0] * t2[2] + t1[2] * t2[5]
    t_n[3] = 2 * t1[3] * t2[0] + t1[5] * t2[3]
    t_n[4] = 0.5 * t1[4] * t2[4]
    t_n[5] = 2 * t1[3] * t2[2] + t1[5] * t2[5]
    t_n = np.around(t_n, decimals=15)
    return t_n


def get_C(lya, mu):
    C = np.array([lya + mu, 2 * mu, lya, lya, 4 * mu, lya + 2 * mu])
    return C