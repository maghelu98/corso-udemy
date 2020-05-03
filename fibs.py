#!/usr/bin/env python

COUNT = 0


def ctr_incr():
    global COUNT
    COUNT = COUNT + 1
    return COUNT


def ctr_reset():
    global COUNT
    COUNT = 0


##
# raw
#

def fib(n):
    print("--- %d) fib(%d)" % (ctr_incr(), n))
    return n if n < 2 else fib(n - 1) + fib(n - 2)


##
# explicit
#

fibcache = {}


def fib_memo(n):
    if n in fibcache:
        return fibcache[n]
    else:
        print("--- %d) fib_memo(%d)" % (ctr_incr(), n))
        fibcache[n] = n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)
        return fibcache[n]


##
# auto
#

def memoize(function):
    from functools import wraps

    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


@memoize
def fibonacci(n):
    print("--- %d) fibonacci(%d)" % (ctr_incr(), n))
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci(25)


modes = {
    'f': fib,
    'e': fib_memo,
    'a': fibonacci,
}


def main():
    while True:
        mode = input("... Mode ('f':no-cache,'e':explicit, 'a':auto): ? ")  #

        if mode == "":
            print("no-mode => exit")
            break

        if (not mode in modes):
            continue

        ctr_reset()

        f = modes[mode]
        nns = input("... n ? ")
        if nns == "":
            print("EOF => exit")
            break
        nn = int(nns)
        res = f(nn)
        print("::: fibonacci[%s](%d) -> %r" % (mode, nn, res))


main()
