def inverse_tensor(t):
    delta = 2 * (t[0] * t[5] - t[2] * t[3])
    i_t = [0] * 6
    i_t[0] = 0.5 * t[5] / delta
    i_t[1] = 1 / t[1]
    i_t[2] = -t[5] / delta
    i_t[3] = -t[5] / delta
    i_t[4] = 4 / t[4]
    i_t[5] = 2 * t[0] / delta
    return i_t


def t_multiply(t1, t2):
    t_n = [0] * 6
    if t1[0] != 0:
        if t2[0] != 0:
            t_n[0] += 2 * t1[0] * t2[0]

        if t2[2] != 0:
            t_n[2] += 2 * t1[0] * t2[2]

    if (t1[1] != 0) & (t2[1] != 0):
        t_n[1] += t1[1] * t2[1]

    if t1[2] != 0:
        if t2[3] != 0:
            t_n[0] += t1[2] * t2[3]

        if t2[5] != 0:
            t_n[2] += t1[2] * t2[5]

    if t1[3] != 0:
        if t2[0] != 0:
            t_n[3] += 2 * t1[3] * t2[0]

        if t2[2] != 0:
            t_n[5] += 2 * t1[3] * t2[2]

    if (t1[4] != 0) & (t2[4] != 0):
        t_n[4] += 0.5 * t1[4] * t2[4]

    if t1[5] != 0:
        if t2[3] != 0:
            t_n[3] += t1[5] * t2[3]

        if t2[5] != 0:
            t_n[5] += t1[5] * t2[5]

    return t_n
