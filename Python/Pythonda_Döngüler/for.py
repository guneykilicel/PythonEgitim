numbers=[1,2,3,4,5]

for i in numbers:
    print(i)

names=["güney","irem","kuzey"]
for name in names:
    print(name)

name="Güney Kılıçel"
for n in name: #string ifadenin her karakterini tek tek alır char gibi düşün
    print(n)

tuple = (1,2,3,4,5)
for t in tuple:
    print(t)


tuple = [(1,2),(3,4),(5,6),(7,8)]
for t in tuple:
    print(t)

tuple = [(1,2),(3,4),(5,6),(7,8)]
for a,b in tuple:
    print(a)

tuple = [(1,2),(3,4),(5,6),(7,8)]
for a,b in tuple:
    print(a,b)


dictionary={"k1":1, "k2":2, "k3":3}
for item in dictionary:
    print(item) # keyleri verir listedeki gibi hepsini vermez k1,k2 verir

dictionary={"k1":1, "k2":2, "k3":3}
for key,value in dictionary.items(): # .items() i eklersek value lara ulaşabiliriz.
    print(key,value)


