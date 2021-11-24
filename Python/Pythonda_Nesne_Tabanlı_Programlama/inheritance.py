#Yapmak istediğimiz şey bir class yaptık özelliklerini methodlarını yazdık 
# başka class açtığımızda bu class ın da bu metodlardan faydalanmasını istiyoruz 
# bunun için kullanım şekli

#Mesela class Animal() --> class Dog(Animal), class Cat(Animal)
 

class Person():
    def __init__(self, fname, lname):
        self.first_name=fname
        self.last_name=lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person.")


class Student(Person):
    def __init__(self, fname, lname,number):#PERSON DAN MİRAS ALMASI İÇİN ONUN GİBİ 
        #DEĞİŞKEN ALMALI KENDİSİ İÇİN DE EKSTRA ALABİLİR. BURADA NUMBER ALDI MESELA KENDİSİ İÇİN

        Person.__init__(self,fname, lname) #İçeride person u çağırmış ta olduk
        self.studentNumber=number
        print("Student Created")


    #override = Aynı isimdeki bir metod temel sınıftaki metyodu ezer
    def who_am_i(self): #Yani who_am_i person da da vardı ama 
        #biz burada da oluşturunca ve student objesini çalıştırınca buradaki çalışacak
        print("I am a student")

    def sayHello(self):
        print("Hello i am a student")


class Teacher(Person):
    def __init__(self, fname, lname,branch): 
        super().__init__(fname, lname) #ŞİMDİ BİZ BUNUN PERSON DAN MİRAS ALMASI İÇİN
        # Person.__init__(self,fname, lname) YAZIYORDUK YA BUNDA SELF DE YAZMAMIZ GEREKLİ
        # AMA BU ŞEKİLDE KISA YOLDAN OLUYOR HEM PROGRAM KENDİSİ TAMAMLIYOR BURAYI :)
        self.branch=branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")


p1= Person("Güney","Kılıçel")
s1= Student("İrem","Ocak",1234) #class ı verirken Person dedik onun gibi değerler almalı
t1= Teacher("Kuzey","Kılıçel","Math")

print(f"{p1.first_name} {p1.last_name}")
print(s1.first_name+" "+s1.last_name+" "+str(s1.studentNumber))


p1.who_am_i()
s1.who_am_i() #Personda who_am_i var ama student erson dan miras aldığı için kullanabiliyor
s1.sayHello()
t1.who_am_i()

























