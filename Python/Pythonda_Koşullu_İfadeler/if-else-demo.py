# 1-Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet 
#   alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve  
#   eğitim durumu lise ya da üniversite olmalıdır


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#   0 -24 => 0
#   25-44 => 1
#   45-54 => 2
#   55-69 => 3
#   70-84 => 4
#   85-100 => 5


# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesapla.
#   1.bakım => 1. yıl
#   2.bakım => 2. yıl
#   3.bakım => 3. yıl
# Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
# datetime modülünü kullanmanız gerekiyor.
# (şimdi) - (2018/8/1) =>gün


#1
"""
name=input("isminizi giriniz: ")
age=int(input("Yaşınızı giriniz: "))
education=input("Eğitim durumu (Lise,Üniversite): ")

if(age>=18):
    if(education.title()=="Lise" or education.title()=="Üniversite"):
        print("Alabilirsiniz.")
    else:
        print("Alamazsınız.")
else:
    print("Alamazsınız.")
"""

#2
"""
n1=float(input("Not1: "))
n2=float(input("Not2: "))
sozlu=float(input("Sözlü: "))

ort=(n1+n2+sozlu)/3
if(0<=ort<=24):
    print("0")
elif(25<=ort<=44):
    print("1")
elif(45<=ort<=54):
    print("2")
elif(55<=ort<=69):
    print("3")
elif(70<=ort<=84):
    print("4")
elif(85<=ort<=100):
    print("5")
"""

#3
import datetime

tarih=input("aracınız hanngi tarihte trafiğe çıktı(2019/8/9): ")
tarih = tarih.split("/")

trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi-trafigeCikis
days=fark.days

if days<=365:
    print("1. servis aralığı")
elif days>365 and days<=365*2:
    print("2. servis aralığı")
elif days>365*2 and days<=365*3:
    print("3. servis aralığı")
else:
    print("hatalı süre bilgisi")




















