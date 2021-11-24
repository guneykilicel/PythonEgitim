name="Güney Kılıçel"

for letter in name:
    if letter == "e":
        break #break direkt kırar
    print(letter)


print("\n")


for letter in name:
    if letter == "e":
        continue #continue ise şart sağlandığında atlar mesela e harfini atlayacak
    print(letter)



x=0
while x<5:
    if x==2:
        break
    print(x)
    x=x+1


# 1-100 e kadar tek sayıların toplamı
x=1
result=0

while x<=100:
    x+=1
    if x%2==0:
        continue

    result +=x

print(result)



