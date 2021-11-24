# x = 5
# y = 10
# z = 20



x, y, z=5, 10, 20
print(x,y,z)

x,y = y,x
print(x,y,z)

y = y//5 #veya y //= 5 bölümün tam kısmını verir int gibi
y **=5 #veya y=y**5 y üzeri 5 gibi çalışır



values = 1,2,3 #tuple liste oldu burası
print(values)
print(type(values))

#tuple listemizdeki değerlerimizi x,y ve z değerlerimize aktarmak istiyoruz

x,y,z=values

print(x,y,z)

values=1,2,3,4,5
x,y,*z=values #önüne yıldız attık *dizi görevi aldı
print(x,y,z)
print(x,y,z[1])

print(type(z))






