sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp tüm tek sayıları ekrana yazdırın.
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
# 4: Kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın.
# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun
#    ** dictionary listesi yapısı (name,price) şeklinde olsun
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.


#1
"""
x=0
while x<len(sayilar):
    print(sayilar[x])
    x +=1
"""
#2
"""
print("\n")
start=int(input("Başlangıç değerini giriniz: "))
finish=int(input("Bitiş değerini giriniz: "))

while start<finish:
    if start%2==1:
        print(start)
    start +=1
"""

#3
"""
i=100
while i>0:
    print(i)
    i -=1
"""
#4

liste=[]
x=0
while x<5:
    sayi=int(input(f"{x}. sayıyı giriniz: "))
    liste.append(sayi)
    x +=1
liste.sort()
print(liste)


#5
"""
uruns=int(input("Ürün sayısı: "))

urunler={}
x=0
while x<uruns:
    urunad=input("Ürün adını giriniz: ")
    urunfiyat=input("ürün fiyatını giriniz: ")
    urunler.update({
    x: {
    "urunad" : urunad,
    "urunfiyat" : urunfiyat
    }
})
    x +=1

print(urunler)

"""









