import random
import re


class Calculator:
    def addition(self, a,b):
        try:
            w = a + b
        except:
            return False
        else:
            return w
    def subtraction(self, a, b):
        try:
            w = a - b
        except:
            return False
        else:
            return w
    def product(self, a, b):
        try:
            w = a * b
        except:
            return False
        else:
            return w
    def quotient(self, a, b):
        try:
            w = a / b
        except:
            return False
        else:
            return w
    def powerOf(self, a, b):
        try:
            w = a ** b
        except:
            return False
        else:
            return w
    def elementOf(self, a, b):
        try:
            w = a ** (1/b)
        except:
            return False
        else:
            return w
    def random(self, a, b):
        try:
            w = random.randint(a,b)
        except:
            return False
        else:
            return w

class Aplication:
    def __init__(self):
        self.connect = Calculator()

    def askToContinue(self):
        flag = 0
        while (flag != 1):
            decide=input("Czy chcesz wprowadzić nowe dane? Y/N ")
            if(bool(re.match("^[YyNnTt]$",decide))):
                flag = 1
                if(decide != "N" and decide != "n"):
                    self.run()
        exit()

    def inserValues(self):
        while True:
            try:
                arg = float(input("Podaj liczbę: "))
            except:
                print("Błędna wartość")
                continue
            else:
                return arg
    def addition(self,a,b):
        w = self.connect.addition(a,b)
        if(w == False):
            print("Nieprawidłowa operacja")
        else:
            print("Wynik to "+str(w))
        self.askToContinue()
    def subtraction(self,a,b):
        w = self.connect.subtraction(a,b)
        if(w == False):
            print("Nieprawidłowa operacja")
        else:
            print("Wynik to "+str(w))
        self.askToContinue()
    def product(self,a,b):
        w = self.connect.product(a,b)
        if(w == False):
            print("Nieprawidłowa operacja")
        else:
            print("Wynik to "+str(w))
        self.askToContinue()
    def quotient(self,a,b):
        w = self.connect.quotient(a,b)
        if(w == False):
            print("Nieprawidłowa operacja")
        else:
            print("Wynik to "+str(w))
        self.askToContinue()
    def powerOf(self,a,b):
        w = self.connect.powerOf(a,b)
        if(w == False):
            print("Nieprawidłowa operacja")
        else:
            print("Wynik to "+str(w))
        self.askToContinue()
    def elementOf(self,a,b):
        w = self.connect.elementOf(a,b)
        if(w == False):
            print("Nieprawidłowa operacja")
        else:
            print("Wynik to "+str(w))
        self.askToContinue()
    def random(self,a,b):
        w = self.connect.random(a,b)
        if(w == False):
            print("Nieprawidłowa operacja")
        else:
            print("Wynik to "+str(w))
        self.askToContinue()
    def run(self):
        a = self.inserValues()
        b = self.inserValues()

        def setMode():
            print(" ----- Witamy w wesołym kalkulatorze -----")
            print(" Proszę wybrać, jeden z poniższych trybów ")
            print("[1] Dodawanie")
            print("[2] Odejmowanie")
            print("[3] Mnożenie")
            print("[4] Dzielenie")
            print("[5] Potęgowanie")
            print("[6] Pierwiastkowanie")
            print("[7] Wyjdź")
            while True:
                try:
                    mode = int(input("Wybierz tryb: "))
                except:
                    print("Błędna wartość")
                    continue
                else:
                    if(mode > 7):
                        print("Błędna wartość")
                        continue
                    break
            return mode

        match setMode():
            case 1:
                self.addition(a,b)
            case 2:
                self.subtraction(a,b)
            case 3:
                self.product(a,b)
            case 4:
                self.quotient(a,b)
            case 5:
                self.powerOf(a,b)
            case 6:
                self.elementOf(a,b)
            case 7:
                exit()


app = Aplication()
app.run()

