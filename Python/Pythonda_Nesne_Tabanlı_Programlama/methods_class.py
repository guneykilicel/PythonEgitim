#class.py den farkı mothodlar eklendi person içine bak

#class

class Person:
    #bu fonksiyonlarda hani altını boş bırakınca hata veriyordu if falan içinde böyleydi ya 
    #heh şimdi artık bu "pass" sayesinde altını boş bırabileceğiz pass yazıp

    # class attiributes
    address="no information"



    # object attiributes
    #constructor(yapıcı metod)
    def __init__(self,name,year):
        self.name = name
        self.year = year


    
    # instance methods
    def intro(self):
        print("Hello There. I am "+self.name)

    # instance methods
    def calculateAge(self):
        return 2021-self.year



#object(instance)
p1 = Person("Güney",2001)
p2 = Person(name="İrem",year=2001)

p1.intro()
p2.intro()

print(f"{p1.name} yaşı: {p1.calculateAge()}")
print(f"{p2.name} yaşı: {p2.calculateAge()}")


class Circle:
    #class object attribute
    pi=3.14

    def __init__(self,yaricap=1): #r=1 dedik kullanıcı yarıçap vermezse hata yerine r yi 1 alıcak
        self.yaricap=yaricap

    #methods
    def cevre_hesapla(self):
        return 2*self.pi + self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() #yarıcağ 1 olarak kullanılacak çünkü değer verilmemiş
c2 = Circle(5)

print(f"c1: alan= {c1.alan_hesapla()} çevre= {c1.cevre_hesapla()}")
print(f"c2: alan= {c2.alan_hesapla()} çevre= {c2.cevre_hesapla()}")

















