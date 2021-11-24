sayilar=[1,3,5,7,9,12,19,21]

# 1- Sayılar listesindeki hangi sayılar 3 ün katıdır?
# 2- Sayılar listesinde sayıların toplamı kaçtır
# 3- Sayılar listesindeki tek sayıların karesini alınız

sehirler=["Kocaeli","İstanbul","Ankara","İzmir","Rize"]

#Şehirlerden hangileri en fazla 5 karakterlidir?

urunler=[
    {"name":"samsung S6","price":"3000"},
    {"name":"samsung S7","price":"4000"},
    {"name":"samsung S8","price":"5000"},
    {"name":"samsung S9","price":"6000"},
    {"name":"samsung S10","price":"7000"}
]

# 5-Ürünlerin fiyatları toplamı nedir?
# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz?


#1
for i in sayilar:
    if(i%3==0):
        print(i)

#2
print("\n")
toplam=0
for i in sayilar:
    toplam +=i
print(toplam)

#3
print("\n")
for i in sayilar:
    if(i%3==0):
        print(i**2)


#4
print("\n")
for a in sehirler:
    if(len(a)<=5):
        print(a)


#5
toplam=0
print("\n")
for urun in urunler:
    toplam+=int(urun['price'])

print(toplam)

#6
for urun in urunler:
    if int(urun["price"])<=5000:
        print(urun["name"])




