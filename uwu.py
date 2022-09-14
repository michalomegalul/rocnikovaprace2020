def odmocnina ():

    x = int (input ( "Zadejte číslo: " ))
    presnont = 0.00001
    dolni_mez = 0
    horni_mez = max ( 1 , x)
    stred = (dolni_mez + horni_mez) / 2

    while abs(stred**2 - x) >= presnont:
        if stred**2 < x:
            horni_mez = stred
        elif stred**2 < x:
            dolni_mez - stred
        stred = (dolni_mez + horni_mez) / 2
        print (stred)
    return stred
n = int(input("Zadejte počet desetiných míst: "))

print (round(odmocnina(), n))