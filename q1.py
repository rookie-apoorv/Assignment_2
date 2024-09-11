import matplotlib.pyplot as plt
from math import comb
import pandas as pd
import numpy as np
m = 100
plist = [10]

for p in plist :
    nlist = []
    funclist = []
    for n in range(100,2500) :
        const = comb(m,p) * pow(m,p)
        func = const * pow(1/n,p) * pow((1-(m/n)),m-p)
        nlist.append(n)
        funclist.append(func)
    max_index = funclist.index(max(funclist))
    max = np.max(funclist)

    plt.scatter(nlist,funclist,label = 'Points')
    plt.annotate(f'Point ({nlist[max_index]},{max} )',  # Text label
             xy=(nlist[max_index], max),       # Point to annotate
             xytext=(nlist[max_index], max+0.01), # Position of the text
             arrowprops=dict(facecolor='black', arrowstyle='->')) 
    plt.xlabel("n values")
    plt.ylabel("Pm,p(n)")
    plt.title(f"Plot_m=100_p={p}.jpeg")
    #plt.show()
    plt.savefig(f"Plot_m=100_p={p}.jpeg", format = 'jpeg')

    expected_value_x = sum(x_i * p_i for x_i, p_i in zip(nlist, funclist))
    print(expected_value_x)
    suming = sum(p for p in funclist)
    print(suming)