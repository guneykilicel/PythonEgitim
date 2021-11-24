x=6
hak=5
devam="e"
result=5<=x<10

#and && işareti gibi düşün
result=x>5 and x<10 #True, True => True

result=(hak>0) and (devam =="e")

#or || gibi düşün
result=(x>0) or (x%2 == 0)

#not cevabın tam tersi
result= not(x%2 == 0) #doğru bir koşul ama False verecek tek sayıyı kontrol edersin :)


#x, 5-10 arasında olan bir çift sayı mı?
result=((x>5) and (x<10) and (x%2 == 0))


print(result)












