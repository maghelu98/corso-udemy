n = input("mi dia il numero di studenti a disposizione: ")
if(n > 30):
    print("gli studenti devono essere divisi in piu' classi")
elif(n < 15):
    print("troppi pochi studenti per formare una classe")
else:
    print("la classe e' formata da %d studenti" % (n))
