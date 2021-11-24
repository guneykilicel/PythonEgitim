#Sayı tahmin oyunu

import random

puan=0


for x in range(5):
    sayi= random.randrange(1,100,1) #randrange ile bu sayı şeklinde verdik
    print(sayi)
    print("*************Yeni Soru*************")
    can=int(input("Kaç canınız olsun :"))
    for i in range(can):
        
        gir=int(input("Tahmini giriniz: "))
        if(gir==sayi):
            puan +=20
            print(f"Doğru tahmin! Puanınız {puan}")
            break
        elif(gir>sayi):
            can -=1
            print(f"Daha küçük tahmin edin. {can} canınız kaldı")

        elif(gir<sayi):
            can -=1
            print(f"Daha büyük tahmin edin. {can} canınız kaldı")


        else:
            can -=1
            print(f"Geçersiz tahmin {can} canınız kaldı")

print(f"TOPLAM PUAN: {puan}")






















