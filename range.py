print("Celsius\tFarhenheit\n")
for c in range(50,151,10):
    f = (9./5.)*c + 32
    print(("%d\t%.1f\n") % (c,f))
