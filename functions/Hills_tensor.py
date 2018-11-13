import numpy as np


def get_hills_tensors_disk(lya, mu):
    p = np.zeros(6)
    q = np.zeros(6)
    k = (lya+mu)/(lya+2*mu)

    p[4] = 1/mu
    p[5] = (1-k)/mu

    q[1] = 2*mu*(4*k-1)
    q[2] = 2*mu
    return p, q


def get_hills_tensors_sphere(lya, mu):
    p = np.zeros(6)
    q = np.zeros(6)
    k = (lya + mu) / (lya + 2 * mu)

    p[0] = (1-k)/(9*mu)+(0.5-1/3)*(5-2*k)/(15*mu)
    p[1] = (5-2*k)/(15*mu)
    p[2] = (1-k)/(9*mu)-(5-2*k)/(45*mu)
    p[3] = p[2]
    p[4] = 2*p[1]
    p[5] = (1-k)/(9*mu)+(1-1/3)*(5-2*k)/(15*mu)

    q[0] = -4*mu*(1-4*k)/9+2*mu*(5+2*k)/15*(0.5-1/3)
    q[1] = 2*mu*(5+2*k)/15
    q[2] = -4*mu*(1-4*k)/9-2*mu*(5+2*k)/45
    q[3] = q[2]
    q[4] = 4*mu*(5+2*k)/15
    q[5] = -4*mu*(1-4*k)/9+2*mu*(5+2*k)/15*(1-1/3)
    return p, q
