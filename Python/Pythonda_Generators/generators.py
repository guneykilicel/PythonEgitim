"""
BELLEKTE YER KAPLAMAYAN BİR "ITERATOR"
"""

#Bellekte yer kaplayan normal dizi ile yaptığımız işlem
def cube():
    result=[]
    for i in range(5):
        result.append(i**3)
    return result
print(cube()) #[0, 1, 8, 27, 64]




# Şimde de "bellekte yer kaplamayan" şekilde yapalım
# Amacımız zaten 0 dan 5 e kadar sayı üretip onların küplerini alıp ekrana yazdırmak
# "liste" yerine "yield" kullanacağız tek seferlik kullanımlı gibi düşün kullan at ama nerede kaldığını bilir
def cube_generator():
    for i in range(5):
        yield i**3 #"generator" u generator yapan "yield"dir yukarıda açıkladım özelliklerini

for i in cube(): #sanki bir "iterator" özellikli dizi gibi çalıştı ama dizi değil yer de kaplamaz :)
    print(i)

# iterator=cube_generator() # Manuel yazdırma
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



print("\n")
"""
LİSTELER NASIL GENERATOR OLUR "[]" yerine "()" kullanılır.
"""
liste=[i**3 for i in range(5)] # Bu şekilde bellekte yer kaplar
print(liste)

liste=(i**3 for i in range(5)) # Bu şekilde bellekte yer kaplamaz ama ekran çıktısı adres yollar
print(liste) # <generator object <genexpr> at 0x000001D01AB21F90>

# print(next(liste)) # Ya bu şekilde manuel ya da alttaki gibi döngü ile

for i in liste:
    print(i)














