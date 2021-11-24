#oop.py dosyasına bak

#class

class Person:
    pass #bu fonksiyonlarda hani altını boş bırakınca hata veriyordu if falan içinde böyleydi ya 
    #heh şimdi artık bu "pass" sayesinde altını boş bırabileceğiz pass yazıp

    # class attiributes
    address="no information"



    # object attiributes
    #constructor(yapıcı metod)
    def __init__(self,name,year):
        self.name = name
        self.year = year


    
    # methods


#object(instance)
p1 = Person("Güney",2001)
p2 = Person(name="İrem",year=2001)

#updating
p1.name="Kuzey"
p1.address="Bursa"
p2.address="Bursa"

#accessing object attributes
print(f"name: {p1.name} year: {p1.year} address: {p2.address}")
print(f"name: {p2.name} year: {p2.year} address: {p2.address}")
print(type(p1))
















