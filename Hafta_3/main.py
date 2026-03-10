import time
import random
from hafta_3 import dizi
from trader import trade

def math(a, b):
    try:
        print(a // b)
    except ZeroDivisionError:
        print("Sayı sıfıra bölünemez")

math(8, 0)

A_tek = ["Aslı", "Sude", "Sıla", "Ece", "Sena"]
print("Tek boyutlu dizi eleman sayısı:", dizi(A_tek))

A_cok = [
    ["Aslı", "Sude", "Sıla", "Ece"],
    ["Aslı", "Sude", "Sıla", "Ece"]
]
for i in A_cok:
    print("İç dizi eleman sayısı:", dizi(i))


while True:
    rsi_ = random.randint(1, 100)
    print("Mevcut RSI:", rsi_)
    trade(rsi_)
    time.sleep(0.5)