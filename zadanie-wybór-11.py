# NWW
# Najprościej to obliczyć poprzez obliczenie NWD, dwuch liczb i podzielenie ilorazu tych liczb przez wynik NWD, konieczne są 2 iteracje NWW dla 3 liczb

# weryfikowałem poprawnośc obliczeń za pomocą dostępnych w internecie kalkulatorów i uzyskiwałem identyczne wyniki, moja metoda okazała się poprawna

def inputValues():
    while True:
        try:
            vinput = float(input("Podaj liczbę: "))
        except:
            print("Błędna wartość")
            continue
        else:
            return vinput


def nwd(a,b):
    while(a != b):
        if(a > b):
            a = a - b
        else:
            b = b - a
    else:
        return a

def nww(a,b):
    try:
        w = (a * b) / nwd(a,b)
    except:
        if(a == 0 or b == 0):
            print("Jedna z wprowadzonych liczb to 0, więc wynik też będzie równy 0")
        else:
            print("Błędne dane wejściowe")
        exit()
    else:
        return w

def run():
    print(nww(nww(inputValues(),inputValues()),inputValues()))

run()