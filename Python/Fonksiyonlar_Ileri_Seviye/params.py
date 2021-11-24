def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,isaret): #Fonksiyon içerisine fonksiyon göndereceğiz
    if isaret=="Toplama":
        return f1(2,3) #yolladığımız printin içerisinde f1 toplama fonksiyonu ile eşleşti

    elif isaret =="Cikarma":
        return f2(8,3)

    elif isaret =="Carpma":
        return f3(6,2)

    elif isaret =="Bolme":
        return f4(9,3)
    
    else:
        print("Hatalı giriş!")

print(islem(toplama,cikarma,carpma,bolme,"Toplama"))

print(islem(toplama,cikarma,carpma,bolme,"Cikarma"))

print(islem(toplama,cikarma,carpma,bolme,"Carpma"))

print(islem(toplama,cikarma,carpma,bolme,"Bolme"))












































