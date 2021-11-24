name="Güney"
surname="Kılıçel"
age=20
#print("My name is {} {}".format(name,surname))

"""
print("My name is {0} {1}".format(name,surname)) My name is Güney Kılıçel yazar C deki %s gibi
print("My name is {1} {0}".format(name,surname)) My name is Kılıçel Güney yazar %s burada {}
print("My name is {s} {n}".format(n=name,s=surname)) My name is Kılıçel Güney yazar
"""
print("My name is {} {} and I'm {} veya değişken ile {} years old.".format(name, surname, '20',age))

result=200/700
#print("the result is: {}".format(result))
print("the result is: {r:1.4}".format(r=result)) #virgülden sonraki 4 basamağı alıyor baştaki bir ise önden boşluk
print("the result is: {r:7.2}".format(r=result))

print(f"My name is {name} {surname} and I'm {age} years old.")#bu da f string yöntemi ilk tırnaktan önce bir f yazıp {} bunların içine değişkenlerimizi yazıyoruz.


