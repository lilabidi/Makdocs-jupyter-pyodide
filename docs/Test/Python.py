# tri par insertion
# 2018-02-06    PV

import random

def tri_insertion(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i
        while j>0 and a[j-1]>x:
            a[j] = a[j-1]
            j = j-1
        a[j] = x