class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director= director
        self.duration=duration

    def __str__(self): #BU METHODLAR BİZİM CLASSLARIMIZ DÜZGÜN ÇALIŞMAZ GENELDE 
        #BİZDE BU METHODLARI BU ŞEKİLDE DÜZENLEYEBİLİRİZ.
        return f"{self.title} by {self.director}"

    def __len__(self): #MESELA "len()" HATA VERİYOR AMA BU ŞEKİLDE ÇÖZEBİLİRİZ
        #NORMALDE UZUNLUK VERİR BİZ FİLM BİLGİLERİNİ İŞLEDİĞİMİZ ÇİN FİLM UZUNLUĞUNU VERSİN 
        return self.duration

    def __del__(self): #DEL METODU KULLNIMI "del m" ŞEKLİNDE 
        #AMA KULLANMASAK BİLE BİZE BU MESAJI VERİYOR 
        #ÇÜNKÜ PYTHON KULLANMADIĞI ŞEYİ DİREKT SİLİYOR BELLEKTEN İŞLEM BİTTİKTEN SONRA TEMİZLİYOR
        print("Film objesi silindi")




m=Movie("Film","Yönetmen",120)

print(str(m))
print(len(m))


#PYTHON SPECİAL METHODS LİSTS YAZARAK DAHA FAZLASINA ULAŞABİLİRSİN HAZIR YAZILMIŞ








































