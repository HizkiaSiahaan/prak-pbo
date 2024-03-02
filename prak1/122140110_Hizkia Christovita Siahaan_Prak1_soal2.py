jari2 = int(input("Inputkan jari - jari : "))
phi = 3.14

if(jari2 < 0):
    print ("Jari-jari lingkaran tidak boleh negatif")
else:
    Keliling = phi * jari2 * 2
    Luas = phi * jari2 * jari2
    print ("Luas = " + str(Luas))
    print ("Keliling = " + str(Keliling))
