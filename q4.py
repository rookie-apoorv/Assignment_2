import numpy as np
import matplotlib.pyplot as plt
from math import comb

def func(M , c) : 
    sum = 0
    for i in range(M+1,2*M + 2) :
        sum += comb(2*M+1,i)*pow((0.5+c),i)*pow((0.5-c),2*M+1-i)

    return sum



clist = [round((0.05 + 0.01*i),2) for i in range ( 0 ,21)]

for c in clist :
    mlist = [ i for i in range(0,20)]
    funclist = [func(m,c) for m in mlist]

    closest_index_7 = min(range(len(funclist)), key=lambda i: abs(funclist[i] - 0.75))
    if funclist[closest_index_7] - 0.75 < 0 and closest_index_7 < 19 : closest_index_7+=1
    closest_index_9 = min(range(len(funclist)), key=lambda i: abs(funclist[i] - 0.9))
    if funclist[closest_index_9] - 0.9 < 0  and closest_index_9 < 19 : closest_index_9+=1
    plt.scatter(mlist,funclist)
    plt.xlabel("M values")
    plt.ylabel("P(Fair Decision)")
    plt.xticks(np.arange(0,21,1))
    plt.axhline(y=0.75, color='r', linestyle='--')
    plt.axhline(y=0.9, color='r', linestyle='--')
    plt.annotate(f'({mlist[closest_index_7]},{funclist[closest_index_7]} )',  # Text label
             xy=(mlist[closest_index_7],funclist[closest_index_7]),       # Point to annotate
             xytext=(mlist[closest_index_7]-0.1, funclist[closest_index_7]+0.01), # Position of the text
             arrowprops=dict(facecolor='black', arrowstyle='->')) 
    plt.annotate(f'({mlist[closest_index_9]},{funclist[closest_index_9]} )',  # Text label
            xy=(mlist[closest_index_9],funclist[closest_index_9]),       # Point to annotate
            xytext=(mlist[closest_index_9]-1, funclist[closest_index_9]+0.05), # Position of the text
            arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.title(f'c = {c}')
    plt.savefig(f"c= {c}.jpeg",format ='jpeg')
    plt.clf()


