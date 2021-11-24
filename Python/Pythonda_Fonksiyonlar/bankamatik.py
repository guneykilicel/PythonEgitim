"""
BURADA ADRES GÖNDEREBİLMEK İÇİN DİZİ KULLANIYORUM.
"""
GuneyHesap ={
    "ad": "Güney Kılıçel",
    "hesapNo": "123456789",
    "bakiye": 3000,
    "ekHesap": 2000
}

IremHesap ={
    "ad": "İrem Ocak",
    "hesapNo": "987654321",
    "bakiye": 3000,
    "ekHesap": 1000
}

#print(GuneyHesap["ad"])

def paraCek(hesap,miktar):
    """
    Bankamatik uygulaması.
    """
    print(f"Merhaba {hesap['ad']}")
    
    if hesap['bakiye'] >=miktar:
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz.")
        print(f"Hesabınızda kalan miktar: {hesap['bakiye']}")

    else: 
        if hesap['bakiye']+hesap['ekHesap'] >= miktar:
            sor=input("Bakiye yetersiz ekHesap kullanılsın mı? (e/h): ")
            if sor=="e":
                ek_hesap_cek= miktar-hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ek_hesap_cek
                print("Paranızı alabilirsiniz.")
                print(f"Hesabınızda kalan bakiye: {hesap['bakiye']} ekHesap: {hesap['ekHesap']}")
            elif sor=="h":
                print("Para çekme işlemi iptal edildi.")
            else:
                print("Hatalı giriş")


        else:
            print("Tüm bakiyeler toplamı yetersiz.")

        
            



print("\n")
paraCek(GuneyHesap,3000)
print("----------------------")
paraCek(GuneyHesap,2000) #2. kez çektiğimde hesabın güncellenmiş yani para çekilmiş haliyle işlem yapılıyor.




"""
hesapnogir=input("Hesap no gir: ")
miktar_gir=int(input("Çekilecek miktarı gir: ")

"""



#PARA YATIRMA FONKSİYONU DA YAZABİLİRSİN.













