n = input("dimmi un numero: ")
if n <= 0:
    print("ERRORE")
else:
    if n%2 == 0:
        print("pari")
    elif n%2 != 0:
        print("dispari")
    else:
        print("strano")
