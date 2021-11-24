x,y,z=2,5,10
numbers=1,5,7,10,6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
# 2- y'nin x'e kalansız bölümünü hesaplayınız
# 3-(x,y,z) toplamının mod 3 ü nedir
# 4- y'nin x. kuvvetini hesaplayınız
# 5- x, *y,z = numbers işlemine göre z'nin küpü kaçtır
# 6- x, *y,z = numbers işlemine göre y nin değerleri toplamı kaçtır?

#1

a=int(input("Sayi gir: ")) #burada aldığımız değer ile matematiksel işlem yapacağımız için int yaptık
b=int(input("Sayi gir: "))
print((a*b)-(x+y+z))

#2
print(y//x)

#3
print((x+y+z)%3)

#4
print(y**x)

#5
x, *y,z = numbers
print(z**3)

#6
x, *y,z = numbers

print(y[0]+y[1]+y[2])




