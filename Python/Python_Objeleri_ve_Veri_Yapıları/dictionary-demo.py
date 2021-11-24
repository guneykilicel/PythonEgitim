ogrenciler={
    "120" : {
        "ad" : "Güney",
        "soyad" : "Kılıçel",
        "telefon" : "532 000 00 01"
    },
    "125" : {
        "ad" : "İrem",
        "soyad" : "Ocak",
        "telefon" : "532 000 00 02"
    },
    "128" : {
        "ad" : "Kuzey",
        "soyad" : "Kuzey",
        "telefon" : "532 000 00 03"
    },

}
# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

numara=input("Okul numaranızı giriniz: ")
isim=input("İsminizi giriniz: ")
soyisim=input("Soyisminizi giriniz: ")
telno=input("Telefon numaranızı giriniz: ")

# ÖĞRENCİ KAYDI BU ŞEKİLDE DE YAPILABİLİR
ogrenciler[numara]={ #çok boyutlu dizi gibi düşün atamayı bu şekilde yapıyoruz
    "ad" : isim,
    "soyad" : soyisim,
    "telefon" : telno
}

numara=input("Okul numaranızı giriniz: ")
isim=input("İsminizi giriniz: ")
soyisim=input("Soyisminizi giriniz: ")
telno=input("Telefon numaranızı giriniz: ")

#İKİNCİ ÖĞRENCİ KAYIT YÖNTEMİ ".update" bu daha güzel "," atıp birden fazla kullanıcı da ekleyebiliriz
ogrenciler.update({
    numara: {
    "ad" : isim,
    "soyad" : soyisim,
    "telefon" : telno
    }
})


print(ogrenciler)



#Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
print("*"*50)
okulno=input("Okul numaranızı giriniz: ")

#print(ogrenciler[okulno])

#bu şekilde cümle halinde yazmak için dikkat et {} içinde TEK TIRNAK kullandım
ogrenci=ogrenciler[okulno]
print(f"Aradığınız {okulno} nolu öğrencinin adı: {ogrenci['ad']} {ogrenci['soyad']} telefon numarası: {ogrenci['telefon']} ")













