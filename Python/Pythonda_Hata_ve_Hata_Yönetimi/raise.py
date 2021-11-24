#x=10

#if x>5:
#    raise Exception("x 5 den büyük olamaz") #x 5 den büyük olursa hata altına bunu yazar

def check_password(psw):
    import re
    if len(psw)<8:
        raise Exception("Parola en az 7 karakter olmalıdır.")

    elif not re.search("[a-z]", psw): # a dan z ye küçük harf
        raise Exception("Parola küçük harf içermelidir.")

    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir.")

    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir.")
    
    elif not re.search("[_@$]", psw): 
        raise Exception("Parola alpha numeric karakter içermelidir.")

    elif re.search("[\s]", psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Geçerli parola")


password="12345678aB_"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli parola buradan")
finally:
    print("Bu uyarı da verse hatasız da çalışsa hep çalışacak")



print("\n")
class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name=name

p=Person("Güneyyyyyyyyyy",2001)











# CTRL+K+U ve CTRL+K+C












