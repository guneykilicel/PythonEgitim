from datetime import datetime
from datetime import timedelta

simdi= datetime.now()

try:
    t=input("Doğum Tarihi(03/07/2001...): ")
    result = datetime.strptime(t, "%d/%m/%Y")
except ValueError:
    print("Tarih girişi yaparken örneğe uygun yaptığınızdan emin olun.")
    
def burc(ay):
    if(ay==7):
        print("Burcunuz: Yengeç")

def yas(yil):
    print(f"Yaşınız: {datetime.now().year-yil}")

burc(result.month)
yas(result.year)









































