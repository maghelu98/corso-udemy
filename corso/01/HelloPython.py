# MCD: massimo comun divisore: algoritmo di Euclide

# https://codereview.stackexchange.com/questions/95521/gcd-using-euclid-algorithm

# versione ricorsiva
def gcd_rec(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19) ->  1
    >>> gcd(39, 91) ->  13
    >>> gcd(20, 30) ->  10
    >>> gcd(40, 40) ->  40
    """
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd_rec(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd_rec(b, a % b)

# versione iterativa
def gcd_iter(a, b):
  while b:
    a, b = b, a % b
  return a

USE_RECURSIVE = True # False # True #

def gcd(a, b):
  if USE_RECURSIVE:
    return gcd_rec(a,b)
  else:
    return gcd_iter(a, b)

def gcd_show(a, b):
    print("\t gcd(%d,%d) -> %d" % (a, b, gcd(a,b)))

def main():
    print("===[GCD]=====")
    gcd_show(34,19)
    gcd_show(39,91)
    gcd_show(20,30)
    gcd_show(40,40)

if __name__ == "__main__":
    main()