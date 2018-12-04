from functions import t_basis as tb


def property_contribution_tensor(T0, T1, Ht):
    pc_tensor = tb.inverse_tensor(tb.inverse_tensor(T1-T0)+Ht)
    return pc_tensor


