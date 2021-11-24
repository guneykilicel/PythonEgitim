from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

simdi= datetime.now() # 2021-09-04 18:12:01.340176
print(simdi)

simdi=datetime.today() # 2021-09-04 18:12:01.340176 "now()" ile aynı işi yapar anlık verir
print(simdi)

result = simdi.year # 2021
result = simdi.month # 9
result = simdi.day # 4
result = simdi.hour # 18
result = simdi.minute # 15
result = simdi.second # 40


result = datetime.ctime(simdi) # Sat Sep  4 18:16:27 2021
result = datetime.strftime(simdi,"%Y") # 2021 (yıl)
result = datetime.strftime(simdi,"%X") # 18:18:15 (saat)
result = datetime.strftime(simdi,"%d") # 04 (gün)
result = datetime.strftime(simdi,"%A") # Saturday (gün yazı ile)
result = datetime.strftime(simdi,"%B") # September (ay yazı ile)
result = datetime.strftime(simdi,"%Y %B %A") # 2021 September Saturday
"""
Daha fazla kullanım için w3school dan bakabilirsin:
https://www.w3schools.com/python/python_datetime.asp
"""

# t= "21 Nisan 2019" #Basit
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

t= "4 September 2021 hour 18:41:25" #ay'ı kabul edebilmesi için ingilizce yazmak lazım
result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S") # 2021-09-04 18:41:25
result = result.year # 2021

birtday = datetime(2001,7,3,19,00,00) # Ekran çıktısı: 2001-07-03 19:00:00

result = simdi-birtday #timedelta #Ekran çıktısı: 7367 days, 23:59:11.420338
#result = result.days # 7368
#result = result.seconds # 58
#result = result.microseconds # 144046

result = simdi+timedelta(days=480) # 2022-12-28 21:34:44.785882
result = simdi+timedelta(days=480, minutes=10) # 2022-12-28 21:45:22.965883 (10dk arttırdık)
result = simdi - timedelta(days=10) # 2021-08-25 21:36:20.250209 ("simdi" den 10 gün azalttık)

print(result)






















