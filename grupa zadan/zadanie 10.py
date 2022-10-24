import random
import re

class Calculator:
    lastResult = 0

    def addition(self, arg):
        sum = self.lastResult
        try:
            sum += arg
        except:
            return False
        self.lastResult = sum

    def subtraction(self, arg):
        sub = self.lastResult
        try:
            sub -= arg
        except:
            return False
        self.lastResult = sub

    def product(self, arg):
        prod = self.lastResult
        try:
            prod *= arg
        except:
            return False
        self.lastResult = prod

    def quotient(self, arg):
        quot = self.lastResult
        try:
            quot /= arg
        except:
            return False
        self.lastResult = quot

    def square(self, arg):
        try:
            arg **= 2
        except:
            return False
        self.lastResult = arg

    def rootSquare(self, arg):
        try:
            rsqua **= 0.5
        except:
            return False
        self.lastResult = arg
        
    def random(self, a, b):
            self.lastResult = random.randint(a,b)

class Aplication:
    def __init__(self):
        self.connection = Calculator()

    def insertValues(self):
            input("Podaj wartość: ")

    def setMode(self):
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

    def askToConitnue(self):
        flag = 0
        while (flag != 1):
            decide=input("Czy chcesz wprowadzić nowe dane? (Wynik twoich obliczeń został zachowany i możesz wykonywać na nim operacje) Y/N")
            if(bool(re.match("^[YyNnTt]$",decide))):
                flag = 1
                if(decide != "N" and decide != "n"):
                    self.connection.lastResult = 0
                    sflag = 0
                    while (sflag != 1):
                        decide=input("Czy chcesz kontynułować obliczenia? Y/N")
                        if(bool(re.match("^[YyNnTt]$",decide))):
                            sflag = 1
                            if(decide != "N" and decide != "n"):
                                self.run()
                        else:
                            print("Błędna wartość")
            else:
                print("Błędna wartość")
            
                        
       

    def addition(self):
        print("Możesz podać dowolną ilość liczb do zsumowania, by wyjść wpisz exit")
        val = []
        i = 0
        while True:
            val.append(self.insertValues())
            if(val[i] != "exit" or val[i] != "Exit"):
                val = val [ : -1]
                break
            i += 1
        for x in val:
            self.connection.addition(x)
        print(self.connection.lastResult)
        self.askToConitnue()

    def subtraction(self):
        print("Możesz podać dowolną ilość liczb do odjęcia, by wyjść wpisz exit, lub control + c")
        val = []
        i = 0
        while True:
            val.append(self.insertValues())
            if(val[i] != "exit" or val[i] != "Exit"):
                val = val [ : -1]
                break
            i += 1
        for x in val:
            self.connection.subtraction(x)
        print(self.connection.lastResult)
        self.askToConitnue()

    def product(self):
        print("Możesz podać dowolną ilość liczb do pomnożenia, by wyjść wpisz exit, lub control + c")
        val = []
        i = 0
        while True:
            val.append(self.insertValues())
            if(val[i] != "exit" or val[i] != "Exit"):
                val = val [ : -1]
                break
            i += 1
        for x in val:
            self.connection.product(x)
        print(self.connection.lastResult)
        self.askToConitnue()
    def quotient(self):
        print("Możesz podać dowolną ilość liczb do podzielenia, by wyjść wpisz exit, lub control + c")
        val = []
        i = 0
        while True:
            val.append(self.insertValues())
            if(val[i] != "exit" or val[i] != "Exit"):
                val = val [ : -1]
                break
            i += 1
        for x in val:
            self.connection.quotient(x)
        print(self.connection.lastResult)
        self.askToConitnue()

    def square(self):
        print("")
    def rootSquare(self):
        print("")
    def random(self):
        print("")

    def run(self):
        match self.setMode():
            case 1:
                self.addition()
            case 2:
                self.subtraction()
            case 3:
                self.product()
            case 4:
                self.quotient()
            case 5:
                self.square()
            case 6:
                self.rootSquare()
            case 7:
                exit()
        self.run()


app = Aplication()
app.run()
