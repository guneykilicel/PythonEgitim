#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
#2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.
#4- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun
#4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.


#1

def loop(word,pointer):
    """
    Verilen sayı kadar kelime tekrarlar
    """
    i=0
    while(i<pointer):
        print(word)
        i +=1

"""
myString=input("Kelime gir: ")
ptr=int(input("Kaç kere tekrarlansın: "))


loop(myString,ptr)
"""

#2
def add_to_the_list(add_word,add_list):
    """
    Kullanıcının girdiği kelimeleri diziye çevirmeye yarar
    """
    add_list.append(add_word)

"""
how_many_words=int(input("Kaç kelime girilecek: "))

last_list=[]
a=0
while(a<how_many_words):
    enter_word=input("Kelime gir: ")
    add_to_the_list(enter_word,last_list)
    a +=1

print(last_list)

"""


#3

def prime_number(s1,s2):
    """
    Girilen iki limit arasındaki asal sayıları bulur.
    """
 
"""    
    for i in range(s1,s2):
        ctrl=True
        a=2
        if a>i:
            ctrl=False
        
        while a<i:
            if i%a==0 or i==1:
                ctrl=False
                if i==2:
                    ctrl=True
                break
            a +=1
        if ctrl:
            print(i)


prime_number(0,15)

"""



#4
def tam_bolen(s1):
    for i in range(1,s1):
        if int(s1)%i==0:
            print(i)


tam_bolen(198445)






























