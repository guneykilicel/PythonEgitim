# key-value

# 41=> kocaeli 34=>istanbul

sehirler=["Kocaeli","İstanbul"]
plakalar=[41,34]

print(plakalar[sehirler.index("İstanbul")]) # bu yöntemde sıraların uyuyor olması gerekli

# BİZİM İSTEDİĞİMİZ
# print(plakalar["Kocaeli"]) => 41
# print(plakalar["İStanbul"]) => 34

#plakalar={"key" : "value"} bu şekilde yapacağız dikkat et SÜSLÜ PARANTEZ

plakalar={"Kocaeli" : 41 , "İstanbul" : 34}

print(plakalar["Kocaeli"])

plakalar["Ankara"]=6 # bu şekilde atama yapabiliriz
plakalar["Kocaeli"]="new value" #bu şekilde de değiştirebiliriz istediğini yaz "" içine

users={ #bak burası 3 boyutlu dizi gibi users altında güney kılıçel onun altında age email falan
    "güneykılıçel" : {
        "age" : 20,
        "roles" : ["admin","user"],
        "email" : "guney@gmail.com",
        "address" : "Bursa",
        "phone" : "01234567899"

    },
    "iremocak" : {
        "age" : 20,
        "roles" : ["user"],
        "email" : "irem@gmail.com",
        "address" : "Bursa",
        "phone" : "99876543210"
    }
}

print(users["güneykılıçel"])
print(users["güneykılıçel"]["email"]) 
print(users["güneykılıçel"]["roles"][0])






