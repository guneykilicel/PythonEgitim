"""
isim bilgisi ad soyad 3not bunları dosyaya kaydet
kaydettiğin dosyada ortalamayı bul harf karşılığı da bul sonra bunları farklı bir dosyaya kaydet
"""

def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    ogrenciAdi=liste[0]
    notlar=liste[1]
    notlar=notlar.split(",")
    ort=(int(notlar[0])+int(notlar[1])+int(notlar[2]))/3

    if ort >=90 and ort<=100:
        harf="AA"
    elif ort>=85 and ort<=89:
        harf="BA"
    elif ort>=65 and ort<=84:
        harf="CC"
    else:
        harf="FF"

    return (f"{ogrenciAdi} {harf}")
    

def ortalamalari_oku():
    with open("notlar.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad=input("Öğrenci ad: ")
    soyad=input("Öğrenci soyad: ")
    not1=int(input("1. not: "))
    not2=int(input("2. not: "))
    not3=int(input("3. not: "))
    with open("notlar.txt","a",encoding="utf-8") as file:
        #file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")
        file.write(f"{ad} {soyad}:{not1},{not2},{not3}\n")

def notlari_kayitet():
    with open("notlar.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i+"\n")



while True:
    islem=int(input("1-Noktları Oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Çıkış\n"))
    if islem == 1:
        ortalamalari_oku()
    elif islem ==2:
        not_gir()
    elif islem ==3:
        notlari_kayitet()
    else:
        break






















