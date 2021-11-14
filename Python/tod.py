print("=" * 5, "Tugas Konversi Suhu", "=" * 5)

print()
print(" 1. Celcius \n 2. Fahrenheit \n 3. Reamur \n 4. Kelvin \n")

suhu = int(input("Silahkan masukan angka satuan suhu yang ingin dipilih : "))

print()

#Jika input user adalah satu = Celcius
if suhu == 1:
    suhu1 = int(input("Masukan besar suhu dalam Celcius (C) : "))
    print()
    F = (suhu1 * 9/5) + 32
    print("Fahrenheit : ", F, "F")
    R = (4/5) * suhu1
    print("Reamur   : ", R, "R")
    K = suhu1 + 273.15
    print("Kelvin    : ", K, "K")

#jika input user adalah 2 = Fahrenheit
elif suhu == 2:
    suhu2 = int(input("Masukan besar suhu dalam Fahrenheit (F) : "))
    print()
    C = (suhu2 - 32) * 5/9
    print("Celcius   : ", C, "C")
    R = 4/9 * (suhu2 - 32)
    print("Reamur   : ", R, "R")
    K = (suhu2 + 459.67) * 5/9
    print("Kelvin    : ", K, "K")

#jika input user adalah 3 = Reamur
elif suhu == 3:
    suhu3 = int(input("Masukan besar suhu dalam Reamur (R) : "))
    print()
    C = suhu3 / 0.8
    print("Celcius   : ", C, "C")            
    F = (suhu3 * 2.25) + 32
    print("Fahrenheit : ", F, "F")           
    K = (suhu3 / 0.8) + 273.15
    print("Kelvin    : ", K, "K") 

#jika input user adalah 4 = kelvin
elif suhu == 4:
    suhu4 = int(input("Masukan besar suhu dalam Kelvin (K) : "))
    print()        
    C = suhu4 - 273.15
    print("Celcius   : ", C, "C")           
    F = (suhu4 * 9/5) - 459.67
    print("Fahrenheit : ", F, "F")            
    R = 4/5 * (suhu4 - 273)
    print("Reamur   : ", R, "R")

#jika input user selain 1-4 = false
else:
    print("Harap masukan input dengan benar ya sayang :3 lopyuu dari bimjiKocheng")