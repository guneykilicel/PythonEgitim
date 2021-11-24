# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. Dosyayı konumda oluşturur. Var olanıbilgiyi siler. C ile aynı
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# "e": (Read) okuma. Dosya konumda yoksa hata verir.



#"w"

# file = open("newfile.txt","w")
# file.close()

#file = open("C:/Users/90546/Documents/Python/Pythonda_Dosya_Yönetimi/newfile.txt","w")

# file = open("newfile.txt","w",encoding='utf-8')
# file.write("Güney Kılıçel")
# file.close()


#"a"

# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nİrem Ocak")
# file.close()


#"x"
file = open("newfile2.txt","x",encoding='utf-8')



































