
def us_al(number):
    def inner(power):
        return number**power
    return inner

two=us_al(2)
print(two(3)) #two yu us_al ile eşitleyip içerisine ilk 2 attık ama us_al fonksiyon döndüren bir fonksiyon olduğu için
#two nun içerisine 3 girdik ve 2üzeri 3 işlemi yapıldı.



def yetki_sorgula(page):
    def inner(role):
        if role=="Admin":
            return("Entered the {0} by {1}".format(page,role))
        else:
            return("Permisson denied the {0} by {1}".format(page,role))
    return inner

html=yetki_sorgula("html.html")
print(html("Admin"))



def islem(isaret):
    def toplam(*args): #* yaptık sınırsız değer alır
        toplam=0
        for i in args:
            toplam +=i
        return toplam

    def caprim(*args):
        carp=1
        for i in args:
            carp *=i
        return carp

    if isaret =="Toplama":
        return toplam
    elif isaret =="Carpma":
        return caprim

toplayalim=islem("Toplama")
print(toplayalim(1,2,3,4,5,6,7,8,9,10,89,99)) #def toplam(*args): !!!!! *args

carpalim=islem("Carpma")
print(carpalim(1,2,3,4,5,6,7,8,9,10,89,99))






































