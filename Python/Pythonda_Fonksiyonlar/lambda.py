def square(num): return num**2

numbers=[1,2,3,4,5]
"""MAP"""
#Dizideki tüm elemanlara "square" fonksiyonunu uygulamak istiyoruz. Döngü ilede yapılabilir.
# "map" metodunu kullanacağız:

map(square,numbers) #kullanacağımız fonksiyonu ve sonrasında diziyi veriyoruz her elemana
# fonksiyonu uyguluyor. Ama iş ekrana vermeye gelince bir sürü eleman vereceği için
#liste olarak vermeliyiz.

result=list(map(square,numbers)) #Birden fazla eleman vereceği için "list()"" kullandık
print(result)


for item in map(square,numbers): #ya list olucak ya da böyle döngü ile tek tek alıcan
    print(item)



print("\n")
"""LAMBDA"""
#Şimdi yapmak istediğimiz şey elimizde bir fonksiyon yok 
# ama dizinin her elemanına bir işlem yapmak istiyoruz GEÇİÇİ fonksiyon yapabiliriz

sayilar=[1,3,5,9]
result=list(map(lambda sayi: sayi**2, sayilar)) #lamda dedik istediğimiz işlemi yaptık

print(result)

#Hatta lambda ile bir değişkeni fonksiyon yapabiliriz:
kup= lambda a: a**3
print(kup(5))





""" ŞİMDİ BİZ BASİT İŞLEMLER YAPTIK "MAP" İLE AMA SORGULAMA DA YAPALIM MESELA BU FONKSİYONU
    DİZİDEKİ SADECE ÇİFT ELEMANLARA UYGULA GİBİ"""
numbers=[1,2,3,4,5,6,7,8,9,10]
def check_even(num): return num%2==0 #1 Normal fonksiyon tanımlayıp map de bu fonksiyonu verebiliriz

check_even_lambda=lambda num: num%2==0 #2 Lamda ile fonksiyon yaratıp bunu map e verebiliriz

result= list(filter(check_even,numbers)) #Filter kullanıyoruz çünkü filtreliyoruz
# map kullanırsak [False, True, False, True, False, True, False, True, False, True] verir.

result= list(filter(lambda c: c%2==0,numbers)) #3 direkt lambda ile kısa yoldan yapabilirsin.

result= check_even(numbers[2]) #bu şekilde sorgulama da yapabilirsin 2. index 3 olduğu için False

print(result)




















