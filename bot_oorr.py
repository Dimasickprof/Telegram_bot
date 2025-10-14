import random

def chose():
    itog = ""
    udacha = random.randint(1,100)
    if udacha == 1:
        itog = "Ого, тебе выпало ребро. Супер везение!"
    elif udacha > 1 and udacha < 50:
        itog = "Выпала решка. Тоже неплохо"
    elif udacha >= 50:
        itog = "Она полетела, как орёл. Он и выпал."
    return itog