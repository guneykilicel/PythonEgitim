website="http://www.sadikturan.com"
course="Python kursu: Baştan sona Python Programlama Rehberiniz (40 saat)"

#"course" karakter dizisinde kaç karakter bulunmaktadır?
print(len(course))

#"website" içinden www karakterlerini alın.
print(website[7:10])

#"website" içerisinden com karakterlerini alın.
print(website[22:])

#"course" içinden ilk 15 ve son 15 karakterlerini alın.
print(course[:15]+" "+course[-15:])

#"course" ifadesindeki karakterleri tersten yazdır.
print(course[::-1]) # "::" ile tüm karakterleri aldık -1 ile ters yazdırdık



name, surname, age, job="Güney","Kılıçel","20","Mühendis"

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")
print("Benim adım {} {}, Yaşım {} ve mesleğim {}".format(name,surname,age,job))



#"Hello world" ifadesindeki w harfini W harfi ile değiştirelim.
hi="Hello world"
print(hi[:6]+"W"+hi[7:] )


#abc ifadesini yan yana 3 defa yazdırın.
harf="abc"*3 #string ifadeyi çarpınca ondan ardı ardına ekliyoruz çarptığımız kadar
print(harf)