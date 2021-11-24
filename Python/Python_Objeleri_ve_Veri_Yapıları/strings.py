name="Guney"
surname="Kilicel"
age=36

#print("My name is "+name+" "+surname+" "+"and \nI am "+str(age)+" "+"years old")
greeting="My name is "+name+" "+surname+" "+"and \nI am "+str(age)+" "+"years old"

#print(len(greeting))
length=len(greeting)

print(greeting[length-1])
#print(greeting[-1])

print(greeting[3:7]) # 3:5 yaparsak 3 den başla 7 ye kadar git deriz
print(greeting[3:]) #3: yaptım 3. karakterden başlayıp sonuna kadar gidicek
print(greeting[:15]) # :15 yaptım baştan başlayıp 15. karaktere kadar gidecek

print(greeting[2:40:2]) #2:40:2 yaptım sondaki ':2' 2 karakter almadan almadan git 2 almadı 2 aldı 2 almadı... bu şekilde
