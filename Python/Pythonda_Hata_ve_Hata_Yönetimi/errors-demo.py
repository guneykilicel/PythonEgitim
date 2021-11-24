
liste=["1","2","5a","10b","abc","10","50"]

#1: Liste elemanları içindeki sayısal değerleri bulunuz.

#2: Kullanıcı "q" değerini girmedikçe aldığınız her inputun sayısal 
# olduğundan emin olunuz aksi halde hata mesajı yazın

#3: girilen parola içinde türkçe karakter hatası veriniz.

#4:faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.


#1
for x in liste:
    try:
        value=int(x)
        print(x)
    except ValueError:
        pass


#2
# while True:
#     try:
#         value=input("Sayı giriniz(döngüden çıkmak için 'q' giriniz): ")
#         if(value=="q"):
#             break
#         value=int(value)

#     except ValueError:
#         print("Sayı girdiğinizden emin olun.")




#3

# def check_passwd(passwd):
#     import re
#     if re.search("[ğüşıöç]",passwd):
#         raise Exception("Türkçe karakter girilmemelidir.")

# passwd=input("Şifre gir: ")

# check_passwd(passwd)




#4

def faktoriyel(s):
    s=int(s)
    if s<0:
        raise ValueError("Negatif değer ile faktöriyel hesaplanamaz.")
    
    result=1
    for i in range(1,s+1):
        result *=i

    return result

#print(faktoriyel(-5))

for i in [5,10,2,-3,"10a",6]:
    try:
        y=faktoriyel(i)
    except ValueError as err:
        print(err)
        continue
    print(y)

























