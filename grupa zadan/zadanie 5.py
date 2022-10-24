# " Przy wpisywaniu należy użyć komunikatu “Wprowadzona przez Ciebie liczba to [LICZBA]”. "  -- trochę jest to dla mnie mało zrozumiałe, ale liczę że o to chodziło.
#  Ponieważ bardziej ten komunikat pasowałby do wypisywania. Taka mała moja sugestia lub literówka :)
# Dało się jednak wykonać zadanie wg. tej specyfikacji, więc tak zrobiłem :)

def inputValue():
    while True:
        try:
            a = float(input("Wprowadzona przez Ciebie liczba to "))
        except:
            print("błędna wartość")
            continue
        else:
            break
    return(a)

print("Wpisałeś "+str(inputValue()))
