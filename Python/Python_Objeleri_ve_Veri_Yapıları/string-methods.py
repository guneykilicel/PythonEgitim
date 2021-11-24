message="Hello There. My name is Güney Kılıçel"

#message=message.upper()#message değişkeni içerisindeki bütük karakteri "BÜYÜK HARF" yapar
#message=message.lower()#bütün harfleri "küçük harf" yapar
#message=message.title()#bütün kelimelerin "BAŞ HARFLERİNİ BÜYÜK HARF" yapar
#message=message.capitalize()#sadece "İLK HARF BÜYÜK" olur

#message=message.strip()#Başlangıçtaki boşluk karakteri silinir. Parola kontrollerinde falan gerekli

""""
message=message.split()# kelime dizisi gibi her kelimeyi tek tek yazıyor ['Hello', 'There.', 'My', 'name', 'is', 'Güney', 'Kılıçel']
print(message[3])#split diziye dönüştürdüğü için elemanları kelime kelime çekebiliyoruz. Normalde 3. karakter gelmeliydi
"""
"""
message=message.split(".") #şimdi split içine "." koyduk hani split normalde her boşlukta bir kelime kabul edip dizi yapıyordu ya biz içine ne koyarsak ona göre çalışır.
#Şimdi içine nokta koyduk ve noktaya göre dizileme işlemi yapacak ['Hello There', ' My name is Güney Kılıçel']
"""
"""
message=message.split()
message=" ".join(message) #biz split ile ayırdık ya diziye şimdi diziyi birleştirme komutu olarak join kullanıyoruz.
#join yaparken önündeki " " arasına ne koyarsak onu koyup birleştirir mesela *,--,/ gibi veya hiçbir şey koymazsak bütün kelimeleri bitişik yazar
"""
"""
index=message.find("Güney") #bununla cümle içerisinde kelime arıyoruz eğer aradığımız kelime varsa ilk harfinin sayı olarak sırasını veriyor mesela G 24. sıradaymış
#-1 verirse kelime cümle içerisinde yok
print(index)
"""
"""
#isFound=message.startswith("H") #bu metod True ve False dönderir İLK HARFE BAKAR mesela ben şart olarak "H" vermişim ve cümlem Hello ile başladığı için True döndürecek
isFound=message.endswith("l") #startswith ilk harfe bakar bu da onun son harfe bakanı
print(isFound)
"""
"""
message=message.replace("Güney","Kuzey")#replace metodu işte güneyi kuzey ile değiştirdi
message=message.replace(" ","*") #Boşlukları * ile değiştirdim
"""
"""
#message=message.center(100) #100lük bi alan açıp tam ortasına koydu bizi
message=message.center(100,"*") #sağdaki ve soldaki boşluklara * koydurduk
"""



daha fazla string metodları için https://www.w3schools.com/python/python_ref_string.asp









print(message)