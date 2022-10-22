# jako argument tu przyjmuje tuple, co wydaje mi się mniej czytelne ale zdecydowałem się to tu zrobić
from asyncio.windows_events import NULL


def printValues(a):
    print("podałeś następujące wartości:")
    for c in a:
        print(c)
    print(" -- Zakres wartości --")
    j = int(a[0])
    i = int(a[1])
    global z
    z = NULL

# celowo pomijam liczbę z jeśli jest caukowita, by być zgodnym z poleceniem
    if((i-j) > 20):
        z = (j+i)/2
        j = round(z, 0)-3
        i = j+6

    while (i != j):
        if(j == z):
            i+=1
            j+=1
            continue
        print(j)
        j+=1

def inputValues():
    while True:
        try:
            a = int(input("Prosze podać liczbę będącą dolną granicą wypisywanego zakresu "))
        except ValueError:
            print("Błędna wartość")
            continue
        else:
            break
    while True:
        try:
            b = int(input("Prosze podać liczbę będącą górną granicą wypisywanego zakresu "))
        except ValueError:
            print("Błędna wartość")
            continue
        else:
            break
    return a,b

printValues(inputValues())