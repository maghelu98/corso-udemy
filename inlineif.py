n = input("dimmi un numero: ")
if(n <= 0):
    print("ERRORE")
else:
    print("pari" if(n%2 == 0) else "dispari")
