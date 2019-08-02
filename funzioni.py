def fa(c):
    """converte gradi celsius in farheneit"""
    f = (9./5.)*c + 32
    return(f)

def fact(n):
    print (" ... fact(%d)" % n)

    if (n == 0):
        res = 1
    else:
        res = (n * fact( n - 1))
    print (" ... fact(%d) -> %d" % (n,res))
    return res


print(fact(5))



def scalinata_di_Giacobbe():
    print "scalino"
    scalinata_di_Giacobbe()
