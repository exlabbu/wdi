import random
import re


class Calculator:
    lastResult = 0

# zastosować ** dla wszystkich, bo zmieniam z tupl na listy
    def addition(self, **kargs):
        sum = self.lastResult
        for x in kargs:
            sum += kargs[x]
        self.lastResult = sum

    def subtraction(self, *args):
        sub = self.lastResult
        for x in args:
            sub -= args[x]
        self.lastResult = sub

    def product(self, *args):
        prod = self.lastResult
        for x in args:
            prod *= args[x]
        self.lastResult = prod

    def quotient(self, *args):
        quot = self.lastResult
        for x in args:
            quot /= args[x]
        self.lastResult = quot

    def square(self, arg):
        squa = self.lastResult
        squa **= 2
        self.lastResult = squa

    def rootSquare(self, arg):
        rsqua = self.lastResult
        rsqua **= 0.5
        self.lastResult = rsqua
        
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
        while (flag != 1):
            decide=input("Czy chcesz kontynułować obliczenia? Y/N")
            if(bool(re.match("^[YyNnTt]$",decide))):
                flag = 1
                if(decide != "N" and decide != "n"):
                    while (sflag != 1):
                        decide=input("Czy chcesz wprowadzić nowe dane? (Wynik twoich obliczeń został zachowany i możesz wykonywać na nim operacje) Y/N")
                        if(bool(re.match("^[YyNnTt]$",decide))):
                            sflag = 1
                            if(decide != "N" and decide != "n"):
                                self.connection.lastResult = 0
                        else:
                            print("Błędna wartość")
                    self.run()
            else:
                print("Błędna wartość")
            
                        
       

    def addition(self):
        print("Możesz podać dowolną ilość liczb do zsumowania, by wyjść wpisz exit, lub control + c")
        # val definiuje w ten sposób by zasygnalizować programowi że chce mieć tu listę
        val = []
        i = 0
        while True:
            val.append(self.insertValues())
            if(val[i] != "exit" or val[i] != KeyboardInterrupt):
                break
            i += 1
        self.connection.addition(val)
        print(self.connection.lastResult)
        self.askToConitnue()

    def subtraction(self):
        print("Możesz podać dowolną ilość liczb do odjęcia, by wyjść wpisz exit, lub control + c")
        val = tuple(0)
        i = 0
        while(val[i] != "exit" or val[i] != KeyboardInterrupt):
            val[i] = self.insertValues()
            i += 1
        self.connection.subtraction(val)
        print(self.connection.lastResult)
        self.askToConitnue()

    def product(self):
        print("Możesz podać dowolną ilość liczb do pomnożenia, by wyjść wpisz exit, lub control + c")
        val = tuple(1)
        i = 0
        while(val[i] != "exit" or val[i] != KeyboardInterrupt):
            val[i] = self.insertValues()
            i += 1
        self.connection.product(val)
        print(self.connection.lastResult)
        self.askToConitnue()

    def quotient(self):
        print("Możesz podać dowolną ilość liczb do podzielenia, by wyjść wpisz exit, lub control + c")
        val = tuple(1)
        i = 0
        while(val[i] != "exit" or val[i] != KeyboardInterrupt):
            val[i] = self.insertValues()
            i += 1
        self.connection.quotient(val)
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
