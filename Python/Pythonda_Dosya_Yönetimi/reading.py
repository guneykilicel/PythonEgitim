# try:
#     file = open("newfile.txt","r",encoding="utf-8")
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     file.close()
#     print("Dosya kapandı.")


file= open("newfile.txt","r",encoding="utf-8")
#for döngüsü ile okuma

# for i in file:
#     print(i,end="") #boş satırları silmek için ,end=""


#read fonksiyonu ile okuma
content1=file.read()
print("İçerik 1")
print(content1)


file= open("newfile.txt","r",encoding="utf-8") #DOSYAYI TEKRAR OKUMAK İSTİYORSAK TEKRAR AÇACAĞIZ
content2=file.read() #Bir kere okuduk C deki gibi ikinci kez okumaz
print("İçerik 2")
print(content2)


file= open("newfile.txt","r",encoding="utf-8")
print("\n")
content=file.read(5) #İlk 5 karakteri alır
content=file.read(3) #Yukarıda 5  byte lık karakter aldık şimdi ondan sonra 3 karakter alırız.
content=file.read(3)
print(content)


#READLINE() fonksiyonu******** satır satır okuma
file= open("newfile.txt","r",encoding="utf-8")
print("\n")
print(file.readline(),end="")
print(file.readline(),end="")





#READLINES() fonksiyonu******** tüm satırları okur her satırı bir DİZİNİN elemanı haline getirir
file= open("newfile.txt","r",encoding="utf-8")
print("\n")
liste=file.readlines()
print(liste)

print(liste[0]) #Dizi ye dönüştürdüğü için eleman eleman satır getirttirebiliyoruz.
print(liste[2])









file.close()








