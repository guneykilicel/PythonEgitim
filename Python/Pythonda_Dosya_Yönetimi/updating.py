
# with open("newfile.txt","r+",encoding='utf-8') as file:
#     file.seek(10)
#     file.write("deneme") #üste seek dedik 20.byte a gitti oradan sonrasını deneme ile değiştirdi

# with open("newfile.txt","r+",encoding='utf-8') as file:
#     print(file.read())


#Şimdi de dosyanın sonuna ekleme yapalım şimdi "a" append modu

# with open("newfile.txt","a",encoding='utf-8') as file:
#     file.write("\nGüney Kılıçel\nİrem Ocak")

# with open("newfile.txt","r",encoding='utf-8') as file:
#     print(file.read())



#içeriği alıp güncelleme sayfa başı

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content=file.read()
#     content= "Güney Kılıçel" + content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())


#sayfa ortası
with open("newfile.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,"Kuzey") # 1. indexten önceye ekler yukarıda listeye dönüştürdük
    file.seek(0) #konum

    #for i in list: #listemizi bu şekilde de yazdırabiliriz dosyaya kısa yolu da var yazdırmamızın amacı biz listeyi güncelledik ve listeyi sayfaya yazdırıyoruz
    #    file.write(i)
    file.writelines(list) #listeyi direkt sayafaya atar
with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())















