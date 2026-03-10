def dizi(array):
    try:
        sayac = 0
        while True:
            x = array[sayac]
            sayac += 1
    except IndexError:
        pass
    return sayac