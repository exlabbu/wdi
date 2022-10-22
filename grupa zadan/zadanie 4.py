import re

class Human:

    def __init__(self):
        while True:
            name = input("Proszę podaj swoje imie: ")
            if(bool(re.match("^[A-Za-zżńóąśćłźŹŚ'-]+$",name))):
                self.name = name
                break
            print("błędna wartość")
        while True:
            surName = input("Proszę podaj swoje nazwisko: ")
            if(bool(re.match("^[A-Za-zżńóąśćłźŹŚ' -.]+$",surName))):
                self.surName = surName
                break
            print("błędna wartość")
        while True:
            try:
                self.age = int(input("Proszę podaj swój wiek: "))
            except ValueError:
                print("błędna wartość")
                continue
            else:
                break
        while True:
            favAnimal = input("Proszę podaj swoje ulubione zwierze: ")
            if(bool(re.match("^[A-Za-zżńóąśćłźŹŚ]+$",favAnimal))):
                self.favAnimal = favAnimal
                break
            print("błędna wartość")
        while True:
            favDish = input("Proszę podaj swoją ulubioną potrawę: ")
            if(bool(re.match("^[A-Za-zżńóąśćłźŹŚ]+$",favDish))):
                self.favDish = favDish
                break
            print("błędna wartość")


    def printIntroduction(self):
        print(" -- Parametry jednostki -- ")
        print("Imie: "+self.name)
        print("Nazwisko: "+self.surName)
        print("Wiek: "+str(self.age))
        print("Ulubione Zwierze: "+self.favAnimal)
        print("Ulubiona Potrawa: "+self.favDish)

    def doMath(self,a,b):
        try:
            w = a/b
        except:
            print("błędne wartości")
        else:
            print(w)

obj = Human()

obj.printIntroduction()

print(" -- Dzielenie 5 przez 7 -- ")
obj.doMath(5,7)

