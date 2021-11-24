def my_decorators(func):
    def wrapper(name):
        print("Fonksiyondan önceki işlemler")
        func(name)
        print("Fonksiyondan sonraki işlemler")
    return wrapper

# def sayHello():
#     print("Hello")

# sayHello=my_decorators(sayHello) # ekleme işleme bu şekilde de olabilir ama kısa yolu var
# sayHello()


@my_decorators #KISA YOLDAN DECORATORS
def sayHello(name):
    print("Hello", name)

sayHello("Güney")

print("\n")

import time
import math

def calculate_time(func): #decarator
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)#burada 1 saniye bekleyecek
        func(*args,**kwargs,)
        finish=time.time()
        print("fonksiyon "+func.__name__+" "+str(finish-start)+" saniye sürdü")
    return inner

@calculate_time
def us_alma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(a):
    print(math.factorial(a))


us_alma(5,4)
faktoriyel(5)
























































