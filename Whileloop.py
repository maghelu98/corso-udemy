print("Celsius\tFahrenheit\n")
c = 50
while c < 151:
    f = (9./5.)*c + 32
    print("%d\t%.1f\n" % (c, f))
    c += 10
