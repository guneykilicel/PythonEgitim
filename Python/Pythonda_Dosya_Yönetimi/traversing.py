with open("newfile.txt","r",encoding="utf-8") as file: #with ile file.close()a ihtiyaç yok
    content= file.read()
    print(content)
    file.seek(10) #0 yazarsak en baştan tekrar okumaya olanak tanır 10 yazdım 10. karakterden sonra
    print(file.tell()) #95 byte 95. karakter
    content2= file.read()
    print(content2)























