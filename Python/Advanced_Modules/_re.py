import re
result = dir(re)

# ********************re module*****************************
mystr = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

#--------re.findall()---------
result = re.findall("Python",mystr) #"Python" ları bulup dizi şeklinde verir: ['Python', 'Python']
result = len(result) #Bu şekilde yaparsak hani üstte dizi yaptı ya şimdi de kaç tane "Python" var gibi oluyor: 2


#--------re.split()-----------
result = re.split(" ",mystr) #['Python', 'Kursu:', 'Python', 'Programlama', 'Rehberiniz', '|', '40', 'saat']
result = re.split("R",mystr) #['Python Kursu: Python Programlama ', 'ehberiniz | 40 saat']


#--------re.sub()-------------
result = re.sub(" ","-",mystr) # Boşluk karakterlerini silip yerlerine '-' koyar
result = re.sub("\s","-",mystr) #"\s" == boşluk demek üstteki ile aynı şeyi yapar


#--------re.search()----------
result = re.search("Python",mystr) #<re.Match object; span=(0, 6), match='Python'>
#span=(0, 6): 0'dan 6. karakter = match='Python' Pythonmuş
# result = result.span() #(0, 6)
# result = result.start() # 0
# result = result.end() # 6
# result = result.group() # Python
result = result.string #Python Kursu: Python Programlama Rehberiniz | 40 saat


# ********************regular expression*********************
"""
    [] = Köşeli parantezler arasında yazılan bütünkarakterler aranır.

        [abc] => a      : 1 match
                 ac     : 2 match
                 Python : No matches

        [a-e]  => [abcde]
        [1-5]  => [12345]
        [0-395] => [012395]

        [^abc] => abc dışındaki karakterler.
        [^0-9] => rakam olmayan karakterler.


"""
result = re.findall("[abc]",mystr) #['a', 'a', 'a', 'b', 'a', 'a']
result = re.findall("[sat]",mystr) #['t', 's', 't', 'a', 'a', 'a', 's', 'a', 'a', 't']
result = re.findall("[a-e]",mystr) #['a', 'a', 'a', 'e', 'b', 'e', 'a', 'a']
result = re.findall("[0-5]",mystr) #['4', '0']
result = re.findall("[^abc]",mystr) #['P', 'y', 't', 'h', 'o', 'n', ' ', 'K', 'u', 'r', 's', 'u', ':', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'm', 'l', 'm', ' ', 'R', 'e', 'h', 'e', 'r', 'i', 'n', 'i', 'z', ' ', '|', ' ', '4', '0', ' ', 's', 't']




"""
    . = Herhangi bir karakteri belirtir.

        .. =>    a      : No matche
                 ab     : 1 match
                 abc    : 1 match
                 abcd   : 2 matches

"""

result = re.findall("...",mystr) #['Pyt', 'hon', ' Ku', 'rsu', ': P', 'yth', 'on ', 'Pro', 'gra', 'mla', 'ma ', 'Reh', 'ber', 'ini', 'z |', ' 40', ' sa']
result = re.findall("Py..on",mystr) #['Python', 'Python'] mesela Pyacon, Pydacon da olsaydı ekrana verilecekti





"""
    ^ = Belirtilen karakterle başlıyor mu? Stringin tamamını kastediyoruz 
         yani kelime kelime değil direkt CÜMLENİN İLK HARFİ

        ^  =>    a      : 1 match
                 abc    : 1 match
                 bac    : No match

"""
result = re.findall("^P",mystr) #['P'] NOT: değildir işareti ile karıtırma o [^P] diye yazılır bu ^P






"""
    $ = Belirtilen karakterle bitiyor mu? Stringin tamamını kastediyoruz 
         yani kelime kelime değil direkt CÜMLENİN SON HARFİ

        a$  =>   a      : 1 match
                 lamba  : 1 match
                 Python : No match

"""
result = re.findall("t$",mystr) #['t']
result = re.findall("saat$",mystr) #['saat']
result = re.findall("saattt$",mystr) #






"""
    * = Bir karakterin 0 ya da daha fazla sayıda olmasını kontrol eder.

        ma*n =>  mn      : 1 match
                 man     : 1 match
                 maaan   : 1 match
                 main    : No matche (a'nın arkasından n gelmiyor.)

"""
result = re.findall("sa*t",mystr) #['saat']






"""
    + = Bir karakterin 1 ya da daha fazla sayıda olmasını kontrol eder.

        ma+n =>  mn      : No match
                 man     : 1 match
                 maaan   : 1 match
                 main    : No matche (a'nın arkasından n gelmiyor.)

"""

result = re.findall("sa+t",mystr) #['saat']



"""
    ? = Bir karakterin 0 ya da 1 kez olmasını kontrol eder.

        ma+n =>  mn      : 1 match
                 man     : 1 match
                 maaan   : No match (2 tane 'a' var)
                 main    : No matche (a'nın arkasından n gelmiyor.)

"""
result = re.findall("sa?t",mystr) #[] Çünkü 2 tane 'a' var.





"""
    {} = Bir karakterin 0 ya da 1 kez olmasını kontrol eder.

        al{2}   => 'a' karakterinin arkasına 'l' karakteri 2 kez tekrarlanmalı.
        al{2,3} => 'a' karakterinin arkasına 'l' karakteri en az 2 en fazla 3 kez tekrarlanmalı.
        [0-9]{2,4}   => en az 2 en çok 4 basamaklı sayılar.

"""
result = re.findall("a{2}",mystr) #['aa']
result = re.findall("[0-9]{2}",mystr) #['40']






"""
    | = Alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde     : No match
            ade     : 1 match
            acdbea  : 3 match

"""
result = re.findall("a|b",mystr) #['a', 'a', 'a', 'b', 'a', 'a']







"""
    () = Gruplamak için kullanılır.

        (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.

"""






"""
    \ = Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani $ regular exp.
                engine tarafından yorumlanmaz.

    \A = Belirtilen karakter string in başında mı?
        \Athe => the string in başında mı

    \Z = Belirtilen karakter stringin soununda mı?
        the\Z => the sting in sonunda mı

    \b = Belirtilen karakter kelimenin en başında ya da sonunda mı ?
        \bthe => the kelimenin başında mı?
        the\b => the kelimenin sonunda mı?

    \d = [0-9] ile aynı anlama gelir yani rakamları arar.
        \d => 12abc34
    
    \D = [^0-9] ile aynı anlama gleir yani rakam olmayanları arar.
        \D => 1ab44_50

    \s = Boşluk karakterlerini arar
    \S = Boşluk karakterleri dışındakiler
    \w = Alfabetik karakterler, rakamlar ve al çizgi karakterleri
    \W = \w nin tam tersi

DAHA FAZLASI İÇİN:
https://www.w3schools.com/python/python_regex.asp

"""

result = re.findall("\APython",mystr) #['Python']
result = re.findall("saat\Z",mystr) #['saat']














print(result)
















































