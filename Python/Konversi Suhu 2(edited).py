import time

print()

print("=" * 20," Program Konversi Suhu ","=" * 20)
def Konversi() :
    print()

    print('''Silakan Pilih satuan Suhu yang diketahui: 

    1. Celcius
    2. Fahrenheit
    3. Reamur
    4. Kelvin
    ''')

    Suhu = int(input("Ketik 1 untuk Celcius, 2 untuk Fahrenheit, 3 untuk Reamur, 4 untuk Kelvin : "))
   
    print()

    # Celcius
    if Suhu == 1 :
        Suhu1 = float(input("Masukan besar suhu dalam Celcius (C) : "))
        print()
        F = (Suhu1 * 9/5) + 32
        print("Fahrenheit : ", F, "F")
        R = (4/5) * Suhu1
        print("Reamur   : ", R, "R")
        K = Suhu1 + 273.15
        print("Kelvin    : ", K, "K")

    # Fahrenheit
    elif Suhu == 2 :
        Suhu2 = float(input("Masukan besar suhu dalam Fahrenheit (F) : "))
        print()
        C = (Suhu2 - 32) * 5/9
        print("Celcius   : ", C, "C")
        R = 4/9 * (Suhu2 - 32)
        print("Reamur   : ", R, "R")
        K = (Suhu2 + 459.67) * 5/9
        print("Kelvin    : ", K, "K")

    # Reamur
    elif Suhu == 3 :
        Suhu3 = float(input("Masukan besar suhu dalam Reamur (R) : "))  
        print()
        C = Suhu3 / 0.8
        print("Celcius   : ", C, "C")            
        F = (Suhu3 * 2.25) + 32
        print("Fahrenheit : ", F, "F")           
        K = (Suhu3 / 0.8) + 273.15
        print("Kelvin    : ", K, "K")    

    # Kelvin
    elif Suhu == 4 :
        Suhu4 = float(input("Masukan besar suhu dalam Kelvin (K) : "))  
        print()
        C = Suhu4 - 273.15
        print("Celcius   : ", C, "C")           
        F = (Suhu4 * 9/5) - 459.67
        print("Fahrenheit : ", F, "F")            
        R = 4/5 * (Suhu4 - 273)
        print("Reamur   : ", R, "R")

    print()
    
    Var = str(input("Ingin mengkonversi lagi ? (y/n) : " ))
        

    if Var.lower() == "y" :
            Konversi()
    
    elif Var.lower() == "n":
        print()
        print("Terimakasih Telah Mencoba:)")
            
    else:
        print("Nomor Tidak Terdaftar")
        time.sleep(2)
        return Konversi()
   
Konversi()
 
time.sleep(5)

