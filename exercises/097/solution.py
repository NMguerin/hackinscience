def love_meet(L1, L2):
    L1 = set(L1)
    L2 = set(L2)
    L3 = L1 & L2
    return(L3)

def affair_meet(L1, L2, L3):
    L1 = set(L1)#bob
    L2 = set(L2)#alice
    L3 = set(L3)#silvester
    L4 = L2 & L3#là où vont alice et silvester
    L5 = L4 - L1#là ou ils vont tous
#    L6 = 
    return(L5)
