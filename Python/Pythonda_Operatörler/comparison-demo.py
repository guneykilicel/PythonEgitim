# 1- Girilen 2 sayıdan hangisi büyüktür
# 2- Kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız
#    Eğer ortalama 50 ve üzerinde ise geçti değilse kaldı yazdırın
# 3- girilen bir sayının tek mi çift mi olduğunu yazdırın
# 4- girilen bir sayının negatif pozitif durumunu yazdırın
# 5- parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: guney@gmail.com parola:abc123)


#1
"""
a = int(input("a: "))
b = int(input("b: "))

result = a>b
print(f"a: {a} b: {b} den büyüktür: {result}")
"""
#2
"""
vize = int(input("1. Vize: "))
vize1 = int(input("2. Vize: "))
final = int(input("Final: "))

result= (vize+vize1)/2*60/100 + final*40/100

print(f"not ortalaması: {result} ve dersten geçme durumu: {result>=50}")
"""

#3
"""
s=int(input("sayi gir: "))
result=s%2
print(f"{s} sayisinin çift sayı olma durumu: {result == 0}")
"""

#4
"""
s=int(input("sayi gir: "))
print(f"{s} sayisinin negatif olma durumu: {s<0}")
"""

#5
parola="abc123"
email="kilicelguney@gmail.com"
enteremail=input("email: ")
enterpassw=input("password: ")

print(f"{enteremail.lower().strip()}: {email==enteremail.lower().strip()} and {enterpassw.strip()}: {parola.strip()==enterpassw}")







