# Zastosowałem tu takie rozwiązanie przez globane, by konstruktor klasy był bardziej uniwersalny niż dostosowany do tupli utworzonej przez return a,b
# Dodatkowo to rozwiązanie pozawla mi podać wcześniej pobrane podczas działania programu zmienne niejako do konstruktora kalsy
def inputValues():
    while True:
            try:
                aVal = int(input("Proszę podać pierwszą liczbę: "))
                bVal = int(input("Proszę podać drugą liczbę: "))
            except:
                print("błędna wartość")
                continue
            else:
                global a,b
                a = aVal
                b = bVal
                break


class PairOfNumbers:

    w = 0

    def __init__(self,a,b):
        if(a < 0 and b < 0):
            print("Obie podane liczby są mniejsze niż 0")
            exit()
        elif(a < 0 or b < 0):
            print("jedna z podanych liczb jest mniejsza niż 0")
            """
            -- Tu proszony komentarz blokowy --
                Wykonuje operację na obu, ponieważ zmieniam wartość liczby mniejszej od zera na wartość jej modułu.
                Natomiast wartość liczby nieujemnej się nie zmieni (tak zakładam że może to być też 0).
            """
            try:
                a = (a ** 2) ** 0.5
                b = (b ** 2) ** 0.5
            except:
                print("Prawdopodobnie użyłeś zbyt dużych liczb, lub wykożystałeś błędną wartość")
        else:
            self.a = a
            self.b = b

    def error(err):
        def printOverflow():
            print("Prawdopodobnie użyłeś zbyt dużych liczb, lub wykożystałeś błędną wartość")
        def printBadValues():
            print("Błędna wartość")
        
        match err:
            case "Overflow":
                printOverflow()
            case "BadValues":
                printBadValues()

    def addition(self):
        try:
            self.w = self.a + self.b
        except:
            self.errors("Overflow")
        else:
            print("Wynik dodawania to "+str(self.w))
    def subtraction(self):
        try:
            self.w = self.a - self.b
        except:
            self.errors("Overflow")
        else:
            print("Wynik odejmowania to "+str(self.w))
    def product(self):
        try:
            self.w = self.a * self.b
        except:
            self.errors("Overflow")
        else:
            if(self.w == 10):
                print("Yay!")
            # dodje tu wyjątek bo udało mi się na ogromnych wartościach, doprowadzić do przerwania programu przy konwersji w na str
            try:
                print("Wynik mnożenia to "+str(self.w))
            except:
                self.errors("Overflow")
    def quotient(self):
        try:
            self.w = self.a / self.b
        except:
            if(self.b == 0):
                print("Nieprawidłowe dzielenie przez 0")
            else:
                self.errors("BadValues")
        else:
            print("Wynik dzielenia to "+str(self.w))
    def square(self):
        try:
            self.w = [self.a ** 2, self.b ** 2]
        except:
            self.errors("BadValues")
        else:
            print("Wyniki kwadratu liczb to dla a^2 = "+str(self.w[0])+" i b^2 = "+str(self.w[1]))
    def rootSquare(self):
        try:
            self.w = [self.a ** 0.5, self.b ** 0.5]
        except:
            self.errors("BadValues")
        else:
            print("Wyniki pierwiastka kwadratowego liczb to dla sqrt(a) = "+str(self.w[0])+" i sqrt(b) = "+str(self.w[1]))

            


inputValues()
obj = PairOfNumbers(a,b)
del a,b

obj.addition()
obj.subtraction()
obj.product()
obj.quotient()
obj.square()
obj.rootSquare()