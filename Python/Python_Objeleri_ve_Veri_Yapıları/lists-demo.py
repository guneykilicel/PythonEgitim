# "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
list=["Bmw", "Mercedes", "Opel", "Mazda"]

#liste kaç elemanlıdır
print(len(list))

#listenin ilk ve son elemanı nedir
print(f"İlk eleman: {list[0]}")
print(f"Son eleman: {list[len(list)-1]}")


#mazda değerini Toyota ile değiştirin
listex=list
ptr=listex.index("Mazda")
listex[ptr]="Toyota"
print(listex)


#mercedes listenin bir elemanı mıdır
listex1=list
listex1=listex1.index("Mercedes") #bu index kullanımı sıkıntılı eğer yoksa direkt error veriyor
print(listex1)

#listenin -2 indexindeki değer nedir
print(list[-2]) #opel -1 -2 diye gidiyor


#listenin ilk 3 elemanını alın
listex2=[list[0],list[1],list[2]]
print(listex2)

#listenin son iki elemanı yerine Toyota ve Renault değerlerini ekleyin
listex3=list
listex3[len(listex3)-1]="Renault"
listex3[len(listex3)-2]="Toyota"
#veya listex3=listex3[-2:]=["Toyota","Renault"]
print(listex3)


#listenin üzerine Audi ve Nissan ekleyin
listex3=listex3 + ["Audi", "Nissan"]
print(listex3)


# listenin son elemanını silin
del listex3[-1]
print(listex3)

#liste elemanlarını tersten yazdırınız
print(listex[::-1]) #düz gitmek için 1 ters gitmek için1


#aşağıdaki verileri bir liste içersinde saklayınız
#studentA: Güney Kılıçel 2001, (70,60,70)
#studentA: İrem Ocak 2001, (70,60,70)
#studentA: Güney Güney 2000, (70,60,70)

studentA= ["Güney", "Kılıçel",2001,[100,99,100]]
studentB= ["İrem", "Ocak",2001,[100,99,100]]
studentC= ["Güney", "Güney",2000,[99,99,100]]

#liste elemanlarını ekrana yazdırınız

print(studentA)
print(studentB)
print(studentC)
print(studentB[1])
print(studentB[3][1])

print(f"{studentA[0]} {studentA[1]} {2021-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}")

