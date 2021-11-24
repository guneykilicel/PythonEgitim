"""
Şimdi biz bir "liste" tanımladık ve "for i in liste" liste dedik for döngüsü listedeki 
bütün elemanları alıyor ve ekrana verebiliyor. Bu "list" "class" ı için hazdır oluşturulmuş 
bir özellik "iterators" özelliği nerede kullanırız dersen "KENDİ CLASS" ımızda bir şey 
tanımladık diyelim ve liste gibi olucak bu ama for ile itemlerine ulaşamıyoruz ulaşabilmek 
için aynı "list classında" ki gibi bizimde iterators özelliğini kodlamamız gerek.
"""

# liste=[1,2,3,4,5]

# # for i in liste: #FOR DÖNGÜSÜ NASIL TÜM ELEMANLARA ULAŞABİLİYOR
# #     print(i)

# iterator=iter(liste) #listemiz "list classından" olduğu için iter(liste) ile iterator kullanabildik 
# print(next(iterator)) #next(iterator) ile bir sonraki elemana geçiyoruz
# print(next(iterator)) #"for döngüsü" bunu otomatik yapıyor
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


#"list" CLASS DA "for" DÖNGÜSÜ "iterator" İÇİN NASIL KODLANMIŞ:
liste=[1,2,3,4,5]
iterator=iter(liste)

while True:
    try:
        element=next(iterator)
        print(element)
    except StopIteration: #Okunulacak değer kalmadığında dönen hata
        break


print("\n")
#KENDİMİZ BİR "CLASS" OLUŞTURDUĞUMUZDA NASIL "iterator" UYGULAYACAĞIZ:
class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x=self.start
            self.start +=1
            return x
        else:
            raise StopIteration

list=MyNumbers(10,20)

for i in list: #"MyNumber" classımız aynı "list" classındaki gibi "iterator" özelliği kazandı
    print(i)   # bu sayede "döngü" içerisinde yazdırılabiliyor.













