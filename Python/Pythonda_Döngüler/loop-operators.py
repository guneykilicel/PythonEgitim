#Bizim bir listemiz yoksa range() i direkt kullanabiliriz
for item in range(10):
    print(item)

print("\n")
for item in range(10,100,20): #10 dan 100e kadar 20 20 arttır
    print(item)

print("\n")
print(list(range(5,100,10)))


print("\n")
index=0
greeting="Hello"
for letter in greeting:
    print(f"index:{index} letter:{letter} / Farklı Gösterim: {greeting[index]}")
    index +=1

#Şimdi bunu "enumerate" ile yapalım
print("\n")
greeting="Hello"
for index,letter in enumerate(greeting):
    print(f"index:{index} letter:{letter}")
    index +=1


for item in enumerate(greeting):
    print(item)


# zip metodu eşleştirmeye yarar
print("\n")
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]

print(list(zip(list1,list2)))
print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3): #şimdi biz for da bu listeleri eşletirip işlem yaptık
    print(item) #birleştirilmiş halde verir


for a,b,c in zip(list1,list2,list3):
    print(a) #list1 in elemanlarını çekeriz

















