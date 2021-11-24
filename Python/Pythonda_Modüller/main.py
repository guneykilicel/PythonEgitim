import mod

#result = help(mod)
#result = help(mod.func)
result = mod.number
result = mod.numbers
result = mod.person["name"]
result = mod.person["age"]
result = mod.func(10)

p = mod.Person()
p.speak()


print(result)

"""
MODÜLLER NEREDE SAKLANIR:
İLK ÖNCE DOSYAMIZLA AYNI DİZİNE BAKAR ORADA YOK İSE BAKACAĞI YERİ GÖRMEK İÇİN KODLAR:
Şu alttaki visual studio terminalimize yazacağız
1. python
2. import sys
3. sys.path
ÖNÜMÜZE DOSYA YOLLARI ÇIKICAK BİZ "lib" i bulmaya çalışıyoruz:
C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.8_3.8.2800.0_x64__qbz5n2kfra8p0\\lib
C deki gibi yazarken // var sen / yap aratırken:
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.2800.0_x64__qbz5n2kfra8p0\lib

TAMAM ŞİMDİ DİĞER GÖMÜLÜ MODÜLLER NEREDE ÖĞRENDİK 
BİZ DE KENDİ MODÜLÜMÜZÜ BURAYA ATARSAK SORUNSUZ ÇALIŞIR VEYA DOSYAMIZLA AYNI DİZİNDE OLURSA

"""





























