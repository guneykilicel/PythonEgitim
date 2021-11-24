# 'os' modülü genellikle işletim sistemi için kullanılır.

import os
import datetime #tarih bilgilerini sayıdan çevirebilmek için kullanacağız

result = dir(os) # os ile kullanlabileceğimiz .birşeyler
result = os.name # İşletim sistemini ekrana yazar. Ekran çıktısı: nt   (nt windows demek)
result = os.getcwd() # nerede olduğumuzu gösterir: C:\Users\90546\Documents\Python



# ***********DİZİN DEĞİŞTİRME**************
# os.chdir("C:\\") #konum değiştirmeye yarar ama bizi değiştirmez 
#mesela şimdi bir dizin oluşturucam ve bu değiştirdiğim yerde oluşucak
# os.chdir("..") # bizi bir üst klasöre atar
# os.chdir("../..") # bizi iki klasör üste atar
# result = os.getcwd()



# ***********KLASÖR OLUŞTURMA**************
# os.mkdir("newdirectory") #linux gibi dizin oluşturur
# os.makedirs("newdirectory/yeniklasor") # iç içe klasör oluşturur
# os.rename("newdirectory","yeniklasor") # 'newdirectory' adlı klasörün adını 'yeniklasor' olarak değiştirdi
# os.rmdir("newdirectory") #klasör silmek için kullanılır (alt klasör yoksa kullanılır)
# os.removedirs("yeniklasor/yeniklasor") #hepsini siler

# ***********LİSTELEME*********************
# result = os.listdir() # dosyalarımı listeler(dizinler de dahil)
# result = os.listdir("C:\\") # 'C' deki dosyaları ekrana verir yani belirli konum ayarlanabilir

#Sadece ".py" uzantılı dosyaları listelemek için:
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

result = os.stat("list-methods.py") # Dosya hakkında bilgi almamızı sağlar:
"""
Bilgi:
os.stat_result(st_mode=33206, st_ino=67272519433889828, st_dev=2761673009, st_nlink=1, 
st_uid=0, st_gid=0, st_size=1482, st_atime=1630160187, st_mtime=1628855203, 
st_ctime=1628853623)

AÇIKLAMA:
st_size=1482 : Dosyanın byte cinsinden büyüklüğünü verir. (1024'e bölüp 'kb' cinsinden hesaplayabilirsin)
st_atime=1630160187 : Dosyaya son erişilme tarihini veriyor ancak bu time bilgisini datetime ile fromtimestamp kullanarak normal tarihe çevireceğiz
st_mtime=1628855203 : Son değiştirilme tarihi yine datetime mevzusu
st_ctime=1628853623 : Oluşturulma zamanı datetime
"""
# ---DATETIME İLE KARMAŞIK TARİH BİLGİSİNİ NORMALE ÇEVİRME---
result = os.stat("list-methods.py")
# result = result.st_size/1024 # 'kb' cinsinden bulduk
# result = datetime.datetime.fromtimestamp(result.st_ctime) # sayılı tarihi normal tarihe çevirdik
# result = datetime.datetime.fromtimestamp(result.st_atime)
# result = datetime.datetime.fromtimestamp(result.st_mtime)




# ***********PROGRAM ÇALIŞTIRMA*************
# os.system("notepad.exe") # notepad i açar


# ***********UZANTI(path) İŞLEMLERİ*********
result = os.path.abspath("_os.py") #Dosyanın konumunu bulur
result = os.path.dirname("C:/Users/90546/Documents/Python/_os.py") #konumu verilen dosyanın dizin ismini bulur
result = os.path.dirname(os.path.abspath("_os.py")) #İkisini beraber kullanıyoruz yani:
# 'os.path.dirname' ile klasörün adını alacağız ve dosyayı bulmak için 'os.path.abspath' kullanıyoruz.

result = os.path.exists("C:/Users/90546/Documents/Python/list-methods.py") #dosya var mı yok mu diye bakar
#Ekran çıktısı: True
#Mesela resim upload edeceğiz veya bir dosya koyacağız üstüne yazılmaması için bu şekilde kontrol etmek gerek

result = os.path.isdir("C:/Users/90546/Documents/Python") #Bu isimde bir klasör var mı?

result = os.path.join("C:\\","deneme","deneme1") # C:\deneme\deneme1 bir path oluşturduk böyle bir şey yok
result = os.path.split("C:\\deneme") # ('C:\\', 'deneme') path i ayırır
result = os.path.splitext("_os.py") # ('_os', '.py') dosya ismi ile uzantıyı ayırır
result = result[0] # _os








print(result)





















