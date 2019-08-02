def porta():
    """ porta(): genera una porta a caso con probabilita' 1/4. 

    Viene utilizzata la funzione random() per generare un numero 
    casuale (reale) >= 0.0 e < 1.0

    Con probabilita'  0.75 non viene generata la porta
    per l'intervallo [0.75,1.0) => 1/4 viene generata la porta

    """
    import random

    r = random.random()
    #print("r=%f" % (r))

    if r > 0.75:
        print ("--- [[[ porta ]]] ---")
        return 1
    else:
        return 0    

def test_porta():
    """ test funzione porta, in media dovrebbe trovare 12/4 = 3 porte """
    print ("\n\n\nTEST-PORTA >>")
    tot = 0
    for i in range(12):
        r = porta()
        tot = tot + r
        print ("%d) porta ? => %d -- totale: %d" % (i,r,tot))
    print ("TEST-PORTA <<\n\n\n")



def scala(n):
    """ scala(): genera una scala e n gradini e ritorna il numero di porte.

    Per ogni gradino viene controllata la presenza di una "porta" casuale
    Viene ritornato il totale delle porte incontrate come risultato

    Per il calcolo dei totali viene utilizzato un parametro "accumulatore"
    simile a quanto usato nell'esempio di "Tail Recursion":

    * http://antoniotancredi.altervista.org/2010/01/20/tail-recursion/



    """

    #@TODO: questa riga *NON* e' giusta, deve essere un argomento di scala()
    totale_porte = 0 

    if n == 0:
        #@TODO: come ritornare il totale finale chiamata ricorsiva?
        print "FINE SCALA -- TOTALE: %d " % (totale_porte)
        return 0

    porta_su_scalino = porta()
    totale_porte = totale_porte + porta_su_scalino
    print "scalino %d -- porta? %d, totale: %d " % (n, porta_su_scalino, totale_porte)

    #@TODO: come propagare il totale nella chiamata ricorsiva?
    return scala(n-1)

def main():
    while True:
        nns = raw_input("... Scala: n ? ")
        if nns == "":
            print ("EOF => exit")
            break
        nn = int(nns)
        res = scala(nn) # @TODO: la chiamata scala() con accumulatore iniziale (=0)
        print "::: scala(%d) -> %r" % (nn, res)

test_porta()
main()
