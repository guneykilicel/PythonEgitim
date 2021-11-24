names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]

# 1- "Cenk" ismini listenin SONUNA ekleyiniz.
# 2- "Sena" ismini listenin BAŞINA ekleyiniz
# 3- "Deniz" ismini listeden SİLİNİZ
# 4- "Deniz" İsminin İndeksi nedir
# 5- "Ali" listenin bir elemanı mıdır?
# 6- Liste elemanlarını TERS ÇEVİRİN
# 7- Liste elemanlarını ALFABETİK olarak SIRALAYINIZ
# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
# 9- str="Chevrolet,Dacia" karakter dizisini listeye çeviriniz
# 10-years dizisinin en büyük ve en küçük elemanı nedir?
# 11- years dizisinde kaç tane 1998 değeri vardır?
# 12- years dizisinin tüm elemanlarını siliniz
# 13- kullanıcılardan aldığınız 3 tane marka bilgisini bir listede saklayınız


#1
names.append("Cengiz")

#2
names.insert(0,"Sena")

#3
#names.remove("Deniz")

#4
print(names.index("Yağmur"))

#5
print("Ali" in names) #veya
result= "Ali" in names #veya
result= names.index("Ali")#veya
result= names.count("Ali")
print(result)

#6
names.reverse()

#7
names.sort()

#8
years.sort()
years.reverse()

#9
str="Chevrolet,Dacia"
result2=str.split(",")
print(result2)

#10
print(min(years))
print(max(years))

#11
print(years.count(1998))

#12
years.clear()

#13
markalar=[]

marka=input("Marka: ")
markalar.append(marka)

marka=input("Marka: ")
markalar.append(marka)

marka=input("Marka: ")
markalar.append(marka)

print(markalar)


print(names)
print(years)





























