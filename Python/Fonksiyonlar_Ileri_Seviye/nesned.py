
def fonksiyon(number):
    if not isinstance(number,int):
        raise TypeError("Sayı girdiğinizden amin olun.")
    if not number >=0:
        raise ValueError("Sıfırdan büyük bir sayı girin.")

    def fonksiyon_inner(number):
        if number <=1:
            return 1
        return number* fonksiyon_inner(number-1)
    
    return fonksiyon_inner(number)

try:
    print(fonksiyon("a"))
except Exception as ex:
    print(ex)












































