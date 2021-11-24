#Identy Operator: is
x= y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z) #True çünkü içerikleri aynı

print(x is y) #x y mi diyoruz True evet aynı pointer mantığı
print(x is z) #x ile z aynı adresi tutmuyorlar False

a=[1,2,3]
b=[2,4]
print(a is b) #False

del a[2] #x in 2. elemanını sildik
b[1]=1
b.reverse()

print(a==a) #True
print(a is b) #False
print(a is not b) #True




#Membership Operator: in
x=["apple","banana"]
print("banana" in x) #x in içinde banana var mı True, var

name="Güney"
print("e" in name) #True
print("e" not in name) #False







