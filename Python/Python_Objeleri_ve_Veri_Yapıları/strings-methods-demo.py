website="http://www.sadikturan.com"
website1="http://www.sadikturan.com"
website2="www.sadikturan.com"
website3="www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- "Hello World" karakter dizisinin baş ve sondaki boşluk karakterini silin.
#sadece soldakini silsin istersek lstrip(), sadece sağdakini silsin istersek rstrip()
#baştaki http:// yı silsin istersek lstrip("/:pth") bir kere yazsak yeterlğ karışık da olur
hi=" Hello World "
hi=hi.strip()
hi_len=len(hi)
print(hi_len)
print(hi)

# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.
site="www.sadikturan.com"
site=site.split(".")
print(site[1])


# 3- course karakter dizisinin tüm karakterlerini küçük harf yapın
course=course.lower()
print(course)


# 4- "website" içerisinde kaç tane a hari vardır (count(a))
website=website.count("a")
print(website)

# 5-"website" www ile başlayıp com ile bitiyor mu?
website2=website2.startswith("www")
print(f"www: {website2}")
search1=website3.endswith("com")
print(f"com: {search1}")

# 6- "website" içinde ".com" ifadesi var mı?
search=website1.find(".com") #.find(".com",0,10) 0 dan 10 a kadar bakar #rfind sağdan başlar
print(f"Aranan kelimenin başladığı karakter: {search}")



# 7- "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha(tüm karakterler harf ise True), isdigit(tüm karakterler rakam ise True))
abcd=course.isalpha()
print(abcd)


# 8- "contents" ifadesini satırda 50 karakter iççine yerleştirip saağ ve soluna * ekleyiniz.
contents="Contents"
contents=contents.center(50,"*") # .center yerine .ljust ve rjust sola sağa yaslama
print(contents)


# 9- course karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştir
course1=course
course1=course1.replace(" ","-")
print(course1)


# 10- "Hello World" karakter dizisinin "World ifadesini "There" olarak değiştirelim
change="Hello World"
change=change.replace("World","There")
print(change)


# 11-"course karakter dizisini" boşluk karakterlerinden ayırın.
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)".split()
print(course)
