fruits={"orange","apple","banana"}

#print(fruits[0]) SÜSLÜ PArantezle yaptığımız bir liste dictionary olduğu için İNDEXLENEMEZ


#bunlar sıralanamaz da A dan Z ye gibi yapılamaz
#elemanlarına döngü kullanarak ulaşırız
for x in fruits:
    print(x)

# ELEMAN EKLEMEK için
fruits.add("cherry")
print(fruits)

fruits.update(["mango","grape"]) #listede olan bir elema eklemeye kalkarsak eklenmez eleman tek kalır
print(fruits)

myList=[1,2,3,5,4,4,3,2,1]
print(myList)
print(set(myList)) #bu set süslü parantezli listeler gibi bir elemanı bir defa göstermemizi sağlar



#ELEMAN SİLMEK İÇİN
fruits.remove("mango")
print(fruits)

fruits.discard("apple")
print(fruits)

fruits.pop()#normalde pop içini noş bırakırsak listenin son elemanını silerdi
#ama burada farkettiysen her şey karışık geliyor bu yüzden neyi sileceği belli olmaz

fruits.clear()
print(fruits)





