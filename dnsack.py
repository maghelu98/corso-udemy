#!/usr/bin/env python3

def KnapSackTable(weight, value, P, n):
    T = [[ 0 for w in range(P + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        print("i:",i," | ",end='\t')
        for w in range(P + 1):
            b = ' '
            if i == 0 or w == 0:
                T[i][w] = 0
            elif weight[i - 1] <= w:
                T[i][w] = max(value[i-1]+T[i - 1][w - weight[i -1]],
                T[i - 1][w])
                d = value[i-1]+T[i - 1][w - weight[i -1]] - T[i - 1][w]
                b = '*' if d > 0 else '=' if d == 0 else '-'
            else:
                T[i][w] = T[i - 1][w]
            print(T[i][w],b,end='\t')
        print("")
    res = T[n][P]
    print("Total Value: ", res)
    w = P
    totweight = 0
    for i in range(n, 0, -1):
        if res < 0:
            break
        if res == T[i - 1][w]:
            continue
        else:
            print("Item selected: (%d, %d)" % (weight[i -1],value[i - 1]))
            totweight += weight[i - 1]
            res -= value[i - 1]
            w -= weight[i - 1]
    print("Total weight: ", totweight)

objects = [ (5, 18), (2, 9), (4, 12), (6, 25) ]
print("Items available: ", objects)
print("*******************************")
value = []
weight = []
for item in objects:
    weight.append(item[0])
    value.append(item[1])
P = 10
n = len(value)
KnapSackTable(weight, value, P, n)
