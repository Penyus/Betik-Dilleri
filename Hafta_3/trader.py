def trade(rsi):
    if rsi < 30:
        print("Alım yap")
    elif rsi > 70:
        print("Satım yap")
    else:
        print("Bekle")