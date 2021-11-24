numbers=[1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]
val=min(numbers) #en küçük sayı
val=max(numbers) # en büyük sayı
val=max(letters) #alfabe sırasına göre yazar burada en son gelen y dir en büyük y olur
val=min(letters) # a verir çünkü ilk harf yani en küçük3
val=numbers[3:6]
val=numbers[:3]
val=numbers[4:]
numbers[4]=40
print(val)
#numbers.append("49") #49 u listeinin en sonuna string olarak ekledik
numbers.append(49) #49 u listeinn en sonuna sayı olarak ekledik
numbers.insert(3,78) #3. indexten hemen önce 78 sayısını ekler insert istediğimiz yere koymamızı sağlar
numbers.insert(-1,52) #en sondakinin önüne ekler

numbers.pop() #listeden eleman siler içerisie bir şey yazmasak en sondaki elemanı siler
numbers.pop(0) #ilk elemanı siler
numbers.remove(9) #sıra yerine direkt elemanı yazıyoruz bunda

numbers.sort() #listeyi küçükten büyüğe sıralar
letters.sort() #alfabetik olarak sıralanır
numbers.reverse()#bu da ters çevirme komutu ilk sort ile sırala sonra ters çevir
letters.reverse() #yine ters çevirir ilk önce sort amak gerek

print(numbers)
print(letters)

print(len(numbers)) #kaç elemanlı
print(len(letters)) #kaç elemanlı
print(numbers.count(10))#10 dan kaç tane var
print(letters.count("a")) #"a" dan kaç tane var

numbers.clear() #tüm elemanları siler

print(numbers)

#lists methods in python https://www.w3schools.com/python/python_ref_list.asp


