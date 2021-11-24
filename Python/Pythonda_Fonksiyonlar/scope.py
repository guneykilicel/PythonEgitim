#Şimdi konumuz global ve local değişkenler:
# Biz bir değişkeni fonksiyon içinde değiştirdik ve dışarıda da farklı bir değeri var diyelim.
# Eğer fonksiyon dışında çağırırsak dışarıdaki x değeri karşımıza gelir
# Ama fonksiyon içinde çağırırsak fonksiyon içerisinde değiştirdiğimiz değer gelir.
# Hatta biraz daha ileri gidelim fonksiyon içerisindeki fonksiyonda çağırırsak:
    # en son tanımlanmış değeri bize verir yani değiştirilmişi verir.
""" AMA BİZ FONKSİYON İÇERİSİNDEN DIŞARIDAKİ DEĞİŞKENİ DEĞİŞTİRMEK İSTERSEK C DEKİ POİNTER
    MANTIĞI GİBİ ORADA POİNTER A ATAYIP POİNTER İLE İŞLEM YAPIYORDUK YA BURADA DAHA KOLAY
    SADECE "global x(değişkenimiz)" YAZIYORUZ VE BİTTİ ARTIK POİNTER İLE İŞLEM YAPIYORMUŞSUN
    GİBİ DÜŞÜN."""


x=50
def test(x):
    print(f"x: {x}")

    x=100
    print(f"changed x to {x}")

test(x)
print(f"Did x change: {x} (no :))")


print("***************ŞİMDİ GLOBAL**************")
x=50
def test_global():
    global x
    print(f"x: {x}")
    x=100
    print(f"changed x to {x}")

test_global()
print(f"Did x change: {x} (yes ;))")



name="Güney"
def changeName(new_name):
    global name
    name=new_name

newname="İrem"
changeName(newname)
print(name)






















