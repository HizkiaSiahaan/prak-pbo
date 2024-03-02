x = int(input("Inputkan batas bawah : "))
y = int(input("Inputkan batas atas : "))
z = 0

if(x < 0 or y < 0 ):
    print("Batas bawah dan atas tidak boleh dibawah nol")
else:
    for i in range (x,y):
        if(i%2 == 1):
            print(i)
            z += i
    print("Jumlah total bilangan ganjil adalah = " + str(z))
