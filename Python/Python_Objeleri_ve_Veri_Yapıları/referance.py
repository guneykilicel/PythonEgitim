#value types => string, number
x = 5
y = 25

x = y

y = 10

print(x,y)

#referance types => liste, class (ilerde göreceğiz)
#ikisi eşleştirilip biri sonradan değiştirilirse diğeri de değişik pointer gibi
a = ["apple","banana"]
b = ["apple","banana"]

a=b

b[0]="grape"

print(a) #b de değiştim a da değişti çünkü aynı adresi taşıyorlar diziler zaten pointerdır ;)







