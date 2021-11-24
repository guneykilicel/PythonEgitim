#DOSYA ADI MODÜL İLE AYNI OLMAMALI!!!! aksi halde hata verir

import random
"""
result= dir(random)
print(result)
result= help(random)
print(result)
"""
result = random.random() # 0.0 - 1.0 arasında sayı üretir
result = random.random()*100 #0.0 - 100.0 arasında
result = random.uniform(10,100) #10.0 ile 100.0 arasında
result = int(random.uniform(10,100)) # int ile ondalıklı kısmı attık
result = random.randint(1,100) #üsttekinin hazır hali :)

names=["Güney","Kılıçel","İrem","Ocak"]
result=names[random.randint(0,len(names)-1)] #Sınırlar dahil olduğu için -1 yaptık 
#rastgele diziden kelime çekiyor
result = random.choice(names) #üsttekinin hazır hali var :)

greeting="Hello There"
result=random.choice(greeting) #greeting içerisinden rastgele harf çeker

liste=list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(liste) #[9, 7, 6, 3, 0, 2, 4, 8, 1, 5], [1, 3, 5, 7, 2, 0, 8, 9, 6, 4] rastgele dağıtıyor


liste=range(100)
result=random.sample(liste,3) #[29, 46, 81], [55, 17, 70] rastgele 3 eleman
result=random.sample(names,2) #aynı şeyi names dizimiz içinde yapabiliriz

print(result)



































