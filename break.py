delta = input("delta: ")
try:
    for i in range(1,20):
        try:
            print("i = %d ..." % (i))
            j = 1.0/(delta+10.0-i)
            print("i =%d , j = %f " % (i,j))
        except Exception as e:
            print("prima di raise: {}, per i = {:d}".format(e, i))
            raise
            print("dopo di raise: {}, per i = {:d}".format(e,i))
            break
    print("programma completato")
except Exception as e:
    print("programma in errore: {}".format(e))
    raise
