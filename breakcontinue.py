for x in range(20):
    print("%d")
    if x % 3 == 0:
        print("%d mod 3 == 0" % x)
        break
    else:
        continue

