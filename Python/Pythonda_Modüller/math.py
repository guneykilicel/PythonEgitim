import math
#TAKMA AD VERMEK İÇİN: "import math as islem" kodunu yazarak math ı tanımlarken islem takma adını koyuyoruz.
# result= islem.sqrt(144) yaparsak islem math gibi çalışır

#DİREKT SADECE FONKSİYON İSMİ KULLANIP İŞLEM YAPMAK İÇİN: mesela math.sqrt(4) değil de sqrt(4)
#gibi yapabilmek için GEREKEN KOD: "from math import *"
# result= math.sqrt(144) yerine result= sqrt(144) kullanabiliriz

"""
value=dir(math)
print(value) #Bu şekilde bütün kullanımları ekrana yazdırabiliriz
value=help(math.factorial) #bu şekilde de açıklamalarına ulaşabiliriz.
print(value)
"""
result=math.sqrt(49)
result=math.factorial(5)
result= math.floor(5.9) #Aşağı yuvarlar yani "5"
result = math.ceil(5.9) #Yukarı yuvarlar yani "6"
print(result)














