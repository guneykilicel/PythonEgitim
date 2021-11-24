# 1- girilen br sayinin 0-100 arasında olup olmadığını kontrol ediniz
# 2- girilen sayının pozitif çift sayı olup olmadığını kontrol ediniz
# 3- email ve parola bilgileri ile giriş kontrolü yapınız
# 4- girilen 3 sayıyı büyüklük olarak karşılaştırınız
# 5- kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız
#    eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırsın
#    a-) ortalama 50 olsa bile final notu en az 50 olmalıdır
#    b-) finalden 70 aldığında ortalamanın önemi olmasın
# 6-Kişisinin ad,kilo ve bilgilerini alıp kilo indekslerini hesaplayınız
#   Aşağıdaki tabloya göre hangi gruba girmektedir
#   0-18.4    => zayıf
#   18.5-24.9 => normal
#   25.0-29.9 => fazla kilolu
#   30.0-34.9 => şişman(obez)

#1
"""
s=int(input("sayı gir: "))
print(f"Sayı 0-100 arasındadır: {0<s<100}")
"""

#2
"""
s=int(input("sayı gir: "))
print(f"Sayı pozitif ve çifttir: {s>0 and s%2==0}")
"""

#3
"""
email="guney@gmail.com"
password="abc123"
enteremail=input("email: ")
enterpassw=input("password: ")

print(f"{enteremail.lower().strip()==email and enterpassw.strip()==password}")
"""

#4
"""
s=int(input("sayı gir: "))
s1=int(input("sayı gir: "))
s2=int(input("sayı gir: "))

print(f"En büyük sayı {s}dir: {s>s1 and s>s2}")
print(f"En büyük sayı {s1}dir: {s1>s and s1>s2}")
print(f"En büyük sayı {s2}dir: {s2>s1 and s2>s}")
"""

#5
"""
vize=int(input("sayı gir: "))
vize1=int(input("sayı gir: "))
final=int(input("sayı gir: "))

avarage=(vize+vize1+final)/3

print(f"Dersi geçti: {avarage>=50 and final>=50 or final>=70}")
"""

#6
isim=input("isim gir: ")
kilo=float(input("kilo gir: ")) #ondalıklı sayılarda float olur boy içinde geçerli
boy=float(input("boy gir(metre cinsinden ex: 1.80): "))
index=kilo/boy**2
zayıf=(index >=0) and (index<=18.4)
normal=(index>18.4) and (index<=24.9)
kilolu=(index>25) and (index<=29.9)
obez=(index>30) and (index<=34.9)



print(f"{isim} kilo indeksin: {index} ve kilo değerlendirmen Zayıf: {zayıf}")
print(f"{isim} kilo indeksin: {index} ve kilo değerlendirmen Normal: {normal}")
print(f"{isim} kilo indeksin: {index} ve kilo değerlendirmen Fazla Kilolu: {kilolu}")
print(f"{isim} kilo indeksin: {index} ve kilo değerlendirmen Obez: {obez}")


