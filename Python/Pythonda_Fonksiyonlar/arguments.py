def change(number):
    number=10

n=20
change(n)
print(n)



def change2(list1):
    list1[0]=50

liste=[1,2,3,4,5] #dizi mantığı pointer olur ve değiştirebilir
change2(liste)
print(liste)



def change3(list2):
    list2[0]="Adana"

liste1=["Ankara","İstanbul"]
n=liste1
change3(n)
print(n)
print(liste1)


def change3(list2):
    list2[0]="Adana"

liste1=["Ankara","İstanbul"]
n=liste1[:] #bu şekilde adresler farklı olur biri değişirse diğeri değişmez. slicing yapmış oluruz
change3(n)
print(n)
print(liste1)

































