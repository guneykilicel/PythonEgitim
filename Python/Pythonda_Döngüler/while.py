# 1 den 100 e kadar

x=0

while x<=100:
    if x%2 == 1:
        print(f"Sayı tek: {x}")
    else:
        print(f"Sayı çift: {x}")
    x +=1


name ='' #False
while not name.strip(): #kullanıcı ismini girmediği sürece sürekli sorucak ama boşluk girerse 
#adını " "(boşluk) sanıyor o yüzden strip kullandık :)
    name=input("İsminizi giriniz: ")
print(f"Merhaba, {name}")
































