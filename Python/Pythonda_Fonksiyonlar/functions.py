def sayHello():
    print("Hello")

sayHello()
sayHello()



print("\n")
def sayHello1(name):
    print("Hello "+name)

sayHello1("Güney")
sayHello1("İrem")



print("\n")
def sayHelloVarsayilanli(name="user"):
    print("Hello "+name)

sayHelloVarsayilanli("Güney")
sayHelloVarsayilanli() #varsayılan olarak "user" verdik o yüzden "Hello user" yazar.




print("\n")
def sayHelloReturnlu(name="user"):
    return "Hello "+name #return C deki gibi burada string de yollayabiliyoruz.

msg=sayHelloReturnlu("İrem") #C deki mantık üsttekiler void fonk du bu int gibi düşün atama gerek
print(msg)



print("\n")
def total(num1,num2):
    return num1+num2

result=total(10,20)
print(result)




print("\n")
def yasHesapla(dogumyili):
    return 2021-dogumyili
guney=yasHesapla(2001)
print(guney)

#Şimdi fonksiyon içinde fonksiyon kullanalım.

def emeklilik(dogumyili,name):
    """ Bu şekilde açıklama yazmak gerek fonksiyonu kullanmak isteyenler için help() ile kullanılır.
    DOCSTRING: Doğu yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT: Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi
    """
    yas=yasHesapla(dogumyili) #fonksiyon içerisinde fonksiyon kullandık.
    emekli=65-yas

    if emekli>0:
        print(f"{name}'in emekliliğine {emekli} yıl var.")
    else:
        print("Zaten emeklisiniz.")

emeklilik(2001,"İrem")

print(help(emeklilik)) #fonksiyon açıklamasını alırız. yazma şekli de yukarıda var.

#ÖRNEK:
list=[1,2,3]
print(help(list.append))








































