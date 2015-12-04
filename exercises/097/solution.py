def love_meet(L1, L2):
    L1 = set(L1)
    L2 = set(L2)
    L3 = L1 & L2
    return(L3)

def affair_meet(L1, L2, L3):
    L1 = set(L1)
    L2 = set(L2)
    L3 = set(L3)
    L4 = L2 & L3
    L5 = L4 - L1
    return(L5)
