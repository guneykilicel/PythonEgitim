#error handling => hata yönetimi


#HATA YÖNETİMİDE HATANIN OLUŞABİLECEĞİ DURUMLARI HATA MESAJLARININ İSİMLERİNİ KULLANARAK ÖNLEM ALIYORUZ


#try: #Normal işlemlerimiz buraya
#    x=int(input("x: "))
#    y=int(input("y: "))
#    print(x/y)
    
   
#except ZeroDivisionError: #anlarsın burayı 0 a bölünemez hatası
#    print("y için 0 girilemez")

#except ValueError: #mesela yanlışlıkla 8514 yazacağına 85q4 yazdı bu bir valueerror olur.
#    print("x ve y için sayısal değer girdiğinizden emin olun.")


#VEYA BU İKİ HATAYI BİRLEŞTİRİP TEK UYARI VERMESİNİ SAĞLAYABİLİRİZ
#except (ZeroDivisionError, ValueError):
#    print("Yanlış bilgi girdiniz.")


#HATALARA İSİM VERİP EKRANA VEREBİLİRİZ.
#except (ZeroDivisionError, ValueError) as e: #as e deriz hatayı içine alır allta print ile veririz
#    print("Yanlış bilgi girdiniz.")
#    print(e) #burada da hatayı ekrana verdik hemde 2 hata yazdık ya hangi hatayı yaparsak onu verir
 
#BÜTÜN HATALARI TEKTE ELEMEK İÇİN :)
#except: #except i boş bırakırız.
#    print("Hatalı bilgi giriniz.")
#İSTEĞE BAĞLI ELSE KUKLLANIMI:
#else:
#    print("Her şey yolunda")
#BU NEREDE İŞİMİZE YARAR MESELA WHİLE İLE HATALIYSA SÜREKLİ SORAR DEĞİLSE BİTİRİR

while True:
    try:
        x=int(input("x: "))
        y=int(input("y: "))
        print(x/y)
    except Exception as e: #Bu şekilde direkt hata açıklamasını alabiliriz
        print("Yanlış bilgi girdiniz.", e) #Bu şekilde yazdırırız
    else:
        break
    finally: #except çalışırsa çalışır bu da dosyalarla işle yaptık diyelim işimiz bitti dosya kapatmaak için kullanabiliriz.
        print("try except sonlandı.")










