# Aż prosi się tu by wykorzystać jeden z designe patternów jakim jest fasade
# Facade, ponieważ w tym przypadku sprowadzenie wszystkiego do obiektu da użytkownikowi wygodę użytkowania, bez konieczności by wiedział co jest pod spodem.

#from __future__ import print_function, unicode_literals
#from InquirerPy import prompt myślałem nad jego użyciem, ale chyba nie będę tu robić 'wodotrysków'

import re

# w obecnej formie ten podział wydaje się niepotrzebny, ale pozwala nam w bardzo prosty sposób robudować funkcjonalności poprzez niewielkie zmiany (de facto najlepiej było by tu stosować interfejsy ale trochę nie chciało mi się tego ograniać w pythonie)
# co nie zmienia faktu że jeśli chciałbym wprowadzić mechanizmy weryfikacyjne lub wprowadzić nowe zasady dotyczące płatności, mogę to zrobić bez większej ingerencji w fasadę (poza weryfikacją gdzie należało by tylko dopisać taką funkcjonalność)
class ATMsafe():
    _saldo = 0.0
    __pin = 0000

    def checksaldo(self,pin):
        if(self.checkPINNumber(pin) == 1):
            self.badpin = 0
            return float(self._saldo)
        else:
            return "badpin"

    def checkPINNumber(self,pin):
        if(pin == self.__pin):
            return 1
        else:
            return 0

    def setPINNumber(self,pin):
        if(bool(re.match("^[0-9]{4}$",str(pin))) == 1):
            self.__pin = pin
            return 1
        else:
            return -1

class ATMpayment(ATMsafe):

    def payment(self,cash,pin):
        if(self.checkPINNumber(pin) == 1):
            if(cash > 0):
                self._saldo += cash
                return 1
            else:
                return 0
        else:
            return -1

class ATMcashMachine(ATMsafe):
    def payout(self,cash,pin):
        if(self.checkPINNumber(pin) == 1):
            if(self.checksaldo(pin) < cash):
                return 0
            else:
                self._saldo -= cash
                return 1
        else:
            return -1

class ATM(ATMpayment,ATMcashMachine,ATMsafe):
    def __init__(self,a,pin):
        if(a > 0):
            self._saldo = a
        self.setPINNumber(pin)




# moja fasada
class Aplication:
    def __init__(self,startCash,pin):
        self.connection = ATM(startCash,pin)

    def insertValues(self):
        while True:
            try:
                w = float(input("Podaj liczbę: "))
            except:
                print(" - błędna wartość - ")
                continue
            else:
                if(w <= 0):
                    print(" - błędna wartość - ")
                    continue
                return w

    def insertPIN(self):
        while True:
            try:
                w = str(input("Podaj PIN: "))
            except:
                print(" - błędna wartość - ")
                continue
            else:
                if(bool(re.match("^[0-9]{4}$",w)) !=1):
                    print(" - błędna wartość - ")
                    continue
                return w

    def payout(self,cash,pin):
        if(self.connection.payout(pin,cash) == 1):
            print("\n - operacja zakończona powodzeniem - ")
        elif(self.connection.payout(pin,cash) == -1):
            print("\n Błędny PIN ")
        else:
            print("\n - Coś poszło nie tak, upewnij się że masz wystarczającą liczbę środków na koncie - ")

    def payment(self,cash,pin):
        if(self.connection.payment(pin,cash) == 1):
            print(" - operacja zakończona powodzeniem - ")
        elif(self.connection.payout(pin,cash) == -1):
            print("\n Błędny PIN")
        else:
            print("\n - Coś poszło nie tak, podane środki nie zsotały przypisane do salda konta - ")

    def checkSaldo(self, pin, *args):
        if(len(args) >= 2):
            return self.connection.checksaldo(pin)
        elif(self.connection.checksaldo(pin) == "badpin"):
            print("\n Błędny PIN")
        else:
            print("\n == Masz na koncie: "+str(round(self.connection.checksaldo(pin),2))+" zł == ")
    def run(self, *args):
        if(len(args) > 0):
            print("\n")
            print(" --- Co chcesz zrobić w kolejnym kroku? --- ")
        else:
            print("\n")
            print(" --- Witamy w bankomacie firmy \"Uczciwość Jacka\" nasze motto to \"Może i ukradłem, ale tylko głupi by nie ukradł!\" --- ")
            print("Wybierz operację: ")
        print("[1] Wpłata")
        print("[2] Wypłata")
        print("[3] Sprawdzenie Salda Konta")
        print("[4] wyjście")
        while True:
            try:
                op = int(input("Operacja: "))
            except:
                print("Błędna wartość")
                continue
            else:
                if(op > 4):
                    print("Błędny numer operacji")
                    continue
                break
        match op:
            case 1: 
                self.payment(self.insertPIN(), self.insertValues())
            case 2:
                self.payout(self.insertPIN(), self.insertValues())
            case 3:
                self.checkSaldo(self.insertPIN())
            case 4:
                exit()
        self.run(1)




def autoTestUserOperations():
    moneyOnAccount = 20.20
    user = Aplication(moneyOnAccount,1111)
    wpłata = 100
    wypłata = 60
    pin = 1111
    try:
        user.payment(pin,wpłata)   # na koncie powinno na start być 20 bo tyle w kontruktorze user dostał, więc po tej operacji będzie 120.20
        user.payout(pin,wypłata)     # po tej operacji powinno być 60.20
        user.checkSaldo(pin)
        
        if (user.checkSaldo(pin,1) != (wpłata-wypłata+moneyOnAccount)):
            print("Błędna ilość środków na koncie")
            exit()
        elif (user.checkSaldo(pin,1) < 0):
            print("Tu nie powinno się dać osiągnąć długu")
            exit()
    except Exception as err:
        print("testy nie zaliczone " + str(err))
    #else:
    #    print("wykik testów pozytywny")

# test
#autoTestUserOperations()

# tu jest pin, w konstruktorze
app = Aplication(50.5,str(2022))
app.run()
