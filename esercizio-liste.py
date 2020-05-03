raw_
n = int(input("n: "))
lr = []
for i in range(0,n):
    ld = []
    for j in range(2,i-1):
        if i%j == 0:
            ld.append(j)
    lr.append(ld)
print(lr)
